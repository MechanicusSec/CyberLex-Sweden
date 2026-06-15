from pathlib import Path
from case_search import search_related_cases
import re
import html
import streamlit as st
from vector_search import build_chunk_index, search_chunks as experimental_search_chunks

st.set_page_config(
    page_title="CyberLex Sweden",
    page_icon="💻",
    layout="wide"
)

DATA_DIR = Path("data")
CASES_DIR = Path("cases")


@st.cache_data
def load_experimental_search_index():
    # Loads the experimental search chunks once and keeps them cached.
    # This avoids rebuilding the test index every time Streamlit refreshes.
    return build_chunk_index()


def clean_words(text):

    # Converts text into simple searchable lowercase words.
    punctuation = ",.?!:;()[]{}\"'`"
    text = text.lower()

    for mark in punctuation:
        text = text.replace(mark, " ")

    return text.split()


def normalize_query_text(text):
    # Normalizes common wording and small typos before intent matching.
    # This keeps CyberLex from refusing a good question because of one tiny human typo.
    text_lower = str(text or "").lower()

    replacements = {
        "kontör": "konto",
        "kontr": "konto",
        "kontot": "konto",
        "e post": "e-post",
        "epost": "e-post",
        "mail": "mejl",
        "vårat": "vårt",
        "inlogning": "inloggning",
        "ransomewere": "ransomware",
        "ransomwere": "ransomware",
        "kryptats": "krypterats",
        "kund data": "kunddata",
        "customerdata": "customer data",
    }

    for wrong, right in replacements.items():
        text_lower = text_lower.replace(wrong, right)

    return text_lower


def contains_any(text, terms):
    # Returns True if any phrase in terms exists in text.
    # CyberLex uses this for simple intent detection.
    text_lower = normalize_query_text(text)
    normalized_terms = [normalize_query_text(term) for term in terms]
    return any(term in text_lower for term in normalized_terms)



def is_cyberlex_self_description_question(question):
    # Detects questions about CyberLex Sweden itself.
    # These should be answered from the app identity text, not routed into the
    # legal source knowledge base. Otherwise "What is CyberLex Sweden?" can
    # accidentally match NIS2 or other legal sources, which looks confusing in a demo.
    question_lower = normalize_query_text(question).strip()

    direct_phrases = [
        "what is cyberlex",
        "what is cyberlex sweden",
        "what does cyberlex do",
        "what does cyberlex sweden do",
        "what is this app",
        "what does this app do",
        "what is the purpose of cyberlex",
        "what is the purpose of cyberlex sweden",
        "explain cyberlex",
        "explain cyberlex sweden",
        "vad är cyberlex",
        "vad är cyberlex sweden",
        "vad gör cyberlex",
        "vad gör cyberlex sweden",
        "vad är denna app",
        "vad gör denna app",
        "vad är syftet med cyberlex",
        "vad är syftet med cyberlex sweden",
        "förklara cyberlex",
        "förklara cyberlex sweden",
    ]

    if contains_any(question_lower, direct_phrases):
        return True

    cyberlex_terms = ["cyberlex", "cyberlex sweden"]
    app_identity_terms = [
        "what is", "what does", "purpose", "explain",
        "vad är", "vad gör", "syfte", "förklara",
    ]

    return contains_any(question_lower, cyberlex_terms) and contains_any(question_lower, app_identity_terms)


def generate_cyberlex_self_description_answer(language="English"):
    # Gives a direct, clean answer about the app itself.
    # No official legal source cards are shown because this is product/app
    # context, not a legal knowledge-base answer.
    use_swedish = language == "Svenska"

    if use_swedish:
        title = "CyberLex Sweden"
        description = (
            "CyberLex Sweden är ett utbildningsprojekt och en källbaserad assistent för svensk och EU-relaterad "
            "cybersäkerhetsrätt, digital compliance och legal-tech research. Appen söker i en lokal betrodd "
            "kunskapsbas och ger källbaserade svar med officiella källänkar, källmetadata och relevant källkontext."
        )
        scope_title = "Vad CyberLex hjälper med"
        scope_items = [
            "förklaringar av NIS2, cybersäkerhetslagen, GDPR, IMY, DORA, Cyber Resilience Act och dataintrång",
            "defensiv vägledning vid incidenter som dataläckor, misstänkt intrång, komprometterade konton och ransomware",
            "SOC-liknande incidentrapporter i Markdown för praktiska incidentfrågor",
            "tydlig källkontext så att användaren kan se vilket lokalt underlag svaret bygger på",
        ]
        limitation_title = "Viktig begränsning"
        limitation = (
            "CyberLex Sweden ger inte juridisk rådgivning och ersätter inte en kvalificerad jurist, dataskyddsombud, "
            "myndighet eller professionellt incidenthanteringsteam."
        )
    else:
        title = "CyberLex Sweden"
        description = (
            "CyberLex Sweden is an educational source-grounded assistant for Swedish and EU-related cybersecurity law, "
            "digital compliance, and legal-tech research. The app searches a trusted local knowledge base and gives "
            "source-based answers with official source links, source metadata, and relevant source context."
        )
        scope_title = "What CyberLex helps with"
        scope_items = [
            "explaining NIS2, the Swedish Cybersecurity Act, GDPR, IMY, DORA, the Cyber Resilience Act, and data intrusion",
            "defensive guidance for incidents such as data leaks, suspected intrusion, compromised accounts, and ransomware",
            "SOC-style Markdown incident reports for practical incident-response questions",
            "clear source context so the user can see which local material supports the answer",
        ]
        limitation_title = "Important limitation"
        limitation = (
            "CyberLex Sweden does not provide legal advice and does not replace a qualified lawyer, data protection officer, "
            "official authority, or professional incident response team."
        )

    item_html = "".join(f"<li>{item}</li>" for item in scope_items)

    return (
        f'<div class="practical-card">'
        f'<div class="practical-card-title">{title}</div>'
        f'<div class="practical-card-text">{description}</div>'
        f'<br>'
        f'<div class="practical-card-title">{scope_title}</div>'
        f'<ul>{item_html}</ul>'
        f'<div class="attention-limitation"><strong>{limitation_title}:</strong> {limitation}</div>'
        f'</div>'
    )




def detect_ui_language_from_question(question):
    # Detects whether a user question should be handled in Swedish or English.
    # This is intentionally broader than a strict dictionary lookup because users
    # often mix Swedish grammar with English security words such as malware,
    # ransomware, phishing, GDPR, NIS2, DORA, or MFA.
    question_lower = normalize_query_text(question).strip()

    if not question_lower:
        return "English"

    words = set(clean_words(question_lower))

    strong_swedish_markers = {
        "är", "å", "ä", "ö", "vårt", "vårat", "vår", "våra",
        "misstänker", "misstänkt", "hackning", "hackad", "hackade",
        "intrång", "dataläcka", "läckt", "komprometterat", "komprometterad",
        "personuppgift", "personuppgifter", "personuppgiftsincident",
        "cybersäkerhet", "cybersäkerhetslagen", "dataintrång", "nätfiske",
        "mejl", "e-post", "inloggning", "inloggningar", "obehörig",
        "åtkomst", "krypterats", "krypterade", "utpressningsvirus",
        "anmälas", "rapporteras", "tillsyn", "myndighet", "svensk", "svenska",
    }

    common_swedish_markers = {
        "jag", "vi", "du", "ni", "han", "hon", "de", "det", "den",
        "har", "haft", "fått", "fick", "blev", "blivit", "tror", "verkar",
        "någon", "nagon", "oss", "vårt", "vårat", "system", "konto",
        "vad", "när", "vilken", "vilka", "hur", "varför", "ska", "bör",
        "måste", "kan", "efter", "om", "i", "på", "av", "för", "med",
        "sverige", "lag", "brott", "ansvarar", "isolera", "bevara", "loggar",
        "cyberincident", "säkerhetsincident", "it-incident", "incidenthantering",
    }

    english_markers = {
        "what", "when", "which", "how", "why", "should", "must", "can",
        "we", "our", "have", "had", "been", "got", "received", "think",
        "believe", "someone", "system", "account", "hacked", "breach",
        "incident", "authority", "law", "report", "reporting", "source",
    }

    language_neutral_cyber_terms = {
        "gdpr", "nis2", "dora", "imy", "mfa", "cert-se", "malware",
        "ransomware", "phishing", "it", "api", "vpn", "oauth",
    }

    swedish_score = 0
    english_score = 0

    swedish_score += 4 * len(words.intersection(strong_swedish_markers))
    swedish_score += 2 * len(words.intersection(common_swedish_markers))
    english_score += 2 * len(words.intersection(english_markers))

    # Swedish letters are a strong signal even when the rest of the question
    # contains English cyber terminology.
    if any(letter in question_lower for letter in "åäö"):
        swedish_score += 4

    # Common Swedish sentence patterns that users type during incident reports.
    swedish_phrases = [
        "vi har", "vi har fått", "vi har haft", "vi har blivit",
        "jag tror", "jag tror att vi", "det verkar", "någon har",
        "någon tagit sig in", "vårt system", "vårat system",
        "i vårt system", "i vårat system", "vad gör vi", "vad ska vi",
        "vad bör vi", "hur ska vi", "hur bör vi",
    ]
    english_phrases = [
        "what should", "what do we", "we have", "we had", "we got",
        "i think", "i believe", "someone hacked", "our system",
    ]

    for phrase in swedish_phrases:
        if phrase in question_lower:
            swedish_score += 5

    for phrase in english_phrases:
        if phrase in question_lower:
            english_score += 4

    # If the grammar is Swedish but the incident word is language-neutral
    # or English, keep the UI and answer in Swedish.
    if words.intersection(language_neutral_cyber_terms) and swedish_score >= 4:
        return "Svenska"

    if swedish_score > english_score and swedish_score >= 3:
        return "Svenska"

    return "English"






def get_current_ui_language():
    # Safely returns the current CyberLex UI language for places where the
    # normal language variable may not yet be available.
    # This prevents example-question rendering from crashing with NameError.
    for variable_name in ("selected_language", "answer_language", "language"):
        if variable_name in globals():
            value = globals().get(variable_name)
            if value in ("English", "Svenska"):
                return value

    for state_key in ("selected_language", "answer_language", "language", "ui_language"):
        value = st.session_state.get(state_key)
        if value in ("English", "Svenska"):
            return value

    return "English"


def clean_example_question_for_language(question, language="English"):
    # Keeps example questions aligned with the selected UI language.
    # English examples should not contain Swedish legal terms unless the term is
    # the official name/acronym being explained, such as IMY or NIS2.
    # Swedish examples should stay Swedish.
    question_text = str(question or "").strip()

    if language == "Svenska":
        return question_text

    english_replacements = {
        "dataintrång": "data intrusion",
        "cybersäkerhetslagen": "the Swedish Cybersecurity Act",
        "personuppgiftsincident": "personal data breach",
        "misstänkt mejl": "suspicious email",
        "misstänkt inloggning": "suspicious login activity",
        "dataläcka": "data leak",
        "komprometterat konto": "compromised account",
        "krypterade filer": "encrypted files",
    }

    cleaned = question_text
    for swedish_term, english_term in english_replacements.items():
        cleaned = re.sub(
            re.escape(swedish_term),
            english_term,
            cleaned,
            flags=re.IGNORECASE,
        )

    # Polish a few common phrasing outcomes.
    cleaned = cleaned.replace("What is data intrusion?", "What is data intrusion?")
    cleaned = cleaned.replace("What is the Swedish Cybersecurity Act?", "What is the Swedish Cybersecurity Act?")

    return cleaned


def localize_section_name(section_name, language="English"):
    # Converts internal Markdown section headings into user-facing labels.
    # The source files intentionally contain mixed English/Swedish headings so
    # search routing can work, but the UI should not show English section names
    # inside the Swedish interface or Swedish section names inside the English UI.
    use_swedish = language == "Svenska"
    raw_section = str(section_name or "").strip()
    normalized = raw_section.lower().strip()

    swedish_names = {
        "introduction": "Introduktion",
        "topic": "Ämne",
        "main authority": "Huvudmyndighet",
        "key idea": "Huvudidé",
        "important points": "Viktiga punkter",
        "swedish summary": "Svensk sammanfattning",
        "useful questions": "Exempelfrågor",
        "swedish useful questions": "Svenska exempelfrågor",
        "official source": "Officiella källor",
        "source metadata": "Källmetadata",
        "disclaimer": "Ansvarsbegränsning",
        "suspected hacking first steps": "Första steg vid misstänkt hackning eller intrång",
        "unauthorized access first steps": "Första steg vid obehörig åtkomst",
        "suspected data leak first steps": "Första steg vid misstänkt dataläcka",
        "ransomware first steps": "Första steg vid ransomware",
        "malware infection first steps": "Första steg vid skadlig kod",
        "compromised account first steps": "Första steg vid komprometterat konto",
        "suspicious login activity first steps": "Första steg vid misstänkt inloggning",
        "swedish suspicious login activity first steps": "Första steg vid misstänkt inloggning",
        "suspicious email and phishing first steps": "Första steg vid misstänkt mejl eller phishing",
        "swedish suspicious email and phishing first steps": "Första steg vid misstänkt mejl eller phishing",
        "suspicious login assessment checklist": "Checklista för misstänkt inloggning",
        "swedish suspicious login assessment checklist": "Checklista för misstänkt inloggning",
        "suspicious email assessment checklist": "Checklista för misstänkt mejl eller phishing",
        "swedish suspicious email assessment checklist": "Checklista för misstänkt mejl eller phishing",
        "first 15 minutes checklist": "Checklista: första 15 minuterna",
        "first hour checklist": "Checklista: första timmen",
        "first 24 hours checklist": "Checklista: första dygnet",
        "first 72 hours checklist": "Checklista: första 72 timmarna",
        "technical containment examples": "Exempel på teknisk begränsning",
        "evidence preservation examples": "Exempel på bevarande av bevisning",
        "documentation template": "Dokumentationsmall",
        "data leak assessment checklist": "Checklista för dataläckebedömning",
        "ransomware assessment checklist": "Checklista för ransomwarebedömning",
        "compromised account checklist": "Checklista för komprometterat konto",
        "communication guidance": "Kommunikationsstöd",
        "what not to do": "Vad man inte bör göra",
        "when to contact cert-se": "När CERT-SE bör övervägas",
        "when to assess imy reporting": "När IMY-anmälan bör bedömas",
        "when to assess cybersecurity incident reporting": "När cybersäkerhetsrapportering bör bedömas",
        "relationship with gdpr": "Relation till GDPR",
        "relationship with nis2 and the swedish cybersecurity act": "Relation till NIS2 och cybersäkerhetslagen",
        "relationship with swedish cybercrime and dataintrång": "Relation till dataintrång och cyberbrott",
        "swedish step-by-step answer for suspected hacking": "Steg för steg vid misstänkt hackning eller intrång",
        "swedish step-by-step answer for suspected data leak": "Steg för steg vid misstänkt dataläcka",
        "english step-by-step answer for suspected hacking": "Steg för steg vid misstänkt hackning eller intrång",
        "english step-by-step answer for suspected data leak": "Steg för steg vid misstänkt dataläcka",
        "incident assessment checklist": "Checklista för incidentbedömning",
        "reporting to imy": "Anmälan till IMY",
        "incident reporting": "Incidentrapportering",
        "relationship with gdpr breach reporting": "Relation till GDPR och personuppgiftsincidenter",
        "relationship with personal data breaches": "Relation till personuppgiftsincidenter",
        "relationship with incident response": "Relation till incidenthantering",
        "swedish relationship with incident response": "Relation till incidenthantering",
        "english relationship with incident response": "Relation till incidenthantering",
        "data protection by design and by default": "Dataskydd genom design och som standard",
        "swedish data protection by design and by default": "Dataskydd genom design och som standard",
        "english data protection by design and by default": "Dataskydd genom design och som standard",
        "legal reference": "Rättslig koppling",
        "practical explanation": "Praktisk förklaring",
        "swedish practical explanation": "Praktisk förklaring",
        "english practical explanation": "Praktisk förklaring",
        "answer guidance": "Svarsstöd",
        "swedish answer guidance": "Svarsstöd",
        "english answer guidance": "Svarsstöd",
        "cybersecurity connection": "Cybersäkerhetskoppling",
        "swedish connection": "Svensk koppling",
        "third-party ict risk": "ICT-tredjepartsrisk",
        "covered sectors": "Omfattade sektorer",
        "swedish covered sectors": "Omfattade sektorer",
        "size assessment": "Storleksbedömning",
        "swedish size assessment": "Storleksbedömning",
        "public administration, municipalities and regions": "Offentlig förvaltning, kommuner och regioner",
        "swedish public administration, municipalities and regions": "Offentlig förvaltning, kommuner och regioner",
        "essential and important entities": "Väsentliga och viktiga verksamhetsutövare",
        "swedish essential and important entities": "Väsentliga och viktiga verksamhetsutövare",
        "annex 1 and annex 2": "Bilaga 1 och bilaga 2",
        "swedish annex 1 and annex 2": "Bilaga 1 och bilaga 2",
        "bilaga 1 och bilaga 2": "Bilaga 1 och bilaga 2",
        "registration": "Anmälan och registrering",
        "swedish registration": "Anmälan och registrering",
        "cyberlex answer guidance": "Svarsstöd",
        "swedish cyberlex answer guidance": "Svarsstöd",
    }

    english_names = {
        "swedish summary": "Swedish summary",
        "swedish useful questions": "Swedish example questions",
        "swedish step-by-step answer for suspected hacking": "Step-by-step answer for suspected hacking or intrusion",
        "swedish step-by-step answer for suspected data leak": "Step-by-step answer for suspected data leak",
        "english step-by-step answer for suspected hacking": "Step-by-step answer for suspected hacking or intrusion",
        "english step-by-step answer for suspected data leak": "Step-by-step answer for suspected data leak",
        "first 15 minutes checklist": "First 15 minutes checklist",
        "first hour checklist": "First hour checklist",
        "first 24 hours checklist": "First 24 hours checklist",
        "first 72 hours checklist": "First 72 hours checklist",
        "compromised account first steps": "First steps for a compromised account",
        "suspected hacking first steps": "First steps for suspected hacking or intrusion",
        "suspected data leak first steps": "First steps for a suspected data leak",
        "unauthorized access first steps": "First steps for unauthorized access",
        "malware infection first steps": "First steps for malware infection",
        "ransomware first steps": "First steps for ransomware",
        "suspicious login activity first steps": "First steps for suspicious login activity",
        "swedish suspicious login activity first steps": "First steps for suspicious login activity",
        "suspicious email and phishing first steps": "First steps for suspicious email or phishing",
        "swedish suspicious email and phishing first steps": "First steps for suspicious email or phishing",
        "suspicious login assessment checklist": "Suspicious login assessment checklist",
        "swedish suspicious login assessment checklist": "Suspicious login assessment checklist",
        "suspicious email assessment checklist": "Suspicious email or phishing assessment checklist",
        "swedish suspicious email assessment checklist": "Suspicious email or phishing assessment checklist",
        "relationship with personal data breaches": "Relationship with personal data breaches",
        "relationship with incident response": "Relationship with incident response",
        "swedish relationship with incident response": "Relationship with incident response",
        "english relationship with incident response": "Relationship with incident response",
        "data protection by design and by default": "Data protection by design and by default",
        "swedish data protection by design and by default": "Data protection by design and by default",
        "english data protection by design and by default": "Data protection by design and by default",
        "covered sectors": "Covered sectors",
        "swedish covered sectors": "Covered sectors",
        "size assessment": "Size assessment",
        "swedish size assessment": "Size assessment",
        "public administration, municipalities and regions": "Public administration, municipalities and regions",
        "swedish public administration, municipalities and regions": "Public administration, municipalities and regions",
        "essential and important entities": "Essential and important entities",
        "swedish essential and important entities": "Essential and important entities",
        "annex 1 and annex 2": "Annex 1 and Annex 2",
        "swedish annex 1 and annex 2": "Annex 1 and Annex 2",
        "bilaga 1 och bilaga 2": "Annex 1 and Annex 2",
        "registration": "Registration",
        "swedish registration": "Registration",
        "practical explanation": "Practical explanation",
        "swedish practical explanation": "Practical explanation",
        "english practical explanation": "Practical explanation",
        "answer guidance": "Answer guidance",
        "swedish answer guidance": "Answer guidance",
        "english answer guidance": "Answer guidance",
        "cyberlex answer guidance": "Answer guidance",
        "swedish cyberlex answer guidance": "Answer guidance",
    }

    if use_swedish:
        if normalized in swedish_names:
            return swedish_names[normalized]

        # Remove leading language markers if a source heading contains them.
        if normalized.startswith("swedish "):
            stripped = raw_section[8:].strip()
            stripped_normalized = stripped.lower().strip()
            if stripped_normalized in swedish_names:
                return swedish_names[stripped_normalized]
            return stripped[:1].upper() + stripped[1:]
        if normalized.startswith("english "):
            stripped = raw_section[8:].strip()
            stripped_normalized = stripped.lower().strip()
            if stripped_normalized in swedish_names:
                return swedish_names[stripped_normalized]
            return stripped[:1].upper() + stripped[1:]

        return raw_section

    if normalized in english_names:
        return english_names[normalized]

    if normalized.startswith("swedish "):
        stripped = raw_section[8:].strip()
        stripped_normalized = stripped.lower().strip()
        if stripped_normalized in english_names:
            return english_names[stripped_normalized]
        return stripped[:1].upper() + stripped[1:]
    if normalized.startswith("english "):
        stripped = raw_section[8:].strip()
        stripped_normalized = stripped.lower().strip()
        if stripped_normalized in english_names:
            return english_names[stripped_normalized]
        return stripped[:1].upper() + stripped[1:]

    return raw_section


def is_practical_incident_response_question(question):
    # Detects defensive "what should I do now?" incident response questions.
    # This is used to route practical hacking/data leak/ransomware questions
    # to the Cyber Incident Response Playbook.
    question_lower = normalize_query_text(question).strip()

    incident_terms = [
        "suspect hacking",
        "suspected hacking",
        "hacked",
        "hackad",
        "hackning",
        "blivit hackade",
        "vi har blivit hackade",
        "hackat vårt system",
        "hackat vårat system",
        "någon hackade",
        "någon har hackat",
        "someone hacked",
        "someone hacked our system",
        "breached our system",
        "breach into our system",
        "someone breached",
        "misstänker hackning",
        "misstänkt hackning",
        "suspect intrusion",
        "suspected intrusion",
        "intrusion",
        "intrång",
        "tagit sig in",
        "tagit sig in i vårt system",
        "tagit sig in i vårat system",
        "någon verkar ha tagit sig in",
        "någon har tagit sig in",
        "misstänker intrång",
        "misstänkt intrång",
        "unauthorized access",
        "obehörig åtkomst",
        "compromised",
        "compromise",
        "komprometterad",
        "komprometterat",
        "komprometterade",
        "account hacked",
        "konto hackat",
        "konto är hackat",
        "compromised account",
        "komprometterat konto",
        "ett konto är komprometterat",
        "ett kontör är komprometterat",
        "kontör är komprometterat",
        "konto är komprometterat",
        "kontot är komprometterat",
        "kontot har komprometterats",
        "malware",
        "ransomware",
        "utpressningsvirus",
        "files encrypted",
        "files are encrypted",
        "our files are encrypted",
        "our files have been encrypted",
        "files have been encrypted",
        "encrypted files",
        "filer har krypterats",
        "filerna har krypterats",
        "våra filer har krypterats",
        "krypterade filer",
        "krypterats",
        "data leak",
        "data leakage",
        "dataläcka",
        "läckt data",
        "data har läckt",
        "customer data exposed",
        "customer data leaked",
        "customer data may have leaked",
        "customer data might have leaked",
        "customer data has leaked",
        "customer data have leaked",
        "kunddata har exponerats",
        "kunddata har läckt",
        "kunddata kan ha läckt",
        "kunddata kan ha exponerats",
        "data och personinformation har läckt",
        "personinformation har läckt",
        "personuppgifter har läckt",
        "exposed data",
        "exponerad data",
        "personal data exposed",
        "personuppgifter exponerats",
        "cyber incident",
        "cyberincident",
        "security incident",
        "säkerhetsincident",
        "it incident",
        "it-incident",
        "incident response",
        "incidenthantering",
        "suspicious login",
        "suspicious sign-in",
        "unusual login",
        "unusual sign-in",
        "impossible travel",
        "suspicious login activity",
        "suspicious account login",
        "suspicious login on an account",
        "received a suspicious login",
        "got a suspicious login",
        "misstänkt inloggning",
        "misstänkt login",
        "misstänkt loggning",
        "fått en misstänkt login",
        "fått misstänkt login",
        "misstänkt login på ett konto",
        "misstänkt login på konto",
        "loggat in på ett konto",
        "loggat in på konto",
        "verkar ha loggat in",
        "någon har loggat in",
        "någon verkar ha loggat in",
        "inloggning på ett konto",
        "login på ett konto",
        "login på konto",
        "ovanlig inloggning",
        "misstänkta inloggningar",
        "ovanliga inloggningar",
        "phishing",
        "nätfiske",
        "suspicious email",
        "misstänkt mejl",
        "misstänkt e-post",
        "misstänkt länk",
        "skadlig länk",
        "okänd länk",
        "suspicious link",
        "malicious link",
        "clicked a suspicious link",
        "someone clicked a suspicious link",
        "someone clicked a link",
        "someone clicked a link on a website",
        "clicked a link on a website",
        "clicked a link in sms",
        "någon klickade på en länk",
        "någon klickade på en länk på en webbsida",
        "klickade på en länk på en webbsida",
        "klickade på en länk i sms",
        "klickat på en länk i sms",
        "länk på en webbsida",
        "länk i sms",
        "länk i chatt",
        "qr-kod",
        "klickade på en misstänkt länk",
    ]

    action_terms = [
        "what should",
        "what do i do",
        "what do we do",
        "what should i do",
        "what should we do",
        "what should a company do",
        "what should an organization do",
        "what should an organisation do",
        "what steps",
        "first steps",
        "after",
        "if i suspect",
        "if we suspect",
        "i suspect",
        "we suspect",
        "suspected",
        "vad ska",
        "vad bör",
        "vad gör",
        "vad ska jag göra",
        "vad ska vi göra",
        "vad bör vi göra",
        "hur ska",
        "hur bör",
        "efter",
        "om jag misstänker",
        "om vi misstänker",
        "jag misstänker",
        "vi misstänker",
        "vi tror",
        "vi tror att",
        "misstänker",
        "misstänkt",
        "har läckt",
        "har krypterats",
        "klickade",
        "klickat",
        "clicked",
    ]

    # Users often report an incident as a statement instead of asking a neat
    # question. CyberLex should still treat that as practical incident response.
    # Example: "Vi har fått en misstänkt login på ett konto".
    statement_terms = [
        "we have", "we had", "we got", "we received", "we have received",
        "i think we", "i believe we", "it looks like", "someone has",
        "someone hacked", "our system", "our account", "our files", "files are encrypted",
        "vi har", "vi hade", "vi fick", "vi har fått", "vi har haft",
        "vi har blivit", "vi tror", "vi tror att", "jag tror att vi", "jag tror vi", "det verkar som",
        "någon har", "någon verkar", "vårt system", "vårat system",
        "på ett konto", "på konto", "i ett konto",
        "våra filer", "filerna", "files are encrypted", "our files are encrypted",
        "kunddata", "kunddata kan ha läckt", "customer data may have leaked",
        "personuppgifter", "personinformation",
        "någon klickade", "someone clicked", "länk i sms", "länk på en webbsida", "link on a website",
    ]

    definition_question_starters = [
        "what is", "what are", "what does", "explain", "define",
        "vad är", "vad betyder", "förklara", "definiera",
    ]

    if is_suspicious_link_question(question_lower):
        return True

    has_incident = contains_any(question_lower, incident_terms)
    has_action = contains_any(question_lower, action_terms)
    has_statement = contains_any(question_lower, statement_terms)
    is_definition_question = any(question_lower.startswith(starter) for starter in definition_question_starters)

    if is_definition_question and not has_statement:
        return False

    return has_incident and (has_action or has_statement)


def is_suspected_hacking_question(question):
    # Detects suspected hacking/intrusion questions.
    question_lower = normalize_query_text(question)
    return contains_any(
        question_lower,
        [
            "suspect hacking",
            "suspected hacking",
            "suspect intrusion",
            "suspected intrusion",
            "hacked",
            "intrusion",
            "unauthorized access",
            "misstänker hackning",
            "misstänkt hackning",
            "misstänker intrång",
            "misstänkt intrång",
            "hackad",
            "hackning",
            "blivit hackade",
            "hackat vårt system",
            "hackat vårat system",
            "någon har hackat",
            "someone hacked",
            "breached our system",
            "someone breached",
            "intrång",
            "tagit sig in",
            "tagit sig in i vårt system",
            "någon verkar ha tagit sig in",
            "obehörig åtkomst",
            "suspicious login",
            "suspicious sign-in",
            "unusual login",
            "unusual sign-in",
            "impossible travel",
            "suspicious login activity",
            "misstänkt inloggning",
            "ovanlig inloggning",
            "misstänkta inloggningar",
            "ovanliga inloggningar",
        ],
    )


def is_data_leak_response_question(question):
    # Detects practical data leak questions.
    question_lower = normalize_query_text(question)
    return contains_any(
        question_lower,
        [
            "data leak",
            "data leakage",
            "data leaked",
            "customer data exposed",
            "customer data leaked",
            "customer data may have leaked",
            "customer data might have leaked",
            "customer data has leaked",
            "personal data exposed",
            "exposed data",
            "dataläcka",
            "data har läckt",
            "läckt data",
            "kunddata har exponerats",
            "kunddata har läckt",
            "kunddata kan ha läckt",
            "kunddata kan ha exponerats",
            "vi tror att kunddata har läckt",
            "personinformation har läckt",
            "personuppgifter har läckt",
            "personuppgifter exponerats",
            "exponerad data",
        ],
    )


def is_suspicious_login_question(question):
    # Detects suspicious login/sign-in questions.
    # This is separate from fully compromised-account questions so CyberLex can give
    # a more precise triage answer instead of always assuming full compromise.
    question_lower = normalize_query_text(question)
    return contains_any(
        question_lower,
        [
            "suspicious login",
            "suspicious logins",
            "suspicious login activity",
            "suspicious sign-in",
            "suspicious signins",
            "suspicious sign in",
            "unusual login",
            "unusual logins",
            "unusual sign-in",
            "unusual sign in",
            "impossible travel",
            "strange login",
            "unknown login",
            "login from unknown country",
            "login from another country",
            "failed login attempts",
            "misstänkt inloggning",
            "misstänkta inloggningar",
            "misstänkt login",
            "misstänkt loggning",
            "misstänkt login på ett konto",
            "misstänkt login på konto",
            "loggat in på ett konto",
            "loggat in på konto",
            "verkar ha loggat in",
            "någon har loggat in",
            "någon verkar ha loggat in",
            "login på ett konto",
            "login på konto",
            "inloggning på ett konto",
            "ovanlig inloggning",
            "ovanliga inloggningar",
            "okänd inloggning",
            "inloggning från okänt land",
            "inloggning från annat land",
            "misslyckade inloggningar",
        ],
    )



def is_suspicious_link_question(question):
    # Detects suspicious link clicks without assuming the link came from email.
    # Links can come from email, SMS, chat, social media, websites, QR codes,
    # documents, ads, or collaboration tools. This needs its own route so the
    # answer does not become too email-specific.
    question_lower = normalize_query_text(question)
    return contains_any(
        question_lower,
        [
            "suspicious link",
            "malicious link",
            "unknown link",
            "clicked a suspicious link",
            "clicked a malicious link",
            "clicked an unknown link",
            "someone clicked a suspicious link",
            "someone clicked a link",
            "someone clicked a link on a website",
            "clicked a link on a website",
            "clicked a link in sms",
            "clicked a link in chat",
            "clicked a link in teams",
            "clicked a link in slack",
            "clicked a qr code",
            "suspicious url",
            "malicious url",
            "misstänkt länk",
            "skadlig länk",
            "okänd länk",
            "klickat på misstänkt länk",
            "klickade på misstänkt länk",
            "klickade på en misstänkt länk",
            "någon klickade på en misstänkt länk",
            "någon klickade på en länk",
            "någon klickade på en länk på en webbsida",
            "klickade på en länk på en webbsida",
            "länk på en webbsida",
            "länk i sms",
            "klickade på en länk i sms",
            "klickat på en länk i sms",
            "länk i chatt",
            "länk i teams",
            "länk i slack",
            "qr-kod",
            "qr kod",
            "klickade på en qr",
            "klickat på en qr",
        ],
    )

def is_suspicious_email_question(question):
    # Detects suspicious email / phishing questions.
    # This is separate from compromised account because a suspicious email may be
    # only a reported message, not yet an account compromise.
    question_lower = normalize_query_text(question)
    return contains_any(
        question_lower,
        [
            "suspicious email",
            "suspicious e-mail",
            "suspicious mail",
            "phishing email",
            "phishing mail",
            "phishing message",
            "malicious email",
            "malicious attachment",
            "suspicious attachment",
            "suspicious link",
            "clicked a suspicious link",
            "clicked phishing link",
            "received a suspicious email",
            "receive a suspicious email",
            "we receive a suspicious email",
            "we received a suspicious email",
            "misstänkt mejl",
            "misstänkt mail",
            "misstänkt e-post",
            "nätfiske",
            "phishing",
            "skadlig bilaga",
            "misstänkt bilaga",
            "misstänkt länk",
            "klickat på misstänkt länk",
            "klickade på misstänkt länk",
            "klickade på en misstänkt länk",
            "någon klickade på en misstänkt länk",
            "klickat på phishinglänk",
            "klickade på phishinglänk",
            "fått ett misstänkt mejl",
        ],
    )


def is_compromised_account_question(question):
    # Detects practical compromised-account questions.
    # Keep this focused on actual account compromise, not every phishing or login question.
    question_lower = normalize_query_text(question)
    return contains_any(
        question_lower,
        [
            "compromised account",
            "account compromised",
            "account is compromised",
            "account has been compromised",
            "account may be compromised",
            "account might be compromised",
            "user account is compromised",
            "employee account is compromised",
            "email account is compromised",
            "account hacked",
            "email account hacked",
            "my account is hacked",
            "their account is hacked",
            "konto komprometterat",
            "komprometterat konto",
            "ett konto är komprometterat",
            "ett kontör är komprometterat",
            "om ett konto är komprometterat",
            "om ett kontör är komprometterat",
            "kontot är komprometterat",
            "kontot har komprometterats",
            "kontot kan vara komprometterat",
            "konto kan vara komprometterat",
            "användarkonto är komprometterat",
            "e-postkonto är komprometterat",
            "mailkonto är komprometterat",
            "kontot är hackat",
            "konto är hackat",
            "konto hackat",
            "mitt konto är hackat",
            "användarkonto hackat",
            "e-postkonto hackat",
        ],
    )


def is_ransomware_response_question(question):
    # Detects practical ransomware and malware response questions.
    question_lower = normalize_query_text(question)
    return contains_any(
        question_lower,
        [
            "ransomware",
            "malware",
            "utpressningsvirus",
            "files encrypted",
            "files are encrypted",
            "our files are encrypted",
            "our files have been encrypted",
            "files have been encrypted",
            "filer har krypterats",
            "filerna har krypterats",
            "våra filer har krypterats",
            "encrypted files",
            "krypterade filer",
            "krypterats",
        ],
    )


def is_encrypted_files_possible_ransomware_question(question):
    # Detects wording where the user says files are encrypted without explicitly
    # saying ransomware. Encryption can be normal, so the answer should frame
    # this as suspicious only when encryption is unexpected or linked to malware.
    question_lower = normalize_query_text(question)
    return contains_any(
        question_lower,
        [
            "files encrypted",
            "files are encrypted",
            "our files are encrypted",
            "our files have been encrypted",
            "files have been encrypted",
            "encrypted files",
            "filer har krypterats",
            "filerna har krypterats",
            "våra filer har krypterats",
            "krypterade filer",
            "krypterats",
        ],
    )


def is_ransomware_or_malware_question(question):
    # Compatibility helper used by source-context prioritization.
    return is_ransomware_response_question(question)


def expand_question_terms(question):
    """
    Expands a user question with related cybersecurity and legal terms.

    This improves local search by helping CyberLex match questions even when
    the user does not use the exact same words as the source files.

    Example:
    "ransomware attack" can also search for incident, breach, reporting,
    security measures, and personal data.
    """

    question_lower = normalize_query_text(question)
    expanded_terms = []

    topic_expansions = {

        "suspect hacking": [
            "cyber incident",
            "incident response",
            "intrusion",
            "unauthorized access",
            "containment",
            "preserve evidence",
            "logs",
            "compromised account",
            "cert-se",
            "imy",
            "nis2",
        ],
        "misstänker intrång": [
            "cyberincident",
            "incidenthantering",
            "intrång",
            "obehörig åtkomst",
            "isolera",
            "bevara bevis",
            "loggar",
            "komprometterat konto",
            "cert-se",
            "imy",
            "nis2",
        ],
        "data leak": [
            "personal data breach",
            "data exposure",
            "imy",
            "gdpr",
            "72 hours",
            "preserve evidence",
            "contain exposure",
            "incident response",
        ],
        "dataläcka": [
            "personuppgiftsincident",
            "exponerad data",
            "imy",
            "gdpr",
            "72 timmar",
            "bevara bevis",
            "begränsa exponering",
            "incidenthantering",
        ],
        "misstänkt login": [
            "suspicious login activity",
            "suspicious sign-in",
            "account security",
            "incident response",
            "preserve logs",
            "mfa",
            "revoke sessions",
        ],
        "misstänkt inloggning": [
            "suspicious login activity",
            "suspicious sign-in",
            "account security",
            "incident response",
            "bevara loggar",
            "mfa",
            "återkalla sessioner",
        ],
        "loggat in på ett konto": [
            "misstänkt inloggning",
            "suspicious login activity",
            "account security",
            "incident response",
            "bevara loggar",
            "mfa",
            "återkalla sessioner",
            "obehörig åtkomst",
        ],
        "någon verkar ha loggat in": [
            "misstänkt inloggning",
            "suspicious login activity",
            "account security",
            "incident response",
            "bevara loggar",
            "mfa",
            "återkalla sessioner",
            "obehörig åtkomst",
        ],
        "suspicious login": [
            "suspicious login activity",
            "suspicious sign-in",
            "account security",
            "incident response",
            "preserve logs",
            "mfa",
            "revoke sessions",
        ],
        "compromised account": [
            "revoke sessions",
            "reset password",
            "mfa",
            "mailbox rules",
            "unauthorized access",
            "incident response",
            "personal data breach",
        ],
        "komprometterat konto": [
            "återkalla sessioner",
            "byt lösenord",
            "mfa",
            "vidarebefordringsregler",
            "obehörig åtkomst",
            "incidenthantering",
            "personuppgiftsincident",
        ],
        "gdpr": [
            "personal data",
            "data protection",
            "privacy",
            "imy",
            "breach",
            "72 hours",
            "notification",
            "controller",
            "processor",
        ],
        "personal data breach": [
            "gdpr",
            "imy",
            "72 hours",
            "notification",
            "risk",
            "data subject",
            "personal data",
            "incident",
        ],
        "breach": [
            "personal data breach",
            "incident",
            "notification",
            "imy",
            "gdpr",
            "risk",
        ],
        "incident": [
            "incident reporting",
            "cybersecurity incident",
            "nis2",
            "gdpr",
            "breach",
            "reporting",
        ],
        "our files are encrypted": [
            "ransomware",
            "malware",
            "cyber incident",
            "incident response",
            "preserve evidence",
            "backups",
            "containment",
            "imy",
            "nis2",
        ],
        "files are encrypted": [
            "ransomware",
            "malware",
            "cyber incident",
            "incident response",
            "preserve evidence",
            "backups",
            "containment",
            "imy",
            "nis2",
        ],
        "våra filer har krypterats": [
            "ransomware",
            "malware",
            "cyber incident",
            "incident response",
            "preserve evidence",
            "backups",
            "containment",
            "imy",
            "nis2",
        ],
        "någon klickade på en misstänkt länk": [
            "suspicious link",
            "malicious url",
            "phishing",
            "incident response",
            "compromised account",
            "revoke sessions",
            "mfa",
            "preserve evidence",
            "browser downloads",
            "web filtering",
        ],
        "någon klickade på en länk": [
            "suspicious link",
            "malicious url",
            "phishing",
            "incident response",
            "compromised account",
            "preserve evidence",
            "mfa",
            "browser downloads",
            "web filtering",
        ],
        "someone clicked a suspicious link": [
            "suspicious link",
            "malicious url",
            "phishing",
            "incident response",
            "compromised account",
            "preserve evidence",
            "mfa",
            "browser downloads",
            "web filtering",
        ],
        "someone clicked a link": [
            "suspicious link",
            "malicious url",
            "phishing",
            "incident response",
            "compromised account",
            "preserve evidence",
            "mfa",
            "browser downloads",
            "web filtering",
        ],
        "kunddata kan ha läckt": [
            "data leak",
            "personal data breach",
            "gdpr",
            "imy",
            "72 hours",
            "incident response",
            "preserve evidence",
        ],
        "kunddata har läckt": [
            "data leak",
            "personal data breach",
            "gdpr",
            "imy",
            "72 hours",
            "incident response",
            "preserve evidence",
        ],
        "customer data may have leaked": [
            "data leak",
            "personal data breach",
            "gdpr",
            "imy",
            "72 hours",
            "incident response",
            "preserve evidence",
        ],
        "customer data leaked": [
            "data leak",
            "personal data breach",
            "gdpr",
            "imy",
            "72 hours",
            "incident response",
            "preserve evidence",
        ],
        "tagit sig in": [
            "suspected hacking",
            "intrusion",
            "unauthorized access",
            "incident response",
            "preserve evidence",
            "logs",
            "cert-se",
        ],
        "ransomware": [
            "cyber incident",
            "incident reporting",
            "personal data breach",
            "gdpr",
            "nis2",
            "security measures",
            "unauthorized access",
            "availability",
        ],
        "cyber attack": [
            "cyber incident",
            "incident reporting",
            "personal data breach",
            "gdpr",
            "nis2",
            "security measures",
            "unauthorized access",
            "availability",
        ],
        "cyberattack": [
            "cyber incident",
            "incident reporting",
            "personal data breach",
            "gdpr",
            "nis2",
            "security measures",
            "unauthorized access",
            "availability",
        ],
        "security incident": [
            "cyber incident",
            "incident reporting",
            "nis2",
            "gdpr",
            "breach",
            "security measures",
        ],
        "bilaga 1": [
            "annex 1",
            "annex 2",
            "sector lists",
            "covered sectors",
            "essential entities",
            "important entities",
        ],
        "bilaga 2": [
            "annex 1",
            "annex 2",
            "sector lists",
            "covered sectors",
            "essential entities",
            "important entities",
        ],
        "annex 1": [
            "annex 2",
            "sector lists",
            "covered sectors",
            "essential entities",
            "important entities",
        ],
        "annex 2": [
            "annex 1",
            "sector lists",
            "covered sectors",
            "essential entities",
            "important entities",
        ],
        "nis2": [
            "cybersecurity",
            "incident reporting",
            "essential entities",
            "important entities",
            "risk management",
            "security measures",
            "msb",
        ],
        "dora": [
            "digital operational resilience",
            "financial sector",
            "ict risk",
            "ict incident",
            "third-party ict",
            "resilience testing",
        ],
        "third-party": [
            "ict third-party risk",
            "supplier",
            "provider",
            "outsourcing",
            "cloud",
            "dora",
        ],
        "dataintrång": [
            "unauthorized access",
            "cybercrime",
            "information system",
            "data intrusion",
            "brottsbalken",
        ],
        "unauthorized access": [
            "dataintrång",
            "cybercrime",
            "illegal access",
            "information system",
            "data intrusion",
        ],
        "cyber resilience act": [
            "cra",
            "products with digital elements",
            "vulnerability handling",
            "manufacturer",
            "security requirements",
        ],
        "cra": [
            "cyber resilience act",
            "products with digital elements",
            "vulnerability handling",
            "manufacturer",
            "security requirements",
        ],
        "imy": [
            "gdpr",
            "data protection",
            "personal data breach",
            "supervision",
            "notification",
        ],
    }

    for trigger, related_terms in topic_expansions.items():
        if trigger in question_lower:
            expanded_terms.extend(related_terms)

    return expanded_terms


def extract_official_sources(content):
    # Extracts official source links from the "## Official source" section.
    # Supports:
    # https://example.com
    # [Source name](https://example.com)
    # - [Source name](https://example.com)
    # - https://example.com

    lines = content.splitlines()
    sources = []
    in_official_source_section = False
    previous_label = ""

    for line in lines:
        stripped_line = line.strip()

        heading_lower = stripped_line.lower()

        if heading_lower.startswith("## official source"):
            in_official_source_section = True
            continue

        if in_official_source_section and stripped_line.startswith("## "):
            break

        if not in_official_source_section or not stripped_line:
            continue

        # Remove common Markdown bullet prefixes before parsing links.
        cleaned_line = stripped_line
        while cleaned_line.startswith(("-", "*")):
            cleaned_line = cleaned_line[1:].strip()

        # Markdown link format:
        # [Source name](https://example.com)
        if cleaned_line.startswith("[") and "](" in cleaned_line and ")" in cleaned_line:
            label = cleaned_line.split("](", 1)[0].replace("[", "").strip()
            url = cleaned_line.split("](", 1)[1].split(")", 1)[0].strip()

            if label and url.startswith("http"):
                sources.append(
                    {
                        "label": label,
                        "url": url
                    }
                )
                previous_label = ""
                continue

        # Raw URL format:
        # https://example.com
        if cleaned_line.startswith("http"):
            label = previous_label if previous_label else cleaned_line

            sources.append(
                {
                    "label": label,
                    "url": cleaned_line
                }
            )
            previous_label = ""
            continue

        # Label on one line followed by URL on next line.
        # Example:
        # EUR-Lex - Directive 2013/40/EU
        # https://eur-lex.europa.eu/...
        previous_label = cleaned_line.rstrip(":")

    return sources


def extract_section_text(content, heading):
    # Extracts text from a specific Markdown heading section.
    lines = content.splitlines()
    section_lines = []
    in_section = False

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.lower() == heading.lower():
            in_section = True
            continue

        if in_section and stripped_line.startswith("## "):
            break

        if in_section:
            section_lines.append(line)

    return "\n".join(section_lines).strip()


def extract_source_metadata(content):
    # Extracts source date and version notes from a Markdown knowledge file.
    # Supports both the older layout:
    # ## Source date
    # ## Version notes
    #
    # and the newer combined layout:
    # ## Source metadata
    # Source date: Last checked: 2026-06-03
    # Version notes: Source reviewed...

    source_date = extract_section_text(content, "## Source date")
    version_notes = extract_section_text(content, "## Version notes")

    metadata_section = extract_section_text(content, "## Source metadata")

    if metadata_section:
        metadata_lines = metadata_section.splitlines()

        for index, line in enumerate(metadata_lines):
            stripped_line = line.strip()
            lower_line = stripped_line.lower()

            if lower_line.startswith("source date:"):
                source_date = stripped_line.split(":", 1)[1].strip()

            elif lower_line.startswith("version notes:"):
                version_text = stripped_line.split(":", 1)[1].strip()

                # Include following non-empty lines until another metadata field appears.
                extra_lines = []
                for following_line in metadata_lines[index + 1:]:
                    following_stripped = following_line.strip()
                    following_lower = following_stripped.lower()

                    if following_lower.startswith("source date:") or following_lower.startswith("version notes:"):
                        break

                    if following_stripped:
                        extra_lines.append(following_stripped)

                if extra_lines:
                    version_text = " ".join([version_text] + extra_lines).strip()

                version_notes = version_text

    if not source_date:
        source_date = "No source date stored for this document yet."

    if not version_notes:
        version_notes = "No version notes stored for this document yet."

    return {
        "source_date": source_date,
        "version_notes": version_notes
    }


def load_documents():
    # Loads all Markdown files from the data folder.
    documents = []

    for file_path in DATA_DIR.glob("*.md"):
        content = file_path.read_text(encoding="utf-8")
        metadata = extract_source_metadata(content)

        documents.append(
            {
                "filename": file_path.name,
                "content": content,
                "official_sources": extract_official_sources(content),
                "source_date": metadata["source_date"],
                "version_notes": metadata["version_notes"]
            }
        )

    return documents


def split_into_chunks(document):
    # Splits a Markdown document into smaller searchable chunks based on headings.
    filename = document["filename"]
    content = document["content"]
    official_sources = document["official_sources"]
    source_date = document["source_date"]
    version_notes = document["version_notes"]

    chunks = []
    current_title = "Introduction"
    current_lines = []

    def save_chunk(title, lines):
        chunk_content = "\n".join(lines).strip()
        plain_words = clean_words(chunk_content)

        if len(plain_words) < 8:
            return

        chunks.append(
            {
                "filename": filename,
                "section": title,
                "content": chunk_content,
                "official_sources": official_sources,
                "source_date": source_date,
                "version_notes": version_notes
            }
        )

    for line in content.splitlines():
        if line.startswith("#"):
            if current_lines:
                save_chunk(current_title, current_lines)

            current_title = line.replace("#", "").strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        save_chunk(current_title, current_lines)

    return chunks


def load_chunks():
    # Loads all documents and splits them into searchable chunks.
    documents = load_documents()
    all_chunks = []

    for document in documents:
        all_chunks.extend(split_into_chunks(document))

    return documents, all_chunks



def is_imy_gdpr_security_measures_question(question):
    # Detects GDPR security-measure questions that should prefer the dedicated
    # IMY security-measures source instead of general breach or authority files.
    q = normalize_query_text(question)

    direct_phrases = [
        "vad säger imy om säkerhetsåtgärder",
        "vilka säkerhetsåtgärder är viktiga enligt gdpr",
        "säkerhetsåtgärder enligt gdpr",
        "hur bör vi skydda personuppgifter",
        "hur ska vi skydda personuppgifter",
        "skydda personuppgifter",
        "skydd av personuppgifter",
        "kräver gdpr mfa",
        "kräver gdpr multifaktor",
        "mfa enligt gdpr",
        "kräver gdpr kryptering",
        "kryptering enligt gdpr",
        "does gdpr require mfa",
        "does gdpr require multi-factor",
        "does gdpr require multifactor",
        "mfa under gdpr",
        "does gdpr require encryption",
        "encryption under gdpr",
        "what security measures matter under gdpr",
        "security measures under gdpr",
        "what does imy say about security measures",
        "how should we protect personal data",
        "protect personal data",
    ]

    if contains_any(q, direct_phrases):
        return True

    security_terms = [
        "säkerhetsåtgärd", "säkerhetsåtgärder", "tekniska åtgärder",
        "organisatoriska åtgärder", "multifaktor", "kryptering",
        "åtkomstkontroll", "loggning", "säkerhetskopior", "skydda",
        "security measure", "security measures", "technical measures",
        "organizational measures", "organisational measures", "encryption",
        "multi-factor", "multifactor", "access control", "logging",
        "backups", "protect",
    ]
    gdpr_or_imy_terms = ["gdpr", "imy", "personuppgifter", "personal data", "dataskydd", "data protection"]

    has_security_marker = contains_any(q, security_terms) or has_mfa_term(q)
    return contains_any(q, gdpr_or_imy_terms) and has_security_marker


def is_gdpr_security_guidance_question(question):
    # Routes GDPR security, IMY/EDPB guidance, and breach assessment questions
    # to the richer GDPR/IMY/EDPB source file instead of generic incident or NIS2 files.
    q = normalize_query_text(question)

    direct_phrases = [
        "vad bör vi bedöma efter en personuppgiftsincident",
        "vad ska vi bedöma efter en personuppgiftsincident",
        "vad bör man bedöma efter en personuppgiftsincident",
        "bedöma efter en personuppgiftsincident",
        "efter en personuppgiftsincident",
        "what should we assess after a personal data breach",
        "what should an organization assess after a personal data breach",
        "what do we assess after a personal data breach",
        "what should be assessed after a personal data breach",
        "after a personal data breach",
        "how does gdpr connect to incident response",
        "how does gdpr relate to incident response",
        "gdpr connect to incident response",
        "gdpr incident response",
        "hur kopplas gdpr till incidenthantering",
        "hur hänger gdpr ihop med incidenthantering",
        "gdpr och incidenthantering",
        "vilka säkerhetsåtgärder är viktiga enligt gdpr",
        "säkerhetsåtgärder enligt gdpr",
        "what security measures matter under gdpr",
        "security measures under gdpr",
        "vad säger imy om säkerhetsåtgärder",
        "hur bör vi skydda personuppgifter",
        "hur ska vi skydda personuppgifter",
        "skydda personuppgifter",
        "does gdpr require mfa",
        "does gdpr require multi-factor",
        "does gdpr require multifactor",
        "does gdpr require encryption",
        "kräver gdpr mfa",
        "kräver gdpr kryptering",
        "data protection by design",
        "dataskydd genom design",
        "data protection by default",
        "dataskydd som standard",
    ]

    if contains_any(q, direct_phrases):
        return True

    gdpr_markers = [
        "gdpr", "imy", "edpb", "personuppgiftsincident", "personuppgifter",
        "personal data breach", "personal data", "data protection", "dataskydd",
        "registrerade", "rights and freedoms", "rättigheter och friheter",
        "säkerhetsåtgärder", "säkerhetsåtgärd", "kryptering",
        "encryption", "security measures", "skydda personuppgifter",
    ]

    assessment_markers = [
        "bedöma", "bedömning", "bedömas", "bedömt", "risk", "dokumentera",
        "dokumentation", "anmälan", "anmälas", "rapportera", "rapporteras",
        "säkerhetsåtgärder", "säkerhetsåtgärd", "incidenthantering",
        "assess", "assessment", "risk", "documentation", "document", "notify",
        "notification", "report", "reporting", "security measures", "incident response",
        "72 timmar", "72 hours", "informera", "informed", "affected individuals",
        "berörda personer", "design", "default", "require", "requires",
        "kräver", "protect", "skydda", "encryption", "kryptering",
    ]

    has_gdpr_marker = contains_any(q, gdpr_markers)
    has_assessment_marker = contains_any(q, assessment_markers) or has_mfa_term(q)
    return has_gdpr_marker and has_assessment_marker


def is_gdpr_assessment_or_security_file(filename):
    # User-facing GDPR/IMY/EDPB guidance should prefer these files.
    filename_lower = str(filename or "").lower()
    return (
        "gdpr_imy_edpb_security_guidance" in filename_lower
        or "imy_gdpr_security_measures" in filename_lower
        or "gdpr_personal_data_breach" in filename_lower
        or "imy_gdpr_supervision" in filename_lower
        or "gdpr_core_principles" in filename_lower
    )



def is_nis2_sector_scope_question(question):
    # Detects NIS2 / Swedish Cybersecurity Act scope questions.
    # These should use the dedicated sector-scope source, not the generic NIS2 file
    # and definitely not the GDPR/MFA route just because Swedish "omfattas" contains "mfa".
    q = normalize_query_text(question)

    direct_phrases = [
        "vilka sektorer omfattas av cybersäkerhetslagen",
        "vilka sektorer omfattas av nis2",
        "sektorer omfattas av cybersäkerhetslagen",
        "sektorer omfattas av nis2",
        "gäller nis2 för oss",
        "galler nis2 for oss",
        "omfattas vi av nis2",
        "omfattas vi av cybersäkerhetslagen",
        "omfattas kommuner av cybersäkerhetslagen",
        "omfattas kommuner av nis2",
        "omfattas regioner av cybersäkerhetslagen",
        "behöver vi anmäla oss enligt cybersäkerhetslagen",
        "behöver vi registrera oss enligt cybersäkerhetslagen",
        "ska vi anmäla oss enligt cybersäkerhetslagen",
        "ska vi registrera oss enligt cybersäkerhetslagen",
        "anmälan enligt cybersäkerhetslagen",
        "registrering enligt cybersäkerhetslagen",
        "väsentliga verksamhetsutövare",
        "viktiga verksamhetsutövare",
        "väsentlig verksamhetsutövare",
        "skillnaden mellan väsentliga och viktiga",
        "vad är skillnaden mellan väsentliga och viktiga",
        "bilaga 1",
        "bilaga 2",
        "bilaga 1 och bilaga 2",
        "vad är bilaga 1",
        "vad är bilaga 2",
        "vad är bilaga 1 och bilaga 2",
        "viktig verksamhetsutövare",
        "does nis2 apply to us",
        "are we covered by nis2",
        "which sectors are covered by nis2",
        "which sectors are covered by the swedish cybersecurity act",
        "are municipalities covered by the swedish cybersecurity act",
        "are municipalities covered by nis2",
        "are small companies covered by nis2",
        "small companies covered by nis2",
        "micro companies covered by nis2",
        "do we need to register under the swedish cybersecurity act",
        "registration under the swedish cybersecurity act",
        "essential entities",
        "important entities",
        "essential or important entities",
        "difference between essential and important",
        "what is the difference between essential and important",
        "annex 1",
        "annex 2",
        "annex 1 and annex 2",
        "what are annex 1 and annex 2",
        "what is annex 1",
        "what is annex 2",
    ]

    if contains_any(q, direct_phrases):
        return True

    nis2_terms = [
        "nis2", "cybersäkerhetslagen", "cybersecurity act",
        "swedish cybersecurity act",
    ]
    scope_terms = [
        "omfattas", "gäller", "sektor", "sektorer", "kommun", "kommuner",
        "region", "regioner", "kommunalförbund", "anmäla", "anmälan",
        "registrera", "registrering", "väsentlig", "väsentliga",
        "viktig", "viktiga", "verksamhetsutövare", "storlek", "små företag",
        "covered", "apply", "applies", "sector", "sectors", "municipality",
        "municipalities", "region", "regions", "register", "registration",
        "essential", "important", "entity", "entities", "small companies",
        "micro companies", "size", "scope", "annex", "annexes", "bilaga", "bilagor",
    ]

    return contains_any(q, nis2_terms) and contains_any(q, scope_terms)


def has_mfa_term(question):
    # Avoid substring bugs: the Swedish word "omfattas" contains the letters "mfa".
    # MFA should only trigger when it appears as its own token or as a real MFA synonym.
    q = normalize_query_text(question)
    words = set(clean_words(q))
    return (
        "mfa" in words
        or "multifaktor" in q
        or "multi-factor" in q
        or "multifactor" in q
        or "tvåfaktor" in q
        or "2fa" in words
    )


def is_case_library_context_question(question):
    # Detects questions that are mainly about case-library-style GDPR/cyber
    # examples, fines, tracking tools, wrong disclosure, or public data leaks.
    # These should not route to the generic incident-response playbook unless
    # the user is asking "what do we do now?".
    q = normalize_query_text(question).strip()

    terms = [
        "meta pixel", "meta-pixel", "facebook pixel", "tracking", "analytics",
        "hashed data", "hashade", "hashade uppgifter", "kry", "apoteket",
        "apohem", "avanza", "sportadmin", "trygg-hansa", "trygg hansa",
        "wrong email", "wrong recipient", "wrong attachment", "sent customer data",
        "email by mistake", "fel mejl", "fel e-post", "fel mottagare",
        "fel bilaga", "skickat kunduppgifter fel", "web form", "webform",
        "website form", "complaint form", "webbformulär", "formulär",
        "darknet", "dark web", "darkweb", "published on the darknet",
        "publicerad på darknet", "published data", "data published",
        "data is published", "what happens if data is published",
        "weak security", "security deficiencies", "security flaws",
        "bristande säkerhet", "säkerhetsbrister", "article 32",
        "what can weak security measures cost", "vad kan svaga säkerhetsåtgärder kosta",
        "what can a gdpr breach cost", "vad kan en gdpr-läcka kosta",
        "administrative fine", "sanktionsavgift", "gdpr fine", "fine",
    ]

    return contains_any(q, terms)

def get_target_source_file(question):
    # Routes clear questions to a specific knowledge file.
    question_lower = normalize_query_text(question).strip()

    # Case-library-style questions should use GDPR/data protection source context,
    # while the actual real-world examples are shown in the related-cases section.
    # This avoids weird combinations like a Meta Pixel question using the generic
    # incident-response playbook as the main source card.
    if is_case_library_context_question(question_lower):
        if contains_any(
            question_lower,
            [
                "wrong email", "wrong recipient", "wrong attachment",
                "sent customer data", "email by mistake", "fel mejl",
                "fel e-post", "fel mottagare", "fel bilaga",
                "data is published", "published on the darknet", "darknet",
                "dark web", "darkweb", "data breach", "personal data breach",
                "dataläcka", "personuppgiftsincident",
            ],
        ):
            return "gdpr_personal_data_breach.md"

        if contains_any(
            question_lower,
            [
                "weak security", "security deficiencies", "security flaws",
                "bristande säkerhet", "säkerhetsbrister", "article 32",
                "security measures", "säkerhetsåtgärder",
            ],
        ):
            return "imy_gdpr_security_measures.md"

        return "gdpr_imy_edpb_security_guidance.md"

    # NIS2 sector/scope/applicability questions should use the dedicated scope file
    # before generic NIS2 and before GDPR security routing.
    if is_nis2_sector_scope_question(question_lower):
        return "nis2_sector_scope_guidance.md"

    # IMY/GDPR security-measure questions should use the dedicated IMY security file
    # instead of the general breach/incident guidance source.
    if is_imy_gdpr_security_measures_question(question_lower):
        return "imy_gdpr_security_measures.md"

    # GDPR assessment/security questions are informational or compliance questions,
    # not generic incident playbook questions. Route them before incident routing.
    if is_gdpr_security_guidance_question(question_lower):
        return "gdpr_imy_edpb_security_guidance.md"

    if is_practical_incident_response_question(question):
        return "cyber_incident_response_playbook.md"

    if (
        "what is imy" in question_lower
        or "vad är imy" in question_lower
        or "vad gör imy" in question_lower
        or "what does imy do" in question_lower
        or question_lower == "imy"
        or "supervises gdpr" in question_lower
        or "supervise gdpr" in question_lower
        or "authority supervises gdpr" in question_lower
        or "authority handles gdpr" in question_lower
        or "which authority supervises gdpr" in question_lower
        or "which authority handles gdpr" in question_lower
        or "personal data protection authority" in question_lower
        or "privacy protection authority" in question_lower
        or "vilken myndighet hanterar gdpr" in question_lower
        or "vilken myndighet ansvarar för gdpr" in question_lower
        or "vilken myndighet har tillsyn över gdpr" in question_lower
        or "dataskyddsmyndighet" in question_lower
    ):
        return "imy_gdpr_supervision.md"

    if is_imy_gdpr_security_measures_question(question_lower):
        return "imy_gdpr_security_measures.md"

    if is_gdpr_security_guidance_question(question_lower):
        return "gdpr_imy_edpb_security_guidance.md"

    # Data breach questions should route to GDPR breach material before broader incident routing.
    if (
        "personal data breach" in question_lower
        or "data breach" in question_lower
        or "breach reported" in question_lower
        or "data breach reported" in question_lower
        or "72-hour" in question_lower
        or "72 hour" in question_lower
        or "breach notification" in question_lower
        or "personuppgiftsincident" in question_lower
        or "när måste en personuppgiftsincident rapporteras" in question_lower
        or "när ska en personuppgiftsincident anmälas" in question_lower
        or "rapportera personuppgiftsincident" in question_lower
        or "72 timmar" in question_lower
    ):
        return "gdpr_personal_data_breach.md"

    if (
        "nis2 incident reporting" in question_lower
        or "ransomware" in question_lower
        or "malware" in question_lower
        or "files are encrypted" in question_lower
        or "our files are encrypted" in question_lower
        or "files have been encrypted" in question_lower
        or "encrypted files" in question_lower
        or "cyber attack" in question_lower
        or "cyberattack" in question_lower
        or "security incident" in question_lower
        or "incident response" in question_lower
        or "after a cyber incident" in question_lower
        or "after ransomware" in question_lower
        or "after a ransomware" in question_lower
        or "what should a company do after" in question_lower
        or "what should an organization check after" in question_lower
        or "nis2-incidentrapportering" in question_lower
        or "nis2 incidents" in question_lower
        or "cybersecurity incident reporting" in question_lower
        or "incident reporting under nis2" in question_lower
        or "incident reporting under the cybersecurity act" in question_lower
        or "swedish cybersecurity act incident reporting" in question_lower
        or "report cybersecurity incident" in question_lower
        or "reported under nis2" in question_lower
        or "reporting duties" in question_lower
        or "can an incident need to be reported under both nis2 and gdpr" in question_lower
        or "incidentrapportering enligt nis2" in question_lower
        or "incidentrapportering enligt cybersäkerhetslagen" in question_lower
        or "rapportera cybersäkerhetsincident" in question_lower
        or "rapporteras enligt både nis2 och gdpr" in question_lower
        or "både nis2 och gdpr" in question_lower
    ):
        return "nis2_incident_reporting.md"

    if (
        "personal data breach" in question_lower
        or "breach reported" in question_lower
        or "data breach reported" in question_lower
        or "72-hour" in question_lower
        or "72 hour" in question_lower
        or "breach notification" in question_lower
        or "personuppgiftsincident" in question_lower
        or "när måste en personuppgiftsincident rapporteras" in question_lower
        or "när ska en personuppgiftsincident anmälas" in question_lower
        or "rapportera personuppgiftsincident" in question_lower
        or "72 timmar" in question_lower
    ):
        return "gdpr_personal_data_breach.md"

    if (
        "gdpr principles" in question_lower
        or "gdpr principle" in question_lower
        or "what are the gdpr principles" in question_lower
        or "gdpr-principer" in question_lower
        or "gdpr principer" in question_lower
        or "vilka är gdpr-principerna" in question_lower
        or "vilka är gdpr principerna" in question_lower
    ):
        return "gdpr_core_principles.md"

    if (
        question_lower == "gdpr"
        or "what is gdpr" in question_lower
        or "vad är gdpr" in question_lower
    ):
        return "gdpr_core_principles.md"

    if (
        "nis2" in question_lower
        or "what is nis2" in question_lower
        or "vad är nis2" in question_lower
        or "cybersecurity act" in question_lower
        or "cybersäkerhetslagen" in question_lower
    ):
        return "nis2_cybersecurity_law.md"

    if (
        "dataintrång" in question_lower
        or "vad är dataintrång" in question_lower
        or "data intrusion" in question_lower
        or "unauthorized access" in question_lower
        or "obehörig åtkomst" in question_lower
        or "är obehörig åtkomst olagligt" in question_lower
    ):
        return "cybercrime_dataintrang.md"

    if (
        "cyber resilience act" in question_lower
        or "products with digital elements" in question_lower
        or "product security" in question_lower
        or "vad är cyber resilience act" in question_lower
        or "cyberresiliensakten" in question_lower
        or "produkter med digitala element" in question_lower
        or "produktsäkerhet" in question_lower
    ):
        return "eu_cyber_resilience_act.md"

    if (
        "attacks against information systems" in question_lower
        or "eu law about attacks" in question_lower
        or "eu cybercrime" in question_lower
        or "attacker mot informationssystem" in question_lower
        or "eu-regler om attacker" in question_lower
        or "eu cyberbrott" in question_lower
    ):
        return "eu_attacks_against_information_systems.md"

    if (
        "dora" in question_lower
        or "vad är dora" in question_lower
        or "digital operational resilience act" in question_lower
        or "digital operational resilience" in question_lower
        or "ict risk management" in question_lower
        or "ict third-party risk" in question_lower
        or "third-party ict risk" in question_lower
        or "financial sector cybersecurity" in question_lower
        or "financial sector cyber" in question_lower
        or "digital operativ motståndskraft" in question_lower
        or "tredjepartsrisk enligt dora" in question_lower
        or "ict-risk enligt dora" in question_lower
        or "finansiell cybersäkerhet" in question_lower
    ):
        return "eu_dora_digital_operational_resilience.md"

    return None


def search_chunks(question, chunks):
    # Searches document chunks using keyword matching, intent boosts, and source routing.
    stopwords = {
        "what", "when", "where", "which", "who", "why", "how",
        "is", "are", "was", "were", "be", "been", "being",
        "a", "an", "the", "to", "in", "on", "of", "for", "and",
        "or", "with", "from", "this", "that", "it", "does", "do",
        "must", "should", "can"
    }

    useful_sections = {
        "key idea",
        "reporting to imy",
        "main authority",
        "important points",
        "incident reporting",
        "legal reference",
        "practical explanation",
        "cybersecurity connection",
        "swedish connection",
        "relationship with gdpr breach reporting",
        "third-party ict risk",
        "suspected hacking first steps",
        "suspected data leak first steps",
        "ransomware first steps",
        "compromised account first steps",
        "first 15 minutes checklist",
        "first hour checklist",
        "first 24 hours checklist",
        "first 72 hours checklist",
        "swedish step-by-step answer for suspected hacking",
        "english step-by-step answer for suspected hacking",
        "swedish step-by-step answer for suspected data leak",
        "english step-by-step answer for suspected data leak",
        "technical containment examples",
        "evidence preservation examples",
        "covered sectors",
        "swedish covered sectors",
        "size assessment",
        "swedish size assessment",
        "public administration, municipalities and regions",
        "swedish public administration, municipalities and regions",
        "registration",
        "swedish registration",
        "essential and important entities",
        "swedish essential and important entities",
        "cyberlex answer guidance",
        "swedish cyberlex answer guidance"
    }

    weak_sections = {
        "useful questions",
        "source",
        "official source",
        "source date",
        "version notes",
        "disclaimer",
        "introduction",
        "topic"
    }

    question_lower = normalize_query_text(question)
    target_source_file = get_target_source_file(question)

    # If routing points to a newer source file that is not present in data/,
    # do not penalize every other file. This keeps CyberLex usable while the
    # knowledge base is being expanded. Because apparently missing scrolls
    # should not make the whole library catch fire.
    if target_source_file:
        available_source_files = {str(chunk.get("filename", "")).lower() for chunk in chunks}
        if target_source_file.lower() not in available_source_files:
            target_source_file = None

    question_words = [
        word for word in clean_words(question)
        if len(word) > 2 and word not in stopwords
    ]

    expanded_terms = expand_question_terms(question)

    for term in expanded_terms:
        expanded_words = [
            word for word in clean_words(term)
            if len(word) > 2 and word not in stopwords
        ]
        question_words.extend(expanded_words)

    question_words = list(dict.fromkeys(question_words))

    results = []

    for chunk in chunks:
        filename = chunk["filename"]
        filename_lower = filename.lower()
        chunk_words = clean_words(chunk["content"])
        chunk_text = chunk["content"].lower()
        section_text = chunk["section"].lower()

        score = 0

        if target_source_file:
            if filename_lower == target_source_file.lower():
                score += 180
            else:
                # Do not punish related GDPR/IMY/EDPB files when the preferred
                # source exists only as one part of a broader GDPR answer.
                if is_gdpr_security_guidance_question(question_lower) and is_gdpr_assessment_or_security_file(filename_lower):
                    score += 60
                else:
                    score -= 80

        if is_gdpr_security_guidance_question(question_lower):
            if "imy_gdpr_security_measures" in filename_lower and is_imy_gdpr_security_measures_question(question_lower):
                score += 420
            elif "gdpr_imy_edpb_security_guidance" in filename_lower:
                score += 320
            elif "gdpr_personal_data_breach" in filename_lower:
                score += 90
            elif "imy_gdpr_supervision" in filename_lower or "gdpr_core_principles" in filename_lower:
                score += 60
            if "cyber_incident_response_playbook" in filename_lower or "nis2_incident_reporting" in filename_lower:
                score -= 140

        for word in question_words:
            if word in chunk_words:
                score += 4

            if word in section_text:
                score += 3

            if word in chunk_text:
                score += 1

        for useful_section in useful_sections:
            if useful_section in section_text:
                score += 5

        for weak_section in weak_sections:
            if weak_section in section_text:
                score -= 10

        if is_gdpr_security_guidance_question(question_lower):
            if "imy_gdpr_security_measures" in filename_lower and is_imy_gdpr_security_measures_question(question_lower):
                score += 170
            if "gdpr_imy_edpb_security_guidance" in filename_lower:
                score += 90
            if "practical explanation" in section_text or "swedish practical explanation" in section_text:
                score += 35
            if "data protection by design" in section_text or "swedish data protection" in section_text:
                score += 35
            if "relationship with incident response" in section_text:
                score += 35
            if "incident response playbook" in filename_lower or "cyber_incident_response_playbook" in filename_lower:
                score -= 80
            if "nis2_incident_reporting" in filename_lower:
                score -= 35

        if "authority" in question_lower or "handles" in question_lower or "supervises" in question_lower:
            if "main authority" in section_text:
                score += 25
            if "imy" in chunk_text or "integritetsskyddsmyndigheten" in chunk_text:
                score += 8

        if (
            "ransomware" in question_lower
            or "malware" in question_lower
            or "cyber attack" in question_lower
            or "cyberattack" in question_lower
            or "security incident" in question_lower
            or "cyber incident" in question_lower
            or "incident response" in question_lower
        ):
            if "nis2_incident_reporting" in filename_lower:
                score += 60
            if "incident reporting" in section_text:
                score += 25
            if "relationship with gdpr breach reporting" in section_text:
                score += 20
            if "practical explanation" in section_text:
                score += 15
            if "cybersecurity" in chunk_text:
                score += 10
            if "personal data" in chunk_text:
                score += 8


        if is_practical_incident_response_question(question):
            if "cyber_incident_response_playbook" in filename_lower:
                score += 120
            if "first steps" in section_text:
                score += 35
            if "step-by-step" in section_text:
                score += 35
            if "checklist" in section_text:
                score += 25
            if "preserve evidence" in chunk_text or "bevara" in chunk_text:
                score += 20
            if "isolate" in chunk_text or "isolera" in chunk_text:
                score += 20
            if "cert-se" in chunk_text:
                score += 15
            if "imy" in chunk_text:
                score += 10
            if "nis2" in chunk_text or "cybersäkerhetslagen" in chunk_text:
                score += 10

        if is_gdpr_security_guidance_question(question):
            if "imy_gdpr_security_measures" in filename_lower and is_imy_gdpr_security_measures_question(question):
                score += 220
            if "gdpr_imy_edpb_security_guidance" in filename_lower:
                score += 140
            if "gdpr_personal_data_breach" in filename_lower:
                score += 90
            if "gdpr_core_principles" in filename_lower or "imy_gdpr_supervision" in filename_lower:
                score += 60
            if "practical explanation" in section_text or "data protection by design" in section_text:
                score += 45
            if "relationship with incident response" in section_text:
                score += 45
            if "swedish practical explanation" in section_text or "swedish relationship" in section_text:
                score += 35
            if "personal data breach" in section_text or "personuppgiftsincident" in section_text:
                score += 30
            if "cyber_incident_response_playbook" in filename_lower or "nis2_incident_reporting" in filename_lower:
                score -= 80

        if is_suspicious_login_question(question):
            if "suspicious login activity first steps" in section_text:
                score += 100
            if "swedish suspicious login activity first steps" in section_text:
                score += 100
            if "suspicious login assessment checklist" in section_text:
                score += 60
            if "swedish suspicious login assessment checklist" in section_text:
                score += 60
            if "suspected hacking" in section_text:
                score -= 35
            if "compromised account" in section_text:
                score -= 20

        if is_suspicious_email_question(question):
            if "suspicious email and phishing first steps" in section_text:
                score += 100
            if "swedish suspicious email and phishing first steps" in section_text:
                score += 100
            if "suspicious email assessment checklist" in section_text:
                score += 60
            if "swedish suspicious email assessment checklist" in section_text:
                score += 60
            if "suspected hacking" in section_text:
                score -= 35
            if "compromised account" in section_text:
                score -= 20

        if is_suspected_hacking_question(question):
            if "suspected hacking first steps" in section_text:
                score += 45
            if "swedish step-by-step answer for suspected hacking" in section_text:
                score += 45
            if "english step-by-step answer for suspected hacking" in section_text:
                score += 45
            if "unauthorized access first steps" in section_text:
                score += 25

        if is_data_leak_response_question(question):
            if "suspected data leak first steps" in section_text:
                score += 45
            if "data leak assessment checklist" in section_text:
                score += 35
            if "swedish step-by-step answer for suspected data leak" in section_text:
                score += 45
            if "english step-by-step answer for suspected data leak" in section_text:
                score += 45

        if is_compromised_account_question(question):
            if "compromised account first steps" in section_text:
                score += 50
            if "compromised account checklist" in section_text:
                score += 35

        if is_ransomware_response_question(question) and is_practical_incident_response_question(question):
            if "ransomware first steps" in section_text:
                score += 55
            if "ransomware assessment checklist" in section_text:
                score += 35

        if is_nis2_sector_scope_question(question_lower):
            if "nis2_sector_scope_guidance" in filename_lower:
                score += 420
            elif "nis2_cybersecurity_law" in filename_lower:
                score += 60
            elif "nis2_incident_reporting" in filename_lower:
                score -= 60
            elif is_gdpr_assessment_or_security_file(filename_lower):
                score -= 140

            if any(key in section_text for key in [
                "covered sectors", "swedish covered sectors", "size assessment",
                "public administration", "municipalities", "registration",
                "essential and important", "practical explanation", "cyberlex answer guidance"
            ]):
                score += 80

        if "nis2" in question_lower or "cybersecurity act" in question_lower or "cybersäkerhetslagen" in question_lower:
            if "nis2" in filename_lower:
                score += 50
            if "key idea" in section_text:
                score += 15
            if "important points" in section_text:
                score += 15
            if "incident reporting" in section_text and not is_nis2_sector_scope_question(question_lower):
                score += 10

        if "dataintrång" in question_lower or "data intrusion" in question_lower or "unauthorized access" in question_lower:
            if "cybercrime_dataintrang" in filename_lower:
                score += 50
            if "key idea" in section_text:
                score += 15
            if "legal reference" in section_text:
                score += 15
            if "practical explanation" in section_text:
                score += 15

        if "gdpr principles" in question_lower or "gdpr principle" in question_lower or "principles" in question_lower or "principer" in question_lower:
            if "important points" in section_text:
                score += 25
            if "key idea" in section_text:
                score += 15
            if "gdpr" in chunk_text:
                score += 10

        if "what is gdpr" in question_lower or "vad är gdpr" in question_lower:
            if "key idea" in section_text:
                score += 20
            if "main authority" in section_text:
                score += 10
            if "gdpr" in chunk_text:
                score += 10

        if "attacks against information systems" in question_lower or "information systems" in question_lower or "eu cybercrime" in question_lower or "informationssystem" in question_lower:
            if "key idea" in section_text:
                score += 20
            if "important points" in section_text:
                score += 15
            if "swedish connection" in section_text:
                score += 10

        if "cyber resilience act" in question_lower or "products with digital elements" in question_lower or "product security" in question_lower:
            if "key idea" in section_text:
                score += 20
            if "important points" in section_text:
                score += 15
            if "cybersecurity connection" in section_text:
                score += 10

        if "dora" in question_lower:
            if "dora" in filename_lower:
                score += 50
            if "key idea" in section_text:
                score += 15
            if "incident reporting" in section_text:
                score += 10
            if "third-party ict risk" in section_text:
                score += 10

        if score > 0:
            results.append(
                {
                    "filename": chunk["filename"],
                    "section": chunk["section"],
                    "content": chunk["content"],
                    "score": score,
                    "official_sources": chunk["official_sources"],
                    "source_date": chunk["source_date"],
                    "version_notes": chunk["version_notes"]
                }
            )

    results.sort(key=lambda item: item["score"], reverse=True)
    return results



def get_incident_source_context_profile(question):
    # Returns the incident subtype for source-context filtering.
    # This keeps the visible "Relevant source context" focused on the user's
    # exact incident type instead of showing nearby incident playbook sections.
    question = str(question or "")

    if is_gdpr_security_guidance_question(question):
        # GDPR security and IMY guidance questions are compliance/source questions,
        # not practical incident-response subtypes. Returning None prevents the
        # incident playbook filter from dragging in hacking or login source cards.
        return None

    if is_suspicious_link_question(question):
        return "suspicious_link"

    if is_suspicious_email_question(question):
        return "suspicious_email"

    if is_suspicious_login_question(question):
        return "suspicious_login"

    if is_compromised_account_question(question):
        return "compromised_account"

    if is_data_leak_response_question(question):
        return "data_leak"

    if is_ransomware_or_malware_question(question):
        return "ransomware_or_malware"

    if is_suspected_hacking_question(question):
        return "suspected_hacking"

    return None


def is_incident_source_context_match(result, question):
    # Returns True when a source-context result belongs to the same incident
    # subtype as the user's practical incident-response question.
    # Search ranking may still use broader sections, but the visible source
    # context should not make CyberLex look confused by mixing phishing,
    # login, data-leak, hacking, ransomware, and account-compromise cards together.
    profile = get_incident_source_context_profile(question)

    if not profile:
        return True

    section = str(result.get("section", "")).lower().strip()
    filename = str(result.get("filename", "")).lower().strip()

    # Strict subtype filtering is only for the incident-response playbook.
    # For practical incident questions, the normal source context should focus
    # on the exact playbook subtype instead of mixing in other playbook incidents.
    if "cyber_incident_response_playbook" not in filename:
        return False

    profiles = {
        "suspicious_link": {
            "allow": [
                "suspicious link",
                "suspicious email",
                "phishing",
                "misstänkt länk",
                "skadlig länk",
                "nätfiske",
            ],
            "block": [
                "suspicious login",
                "misstänkt inloggning",
                "data leak",
                "dataläcka",
                "ransomware",
                "malware",
                "suspected hacking",
                "hacking",
                "intrusion",
                "compromised account",
                "komprometterat konto",
            ],
        },
        "suspicious_email": {
            "allow": [
                "suspicious email",
                "phishing",
                "misstänkt mejl",
                "misstänkt e-post",
                "nätfiske",
            ],
            "block": [
                "suspicious login",
                "misstänkt inloggning",
                "suspected hacking",
                "hacking",
                "intrusion",
                "data leak",
                "dataläcka",
                "ransomware",
                "malware",
                "compromised account",
                "komprometterat konto",
            ],
        },
        "suspicious_login": {
            "allow": [
                "suspicious login",
                "login activity",
                "misstänkt inloggning",
                "ovanlig inloggning",
            ],
            "block": [
                "suspicious email",
                "phishing",
                "misstänkt mejl",
                "data leak",
                "dataläcka",
                "ransomware",
                "malware",
                "compromised account",
                "komprometterat konto",
                "suspected hacking",
            ],
        },
        "compromised_account": {
            "allow": [
                "compromised account",
                "komprometterat konto",
                "account checklist",
            ],
            "block": [
                "suspicious email",
                "phishing",
                "suspicious login",
                "data leak",
                "dataläcka",
                "ransomware",
                "malware",
            ],
        },
        "data_leak": {
            "allow": [
                "data leak",
                "dataläcka",
            ],
            "block": [
                "suspicious email",
                "phishing",
                "suspicious login",
                "suspected hacking",
                "hacking",
                "intrusion",
                "ransomware",
                "malware",
                "compromised account",
            ],
        },
        "ransomware_or_malware": {
            "allow": [
                "ransomware",
                "malware",
                "encrypted files",
                "krypterade filer",
                "filer har krypterats",
            ],
            "block": [
                "suspicious email",
                "phishing",
                "suspicious login",
                "data leak",
                "dataläcka",
                "compromised account",
            ],
        },
        "suspected_hacking": {
            "allow": [
                "suspected hacking",
                "hacking",
                "intrusion",
                "unauthorized access",
                "obehörig åtkomst",
                "misstänkt hackning",
                "misstänkt intrång",
            ],
            "block": [
                "suspicious email",
                "phishing",
                "suspicious login",
                "data leak",
                "dataläcka",
                "ransomware",
                "malware",
                "compromised account",
            ],
        },
    }

    rule = profiles.get(profile)

    if not rule:
        return True

    if any(marker in section for marker in rule["block"]):
        return False

    return any(marker in section for marker in rule["allow"])


def filter_source_context_by_incident_type(search_results, question):
    # Strictly filters visible source-context cards for practical incident
    # questions when CyberLex detects a clear incident subtype.
    # If the strict filter finds nothing, fall back to the original results
    # so the UI never becomes empty because of one odd source heading.
    if not is_practical_incident_response_question(question):
        return search_results

    profile = get_incident_source_context_profile(question)

    if not profile:
        return search_results

    focused_results = [
        result for result in search_results
        if is_incident_source_context_match(result, question)
    ]

    if focused_results:
        return focused_results

    return search_results


def get_nis2_scope_context_profile(question):
    # Returns the exact NIS2 scope subtype for visible source-context cards.
    # This is stricter than normal search routing because the source context is
    # meant to explain the answer, not show every nearby NIS2 section like a
    # bureaucratic confetti cannon.
    q = normalize_query_text(question)

    if contains_any(q, ["kommun", "kommuner", "region", "regioner", "kommunalförbund", "municipality", "municipalities", "public administration"]):
        return "municipality"

    if contains_any(q, ["anmäla", "anmälan", "registrera", "registrering", "register", "registration"]):
        return "registration"

    if contains_any(q, ["små företag", "mikro", "small companies", "small company", "micro companies", "micro company"]):
        return "small_company"

    if contains_any(q, ["bilaga 1", "bilaga 2", "bilagor", "annex 1", "annex 2", "annexes", "annex"]):
        return "annexes"

    if contains_any(q, ["väsentlig", "väsentliga", "viktig", "viktiga", "essential", "important", "entities", "entity", "verksamhetsutövare"]):
        return "essential_important"

    # Sector-list questions should win over broad apply/scope wording.
    if contains_any(q, ["vilka sektorer", "sektorer omfattas", "which sectors", "covered sectors", "sector", "sectors", "sektor", "sektorer"]):
        return "sectors"

    if contains_any(q, ["gäller", "galler", "omfattas", "apply", "applies", "covered", "scope", "oss", "us"]):
        return "applies"

    return "scope_general"


def get_nis2_scope_allowed_sections(question):
    # Strict allow-list for displayed NIS2 source-context sections.
    # Search can still use the whole file, but the user-facing context should
    # not repeat the same generic cards for every NIS2 question.
    profile = get_nis2_scope_context_profile(question)

    allowed = {
        "sectors": [
            "covered sectors",
            "swedish covered sectors",
        ],
        "applies": [
            "practical explanation",
            "swedish practical explanation",
            "cyberlex answer guidance",
            "swedish cyberlex answer guidance",
        ],
        "municipality": [
            "public administration, municipalities and regions",
            "swedish public administration, municipalities and regions",
        ],
        "registration": [
            "registration",
            "swedish registration",
        ],
        "small_company": [
            "size assessment",
            "swedish size assessment",
            "essential and important entities",
            "swedish essential and important entities",
        ],
        "essential_important": [
            "essential and important entities",
            "swedish essential and important entities",
            "annex 1 and annex 2",
            "swedish annex 1 and annex 2",
            "bilaga 1 och bilaga 2",
        ],
        "annexes": [
            "annex 1 and annex 2",
            "swedish annex 1 and annex 2",
            "bilaga 1 och bilaga 2",
            "covered sectors",
            "swedish covered sectors",
        ],
        "scope_general": [
            "practical explanation",
            "swedish practical explanation",
            "cyberlex answer guidance",
            "swedish cyberlex answer guidance",
            "covered sectors",
            "swedish covered sectors",
            "size assessment",
            "swedish size assessment",
        ],
    }

    return allowed.get(profile, allowed["scope_general"])


def is_nis2_scope_allowed_context_section(result, question):
    filename = str(result.get("filename", "")).lower().strip()
    section = str(result.get("section", "")).lower().strip()

    if "nis2_sector_scope_guidance" not in filename:
        return False

    allowed_sections = get_nis2_scope_allowed_sections(question)
    return any(section == allowed or allowed in section for allowed in allowed_sections)


def get_nis2_scope_max_context_cards(question):
    # Specific NIS2 questions usually need only one source card. Broad scope
    # questions can show two because the answer depends on several facts.
    profile = get_nis2_scope_context_profile(question)
    if profile in {"sectors", "municipality", "registration", "essential_important", "annexes"}:
        return 1
    return 2


def get_nis2_scope_source_context_priority(result, question, language="English"):
    # Gives NIS2 scope/source-context cards a subtype-specific priority.
    # This keeps "covered sectors", "municipalities", "registration", and
    # "does NIS2 apply to us" from all showing the same generic source cards.
    q = normalize_query_text(question)
    filename = str(result.get("filename", "")).lower()
    section = str(result.get("section", "")).lower().strip()
    use_swedish = language == "Svenska"

    if "nis2_sector_scope_guidance" not in filename:
        return -1000

    if not is_nis2_scope_allowed_context_section(result, question):
        return -500

    profile = get_nis2_scope_context_profile(question)
    priority = 100

    exact_priorities = {
        "sectors": {
            "covered sectors": 900,
            "swedish covered sectors": 900,
        },
        "applies": {
            "practical explanation": 850,
            "swedish practical explanation": 850,
            "cyberlex answer guidance": 760,
            "swedish cyberlex answer guidance": 760,
        },
        "municipality": {
            "public administration, municipalities and regions": 900,
            "swedish public administration, municipalities and regions": 900,
        },
        "registration": {
            "registration": 900,
            "swedish registration": 900,
        },
        "small_company": {
            "size assessment": 900,
            "swedish size assessment": 900,
            "essential and important entities": 720,
            "swedish essential and important entities": 720,
        },
        "essential_important": {
            "essential and important entities": 900,
            "swedish essential and important entities": 900,
            "annex 1 and annex 2": 650,
            "swedish annex 1 and annex 2": 650,
            "bilaga 1 och bilaga 2": 650,
        },
        "annexes": {
            "annex 1 and annex 2": 950,
            "swedish annex 1 and annex 2": 950,
            "bilaga 1 och bilaga 2": 950,
            "covered sectors": 600,
            "swedish covered sectors": 600,
        },
        "scope_general": {
            "practical explanation": 850,
            "swedish practical explanation": 850,
            "cyberlex answer guidance": 760,
            "swedish cyberlex answer guidance": 760,
            "covered sectors": 550,
            "swedish covered sectors": 550,
            "size assessment": 520,
            "swedish size assessment": 520,
        },
    }

    for marker, value in exact_priorities.get(profile, exact_priorities["scope_general"]).items():
        if section == marker or marker in section:
            priority += value
            break

    if use_swedish and section.startswith("swedish "):
        priority += 60
    elif not use_swedish and not section.startswith("swedish "):
        priority += 60

    return priority


def get_source_context_section_priority(question, section_name, language="English"):
    # Gives extra priority to source context sections that match the user's
    # exact incident subtype. This affects only the displayed source context,
    # not the main legal/source search result.
    question = str(question or "")
    section = str(section_name or "").lower().strip()
    use_swedish = language == "Svenska"

    priority = 0

    def language_bonus():
        if use_swedish and section.startswith("swedish "):
            return 20
        if not use_swedish and not section.startswith("swedish "):
            return 10
        return 0

    if is_nis2_sector_scope_question(question):
        if "covered sectors" in section:
            priority += 120
        if "public administration" in section or "municipalities" in section or "regions" in section:
            priority += 120
        if "registration" in section:
            priority += 120
        if "size assessment" in section:
            priority += 110
        if "essential and important" in section:
            priority += 100
        if "annex 1" in section or "annex 2" in section or "bilaga 1" in section or "bilaga 2" in section:
            priority += 130
        if "practical explanation" in section or "cyberlex answer guidance" in section:
            priority += 90
        if "gdpr" in section or "personal data breach" in section:
            priority -= 120

    elif is_gdpr_security_guidance_question(question):
        if "practical explanation" in section or "data protection by design" in section or "relationship with incident response" in section:
            priority += 120
        if "personal data breach" in section or "personuppgiftsincident" in section:
            priority += 80
        if "suspected hacking" in section or "ransomware" in section or "suspicious login" in section:
            priority -= 80

    elif is_suspicious_link_question(question):
        if "suspicious link" in section or "misstänkt länk" in section or "phishing" in section or "nätfiske" in section:
            priority += 140
        if "suspicious email" in section or "misstänkt mejl" in section:
            priority += 20
        if "suspected hacking" in section:
            priority -= 50
        if "suspicious login" in section:
            priority -= 40

    elif is_suspicious_login_question(question):
        if "suspicious login" in section or "misstänkt inloggning" in section:
            priority += 120
        if "login activity first steps" in section:
            priority += 40
        if "login assessment checklist" in section:
            priority += 25
        if "compromised account" in section:
            priority -= 30
        if "suspected hacking" in section:
            priority -= 50

    elif is_suspicious_email_question(question):
        if "suspicious email" in section or "phishing" in section or "misstänkt mejl" in section:
            priority += 120
        if "email and phishing first steps" in section:
            priority += 40
        if "email assessment checklist" in section:
            priority += 25
        if "compromised account" in section:
            priority -= 30
        if "suspected hacking" in section:
            priority -= 50

    elif is_compromised_account_question(question):
        if "compromised account" in section or "komprometterat konto" in section:
            priority += 120
        if "account first steps" in section:
            priority += 40
        if "account checklist" in section:
            priority += 25
        if "suspicious login" in section:
            priority += 10
        if "suspected hacking" in section:
            priority -= 25

    elif is_data_leak_response_question(question):
        if "data leak" in section or "dataläcka" in section:
            priority += 120
        if "data leak assessment checklist" in section:
            priority += 40
        if "suspected hacking" in section:
            priority -= 40

    elif is_ransomware_or_malware_question(question):
        if "ransomware" in section or "malware" in section:
            priority += 120
        if "first 15 minutes" in section or "first hour" in section:
            priority += 15
        if "suspected hacking" in section:
            priority -= 20

    elif is_practical_incident_response_question(question):
        if "suspected hacking" in section or "unauthorized access" in section:
            priority += 80
        if "first 15 minutes" in section or "first hour" in section:
            priority += 20

    if priority > 0:
        priority += language_bonus()

    return priority


def prioritize_source_context_results(search_results, question=None, language="English"):
    # Sorts source-context cards by topic-specific relevance first, then normal
    # keyword relevance score. If there are strong exact-topic matches, those
    # are shown before broader fallback sections.
    if not question:
        return search_results

    scored_results = []
    for result in search_results:
        section_name = result.get("section", "")
        topic_priority = get_source_context_section_priority(question, section_name, language)
        scored_results.append((topic_priority, result.get("score", 0), result))

    has_topic_specific_match = any(topic_priority > 0 for topic_priority, _, _ in scored_results)

    if has_topic_specific_match:
        topic_matches = [
            (topic_priority, score, result)
            for topic_priority, score, result in scored_results
            if topic_priority > 0
        ]
        fallback_matches = [
            (topic_priority, score, result)
            for topic_priority, score, result in scored_results
            if topic_priority <= 0
        ]

        topic_matches.sort(key=lambda item: (item[0], item[1]), reverse=True)
        fallback_matches.sort(key=lambda item: item[1], reverse=True)

        return [result for _, _, result in topic_matches + fallback_matches]

    return search_results


def is_checklist_section(section_name):
    # Source-context cards should not duplicate the CyberLex assessment checklist.
    # Checklist sections can still be used for search scoring, but they are hidden
    # from the supporting source preview unless there is no better source.
    section = str(section_name or "").lower()
    return "checklist" in section or "checklista" in section



def swedish_language_score(text):
    # Scores how Swedish a source excerpt looks. This is intentionally
    # stricter than merely finding one Swedish word, because many CyberLex
    # source sections mix English legal text with Swedish names such as
    # cybersäkerhetslagen. One Swedish word should not make an English
    # excerpt appear in the Swedish UI.
    sample = f" {str(text or '').lower()} "

    common_words = [
        " och ", " eller ", " inte ", " som ", " att ", " är ", " det ",
        " den ", " detta ", " denna ", " för ", " med ", " till ",
        " från ", " kan ", " ska ", " bör ", " måste ", " har ",
        " personuppgift", " myndighet", " käll", " anmäl", " tillsyn",
        " vägledning", " rättighet", " lag", " ansvar", " behandl",
        " sverige", " svensk", " svenska", " organisationen", " krävs",
    ]

    score = 0
    score += sum(sample.count(marker) for marker in common_words) * 2

    # Swedish letters help, but they are not enough alone because Swedish names
    # can appear inside otherwise English source text.
    score += min(sample.count("å") + sample.count("ä") + sample.count("ö"), 3)

    return score


def english_language_score(text):
    # Scores how English a source excerpt looks.
    sample = f" {str(text or '').lower()} "

    common_words = [
        " the ", " and ", " or ", " not ", " this ", " that ",
        " for ", " with ", " from ", " should ", " must ", " may ",
        " can ", " is ", " are ", " personal data", " data protection",
        " supervision", " authority", " guidance", " organization",
        " organisation", " source", " question", " reporting",
        " compliance", " relevant", " handles", " works with",
        " is used", " implemented", " purpose", " across", " european",
        " cybersecurity", " management", " duties", " sectors",
    ]

    return sum(sample.count(marker) for marker in common_words) * 2


def looks_swedish_text(text):
    # A source excerpt counts as Swedish only when Swedish signals beat
    # English signals. This prevents mixed English/Swedish legal snippets from
    # leaking into the Swedish UI.
    swedish_score = swedish_language_score(text)
    english_score = english_language_score(text)
    return swedish_score >= 3 and swedish_score > english_score


def looks_english_text(text):
    # A source excerpt counts as English only when English signals beat Swedish
    # signals. Mixed text follows the dominant language.
    swedish_score = swedish_language_score(text)
    english_score = english_language_score(text)
    return english_score >= 3 and english_score >= swedish_score


def is_low_value_source_context_section(section_name):
    # These sections are useful internally for routing and testing, but they are
    # not helpful as user-facing source context during a demo or test run.
    section = str(section_name or "").lower().strip()
    low_value_markers = [
        "useful questions",
        "exempelfrågor",
        "topic",
        "ämne",
        "introduction",
        "introduktion",
        "official source",
        "officiella källor",
        "source metadata",
        "källmetadata",
        "source date",
        "version notes",
        "disclaimer",
    ]
    return any(marker in section for marker in low_value_markers)



def is_noise_source_context_line(stripped_line):
    # Removes separators and example-question bullets from source previews.
    # Those lines are useful in Markdown authoring, but look broken in the UI.
    stripped = str(stripped_line or "").strip()
    if not stripped:
        return False

    if stripped in {"---", "----", "-----", "***", "___"}:
        return True

    without_bullet = re.sub(r"^[-*•]\s*", "", stripped).strip()
    lower = without_bullet.lower()

    question_starters = [
        "what should", "what do", "when must", "when should", "how do", "how should",
        "vad ska", "vad bör", "vad gör", "hur gör", "hur ska", "hur bör", "när måste", "när ska",
    ]

    if without_bullet.endswith("?") and any(lower.startswith(starter) for starter in question_starters):
        return True

    return False


def clean_source_context_tail(text):
    # Removes leftover Markdown separators and repeated blank tail junk after compacting.
    lines = [line.rstrip() for line in str(text or "").splitlines()]

    while lines and not lines[-1].strip():
        lines.pop()

    while lines and lines[-1].strip() in {"---", "----", "-----", "***", "___"}:
        lines.pop()
        while lines and not lines[-1].strip():
            lines.pop()

    return "\n".join(lines).strip()

def localize_source_excerpt_for_ui(excerpt, language="English"):
    # Keeps the visible UI language consistent.
    # CyberLex should not silently auto-translate legal/source excerpts, because
    # that could make a translated sentence look like exact source text.
    #
    # Earlier versions showed a developer-style warning when a source section
    # existed only in the other language. That was accurate, but ugly in a
    # user-facing test run. The cleaner behavior is to hide that source-context
    # card and let the answer, official links, metadata, checklist, and incident
    # template carry the normal UI.
    text = str(excerpt or "").strip()
    use_swedish = language == "Svenska"

    if not text:
        return text

    if use_swedish:
        if looks_english_text(text) and not looks_swedish_text(text):
            return ""
        return text

    if looks_swedish_text(text) and not looks_english_text(text):
        return ""

    return text

def trim_excerpt_without_cutting_sentence(excerpt, language="English", max_chars=1400):
    # Trims long source previews only at a natural sentence or paragraph boundary.
    # This avoids ugly half-sentences ending with "..." in the UI.
    text = str(excerpt or "").strip()

    if not text or len(text) <= max_chars:
        return text

    candidate = text[:max_chars].rstrip()
    boundary_positions = [
        candidate.rfind(". "),
        candidate.rfind("? "),
        candidate.rfind("! "),
        candidate.rfind(".\n"),
        candidate.rfind("?\n"),
        candidate.rfind("!\n"),
        candidate.rfind("\n\n"),
    ]
    boundary = max(boundary_positions)

    # If there is no good boundary, keep the full excerpt rather than showing
    # a broken sentence. A slightly longer card is better than a cursed cut-off.
    if boundary < int(max_chars * 0.55):
        return text

    trimmed = candidate[: boundary + 1].strip()

    if language == "Svenska":
        return f"{trimmed}\n\n[Utdraget är förkortat vid en naturlig gräns.]"

    return f"{trimmed}\n\n[Excerpt shortened at a natural boundary.]"

def compact_source_excerpt_spacing(excerpt):
    # Source cards are previews, not full Markdown documents.
    # Compact empty lines so short excerpts do not look like they are scattered
    # across the page like a PDF exploded in the warp.
    text = str(excerpt or "").strip()

    if not text:
        return text

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if not lines:
        return ""

    has_list = any(
        line.startswith(("- ", "* ", "• ")) or re.match(r"^\d+[.)]\s+", line)
        for line in lines
    )

    # Keep list structure readable, but remove empty rows between bullets.
    if has_list:
        return "\n".join(lines)

    # For normal explanatory text, make the preview a compact paragraph.
    return " ".join(lines)


def clean_source_excerpt(content, section_name="", language="English", max_chars=1400):
    # Creates a cleaner preview for "Relevant source context".
    # It removes source-routing examples such as "Use this section when the user asks:"
    # and skips straight to the actual guidance.
    lines = str(content or "").splitlines()

    # Remove leading Markdown heading.
    if lines and lines[0].strip().startswith("#"):
        lines = lines[1:]

    cleaned = []
    skip_question_examples = False
    in_fenced_code_block = False

    start_markers = [
        "### step 1",
        "### steg 1",
        "step 1:",
        "steg 1:",
        "1. ",
        "- ",
    ]

    routing_markers = [
        "use this section when",
        "använd denna sektion",
        "use this checklist",
        "använd denna checklista",
    ]

    internal_helper_markers = [
        "cyberlex should explain",
        "cyberlex sweden should explain",
        "cyberlex should use",
        "cyberlex sweden should use",
        "this source is used for",
        "this section is used for",
        "use this source when",
        "use this section when",
        "useful questions",
        "example questions",
        "exempelfrågor",
        "cyberlex bör",
        "cyberlex sweden bör",
        "cyberlex ska",
        "cyberlex sweden ska",
        "cyberlex bör förklara",
        "cyberlex sweden bör förklara",
        "cyberlex bör använda",
        "cyberlex sweden bör använda",
        "denna källa används",
        "den här källan används",
        "denna sektion används",
        "den här sektionen används",
        "för detaljerade frågor",
        "bör cyberlex även använda",
        "ska cyberlex även använda",
    ]

    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()
        lower = stripped.lower()

        if is_noise_source_context_line(stripped):
            continue

        # Remove Markdown code fences and fenced code blocks from source previews.
        # Source context should show readable source text, not project file paths or leftover HTML.
        if stripped.startswith("```"):
            in_fenced_code_block = not in_fenced_code_block
            continue

        if in_fenced_code_block:
            continue

        if "<div" in lower or "</div" in lower:
            continue

        # Hide internal routing and authoring notes. These are useful for the
        # developer and search logic, but they should not appear as user-facing
        # source context during a demo or test run.
        if any(marker in lower for marker in internal_helper_markers):
            continue

        if not stripped:
            if cleaned:
                cleaned.append("")
            continue

        # Skip routing/example-question introductions.
        if any(marker in lower for marker in routing_markers):
            skip_question_examples = True
            continue

        if skip_question_examples:
            # Keep skipping bullet example questions until actual guidance begins.
            if lower.startswith("### ") or any(lower.startswith(marker) for marker in start_markers):
                skip_question_examples = False
            else:
                continue

        # Remove leftover example-question bullets if they slipped through.
        if stripped.startswith("- ") and stripped.endswith("?"):
            continue

        cleaned.append(line)

    excerpt = "\n".join(cleaned).strip()

    # If the section had only routing text and no step heading, fall back to a short useful body.
    if not excerpt:
        fallback_lines = []
        fallback_in_fenced_code_block = False
        for raw_line in lines:
            stripped = raw_line.strip()
            lower = stripped.lower()
            if is_noise_source_context_line(stripped):
                continue
            if stripped.startswith("```"):
                fallback_in_fenced_code_block = not fallback_in_fenced_code_block
                continue
            if fallback_in_fenced_code_block:
                continue
            if "<div" in lower or "</div" in lower:
                continue
            if any(marker in lower for marker in internal_helper_markers):
                continue
            if not stripped:
                continue
            if any(marker in lower for marker in routing_markers):
                continue
            if stripped.startswith("- ") and stripped.endswith("?"):
                continue
            fallback_lines.append(raw_line.rstrip())
        excerpt = "\n".join(fallback_lines).strip()

    excerpt = trim_excerpt_without_cutting_sentence(excerpt, language=language, max_chars=max_chars)

    excerpt = localize_source_excerpt_for_ui(excerpt, language)
    excerpt = compact_source_excerpt_spacing(excerpt)

    return excerpt


def clean_source_excerpt_relaxed(content, language="English", max_chars=1400):
    # Fallback preview cleaner used only when the stricter cleaner removes too
    # much text. This prevents an expanded source-context section from becoming
    # empty while still removing obvious internal/helper junk.
    lines = str(content or "").splitlines()

    if lines and lines[0].strip().startswith("#"):
        lines = lines[1:]

    cleaned = []
    in_fenced_code_block = False
    internal_helper_markers = [
        "cyberlex should explain",
        "cyberlex sweden should explain",
        "cyberlex should use",
        "cyberlex sweden should use",
        "this source is used for",
        "this section is used for",
        "use this source when",
        "use this section when",
        "useful questions",
        "example questions",
        "exempelfrågor",
        "cyberlex bör",
        "cyberlex sweden bör",
        "cyberlex ska",
        "cyberlex sweden ska",
        "denna källa används",
        "den här källan används",
        "denna sektion används",
        "den här sektionen används",
    ]

    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()
        lower = stripped.lower()

        if is_noise_source_context_line(stripped):
            continue

        if stripped.startswith("```"):
            in_fenced_code_block = not in_fenced_code_block
            continue

        if in_fenced_code_block:
            continue

        if "<div" in lower or "</div" in lower:
            continue

        if any(marker in lower for marker in internal_helper_markers):
            continue

        if not stripped:
            if cleaned and cleaned[-1] != "":
                cleaned.append("")
            continue

        cleaned.append(line)

    excerpt = "\n".join(cleaned).strip()
    excerpt = trim_excerpt_without_cutting_sentence(excerpt, language=language, max_chars=max_chars)
    excerpt = localize_source_excerpt_for_ui(excerpt, language)
    excerpt = compact_source_excerpt_spacing(excerpt)
    excerpt = clean_source_context_tail(excerpt)

    return excerpt



def split_source_excerpt_for_display(excerpt, language="English", max_visible_lines=8):
    # Splits a source-context excerpt into a short visible preview and a longer
    # optional detail view. Normal users get readable source support first;
    # testers and curious users can expand the full cleaned excerpt when needed.
    # Civilization advances one collapsible box at a time.
    use_swedish = language == "Svenska"
    excerpt_text = str(excerpt or "").strip()

    if not excerpt_text:
        return {
            "short_excerpt": "",
            "full_excerpt": "",
            "was_shortened": False,
            "shortened_note": "",
            "details_label": "",
            "details_less_label": "",
        }

    lines = excerpt_text.splitlines()

    # Keep meaningful blank lines, but remove extra empty lines at the edges.
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    if len(lines) <= max_visible_lines:
        return {
            "short_excerpt": excerpt_text,
            "full_excerpt": excerpt_text,
            "was_shortened": False,
            "shortened_note": "",
            "details_label": "",
            "details_less_label": "",
        }

    visible_lines = lines[:max_visible_lines]
    short_excerpt = "\n".join(visible_lines).strip()

    shortened_note = (
        "Utdraget har kortats för läsbarhet."
        if use_swedish
        else "Excerpt shortened for readability."
    )

    details_label = (
        "Visa mer källtext"
        if use_swedish
        else "Show more source text"
    )
    details_less_label = (
        "Visa mindre källtext"
        if use_swedish
        else "Show less source text"
    )

    return {
        "short_excerpt": short_excerpt,
        "full_excerpt": excerpt_text,
        "was_shortened": True,
        "shortened_note": shortened_note,
        "details_label": details_label,
        "details_less_label": details_less_label,
    }

def get_friendly_source_area_name(filename, language="English"):
    # Converts internal Markdown file names into user-friendly source area names.
    # Normal users should not need to understand local .md file names.
    use_swedish = language == "Svenska"
    filename_key = str(filename or "").strip().lower()

    english_names = {
        "gdpr_core_principles.md": "GDPR core principles",
        "gdpr_personal_data_breach.md": "GDPR personal data breach",
        "gdpr_imy_edpb_security_guidance.md": "GDPR, IMY and EDPB security guidance",
        "imy_gdpr_security_measures.md": "IMY GDPR security measures",
        "imy_gdpr_supervision.md": "IMY and GDPR supervision",
        "nis2_cybersecurity_law.md": "NIS2 and the Swedish Cybersecurity Act",
        "nis2_sector_scope_guidance.md": "NIS2 sector scope and applicability",
        "nis2_incident_reporting.md": "NIS2 incident reporting",
        "cybercrime_dataintrang.md": "Swedish cybercrime and data intrusion",
        "eu_attacks_against_information_systems.md": "EU rules on attacks against information systems",
        "eu_cyber_resilience_act.md": "EU Cyber Resilience Act",
        "eu_dora_digital_operational_resilience.md": "DORA and digital operational resilience",
        "cyber_incident_response_playbook.md": "Cyber incident response playbook",
    }

    swedish_names = {
        "gdpr_core_principles.md": "GDPR:s grundprinciper",
        "gdpr_personal_data_breach.md": "GDPR och personuppgiftsincidenter",
        "gdpr_imy_edpb_security_guidance.md": "GDPR, IMY och EDPB:s säkerhetsvägledning",
        "imy_gdpr_security_measures.md": "IMY:s GDPR-säkerhetsåtgärder",
        "imy_gdpr_supervision.md": "IMY och GDPR-tillsyn",
        "nis2_cybersecurity_law.md": "NIS2 och cybersäkerhetslagens omfattning",
        "nis2_sector_scope_guidance.md": "NIS2 sektorer och omfattning",
        "nis2_incident_reporting.md": "NIS2-incidentrapportering",
        "cybercrime_dataintrang.md": "Svensk cyberbrottslighet och dataintrång",
        "eu_attacks_against_information_systems.md": "EU-regler om angrepp mot informationssystem",
        "eu_cyber_resilience_act.md": "EU Cyber Resilience Act",
        "eu_dora_digital_operational_resilience.md": "DORA och digital operativ motståndskraft",
        "cyber_incident_response_playbook.md": "Cyberincidenthantering",
    }

    source_names = swedish_names if use_swedish else english_names

    if filename_key in source_names:
        return source_names[filename_key]

    fallback = filename_key.replace(".md", "").replace("_", " ").replace("-", " ").strip()
    return fallback[:1].upper() + fallback[1:]


def get_friendly_source_type(filename, language="English"):
    # Gives the user a plain-language description of what kind of source area
    # the local knowledge file represents.
    use_swedish = language == "Svenska"
    filename_key = str(filename or "").strip().lower()

    if filename_key == "cyber_incident_response_playbook.md":
        return "Incident response guidance" if not use_swedish else "Stöd för incidenthantering"

    if filename_key.startswith("eu_"):
        return "EU legal and regulatory source area" if not use_swedish else "EU-rättsligt och regulatoriskt källområde"

    if filename_key.startswith("nis2_"):
        return "Swedish and EU cybersecurity source area" if not use_swedish else "Svenskt och EU-baserat cybersäkerhetsområde"

    if filename_key.startswith("gdpr_") or filename_key.startswith("imy_"):
        return "Data protection and supervisory authority source area" if not use_swedish else "Dataskydds- och tillsynsområde"

    if filename_key.startswith("cybercrime_"):
        return "Swedish cybercrime source area" if not use_swedish else "Svenskt cyberbrottsområde"

    return "Local CyberLex knowledge source" if not use_swedish else "Lokal CyberLex-kunskapskälla"

def build_source_context(search_results, language="English", max_results=3, question=None):
    # Builds a short source context summary from the top matched source sections.
    # The context should support the answer, not repeat the CyberLex checklist.
    # Therefore checklist sections are hidden unless no non-checklist source context exists.

    use_swedish = language == "Svenska"

    if use_swedish:
        source_area_label = "Källområde"
        section_label = "Använd sektion"
        source_type_label = "Källtyp"
        excerpt_label = "Stödjande källtext"
    else:
        source_area_label = "Source area"
        section_label = "Used section"
        source_type_label = "Source type"
        excerpt_label = "Supporting source text"

    context_blocks = []
    filtered_results = []
    opposite_language_section_markers = (
        ["swedish ", "svensk "] if not use_swedish else ["english ", "engelsk "]
    )

    for result in search_results:
        section_name = str(result.get("section", "")).strip().lower()

        # Do not show source cards from the opposite language.
        if any(section_name.startswith(marker) for marker in opposite_language_section_markers):
            continue

        filtered_results.append(result)

    if not filtered_results:
        filtered_results = search_results

    if question and is_nis2_sector_scope_question(question):
        nis2_focused = [
            result for result in filtered_results
            if "nis2_sector_scope_guidance" in str(result.get("filename", "")).lower()
        ]

        if nis2_focused:
            allowed_nis2_focused = [
                result for result in nis2_focused
                if is_nis2_scope_allowed_context_section(result, question)
            ]
            if allowed_nis2_focused:
                nis2_focused = allowed_nis2_focused

            filtered_results = sorted(
                nis2_focused,
                key=lambda result: (
                    get_nis2_scope_source_context_priority(result, question, language),
                    result.get("score", 0)
                ),
                reverse=True
            )
        else:
            filtered_results = [
                result for result in filtered_results
                if "gdpr_" not in str(result.get("filename", "")).lower()
                and "imy_" not in str(result.get("filename", "")).lower()
                and "cyber_incident_response_playbook" not in str(result.get("filename", "")).lower()
            ] or filtered_results

    elif question and is_gdpr_security_guidance_question(question):
        gdpr_focused = [
            result for result in filtered_results
            if is_gdpr_assessment_or_security_file(result.get("filename", ""))
        ]
        if gdpr_focused:
            def gdpr_context_sort_key(result):
                filename = str(result.get("filename", "")).lower()
                section_name = str(result.get("section", "")).lower()
                priority = 0
                if "imy_gdpr_security_measures" in filename:
                    priority += 650 if is_imy_gdpr_security_measures_question(question) else 150
                if "gdpr_imy_edpb_security_guidance" in filename:
                    priority += 500
                if "practical explanation" in section_name or "relationship with incident response" in section_name:
                    priority += 120
                if "swedish practical explanation" in section_name or "swedish relationship with incident response" in section_name:
                    priority += 120 if use_swedish else -20
                if "data protection by design" in section_name:
                    priority += 90
                if "gdpr_personal_data_breach" in filename:
                    priority += 70
                return (priority, result.get("score", 0))

            filtered_results = sorted(gdpr_focused, key=gdpr_context_sort_key, reverse=True)
        else:
            filtered_results = [
                result for result in filtered_results
                if "cyber_incident_response_playbook" not in str(result.get("filename", "")).lower()
                and "nis2_incident_reporting" not in str(result.get("filename", "")).lower()
            ] or filtered_results

    filtered_results = prioritize_source_context_results(
        filtered_results,
        question=question,
        language=language
    )

    # For practical incident-response questions, keep the visible source context
    # focused on the detected incident subtype. A phishing question should not
    # display hacking or data-leak source cards unless the user actually asked
    # about those topics.
    filtered_results = filter_source_context_by_incident_type(
        filtered_results,
        question
    )

    if question and is_nis2_sector_scope_question(question):
        nis2_only_results = [
            result for result in filtered_results
            if "nis2_sector_scope_guidance" in str(result.get("filename", "")).lower()
        ]
        if nis2_only_results:
            allowed_nis2_only_results = [
                result for result in nis2_only_results
                if is_nis2_scope_allowed_context_section(result, question)
            ]
            if allowed_nis2_only_results:
                nis2_only_results = allowed_nis2_only_results

            filtered_results = sorted(
                nis2_only_results,
                key=lambda result: (
                    get_nis2_scope_source_context_priority(result, question, language),
                    result.get("score", 0)
                ),
                reverse=True
            )

    # Prefer source sections whose cleaned visible preview matches the selected UI language.
    # Use the cleaned excerpt, not the raw Markdown, because some sections contain
    # English/Swedish example questions before the actual source text.
    same_language_results = []
    for result in filtered_results:
        preview = clean_source_excerpt(
            result.get("content", ""),
            section_name=result.get("section", ""),
            language=language,
            max_chars=1400,
        )

        if not str(preview or "").strip():
            continue

        if use_swedish and looks_swedish_text(preview):
            same_language_results.append(result)
        elif not use_swedish and looks_english_text(preview) and not (looks_swedish_text(preview) and not looks_english_text(preview)):
            same_language_results.append(result)

    if same_language_results:
        filtered_results = same_language_results

    # Avoid duplicating the visible CyberLex assessment checklist.
    non_checklist_results = [
        result for result in filtered_results
        if not is_checklist_section(result.get("section", ""))
    ]

    if non_checklist_results:
        filtered_results = non_checklist_results

    # Hide routing/test/helper sections from normal source context if better
    # explanatory sections are available. The machine-spirit may love helper
    # headings, but users usually do not.
    useful_context_results = [
        result for result in filtered_results
        if not is_low_value_source_context_section(result.get("section", ""))
    ]

    if useful_context_results:
        filtered_results = useful_context_results

    # Remove near-duplicate cards with the same file and display section.
    seen_cards = set()
    selected_results = []

    for result in filtered_results:
        display_section = localize_section_name(result.get("section", ""), language)
        card_key = (result.get("filename", ""), display_section.lower())

        if card_key in seen_cards:
            continue

        seen_cards.add(card_key)
        selected_results.append(result)

        effective_max_results = max_results
        if question and is_nis2_sector_scope_question(question):
            effective_max_results = min(max_results, get_nis2_scope_max_context_cards(question))

        if len(selected_results) >= effective_max_results:
            break

    for result in selected_results:
        display_section = localize_section_name(result.get("section", ""), language)
        excerpt = clean_source_excerpt(
            result.get("content", ""),
            section_name=result.get("section", ""),
            language=language,
            max_chars=2800
        )

        if not str(excerpt or "").strip():
            excerpt = clean_source_excerpt_relaxed(
                result.get("content", ""),
                language=language,
                max_chars=2800
            )

        if not str(excerpt or "").strip():
            continue

        excerpt_display = split_source_excerpt_for_display(
            excerpt,
            language=language,
            max_visible_lines=8
        )
        short_excerpt = excerpt_display["short_excerpt"]
        full_excerpt = excerpt_display["full_excerpt"]

        if excerpt_display["was_shortened"]:
            excerpt_html = (
                f'<div class="context-excerpt">{short_excerpt}</div>'
                f'<div class="context-shortened-note">{excerpt_display["shortened_note"]}</div>'
                f'<details class="context-more-details">'
                f'<summary>'
                f'<span class="details-more-label">{excerpt_display["details_label"]}</span>'
                f'<span class="details-less-label">{excerpt_display["details_less_label"]}</span>'
                f'</summary>'
                f'<div class="context-excerpt context-full-excerpt">{full_excerpt}</div>'
                f'</details>'
            )
        else:
            excerpt_html = f'<div class="context-excerpt">{short_excerpt}</div>'

        friendly_source_area = get_friendly_source_area_name(result.get("filename", ""), language)
        friendly_source_type = get_friendly_source_type(result.get("filename", ""), language)

        context_blocks.append(
            f'<div class="context-card">'
            f'<div class="context-card-title">{display_section}</div>'
            f'<div class="context-row"><strong>{source_area_label}:</strong> '
            f'<span>{friendly_source_area}</span></div>'
            f'<div class="context-row"><strong>{section_label}:</strong> '
            f'<span>{display_section}</span></div>'
            f'<div class="context-row"><strong>{source_type_label}:</strong> '
            f'<span>{friendly_source_type}</span></div>'
            f'<div class="context-excerpt-label">{excerpt_label}:</div>'
            f'{excerpt_html}'
            f'</div>'
        )

    return "\n".join(context_blocks)



def should_show_practical_explanation(question):
    # Shows the practical explanation card only when it adds real value.
    # Simple definition or authority questions already get their explanation in
    # the CyberLex summary, so another "Practical explanation" card becomes noise.
    # Reporting, breach, overlap, duty, and incident-response questions still
    # benefit from a practical explanation.
    question_lower = normalize_query_text(question).strip()

    if not question_lower:
        return False

    if is_practical_incident_response_question(question_lower):
        return True

    practical_markers = [
        "reported",
        "reporting",
        "report ",
        "notification",
        "notify",
        "72 hour",
        "72-hour",
        "72 timmar",
        "breach",
        "personal data breach",
        "personuppgiftsincident",
        "incident need",
        "incident require",
        "under both",
        "both nis2 and gdpr",
        "både nis2 och gdpr",
        "gdpr and nis2",
        "nis2 and gdpr",
        "must a company",
        "must an organization",
        "must an organisation",
        "requirements",
        "obligations",
        "duties",
        "covered organization",
        "covered organisation",
        "security measures",
        "risk management",
        "third-party risk",
        "tredjepartsrisk",
        "skyldighet",
        "skyldigheter",
        "krav",
        "rapportera",
        "rapportering",
        "anmäl",
        "anmäla",
        "anmäls",
        "incidentrapportering",
        "riskhantering",
        "säkerhetsåtgärder",
    ]

    if contains_any(question_lower, practical_markers):
        return True

    simple_definition_markers = [
        "what is ",
        "what are ",
        "what does ",
        "which authority",
        "what authority",
        "vad är ",
        "vad betyder ",
        "vad gör ",
        "vilken myndighet",
        "vilka är ",
    ]

    simple_topic_markers = [
        "nis2",
        "dora",
        "imy",
        "gdpr",
        "dataintrång",
        "cyber resilience act",
        "cyberresiliensakten",
        "attacks against information systems",
        "attacker mot informationssystem",
    ]

    if contains_any(question_lower, simple_definition_markers) and contains_any(question_lower, simple_topic_markers):
        return False

    return False


def generate_practical_explanation(question, search_results, language="English"):
    # Generates a practical explanation based on the question and matched source sections.
    # This is still rule-based and source-grounded. It does not use an external AI model.

    question_lower = question.lower()
    use_swedish = language == "Svenska"

    if use_swedish:
        heading = "Praktisk förklaring"

        if is_suspicious_login_question(question):
            explanation = (
                "Börja med att avgöra om inloggningen var godkänd eller förväntad. Om den var legitim krävs normalt ingen incidenthantering. "
                "Om den är obehörig, okänd eller inte kan förklaras bör ni bevara loggar, kontakta användaren, kontrollera MFA och sessioner, "
                "och behandla kontot som misstänkt påverkat tills motsatsen är klarlagd."
            )

        elif is_practical_incident_response_question(question):
            explanation = (
                "Det här är en praktisk incidenthanteringsfråga. CyberLex bör därför ge defensiva första steg: "
                "begränsa skadan, isolera drabbade system eller konton, bevara loggar och bevis, bedöma om personuppgifter påverkas, "
                "kontrollera om IMY/GDPR eller NIS2/cybersäkerhetslagen kan bli relevanta, och dokumentera tidslinje och beslut."
            )

        elif (
            "ransomware" in question_lower
            or "malware" in question_lower
            or "cyberattack" in question_lower
            or "cyber attack" in question_lower
            or "cyberincident" in question_lower
            or "cyber incident" in question_lower
        ):
            explanation = (
                "I praktiken bör en ransomware- eller cyberincident hanteras både tekniskt och juridiskt. "
                "Organisationen bör begränsa skadan, säkra loggar och bevis, bedöma om personuppgifter påverkas, "
                "kontrollera om rapportering enligt GDPR eller NIS2/cybersäkerhetslagen kan bli aktuell, "
                "och dokumentera beslut, tidslinje och åtgärder."
            )

        elif "personal data breach" in question_lower or "personuppgiftsincident" in question_lower or "72" in question_lower:
            explanation = (
                "I praktiken betyder detta att organisationen först måste bedöma om incidenten påverkar personuppgifter. "
                "Om incidenten sannolikt innebär en risk för registrerade personers rättigheter och friheter kan den behöva anmälas till IMY. "
                "CyberLex visar därför både rapporteringsregeln och den matchade källsektionen så att användaren kan se vad svaret bygger på."
            )

        elif ("nis2" in question_lower or "cybersäkerhetslagen" in question_lower) and "gdpr" in question_lower:
            explanation = (
                "I praktiken kan en och samma cyberincident behöva bedömas från två håll. "
                "NIS2 eller den svenska cybersäkerhetslagen handlar om cybersäkerhetsincidenten som sådan, medan GDPR handlar om personuppgifter. "
                "Om incidenten både påverkar samhällsviktig digital säkerhet och personuppgifter kan flera regelverk bli relevanta samtidigt."
            )

        elif "nis2" in question_lower or "cybersäkerhetslagen" in question_lower:
            explanation = (
                "I praktiken handlar NIS2 och den svenska cybersäkerhetslagen om att vissa organisationer måste arbeta mer systematiskt med cybersäkerhet. "
                "Det kan omfatta riskhantering, säkerhetsåtgärder och incidentrapportering. "
                "CyberLex bör därför alltid visa vilka källor som ligger bakom svaret, eftersom kraven kan bero på organisationstyp och sektor."
            )

        elif "dora" in question_lower or "digital operational resilience" in question_lower:
            explanation = (
                "I praktiken riktar sig DORA främst mot den finansiella sektorn och handlar om digital operativ motståndskraft. "
                "Det betyder att organisationer behöver kunna förebygga, hantera och återhämta sig från ICT-relaterade störningar och cyberincidenter. "
                "Särskilt viktigt är hantering av ICT-risker, incidenter, tester och tredjepartsleverantörer."
            )

        elif "dataintrång" in question_lower or "unauthorized access" in question_lower or "obehörig åtkomst" in question_lower:
            explanation = (
                "I praktiken handlar dataintrång om obehörig åtkomst till data eller informationssystem. "
                "Det är därför viktigt att skilja mellan tillåten säkerhetstestning och obehöriga handlingar. "
                "CyberLex visar källor kopplade till svensk straffrätt för att förklara den juridiska ramen."
            )

        elif "cyber resilience act" in question_lower or "cyberresiliensakten" in question_lower:
            explanation = (
                "I praktiken handlar Cyber Resilience Act om cybersäkerhetskrav för produkter med digitala element. "
                "Det påverkar hur digitala produkter designas, dokumenteras, uppdateras och hanteras när sårbarheter upptäcks. "
                "Reglerna är därför relevanta för produktutveckling, leverantörer och digital säkerhet."
            )

        else:
            explanation = (
                "I praktiken bör detta svar läsas tillsammans med de matchade källsektionerna nedan. "
                "CyberLex visar källkontexten för att göra det tydligt vilka delar av kunskapsbasen som stödjer svaret."
            )

    else:
        heading = "Practical explanation"

        if is_suspicious_login_question(question):
            explanation = (
                "Start by deciding whether the login was approved or expected. If it was legitimate, it is usually not an incident. "
                "If it is unauthorized, unknown, or cannot be explained, preserve logs, contact the user, review MFA and sessions, "
                "and treat the account as potentially affected until proven otherwise."
            )

        elif is_practical_incident_response_question(question):
            explanation = (
                "This is a practical incident response question. CyberLex should therefore give defensive first steps: "
                "limit harm, isolate affected systems or accounts, preserve logs and evidence, assess whether personal data is affected, "
                "check whether IMY/GDPR or NIS2/the Swedish Cybersecurity Act may be relevant, and document the timeline and decisions."
            )

        elif (
            "ransomware" in question_lower
            or "malware" in question_lower
            or "cyberattack" in question_lower
            or "cyber attack" in question_lower
            or "cyber incident" in question_lower
            or "security incident" in question_lower
        ):
            explanation = (
                "In practice, a ransomware or cyber incident should be handled both technically and legally. "
                "The organization should contain the incident, preserve logs and evidence, assess whether personal data is affected, "
                "check whether GDPR or NIS2/Swedish Cybersecurity Act reporting may be relevant, and document the timeline, decisions, and actions taken."
            )

        elif "personal data breach" in question_lower or "breach" in question_lower or "72" in question_lower:
            explanation = (
                "In practice, the organization first needs to assess whether the incident affects personal data. "
                "If the breach is likely to create a risk to individuals' rights and freedoms, it may need to be reported to IMY. "
                "CyberLex shows the matched source sections so the user can see which source material supports the answer."
            )

        elif ("nis2" in question_lower or "cybersecurity act" in question_lower) and "gdpr" in question_lower:
            explanation = (
                "In practice, the same cyber incident may need to be assessed from two angles. "
                "NIS2 or the Swedish Cybersecurity Act concerns the cybersecurity incident itself, while GDPR concerns personal data. "
                "If an incident affects both cybersecurity obligations and personal data, more than one reporting path may be relevant."
            )

        elif "nis2" in question_lower or "cybersecurity act" in question_lower:
            explanation = (
                "In practice, NIS2 and the Swedish Cybersecurity Act focus on more structured cybersecurity duties for covered organizations. "
                "This can include risk management, security measures, and incident reporting. "
                "CyberLex should therefore show the supporting sources, because the exact duties may depend on the organization and sector."
            )

        elif "dora" in question_lower or "digital operational resilience" in question_lower:
            explanation = (
                "In practice, DORA mainly applies to the financial sector and focuses on digital operational resilience. "
                "This means organizations need to prevent, manage, and recover from ICT-related disruptions and cyber incidents. "
                "ICT risk management, incident handling, resilience testing, and third-party ICT providers are especially important."
            )

        elif "dataintrång" in question_lower or "unauthorized access" in question_lower or "data intrusion" in question_lower:
            explanation = (
                "In practice, dataintrång concerns unauthorized access to data or information systems under Swedish criminal law. "
                "This makes it important to separate authorized security testing from unauthorized activity. "
                "CyberLex shows Swedish criminal-law sources to explain the legal context."
            )

        elif "cyber resilience act" in question_lower or "products with digital elements" in question_lower:
            explanation = (
                "In practice, the Cyber Resilience Act concerns cybersecurity requirements for products with digital elements. "
                "It affects how digital products are designed, documented, updated, and handled when vulnerabilities are found. "
                "This makes it relevant for product development, suppliers, and digital security."
            )

        else:
            explanation = (
                "In practice, this answer should be read together with the matched source context below. "
                "CyberLex shows the source context so it is clear which parts of the knowledge base support the answer."
            )

    return (
        f'<div class="practical-card">'
        f'<div class="practical-card-title">{heading}</div>'
        f'<div class="practical-card-text">{explanation}</div>'
        f'</div>'
    )


def generate_assessment_checklist(question, search_results, language="English"):
    # Generates a topic-specific verification checklist based on the user's question.
    # The main CyberLex answer gives the immediate steps.
    # This checklist asks review questions so the user can verify what has been checked and documented.
    # This is not legal advice.

    question_lower = question.lower()
    use_swedish = language == "Svenska"

    def contains_any(terms):
        return any(term in question_lower for term in terms)

    suspicious_login_terms = [
        "suspicious login",
        "suspicious sign in",
        "suspicious sign-in",
        "unusual login",
        "unusual sign in",
        "failed login",
        "impossible travel",
        "misstänkt inloggning",
        "ovanlig inloggning",
        "misslyckad inloggning",
        "inloggningsförsök",
        "login activity",
        "inloggning",
    ]

    suspicious_email_terms = [
        "suspicious email",
        "phishing",
        "phishing email",
        "suspicious mail",
        "malicious email",
        "misstänkt mejl",
        "misstänkt mail",
        "nätfiske",
        "phishingmejl",
        "skadligt mejl",
        "e-post",
        "email",
    ]

    compromised_account_terms = [
        "compromised account",
        "account compromised",
        "account is compromised",
        "account has been compromised",
        "account hacked",
        "hacked account",
        "komprometterat konto",
        "konto komprometterat",
        "kontot är komprometterat",
        "konto hackat",
        "hackat konto",
    ]

    data_leak_terms = [
        "data leak",
        "data leakage",
        "leaked data",
        "exposed data",
        "customer data exposed",
        "customer data leaked",
        "customer data may have leaked",
        "customer data might have leaked",
        "dataläcka",
        "läckt data",
        "exponerad data",
        "kunddata",
        "kunddata kan ha läckt",
    ]

    ransomware_terms = [
        "ransomware",
        "malware",
        "krypterats",
        "våra filer",
        "encrypted files",
        "files encrypted",
        "utpressningsvirus",
        "skadlig kod",
        "filer krypterade",
        "krypterade filer",
    ]

    hacking_terms = [
        "hacking",
        "intrusion",
        "suspected hacking",
        "suspected intrusion",
        "unauthorized access",
        "hackning",
        "intrång",
        "tagit sig in",
        "tagit sig in i vårt system",
        "tagit sig in i vårat system",
        "någon verkar ha tagit sig in",
        "någon har tagit sig in",
        "misstänker intrång",
        "misstänker hackning",
        "obehörig åtkomst",
    ]

    if use_swedish:
        heading = "CyberLex bedömningschecklista"

        if contains_any(suspicious_login_terms):
            items = [
                "Har vi sparat larmet eller loggposten med tidpunkt, användarkonto, IP-adress, plats, enhet och tjänst?",
                "Har vi kontrollerat om inloggningen lyckades eller bara var ett misslyckat försök?",
                "Har vi kontrollerat om samma konto har fler ovanliga inloggningar, MFA-pushar eller misslyckade försök?",
                "Har vi kontaktat användaren på ett säkert sätt och bekräftat om aktiviteten var legitim?",
                "Har vi blockerat kontot tillfälligt eller krävt ny autentisering om aktiviteten inte kan förklaras?",
                "Har vi återkallat aktiva sessioner och tokens i identitetsplattformen, VPN, e-post och molntjänster?",
                "Har vi bytt lösenord från en ren enhet och granskat MFA-metoder för okända eller angriparstyrda metoder?",
                "Har vi granskat e-postregler, vidarebefordran, OAuth-appar och delegerad åtkomst?",
                "Har vi kontrollerat om kontot har använts för att komma åt filer, system, kunddata eller administratörsfunktioner?",
                "Har vi bedömt om personuppgifter kan ha påverkats och om GDPR/IMY-bedömning krävs?",
                "Har vi bedömt om händelsen kan vara relevant enligt NIS2/cybersäkerhetslagen vid större påverkan?",
                "Har vi dokumenterat tidslinje, loggar, beslut och åtgärder?",
            ]

        elif contains_any(suspicious_email_terms):
            items = [
                "Har vi sagt till användaren att inte klicka fler länkar, öppna bilagor eller svara på mejlet?",
                "Har vi sparat mejlet som bevis, inklusive avsändare, ämne, tidpunkt, länkar, bilagor och fullständiga headers om möjligt?",
                "Har mejlet rapporterats till IT/säkerhet enligt organisationens rutin?",
                "Har vi sökt efter samma mejl hos andra användare och karantänsatt eller tagit bort det via e-postskyddet om möjligt?",
                "Har vi kontrollerat om någon klickade på länken, öppnade bilagan eller lämnade inloggningsuppgifter?",
                "Om någon klickade eller skrev in uppgifter: har kontot behandlats som misstänkt komprometterat?",
                "Har vi återkallat sessioner, bytt lösenord från en ren enhet och kontrollerat MFA om uppgifter kan ha läckt?",
                "Har vi kontrollerat e-postregler, vidarebefordran, OAuth-appar och misstänkta skickade meddelanden?",
                "Har vi kontrollerat om mejlet innehöll skadlig kod och om någon klient behöver isoleras?",
                "Har vi bedömt om personuppgifter eller känslig information kan ha påverkats?",
                "Har vi dokumenterat tidslinje, användare, åtgärder, bevis och beslut?",
            ]

        elif contains_any(compromised_account_terms):
            items = [
                "Har vi blockerat eller tillfälligt inaktiverat kontot om kompromettering är sannolik?",
                "Har vi återkallat aktiva sessioner och tokens i identitetssystem, VPN, e-post och molntjänster?",
                "Har lösenordet bytts från en ren enhet och inte från den misstänkt komprometterade klienten?",
                "Har vi granskat MFA-metoder och tagit bort okända eller angriparstyrda metoder?",
                "Har vi granskat e-postregler, vidarebefordran, OAuth-appar, delegerad åtkomst och misstänkta skickade meddelanden?",
                "Har vi granskat inloggningsloggar, IP-adresser, länder, tidpunkter och ovanlig aktivitet?",
                "Har vi kontrollerat om kontot hade administratörsrättigheter eller åtkomst till känsliga system?",
                "Har vi identifierat vilken data kontot kan ha läst, ändrat, laddat ned eller raderat?",
                "Har vi bedömt om personuppgifter kan ha påverkats och om GDPR/IMY-bedömning krävs?",
                "Har vi bedömt om händelsen kan vara relevant enligt NIS2/cybersäkerhetslagen?",
                "Har vi dokumenterat åtgärder, tidslinje, bevis och beslut?",
            ]

        elif contains_any(data_leak_terms):
            items = [
                "Har vi bekräftat vad som är känt och vad som fortfarande är oklart?",
                "Har vi stoppat fortsatt exponering, till exempel publik åtkomst, delningslänkar eller felaktiga behörigheter?",
                "Har vi sparat bevis innan ändringar gjordes, till exempel skärmbilder, länkar, loggar, tidsstämplar och behörighetsinställningar?",
                "Har vi identifierat vilken data som kan ha exponerats och hur länge exponeringen pågick?",
                "Har vi bedömt om datan innehåller personuppgifter, känsliga uppgifter, lösenord, tokens, kunddata eller HR-data?",
                "Har vi bedömt om obehörig åtkomst faktiskt har skett eller om åtkomst bara var möjlig?",
                "Har vi säkrat berörda konton, API-nycklar, lösenord och system från en ren administrativ miljö?",
                "Har vi bedömt risken för registrerade personers rättigheter och friheter?",
                "Har vi bedömt om anmälan till IMY enligt GDPR krävs, normalt inom 72 timmar efter medvetenhet?",
                "Har vi bedömt om berörda personer behöver informeras vid hög risk?",
                "Har vi bedömt om NIS2/cybersäkerhetslagen eller annan incidentrapportering också kan vara relevant?",
                "Har vi dokumenterat beslut, tidslinje, åtgärder, källor och vem som godkände besluten?",
            ]

        elif contains_any(ransomware_terms):
            items = [
                "Har vi isolerat drabbade system för att begränsa spridning?",
                "Har vi säkrat loggar, ransom note, filändelser, systeminformation och annan teknisk bevisning?",
                "Har vi dokumenterat tidslinje, upptäckt, påverkan och vidtagna åtgärder?",
                "Har vi kontrollerat vilka system, delade ytor, servrar och backupmiljöer som är påverkade?",
                "Har vi kontrollerat om säkerhetskopior finns och om de är opåverkade?",
                "Har vi bedömt om data kan ha stulits innan kryptering eller skada?",
                "Har vi bedömt om personuppgifter har påverkats?",
                "Har vi bedömt om GDPR-anmälan till IMY kan vara relevant?",
                "Har vi bedömt om NIS2/cybersäkerhetslagen eller annan incidentrapportering kan vara relevant?",
                "Har vi jämfört bedömningen med aktuella källor och interna incidentrutiner?",
            ]

        elif is_practical_incident_response_question(question) or contains_any(hacking_terms):
            items = [
                "Har vi startat en incidentlogg med upptäckt, tidpunkt, system, konto och ansvariga personer?",
                "Har vi isolerat drabbade klienter, servrar eller konton om det kan göras utan att förstöra bevisning?",
                "Har vi bevarat loggar, larm, skärmbilder, tidsstämplar och annan teknisk bevisning?",
                "Har vi undvikit att radera loggar eller installera om system innan en första bedömning?",
                "Har vi identifierat berörda system, konton, användare, nätverk och data?",
                "Har vi säkrat komprometterade konton, återkallat sessioner och bytt lösenord från en ren enhet?",
                "Har vi bedömt om personuppgifter kan ha påverkats?",
                "Har vi bedömt om IMY-anmälan enligt GDPR kan krävas?",
                "Har vi bedömt om NIS2/cybersäkerhetslagen eller annan incidentrapportering kan vara relevant?",
                "Har vi eskalerat till IT, säkerhet, ledning, juridik, dataskyddsansvarig och incidentexpert vid behov?",
                "Har vi övervägt att kontakta CERT-SE eller officiellt incidentstöd vid allvarlig incident?",
                "Har vi dokumenterat beslut, tidslinje, åtgärder, källor och kvarstående osäkerhet?",
            ]

        elif "personuppgiftsincident" in question_lower or "72" in question_lower:
            items = [
                "Har vi begränsat incidenten och bevarat relevant bevisning?",
                "Har vi identifierat vilka personuppgifter som kan ha påverkats?",
                "Har vi bedömt om incidenten kan innebära risk för registrerade personers rättigheter och friheter?",
                "Har vi kontrollerat när organisationen blev medveten om incidenten?",
                "Har vi bedömt om anmälan till IMY krävs inom 72 timmar?",
                "Har vi bedömt om berörda personer behöver informeras vid hög risk?",
                "Har vi dokumenterat beslut, tidslinje, åtgärder och källor?",
            ]

        elif ("nis2" in question_lower or "cybersäkerhetslagen" in question_lower) and "gdpr" in question_lower:
            items = [
                "Har vi bedömt om incidenten är en cybersäkerhetsincident?",
                "Har vi bedömt om incidenten även påverkar personuppgifter?",
                "Har vi kontrollerat om NIS2/cybersäkerhetslagen och GDPR kan vara relevanta samtidigt?",
                "Har vi identifierat vilka myndigheter eller rapporteringsvägar som kan behöva bedömas?",
                "Har vi dokumenterat varför incidenten omfattas eller inte omfattas av respektive regelverk?",
            ]

        elif "nis2" in question_lower or "cybersäkerhetslagen" in question_lower:
            items = [
                "Har vi identifierat om organisationen kan omfattas av NIS2 eller svensk cybersäkerhetslag?",
                "Har vi bedömt om incidenten är betydande eller rapporteringspliktig enligt relevanta kriterier?",
                "Har vi kontrollerat sektor, verksamhetstyp och ansvarig funktion?",
                "Har vi dokumenterat teknisk påverkan, tidslinje och vidtagna åtgärder?",
                "Har vi jämfört bedömningen med aktuella MSB-källor?",
            ]

        elif "dora" in question_lower or "digital operational resilience" in question_lower:
            items = [
                "Har vi identifierat om verksamheten tillhör den finansiella sektorn?",
                "Har vi bedömt om frågan gäller ICT-risk, incidenthantering, testning eller tredjepartsleverantörer?",
                "Har vi kontrollerat om en ICT-relaterad incident eller störning föreligger?",
                "Har vi dokumenterat påverkan på digital operativ motståndskraft?",
                "Har vi jämfört bedömningen med DORA-källor och relevanta tillsynsmyndigheter?",
            ]

        elif "dataintrång" in question_lower or "obehörig åtkomst" in question_lower:
            items = [
                "Har vi identifierat vilken åtkomst eller påverkan som skett?",
                "Har vi bedömt om åtkomsten var behörig eller obehörig?",
                "Har vi skilt mellan tillåten säkerhetstestning och otillåten aktivitet?",
                "Har vi dokumenterat system, konton, loggar och tidslinje?",
                "Har vi jämfört situationen med svenska straffrättsliga källor?",
            ]

        elif "cyber resilience act" in question_lower or "cyberresiliensakten" in question_lower:
            items = [
                "Har vi identifierat om frågan gäller en produkt med digitala element?",
                "Har vi bedömt om produktdesign, säkerhetskrav eller sårbarhetshantering påverkas?",
                "Har vi kontrollerat ansvar för tillverkare, leverantör eller annan aktör?",
                "Har vi dokumenterat säkerhetsåtgärder, uppdateringar och sårbarhetsprocesser?",
                "Har vi jämfört bedömningen med Cyber Resilience Act-källor?",
            ]

        else:
            items = [
                "Har vi identifierat vilken cyberrättslig eller compliance-fråga som ställs?",
                "Har vi kontrollerat vilka källsektioner CyberLex matchade?",
                "Har vi läst den praktiska förklaringen tillsammans med källkontexten?",
                "Har vi kontrollerat officiella källor och källdatum?",
                "Behövs juridisk eller myndighetsbaserad vägledning innan viktiga beslut fattas?",
            ]

    else:
        heading = "CyberLex assessment checklist"

        if contains_any(suspicious_login_terms):
            items = [
                "Have we preserved the alert or log entry with time, user account, IP address, location, device, and service?",
                "Have we checked whether the login succeeded or was only a failed attempt?",
                "Have we checked whether the same account has more unusual logins, MFA prompts, or failed attempts?",
                "Have we contacted the user through a safe channel to confirm whether the activity was legitimate?",
                "Have we temporarily blocked the account or required fresh authentication if the activity cannot be explained?",
                "Have we revoked active sessions and tokens in identity, VPN, email, and cloud services?",
                "Have we reset the password from a clean device and reviewed MFA methods for unknown or attacker-controlled methods?",
                "Have we reviewed email rules, forwarding, OAuth apps, and delegated access?",
                "Have we checked whether the account was used to access files, systems, customer data, or administrator functions?",
                "Have we assessed whether personal data may have been affected and whether GDPR/IMY assessment is required?",
                "Have we assessed whether the event may be relevant under NIS2/the Swedish Cybersecurity Act if the impact is larger?",
                "Have we documented the timeline, logs, decisions, and actions?",
            ]

        elif contains_any(suspicious_email_terms):
            items = [
                "Have we told the user not to click more links, open attachments, or reply to the email?",
                "Have we preserved the email as evidence, including sender, subject, time, links, attachments, and full headers where possible?",
                "Has the email been reported to IT/security using the organization’s normal process?",
                "Have we searched for the same message in other mailboxes and quarantined or removed it through email security tools where possible?",
                "Have we checked whether anyone clicked the link, opened the attachment, or entered credentials?",
                "If someone clicked or entered credentials, have we treated the account as suspected compromised?",
                "Have we revoked sessions, reset passwords from a clean device, and reviewed MFA if credentials may have leaked?",
                "Have we checked email rules, forwarding, OAuth apps, and suspicious sent messages?",
                "Have we checked whether the email contained malware and whether any endpoint needs isolation?",
                "Have we assessed whether personal data or sensitive information may have been affected?",
                "Have we documented the timeline, users, actions, evidence, and decisions?",
            ]

        elif contains_any(compromised_account_terms):
            items = [
                "Have we blocked or temporarily disabled the account if compromise is likely?",
                "Have we revoked active sessions and tokens in identity, VPN, email, and cloud services?",
                "Was the password reset from a clean device, not from the suspected compromised client?",
                "Have we reviewed MFA methods and removed unknown or attacker-controlled methods?",
                "Have we reviewed email rules, forwarding, OAuth apps, delegated access, and suspicious sent messages?",
                "Have we reviewed sign-in logs, IP addresses, countries, timestamps, and unusual activity?",
                "Have we checked whether the account had administrator rights or access to sensitive systems?",
                "Have we identified what data the account may have viewed, changed, downloaded, or deleted?",
                "Have we assessed whether personal data may have been affected and whether GDPR/IMY assessment is required?",
                "Have we assessed whether the incident may be relevant under NIS2/the Swedish Cybersecurity Act?",
                "Have we documented actions, timeline, evidence, and decisions?",
            ]

        elif contains_any(data_leak_terms):
            items = [
                "Have we confirmed what is known and what remains unclear?",
                "Have we stopped further exposure, such as public access, sharing links, or incorrect permissions?",
                "Have we preserved evidence before making changes, such as screenshots, URLs, logs, timestamps, and permission settings?",
                "Have we identified what data may have been exposed and how long the exposure lasted?",
                "Have we assessed whether the data includes personal data, sensitive data, passwords, tokens, customer data, or HR data?",
                "Have we assessed whether unauthorized access actually occurred or was only possible?",
                "Have we secured affected accounts, API keys, passwords, and systems from a clean administrative environment?",
                "Have we assessed the risk to individuals' rights and freedoms?",
                "Have we assessed whether GDPR notification to IMY is required, normally within 72 hours after awareness?",
                "Have we assessed whether affected individuals must be informed if the risk is high?",
                "Have we assessed whether NIS2/the Swedish Cybersecurity Act or another incident reporting path may also be relevant?",
                "Have we documented decisions, timeline, actions, sources, and who approved the decisions?",
            ]

        elif contains_any(ransomware_terms):
            items = [
                "Have we isolated affected systems to limit further spread?",
                "Have we preserved logs, ransom notes, file extensions, system information, and other technical evidence?",
                "Have we documented the timeline, discovery, impact, and actions taken?",
                "Have we checked which systems, shares, servers, and backup environments are affected?",
                "Have we checked whether backups exist and whether they are unaffected?",
                "Have we assessed whether data may have been stolen before encryption or damage?",
                "Have we assessed whether personal data has been affected?",
                "Have we assessed whether GDPR notification to IMY may be relevant?",
                "Have we assessed whether NIS2/the Swedish Cybersecurity Act or another incident reporting path may be relevant?",
                "Have we compared the assessment with official sources and internal incident response procedures?",
            ]

        elif is_practical_incident_response_question(question) or contains_any(hacking_terms):
            items = [
                "Have we started an incident log with discovery time, system, account, and responsible people?",
                "Have we isolated affected clients, servers, or accounts if this can be done without destroying evidence?",
                "Have we preserved logs, alerts, screenshots, timestamps, and other technical evidence?",
                "Have we avoided deleting logs or reinstalling systems before an initial assessment?",
                "Have we identified affected systems, accounts, users, networks, and data?",
                "Have we secured compromised accounts, revoked sessions, and reset passwords from a clean device?",
                "Have we assessed whether personal data may have been affected?",
                "Have we assessed whether GDPR notification to IMY may be required?",
                "Have we assessed whether NIS2/the Swedish Cybersecurity Act or another incident reporting path may be relevant?",
                "Have we escalated to IT, security, management, legal, data protection, and incident response support when needed?",
                "Have we considered contacting CERT-SE or official incident support for serious incidents?",
                "Have we documented decisions, timeline, actions, sources, and remaining uncertainty?",
            ]

        elif "data breach" in question_lower or "personal data breach" in question_lower or "72" in question_lower:
            items = [
                "Have we contained the incident and preserved relevant evidence?",
                "Have we identified what personal data may have been affected?",
                "Have we assessed whether the breach may create risk to individuals' rights and freedoms?",
                "Have we checked when the organization became aware of the breach?",
                "Have we assessed whether notification to IMY is required within 72 hours?",
                "Have we assessed whether affected individuals may need to be informed if the risk is high?",
                "Have we documented the decision, timeline, actions, and sources?",
            ]

        elif ("nis2" in question_lower or "cybersecurity act" in question_lower) and "gdpr" in question_lower:
            items = [
                "Have we assessed whether the incident is a cybersecurity incident?",
                "Have we assessed whether the incident also affects personal data?",
                "Have we checked whether NIS2/the Swedish Cybersecurity Act and GDPR may both be relevant?",
                "Have we identified which authorities or reporting paths may need to be considered?",
                "Have we documented why each legal framework is or is not relevant?",
            ]

        elif "nis2" in question_lower or "cybersecurity act" in question_lower:
            items = [
                "Have we identified whether the organization may be covered by NIS2 or Swedish cybersecurity rules?",
                "Have we assessed whether the incident may be significant or reportable under relevant criteria?",
                "Have we checked the sector, organization type, and responsible internal function?",
                "Have we documented technical impact, timeline, and actions taken?",
                "Have we compared the assessment with current MSB source material?",
            ]

        elif "dora" in question_lower or "digital operational resilience" in question_lower:
            items = [
                "Have we identified whether the organization belongs to the financial sector?",
                "Have we assessed whether the issue concerns ICT risk, incident handling, testing, or third-party providers?",
                "Have we checked whether an ICT-related incident or disruption exists?",
                "Have we documented the impact on digital operational resilience?",
                "Have we compared the assessment with DORA sources and relevant supervisory guidance?",
            ]

        elif "dataintrång" in question_lower or "unauthorized access" in question_lower or "data intrusion" in question_lower:
            items = [
                "Have we identified what access or interference occurred?",
                "Have we assessed whether the access was authorized or unauthorized?",
                "Have we separated authorized security testing from unauthorized activity?",
                "Have we documented systems, accounts, logs, and timeline?",
                "Have we compared the situation with Swedish criminal-law source material?",
            ]

        elif "cyber resilience act" in question_lower or "products with digital elements" in question_lower:
            items = [
                "Have we identified whether the question concerns a product with digital elements?",
                "Have we assessed whether product design, security requirements, or vulnerability handling are affected?",
                "Have we checked responsibility for the manufacturer, supplier, or other actor?",
                "Have we documented security measures, updates, and vulnerability processes?",
                "Have we compared the assessment with Cyber Resilience Act sources?",
            ]

        else:
            items = [
                "Have we identified the cybersecurity law or compliance issue?",
                "Have we checked which source sections CyberLex matched?",
                "Have we read the practical explanation together with the source context?",
                "Have we checked official sources and source dates?",
                "Is legal or authority-based guidance needed before important decisions are made?",
            ]

    checklist_items = "".join([f"<li>{item}</li>" for item in items])

    return (
        f'<div class="checklist-card">'
        f'<ul>{checklist_items}</ul>'
        f'</div>'
    )


def generate_incident_log_template(question, language="English"):
    # Generates a simple copyable incident log template for defensive incident-response questions.
    # This helps the user document facts, evidence, decisions, reporting assessment, and next owner.
    # The template is shown only for practical incident-response questions.

    if not is_practical_incident_response_question(question):
        return ""

    use_swedish = language == "Svenska"

    if is_suspicious_login_question(question):
        incident_type_en = "Suspicious login activity"
        incident_type_sv = "Misstänkt inloggning"
        extra_fields_en = [
            "Login timestamp:",
            "Username / account:",
            "Source IP / country / device:",
            "Was login successful or blocked:",
            "MFA event observed:",
            "User confirmed activity as legitimate:",
            "Sessions or tokens revoked:",
        ]
        extra_fields_sv = [
            "Tidpunkt för inloggning:",
            "Användarnamn / konto:",
            "Käll-IP / land / enhet:",
            "Lyckades eller blockerades inloggningen:",
            "Observerad MFA-händelse:",
            "Har användaren bekräftat aktiviteten som legitim:",
            "Återkallade sessioner eller tokens:",
        ]

    elif is_suspicious_email_question(question):
        incident_type_en = "Suspicious email or phishing"
        incident_type_sv = "Misstänkt mejl eller phishing"
        extra_fields_en = [
            "Sender address:",
            "Email subject:",
            "Received time:",
            "Links or attachments:",
            "User clicked link or opened attachment:",
            "Credentials entered:",
            "Same email found for other users:",
        ]
        extra_fields_sv = [
            "Avsändaradress:",
            "Mejlämne:",
            "Mottagen tidpunkt:",
            "Länkar eller bilagor:",
            "Har användaren klickat på länk eller öppnat bilaga:",
            "Har inloggningsuppgifter skrivits in:",
            "Samma mejl hittat hos andra användare:",
        ]

    elif is_compromised_account_question(question):
        incident_type_en = "Compromised account"
        incident_type_sv = "Komprometterat konto"
        extra_fields_en = [
            "Affected account:",
            "Account disabled or protected:",
            "Password reset completed:",
            "MFA methods reviewed:",
            "Active sessions revoked:",
            "Mailbox rules / forwarding / OAuth apps checked:",
            "Data or systems accessed by the account:",
        ]
        extra_fields_sv = [
            "Berört konto:",
            "Kontot blockerat eller skyddat:",
            "Lösenord återställt:",
            "MFA-metoder granskade:",
            "Aktiva sessioner återkallade:",
            "E-postregler / vidarebefordran / OAuth-appar kontrollerade:",
            "Data eller system som kontot har åtkomst till:",
        ]

    elif is_data_leak_response_question(question):
        incident_type_en = "Data leak or personal data breach"
        incident_type_sv = "Dataläcka eller personuppgiftsincident"
        extra_fields_en = [
            "Type of data involved:",
            "Personal data involved:",
            "Number of affected people if known:",
            "Exposure contained:",
            "Risk to individuals assessed:",
            "IMY notification assessment:",
            "Affected individuals notification assessment:",
        ]
        extra_fields_sv = [
            "Typ av data som berörs:",
            "Personuppgifter berörda:",
            "Antal berörda personer om känt:",
            "Exponering begränsad:",
            "Risk för registrerade bedömd:",
            "Bedömning av IMY-anmälan:",
            "Bedömning av information till berörda personer:",
        ]

    elif is_ransomware_or_malware_question(question):
        incident_type_en = "Ransomware or malware"
        incident_type_sv = "Ransomware eller skadlig kod"
        extra_fields_en = [
            "Affected systems:",
            "Systems isolated:",
            "Files encrypted or altered:",
            "Backups checked:",
            "Malware sample or alert preserved:",
            "Lateral movement suspected:",
            "Recovery owner:",
        ]
        extra_fields_sv = [
            "Berörda system:",
            "System isolerade:",
            "Filer krypterade eller ändrade:",
            "Backuper kontrollerade:",
            "Prov på skadlig kod eller larm sparat:",
            "Misstänkt lateral rörelse:",
            "Ansvarig för återställning:",
        ]

    else:
        incident_type_en = "Suspected cyber incident"
        incident_type_sv = "Misstänkt cyberincident"
        extra_fields_en = [
            "Affected system / account / service:",
            "Observed alert or symptom:",
            "Evidence preserved:",
            "Containment action:",
            "Technical impact:",
            "Business impact:",
            "Escalation needed:",
        ]
        extra_fields_sv = [
            "Berört system / konto / tjänst:",
            "Observerat larm eller symptom:",
            "Sparad bevisning:",
            "Begränsningsåtgärd:",
            "Teknisk påverkan:",
            "Verksamhetspåverkan:",
            "Behöver eskaleras:",
        ]

    if use_swedish:
        title = "Incidentloggmall"
        intro = (
            "Använd denna mall för att dokumentera vad som är känt, vilka bevis som har sparats, "
            "vilka beslut som har tagits och om rapporteringsbedömning behövs."
        )
        common_fields = [
            f"Incidenttyp: {incident_type_sv}",
            "Tidpunkt för upptäckt:",
            "Rapporterad av:",
            "Första mottagare / ansvarig:",
            "Kort sammanfattning:",
        ]
        final_fields = [
            "Personuppgifter kan vara påverkade: Ja / Nej / Okänt",
            "GDPR / IMY-bedömning behövs: Ja / Nej / Okänt",
            "NIS2 / cybersäkerhetslagen-bedömning behövs: Ja / Nej / Okänt",
            "CERT-SE eller annan eskalering övervägd:",
            "Beslut och motivering:",
            "Nästa åtgärd:",
            "Nästa ansvarig:",
            "Senast uppdaterad:",
        ]
        template_lines = common_fields + extra_fields_sv + final_fields

    else:
        title = "Incident log template"
        intro = (
            "Use this template to document what is known, what evidence has been preserved, "
            "which decisions were made, and whether reporting assessment is needed."
        )
        common_fields = [
            f"Incident type: {incident_type_en}",
            "Time discovered:",
            "Reported by:",
            "First receiver / owner:",
            "Short summary:",
        ]
        final_fields = [
            "Personal data may be affected: Yes / No / Unknown",
            "GDPR / IMY assessment needed: Yes / No / Unknown",
            "NIS2 / Swedish Cybersecurity Act assessment needed: Yes / No / Unknown",
            "CERT-SE or other escalation considered:",
            "Decision and reason:",
            "Next action:",
            "Next owner:",
            "Last updated:",
        ]
        template_lines = common_fields + extra_fields_en + final_fields

    template_text = "\n".join(template_lines)

    return (
        f'<div class="incident-log-card">'
        f'<div class="incident-log-card-title">{title}</div>'
        f'<div class="incident-log-card-text">{intro}</div>'
        f'<div class="incident-log-template">{template_text}</div>'
        f'</div>'
    )



def html_to_plain_text(html_text):
    # Converts CyberLex HTML cards into plain text for the copy-ready incident summary.
    # Streamlit renders the cards as HTML, but incident notes should be easy to copy
    # into tickets, reports, or documentation without carrying UI tags with them.
    text = str(html_text or "")

    replacements = {
        "<li>": "- ",
        "</li>": "\n",
        "<ul>": "\n",
        "</ul>": "\n",
        "<br>": "\n",
        "<br/>": "\n",
        "<br />": "\n",
        "</div>": "\n",
        "</p>": "\n",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"<[^>]+>", "", text)

    html_entities = {
        "&nbsp;": " ",
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&quot;": '"',
        "&#39;": "'",
    }

    for old, new in html_entities.items():
        text = text.replace(old, new)

    lines = [line.strip() for line in text.splitlines()]
    cleaned_lines = []
    previous_blank = False

    for line in lines:
        if not line:
            if not previous_blank and cleaned_lines:
                cleaned_lines.append("")
            previous_blank = True
            continue

        cleaned_lines.append(line)
        previous_blank = False

    return "\n".join(cleaned_lines).strip()


def remove_duplicate_lines(text):
    # Removes repeated consecutive lines from generated plain-text summaries.
    # This keeps downloaded incident notes readable instead of turning them into
    # bureaucratic echo chambers.
    cleaned_lines = []
    previous_line = None

    for raw_line in str(text or "").splitlines():
        line = raw_line.rstrip()
        comparable = line.strip().lower()

        if comparable and comparable == previous_line:
            continue

        cleaned_lines.append(line)
        previous_line = comparable if comparable else None

    return "\n".join(cleaned_lines).strip()


def clean_answer_for_download(answer_text, language="English"):
    # Removes educational disclaimer text from the answer block because the
    # downloaded note already has one short disclaimer at the end.
    use_swedish = language == "Svenska"

    disclaimer_markers = [
        "this is defensive educational guidance",
        "this is educational guidance",
        "not legal advice",
        "professional incident response",
        "for serious incidents",
        "detta är defensiv pedagogisk vägledning",
        "detta är pedagogisk vägledning",
        "inte juridisk rådgivning",
        "professionell incidenthantering",
        "vid allvarliga incidenter",
    ]

    kept_lines = []
    for raw_line in str(answer_text or "").splitlines():
        line = raw_line.strip()
        lower = line.lower()

        if not line:
            kept_lines.append("")
            continue

        if any(marker in lower for marker in disclaimer_markers):
            continue

        kept_lines.append(line)

    return remove_duplicate_lines("\n".join(kept_lines).strip())


def clean_incident_log_for_download(incident_log_text, language="English"):
    # The visual incident log card has a title and explanatory intro.
    # The downloaded file already has a section title, so keep only the fields.
    use_swedish = language == "Svenska"

    removable_starts = [
        "incident log template",
        "incidentloggmall",
        "use this template to document",
        "använd denna mall för att dokumentera",
    ]

    kept_lines = []
    for raw_line in str(incident_log_text or "").splitlines():
        line = raw_line.strip()
        lower = line.lower()

        if not line:
            if kept_lines and kept_lines[-1] != "":
                kept_lines.append("")
            continue

        if any(lower.startswith(marker) for marker in removable_starts):
            continue

        kept_lines.append(line)

    return remove_duplicate_lines("\n".join(kept_lines).strip())


def build_source_list_for_copy(search_results, language="English", max_sources=3):
    # Builds a short plain-text source list for copy-ready incident summaries.
    # The full clickable source links, metadata, source context, and relevance scores
    # are already shown in the CyberLex app. The downloaded incident note should stay
    # readable and practical, not become a raw retrieval dump.

    use_swedish = language == "Svenska"

    if use_swedish:
        no_sources_text = "Inga källor hittades."
        shown_in_app_note = (
            "Officiella länkar, källmetadata och full källkontext visas i CyberLex Sweden-appen."
        )
    else:
        no_sources_text = "No sources found."
        shown_in_app_note = (
            "Official source links, source metadata, and full source context are shown in the CyberLex Sweden app."
        )

    if not search_results:
        return no_sources_text

    unique_sources = []
    seen_pairs = set()

    for result in search_results:
        filename = str(result.get("filename", "")).strip()
        section = str(result.get("section", "")).strip()

        if not filename:
            continue

        source_area = get_friendly_source_area_name(filename, language)
        display_section = localize_section_name(section, language)
        pair_key = (source_area.lower(), display_section.lower())

        if pair_key in seen_pairs:
            continue

        seen_pairs.add(pair_key)

        if display_section:
            if use_swedish:
                unique_sources.append(f"- {source_area} | Sektion: {display_section}")
            else:
                unique_sources.append(f"- {source_area} | Section: {display_section}")
        else:
            unique_sources.append(f"- {source_area}")

        if len(unique_sources) >= max_sources:
            break

    if not unique_sources:
        return no_sources_text

    source_lines = list(unique_sources)
    source_lines.append("")
    source_lines.append(shown_in_app_note)

    return "\n".join(source_lines)


def get_soc_incident_profile(question, language="English"):
    # Produces a SOC-style incident profile for the downloadable incident report.
    # This is a triage aid, not a final severity rating or legal classification.
    question_lower = normalize_query_text(question)
    use_swedish = language == "Svenska"

    if is_encrypted_files_possible_ransomware_question(question):
        if use_swedish:
            return {
                "type": "Möjlig ransomware eller skadlig kod",
                "priority": "Hög, om krypteringen är oväntad eller filer är otillgängliga",
                "objective": "Begränsa spridning, bevara bevisning, förstå omfattning och återställa kontrollerat.",
                "risks": [
                    "Filer eller system kan vara otillgängliga.",
                    "Angriparen kan fortfarande ha åtkomst.",
                    "Data kan ha kopierats innan kryptering.",
                    "Återställning från backup kan misslyckas om åtkomstvägen inte är stängd.",
                ],
            }
        return {
            "type": "Possible ransomware or malware",
            "priority": "High if encryption is unexpected or files are inaccessible",
            "objective": "Limit spread, preserve evidence, understand scope, and recover in a controlled way.",
            "risks": [
                "Files or systems may be unavailable.",
                "The attacker may still have access.",
                "Data may have been copied before encryption.",
                "Backup recovery may fail if the access path is not closed.",
            ],
        }

    if is_data_leak_response_question(question):
        if use_swedish:
            return {
                "type": "Möjlig dataläcka eller personuppgiftsincident",
                "priority": "Hög, om personuppgifter eller känslig information kan ha exponerats",
                "objective": "Stoppa exponering, bevara bevisning, fastställ berörda data och bedöm anmälningsbehov.",
                "risks": [
                    "Personuppgifter kan ha exponerats.",
                    "Berörda personer kan behöva informeras vid hög risk.",
                    "IMY-anmälan kan behöva bedömas inom 72 timmar.",
                    "Incidenten kan även beröra andra rapporteringsvägar.",
                ],
            }
        return {
            "type": "Possible data leak or personal data breach",
            "priority": "High if personal data or sensitive information may be exposed",
            "objective": "Stop exposure, preserve evidence, identify affected data, and assess notification needs.",
            "risks": [
                "Personal data may have been exposed.",
                "Affected individuals may need to be informed if risk is high.",
                "IMY notification may need to be assessed within 72 hours.",
                "The incident may also trigger other reporting paths.",
            ],
        }

    if is_compromised_account_question(question):
        if use_swedish:
            return {
                "type": "Komprometterat konto",
                "priority": "Hög, om kontot har åtkomst till känsliga system eller data",
                "objective": "Stoppa obehörig åtkomst, säkra kontot och identifiera vad kontot har nått.",
                "risks": [
                    "Angriparen kan ha aktiv session eller token.",
                    "E-postregler, OAuth-appar eller vidarebefordran kan finnas kvar.",
                    "Data eller system kan ha nåtts via kontot.",
                    "Fler konton kan vara påverkade.",
                ],
            }
        return {
            "type": "Compromised account",
            "priority": "High if the account has access to sensitive systems or data",
            "objective": "Stop unauthorized access, secure the account, and identify what the account accessed.",
            "risks": [
                "The attacker may still have an active session or token.",
                "Mailbox rules, OAuth apps, or forwarding may persist.",
                "Data or systems may have been accessed through the account.",
                "More accounts may be affected.",
            ],
        }

    if is_suspicious_login_question(question):
        if use_swedish:
            return {
                "type": "Misstänkt inloggning",
                "priority": "Medel till hög beroende på konto, lyckad inloggning och åtkomst",
                "objective": "Bekräfta om inloggningen var legitim, säkra kontot och bevara relevanta loggar.",
                "risks": [
                    "Inloggningen kan vara obehörig.",
                    "MFA kan ha godkänts av fel person.",
                    "Sessioner eller tokens kan fortfarande vara aktiva.",
                    "Kontot kan ha använts för åtkomst till data eller system.",
                ],
            }
        return {
            "type": "Suspicious login activity",
            "priority": "Medium to high depending on account, success, and access",
            "objective": "Confirm whether the login was legitimate, secure the account, and preserve relevant logs.",
            "risks": [
                "The login may be unauthorized.",
                "MFA may have been approved by the wrong person.",
                "Sessions or tokens may still be active.",
                "The account may have been used to access data or systems.",
            ],
        }

    if is_suspicious_link_question(question) or is_suspicious_email_question(question):
        if use_swedish:
            return {
                "type": "Klick på misstänkt länk eller phishing",
                "priority": "Medel till hög beroende på om uppgifter skrevs in, fil kördes eller konto påverkades",
                "objective": "Bevara meddelandet/länken, identifiera användarens åtgärder och kontrollera konto eller enhet.",
                "risks": [
                    "Användaren kan ha skrivit in lösenord eller MFA-kod.",
                    "En fil kan ha laddats ner eller körts.",
                    "Kontot kan vara komprometterat.",
                    "Samma meddelande kan ha nått fler användare.",
                ],
            }
        return {
            "type": "Suspicious link click or phishing",
            "priority": "Medium to high depending on credentials, file execution, or account impact",
            "objective": "Preserve the message/link, identify user actions, and check the account or device.",
            "risks": [
                "The user may have entered a password or MFA code.",
                "A file may have been downloaded or executed.",
                "The account may be compromised.",
                "The same message may have reached other users.",
            ],
        }

    if is_suspected_hacking_question(question):
        if use_swedish:
            return {
                "type": "Misstänkt intrång eller hackning",
                "priority": "Hög tills omfattningen är klarlagd",
                "objective": "Begränsa intrång, bevara bevisning, identifiera åtkomstväg och skydda berörda system.",
                "risks": [
                    "Angriparen kan fortfarande ha åtkomst.",
                    "Flera system eller konton kan vara påverkade.",
                    "Loggar kan behöva säkras snabbt.",
                    "Personuppgifter eller verksamhetskritiska system kan vara berörda.",
                ],
            }
        return {
            "type": "Suspected intrusion or hacking",
            "priority": "High until scope is understood",
            "objective": "Contain intrusion, preserve evidence, identify access path, and protect affected systems.",
            "risks": [
                "The attacker may still have access.",
                "Multiple systems or accounts may be affected.",
                "Logs may need to be preserved quickly.",
                "Personal data or business-critical systems may be involved.",
            ],
        }

    if use_swedish:
        return {
            "type": "Cyberincident för triage",
            "priority": "Bedöms utifrån påverkan, data, system och pågående risk",
            "objective": "Fastställ vad som hänt, vad som påverkas och vilka första åtgärder som krävs.",
            "risks": [
                "Incidenttypen är ännu inte bekräftad.",
                "Teknisk påverkan kan vara större än först känt.",
                "Juridisk eller regulatorisk rapportering kan behöva bedömas.",
            ],
        }

    return {
        "type": "Cyber incident for triage",
        "priority": "Assess based on impact, data, systems, and active risk",
        "objective": "Establish what happened, what is affected, and which first actions are required.",
        "risks": [
            "The incident type is not yet confirmed.",
            "Technical impact may be larger than first known.",
            "Legal or regulatory reporting may need to be assessed.",
        ],
    }


def generate_soc_triage_block(question, language="English"):
    # Builds a SOC-oriented triage section for the downloaded incident report.
    profile = get_soc_incident_profile(question, language)
    use_swedish = language == "Svenska"

    if use_swedish:
        labels = {
            "heading": "SOC-triage",
            "type": "Incidenttyp",
            "priority": "Initial prioritet",
            "objective": "Primärt mål",
            "risks": "Viktigaste risker att bedöma",
        }
    else:
        labels = {
            "heading": "SOC triage",
            "type": "Incident type",
            "priority": "Initial priority",
            "objective": "Primary objective",
            "risks": "Key risks to assess",
        }

    risk_lines = "\n".join(f"- {risk}" for risk in profile["risks"])

    return (
        f"{labels['heading']}\n"
        f"{'-' * len(labels['heading'])}\n"
        f"{labels['type']}: {profile['type']}\n"
        f"{labels['priority']}: {profile['priority']}\n"
        f"{labels['objective']}: {profile['objective']}\n\n"
        f"{labels['risks']}:\n{risk_lines}"
    )


def generate_soc_evidence_and_containment_block(question, language="English"):
    # Adds SOC-style evidence, containment, escalation, and reporting prompts.
    use_swedish = language == "Svenska"
    encrypted_case = is_encrypted_files_possible_ransomware_question(question)
    data_leak_case = is_data_leak_response_question(question)
    account_case = is_compromised_account_question(question) or is_suspicious_login_question(question)
    link_case = is_suspicious_link_question(question) or is_suspicious_email_question(question)

    if use_swedish:
        heading = "SOC-åtgärdsstöd"
        evidence_heading = "Bevisning och artefakter att säkra"
        containment_heading = "Begränsning och stabilisering"
        escalation_heading = "Eskalering och rapporteringsbedömning"

        evidence_items = [
            "Tidslinje: upptäckt, första åtgärd, eskalering och större förändringar.",
            "Berörda konton, system, klienter, servrar, tjänster och nätverkssegment.",
            "Relevanta loggar från identitet, endpoint, e-post, nätverk, brandvägg, VPN, EDR och molntjänster.",
            "Skärmbilder, larm, felmeddelanden och användarens beskrivning.",
        ]
        containment_items = [
            "Begränsa fortsatt påverkan utan att förstöra bevisning.",
            "Undvik onödiga ominstallationer, rensningar eller återställningar innan loggar och artefakter har säkrats.",
            "Dokumentera varje åtgärd, vem som tog den och när.",
        ]
        escalation_items = [
            "Eskalera till IT/säkerhet, ansvarig chef, dataskydd/legal och extern incidentrespons vid behov.",
            "Bedöm om personuppgifter kan vara berörda och om IMY/GDPR behöver hanteras.",
            "Bedöm om NIS2/cybersäkerhetslagen, CERT-SE/MSB eller annan incidentrapportering kan vara relevant.",
        ]

        if encrypted_case:
            evidence_items.extend([
                "Ransom note, ändrade filnamnstillägg, exempel på krypterade filer och berörda kataloger.",
                "Backupstatus, backup-loggar och tecken på manipulation av backupmiljö.",
            ])
            containment_items.extend([
                "Isolera berörda system från nätverket om det kan göras säkert.",
                "Återställ inte från backup förrän åtkomstvägen är förstådd och stängd.",
            ])

        if data_leak_case:
            evidence_items.extend([
                "Vilka datamängder som kan ha exponerats, antal poster och kategorier av personuppgifter.",
                "Exponeringsväg: publik länk, felbehörighet, komprometterat konto, e-post, molntjänst eller systemfel.",
            ])
            escalation_items.extend([
                "Starta 72-timmarsbedömning för IMY om personuppgiftsincident kan föreligga.",
                "Bedöm om berörda personer behöver informeras vid hög risk.",
            ])

        if account_case:
            evidence_items.extend([
                "Inloggningstid, käll-IP, enhet, land, MFA-händelser, sessioner och tokenaktivitet.",
                "Mailbox-regler, vidarebefordran, OAuth-appar och misstänkt skickad e-post.",
            ])
            containment_items.extend([
                "Återkalla sessioner och tokens, återställ lösenord från ren enhet och granska MFA-metoder.",
            ])

        if link_case:
            evidence_items.extend([
                "URL, domän, avsändare, meddelandehuvuden, bilagor, nedladdningar och om uppgifter skrevs in.",
                "Vilka användare som fick meddelandet och vilka som klickade.",
            ])
            containment_items.extend([
                "Blockera skadliga länkar/domäner och sök efter samma meddelande hos andra användare där det är lämpligt.",
            ])

    else:
        heading = "SOC action support"
        evidence_heading = "Evidence and artifacts to preserve"
        containment_heading = "Containment and stabilization"
        escalation_heading = "Escalation and reporting assessment"

        evidence_items = [
            "Timeline: discovery, first action, escalation, and major changes.",
            "Affected accounts, systems, endpoints, servers, services, and network segments.",
            "Relevant logs from identity, endpoint, email, network, firewall, VPN, EDR, and cloud services.",
            "Screenshots, alerts, error messages, and the user's description.",
        ]
        containment_items = [
            "Limit further impact without destroying evidence.",
            "Avoid unnecessary reinstall, cleanup, or restore actions before logs and artifacts are preserved.",
            "Document every action, who took it, and when.",
        ]
        escalation_items = [
            "Escalate to IT/security, management, data protection/legal, and external incident response when needed.",
            "Assess whether personal data may be involved and whether GDPR/IMY handling is required.",
            "Assess whether NIS2/the Swedish Cybersecurity Act, CERT-SE/MSB, or another reporting path may be relevant.",
        ]

        if encrypted_case:
            evidence_items.extend([
                "Ransom note, changed file extensions, samples of encrypted files, and affected directories.",
                "Backup status, backup logs, and signs of backup-environment manipulation.",
            ])
            containment_items.extend([
                "Isolate affected systems from the network if it can be done safely.",
                "Do not restore from backup until the access path is understood and closed.",
            ])

        if data_leak_case:
            evidence_items.extend([
                "Potentially exposed datasets, record counts, and categories of personal data.",
                "Exposure path: public link, wrong permissions, compromised account, email, cloud service, or system error.",
            ])
            escalation_items.extend([
                "Start the 72-hour IMY assessment if a personal data breach may have occurred.",
                "Assess whether affected individuals need to be informed if risk is high.",
            ])

        if account_case:
            evidence_items.extend([
                "Login time, source IP, device, country, MFA events, sessions, and token activity.",
                "Mailbox rules, forwarding, OAuth apps, and suspicious sent email.",
            ])
            containment_items.extend([
                "Revoke sessions and tokens, reset password from a clean device, and review MFA methods.",
            ])

        if link_case:
            evidence_items.extend([
                "URL, domain, sender, message headers, attachments, downloads, and whether credentials were entered.",
                "Which users received the message and which users clicked.",
            ])
            containment_items.extend([
                "Block malicious links/domains and search for the same message across other users where appropriate.",
            ])

    def list_lines(items):
        return "\n".join(f"- {item}" for item in items)

    return (
        f"{heading}\n"
        f"{'-' * len(heading)}\n"
        f"{evidence_heading}:\n{list_lines(evidence_items)}\n\n"
        f"{containment_heading}:\n{list_lines(containment_items)}\n\n"
        f"{escalation_heading}:\n{list_lines(escalation_items)}"
    )



def strip_download_answer_heading(answer_text, language="English"):
    # The visual answer often starts with a title such as
    # "Recommended first steps for...". The downloaded report already has a
    # section heading, so remove that first visual title to avoid repetition.
    use_swedish = language == "Svenska"

    removable_starts = [
        "recommended first steps",
        "recommended actions",
        "rekommenderade första steg",
        "rekommenderade åtgärder",
    ]

    lines = str(answer_text or "").splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)

    if lines:
        first = lines[0].strip().lower()
        if any(first.startswith(marker) for marker in removable_starts):
            lines = lines[1:]

    return remove_duplicate_lines("\n".join(lines).strip())


def generate_soc_download_control_checklist(question, language="English"):
    # Builds a SOC-style validation checklist for the downloaded report.
    # This avoids copying the same first-step list twice while still giving an
    # analyst clear defensive checkpoints. Because apparently repeating the same
    # paragraph with a question mark does not summon operational maturity.
    use_swedish = language == "Svenska"
    encrypted_case = is_encrypted_files_possible_ransomware_question(question) or is_ransomware_response_question(question)
    data_leak_case = is_data_leak_response_question(question)
    account_case = is_compromised_account_question(question) or is_suspicious_login_question(question)
    link_case = is_suspicious_link_question(question) or is_suspicious_email_question(question)
    hacking_case = is_suspected_hacking_question(question)

    if use_swedish:
        items = [
            "- [ ] Incidentägare är utsedd och aktuell status är dokumenterad.",
            "- [ ] Tidslinje är påbörjad med upptäckt, första åtgärd, eskalering och större ändringar.",
            "- [ ] Relevanta loggar och bevis är bevarade innan destruktiva åtgärder görs.",
            "- [ ] Berörda konton, system, användare, data och tjänster är identifierade eller markeras som okända.",
            "- [ ] Påverkan på tillgänglighet, integritet och konfidentialitet är bedömd.",
            "- [ ] Personuppgiftsrisk och eventuell GDPR/IMY-bedömning är tilldelad ansvarig person.",
            "- [ ] Behov av NIS2/cybersäkerhetslagen, CERT-SE/MSB eller annan eskalering är bedömt.",
            "- [ ] Nästa åtgärd, nästa ägare och uppföljningstid är dokumenterade.",
        ]

        if encrypted_case:
            items[3:3] = [
                "- [ ] Berörda värdar är isolerade eller riskbedömda innan de återansluts.",
                "- [ ] Ransom note, ändrade filnamnstillägg, krypterade filexempel och backupstatus är dokumenterade.",
                "- [ ] Återställning från backup väntar tills åtkomstvägen är förstådd och stängd.",
            ]

        if data_leak_case:
            items[3:3] = [
                "- [ ] Exponeringsväg, datamängd, datakategorier och berörda personer är identifierade eller markeras som okända.",
                "- [ ] Exponeringen är stoppad eller begränsad och bevis på tidigare exponering är sparade.",
                "- [ ] 72-timmarsbedömning för IMY är påbörjad om personuppgiftsincident kan ha inträffat.",
            ]

        if account_case:
            items[3:3] = [
                "- [ ] Sessions- och tokenåtkomst är återkallad där det är relevant.",
                "- [ ] MFA-metoder, e-postregler, vidarebefordran, OAuth-appar och delegerad åtkomst är kontrollerade.",
                "- [ ] Inloggningshistorik, privilegier och åtkomst till känsliga system eller data är granskade.",
            ]

        if link_case:
            items[3:3] = [
                "- [ ] URL/domän, avsändare, headers, bilagor och eventuell nedladdning är dokumenterade.",
                "- [ ] Det är kontrollerat om användaren skrev in lösenord, MFA-kod eller annan känslig information.",
                "- [ ] Blockering/sökning efter samma meddelande eller länk är bedömd.",
            ]

        if hacking_case and not account_case:
            items[3:3] = [
                "- [ ] Initial åtkomstväg, påverkade system och möjlig lateral rörelse är bedömda eller markeras som okända.",
                "- [ ] Åtgärder som kan förstöra bevis har pausats tills loggar och artefakter är sparade.",
            ]

    else:
        items = [
            "- [ ] Incident owner is assigned and current status is documented.",
            "- [ ] Timeline is started with discovery, first action, escalation, and major changes.",
            "- [ ] Relevant logs and evidence are preserved before destructive actions are taken.",
            "- [ ] Affected accounts, systems, users, data, and services are identified or marked as unknown.",
            "- [ ] Availability, integrity, and confidentiality impact has been assessed.",
            "- [ ] Personal data risk and possible GDPR/IMY assessment have an assigned owner.",
            "- [ ] NIS2/Swedish Cybersecurity Act, CERT-SE/MSB, or other escalation needs have been assessed.",
            "- [ ] Next action, next owner, and follow-up time are documented.",
        ]

        if encrypted_case:
            items[3:3] = [
                "- [ ] Affected hosts are isolated or risk-assessed before reconnecting.",
                "- [ ] Ransom note, changed file extensions, encrypted file samples, and backup status are documented.",
                "- [ ] Backup restore is delayed until the access path is understood and closed.",
            ]

        if data_leak_case:
            items[3:3] = [
                "- [ ] Exposure path, dataset size, data categories, and affected individuals are identified or marked as unknown.",
                "- [ ] Exposure is stopped or limited, and evidence of prior exposure is preserved.",
                "- [ ] 72-hour IMY assessment is started if a personal data breach may have occurred.",
            ]

        if account_case:
            items[3:3] = [
                "- [ ] Session and token access has been revoked where relevant.",
                "- [ ] MFA methods, mailbox rules, forwarding, OAuth apps, and delegated access are checked.",
                "- [ ] Sign-in history, privileges, and access to sensitive systems or data are reviewed.",
            ]

        if link_case:
            items[3:3] = [
                "- [ ] URL/domain, sender, headers, attachments, and possible download are documented.",
                "- [ ] It is checked whether the user entered a password, MFA code, or other sensitive information.",
                "- [ ] Blocking/searching for the same message or link has been assessed.",
            ]

        if hacking_case and not account_case:
            items[3:3] = [
                "- [ ] Initial access path, affected systems, and possible lateral movement are assessed or marked as unknown.",
                "- [ ] Actions that may destroy evidence are paused until logs and artifacts are preserved.",
            ]

    return "\n".join(items)


def generate_copy_ready_incident_summary(question, best_match, search_results, language="English"):
    # Builds a SOC-oriented Markdown incident report.
    # Markdown makes the downloaded report look professional in VS Code, GitHub,
    # Obsidian, Typora, and many ticket systems while staying easy to edit.
    # The report stays defensive and practical, while avoiding raw retrieval scores
    # and source dumps that belong in diagnostics, not in a SOC handover note.

    if not is_practical_incident_response_question(question):
        return ""

    use_swedish = language == "Svenska"

    if use_swedish:
        title = "CyberLex Sweden SOC-incidentrapport"
        purpose_label = "Syfte"
        purpose_text = (
            "Initialt defensivt triageunderlag för SOC, IT-drift eller incidentansvarig. "
            "Rapporten ska hjälpa till att bevara fakta, begränsa påverkan och dokumentera nästa steg."
        )
        metadata_label = "Rapportmetadata"
        generated_by_label = "Genererad av"
        report_type_label = "Rapporttyp"
        report_type_text = "SOC-triageunderlag"
        status_label = "Status"
        status_text = "Utkast / arbetsunderlag"
        classification_label = "Klassificering"
        classification_text = "Intern"
        priority_review_label = "Prioritetsgranskning"
        priority_review_text = "Krävs av incidentägare"
        prepared_by_label = "Förberedd av"
        prepared_by_text = ""
        generated_time_label = "Genererad tid"
        generated_time_text = ""
        question_label = "Fråga / rapporterad händelse"
        answer_label = "Rekommenderade första steg"
        soc_triage_label = "SOC-triage"
        soc_actions_label = "SOC-åtgärdsstöd"
        checklist_label = "SOC-kontrollchecklista"
        incident_log_label = "Incidentloggmall"
        source_label = "Kort källnotering"
        handling_label = "Hanteringsnotering"
        handling_text = (
            "Behandla detta som ett arbetsunderlag. Komplettera med faktiska tider, systemnamn, konton, "
            "loggkällor, ägare och beslut innan det används i ett ärende eller en slutlig incidentrapport."
        )
        limitation_heading = "Ansvarsbegränsning"
        limitation = (
            "Detta är ett pedagogiskt underlag från CyberLex Sweden. Det är inte juridisk rådgivning, "
            "inte en slutlig incidentklassning och ersätter inte officiella källor, jurist, dataskyddsombud "
            "eller professionellt incidenthanteringsteam."
        )
    else:
        title = "CyberLex Sweden SOC Incident Report"
        purpose_label = "Purpose"
        purpose_text = (
            "Initial defensive triage note for SOC, IT operations, or an incident owner. "
            "The report is meant to preserve facts, reduce impact, and document next steps."
        )
        metadata_label = "Report metadata"
        generated_by_label = "Generated by"
        report_type_label = "Report type"
        report_type_text = "SOC triage note"
        status_label = "Status"
        status_text = "Draft / working note"
        classification_label = "Classification"
        classification_text = "Internal"
        priority_review_label = "Priority review"
        priority_review_text = "Required by incident owner"
        prepared_by_label = "Prepared by"
        prepared_by_text = ""
        generated_time_label = "Generated time"
        generated_time_text = ""
        question_label = "Question / reported event"
        answer_label = "Recommended first steps"
        soc_triage_label = "SOC triage"
        soc_actions_label = "SOC action support"
        checklist_label = "SOC control checklist"
        incident_log_label = "Incident log template"
        source_label = "Short source note"
        handling_label = "Handling note"
        handling_text = (
            "Treat this as a working note. Add real times, system names, accounts, log sources, owners, "
            "and decisions before using it in a ticket or final incident report."
        )
        limitation_heading = "Disclaimer"
        limitation = (
            "This is an educational CyberLex Sweden report. It is not legal advice, not a final incident "
            "classification, and does not replace official sources, a lawyer, data protection officer, or a "
            "professional incident response team."
        )

    answer_text = strip_download_answer_heading(
        clean_answer_for_download(
            html_to_plain_text(generate_simple_answer(question, best_match, language)),
            language
        ),
        language
    )
    checklist_text = generate_soc_download_control_checklist(question, language)
    incident_log_text = clean_incident_log_for_download(
        html_to_plain_text(generate_incident_log_template(question, language)),
        language
    )
    source_text = build_source_list_for_copy(search_results, language, max_sources=3)
    soc_triage_text = generate_soc_triage_block(question, language)
    soc_action_text = generate_soc_evidence_and_containment_block(question, language)

    # Avoid repeated headings inside the SOC helper blocks. The main Markdown report
    # already has section headers, because one chain of command is enough.
    soc_triage_body = "\n".join(soc_triage_text.splitlines()[2:]).strip()
    soc_action_body = "\n".join(soc_action_text.splitlines()[2:]).strip()

    report = f"""# {title}

## 1. {metadata_label}
- {generated_by_label}: CyberLex Sweden
- {report_type_label}: {report_type_text}
- {status_label}: {status_text}
- {classification_label}: {classification_text}
- {priority_review_label}: {priority_review_text}
- {generated_time_label}:
- {prepared_by_label}:

## 2. {purpose_label}
{purpose_text}

## 3. {question_label}
{question}

## 4. {handling_label}
{handling_text}

## 5. {soc_triage_label}
{soc_triage_body}

## 6. {answer_label}
{answer_text}

## 7. {soc_actions_label}
{soc_action_body}

## 8. {checklist_label}
{checklist_text}

## 9. {incident_log_label}
{incident_log_text}

## 10. {source_label}
{source_text}

## 11. {limitation_heading}
{limitation}
"""

    return remove_duplicate_lines(report.strip())

def is_basic_explanation_question(question):
    # Detects basic "what is" / definition-style questions.
    # These should normally be informational, not high attention.
    question_lower = normalize_query_text(question).strip()

    explanation_starts = [
        "what is ",
        "what are ",
        "what does ",
        "explain ",
        "vad är ",
        "vad betyder ",
        "förklara ",
    ]

    explanation_topics = [
        "nis2",
        "dora",
        "imy",
        "gdpr",
        "dataintrång",
        "cyber resilience act",
        "cyberresiliensakten",
        "digital operational resilience act",
        "swedish cybersecurity act",
        "cybersäkerhetslagen",
        "attacks against information systems",
        "attacker mot informationssystem",
    ]

    return (
        any(question_lower.startswith(start) for start in explanation_starts)
        and any(topic in question_lower for topic in explanation_topics)
    )


def is_reporting_or_compliance_assessment_question(question):
    # Detects questions that are not necessarily active incidents but still need
    # more careful compliance assessment than a basic definition question.
    question_lower = normalize_query_text(question)

    assessment_terms = [
        "when must",
        "when should",
        "must be reported",
        "should be reported",
        "need to report",
        "needs to report",
        "reported under",
        "reporting obligation",
        "reporting duties",
        "72 hours",
        "72-hour",
        "72 timmar",
        "när måste",
        "när ska",
        "måste rapporteras",
        "måste anmälas",
        "ska rapporteras",
        "ska anmälas",
        "behöver rapporteras",
        "behöver anmälas",
        "rapporteras enligt",
        "anmälas till",
        "både nis2 och gdpr",
        "both nis2 and gdpr",
    ]

    compliance_topics = [
        "personal data breach",
        "personuppgiftsincident",
        "data breach",
        "gdpr",
        "imy",
        "nis2",
        "cybersecurity act",
        "cybersäkerhetslagen",
        "dora",
        "incident reporting",
        "incidentrapportering",
    ]

    return (
        any(term in question_lower for term in assessment_terms)
        and any(topic in question_lower for topic in compliance_topics)
    )


def is_unsafe_cyber_request(question):
    # Detects requests that should be treated as unsafe/offensive or evasive.
    question_lower = normalize_query_text(question)

    unsafe_terms = [
        "hide logs",
        "delete logs",
        "erase logs",
        "remove logs",
        "cover tracks",
        "hide traces",
        "avoid detection",
        "bypass detection",
        "bypass mfa",
        "bypass multi-factor",
        "steal credentials",
        "steal passwords",
        "hack into",
        "exploit a system",
        "after hacking",
        "radera loggar",
        "ta bort loggar",
        "dölja loggar",
        "dölja spår",
        "undvika upptäckt",
        "kringgå upptäckt",
        "kringgå mfa",
        "kringgår jag mfa",
        "kringgå multifaktor",
        "stjäla lösenord",
        "hacka sig in",
        "efter ett intrång",
    ]

    return any(term in question_lower for term in unsafe_terms)


def generate_unsafe_refusal_answer(question, language="English"):
    # Generates a clean refusal for unsafe or evasive cyber requests.
    # In refusal mode, CyberLex should not show normal source panels, checklists,
    # incident templates, or source context, because that can make the app look
    # like it is still assisting the unsafe request.
    use_swedish = language == "Svenska"

    if use_swedish:
        title = "CyberLex kan inte hjälpa med detta"
        refusal = (
            "CyberLex Sweden kan inte hjälpa till med att radera loggar, dölja spår, kringgå upptäckt, "
            "stjäla inloggningsuppgifter, utnyttja system eller utföra obehörig åtkomst."
        )
        safe_alternative_title = "Säker och laglig inriktning"
        safe_alternative = (
            "För defensiv incidenthantering: bevara loggar och bevis, dokumentera vad som har hänt, "
            "isolera drabbade system om det behövs, följ interna rutiner och eskalera till IT-säkerhet, "
            "juridiskt stöd eller incidentresponsansvariga."
        )
        limitation = (
            "Detta är en säkerhetsgräns i CyberLex Sweden. Appen kan hjälpa med laglig, defensiv "
            "incidenthantering och dokumentation, men inte med instruktioner som underlättar intrång eller undvikande."
        )
    else:
        title = "CyberLex cannot help with this"
        refusal = (
            "CyberLex Sweden cannot help with deleting logs, hiding traces, bypassing detection, "
            "stealing credentials, exploiting systems, or performing unauthorized access."
        )
        safe_alternative_title = "Safe and lawful direction"
        safe_alternative = (
            "For defensive incident handling: preserve logs and evidence, document what happened, "
            "isolate affected systems if needed, follow internal procedures, and escalate to IT security, "
            "legal support, or incident-response owners."
        )
        limitation = (
            "This is a CyberLex Sweden safety boundary. The app can help with lawful defensive "
            "incident handling and documentation, but not with instructions that enable intrusion or evasion."
        )

    return (
        f'<div class="practical-card">'
        f'<div class="practical-card-title">{title}</div>'
        f'<div class="practical-card-text">{refusal}</div>'
        f'<br>'
        f'<div class="practical-card-title">{safe_alternative_title}</div>'
        f'<div class="practical-card-text">{safe_alternative}</div>'
        f'<div class="attention-limitation">{limitation}</div>'
        f'</div>'
    )


def generate_attention_level(question, search_results, language="English"):
    # Generates a simple CyberLex attention level.
    # This is not a legal risk rating. It is an educational signal based on topic and matched sources.

    question_lower = normalize_query_text(question)
    use_swedish = language == "Svenska"

    if is_unsafe_cyber_request(question):
        level = "High"
        if use_swedish:
            reason = (
                "Frågan verkar beröra offensiv eller undvikande cyberaktivitet. CyberLex ska inte ge sådana instruktioner "
                "utan bör styra mot laglig, defensiv incidenthantering."
            )
        else:
            reason = (
                "The question appears to involve offensive or evasive cyber activity. CyberLex should not provide those instructions "
                "and should redirect toward lawful defensive incident handling."
            )

    elif is_practical_incident_response_question(question):
        level = "High"
        if use_swedish:
            reason = (
                "Frågan verkar vara en praktisk incidenthanteringsfråga där snabba defensiva åtgärder, bevarande av bevis, "
                "dokumentation och rapporteringsbedömning kan vara viktiga."
            )
        else:
            reason = (
                "The question appears to be a practical incident-response question where defensive action, evidence preservation, "
                "documentation, and reporting assessment may be important."
            )

    elif is_reporting_or_compliance_assessment_question(question):
        level = "Elevated"
        if use_swedish:
            reason = (
                "Frågan verkar kräva bedömning av rapportering, tidsfrister, personuppgifter eller regelverk. "
                "Det är inte nödvändigtvis en akut incidentfråga, men svaret bör läsas noggrant tillsammans med källorna."
            )
        else:
            reason = (
                "The question appears to require assessment of reporting, timelines, personal data, or regulatory duties. "
                "It is not necessarily an active incident, but the answer should be reviewed carefully with the sources."
            )

    elif is_basic_explanation_question(question):
        level = "Informational"
        if use_swedish:
            reason = (
                "Frågan verkar vara en grundläggande förklaringsfråga inom CyberLex Swedens kunskapsområde."
            )
        else:
            reason = (
                "The question appears to be a basic explanation question within the CyberLex Sweden knowledge area."
            )

    else:
        standard_terms = [
            "gdpr",
            "imy",
            "dataintrång",
            "unauthorized access",
            "obehörig åtkomst",
            "cyber resilience act",
            "cyberresiliensakten",
            "products with digital elements",
            "nis2",
            "dora",
            "cybersecurity act",
            "cybersäkerhetslagen",
        ]

        if any(term in question_lower for term in standard_terms):
            level = "Standard"
            if use_swedish:
                reason = (
                    "Frågan verkar vara relevant för dataskydd, cybersäkerhetsrätt eller digital compliance, "
                    "men den verkar inte vara en praktisk incidentfråga."
                )
            else:
                reason = (
                    "The question appears relevant to data protection, cybersecurity law, or digital compliance, "
                    "but does not appear to be a practical incident-response question."
                )
        else:
            level = "Informational"
            if use_swedish:
                reason = (
                    "Frågan verkar vara en allmän informationsfråga inom CyberLex Swedens kunskapsområde."
                )
            else:
                reason = (
                    "The question appears to be a general information question within the CyberLex Sweden knowledge area."
                )

    css_level = level.lower()

    if use_swedish:
        heading = "CyberLex uppmärksamhetsnivå"
        reason_label = "Motivering"

        translated_levels = {
            "Informational": "Information",
            "Standard": "Standard",
            "Elevated": "Förhöjd",
            "High": "Hög",
        }
        translated_level = translated_levels.get(level, level)

        limitation = (
            "Detta är inte en juridisk riskklassning. Det är en pedagogisk signal baserad på frågans ämne "
            "och matchade källsektioner."
        )

        return (
            f'<div class="attention-card attention-level-{css_level}">'
            f'<div class="attention-label">{heading}: {translated_level}</div>'
            f'<div class="attention-reason"><strong>{reason_label}:</strong> {reason}</div>'
            f'<div class="attention-limitation">{limitation}</div>'
            f'</div>'
        )

    heading = "CyberLex attention level"
    limitation = (
        "This is not a legal risk rating. It is an educational signal based on the question topic "
        "and matched source sections."
    )

    return (
        f'<div class="attention-card attention-level-{css_level}">'
        f'<div class="attention-label">{heading}: {level}</div>'
        f'<div class="attention-reason"><strong>Reason:</strong> {reason}</div>'
        f'<div class="attention-limitation">{limitation}</div>'
        f'</div>'
    )

def detect_question_topic(question, language="English"):
    # Detects a simple human-readable topic label from the user's question.
    # This helps users understand how CyberLex interpreted the question.
    # It does not replace source matching or legal analysis.

    question_lower = normalize_query_text(question)
    use_swedish = language == "Svenska"

    if is_nis2_sector_scope_question(question):
        return "NIS2 och cybersäkerhetslagens omfattning" if use_swedish else "NIS2 scope and applicability"

    if is_suspicious_link_question(question):
        return "Klick på misstänkt länk" if use_swedish else "Suspicious link click"

    if is_practical_incident_response_question(question):
        return "Incidenthantering och första åtgärder" if use_swedish else "Incident response and first steps"

    if is_gdpr_security_guidance_question(question_lower):
        return "GDPR, IMY och säkerhetsbedömning" if use_swedish else "GDPR, IMY and security assessment"

    if (
        "data breach" in question_lower
        or "personal data breach" in question_lower
        or "personuppgiftsincident" in question_lower
        or "72" in question_lower
    ):
        return "GDPR-personuppgiftsincident" if use_swedish else "GDPR data breach"

    if (
        "ransomware" in question_lower
        or "malware" in question_lower
        or "cyberattack" in question_lower
        or "cyber attack" in question_lower
    ):
        return "Ransomware- eller skadlig kod-incident" if use_swedish else "Ransomware or malware incident"

    if (
        "cyber incident" in question_lower
        or "cyberincident" in question_lower
        or "security incident" in question_lower
        or "incident response" in question_lower
    ):
        return "Bedömning av cyberincident" if use_swedish else "Cyber incident assessment"

    if (
        "nis2" in question_lower
        or "cybersecurity act" in question_lower
        or "cybersäkerhetslagen" in question_lower
    ):
        return "NIS2 och cybersäkerhetskrav" if use_swedish else "NIS2 and cybersecurity duties"

    if (
        "dora" in question_lower
        or "digital operational resilience" in question_lower
        or "ict risk" in question_lower
        or "third-party ict" in question_lower
    ):
        return "DORA och ICT-risk" if use_swedish else "DORA and ICT risk"

    if (
        "unauthorized access" in question_lower
        or "dataintrång" in question_lower
        or "obehörig åtkomst" in question_lower
        or "data intrusion" in question_lower
    ):
        return "Obehörig åtkomst / dataintrång" if use_swedish else "Unauthorized access / dataintrång"

    if (
        "cyber resilience act" in question_lower
        or "products with digital elements" in question_lower
        or "product security" in question_lower
    ):
        return "Cyber Resilience Act och produktsäkerhet" if use_swedish else "Cyber Resilience Act and product security"

    if (
        "gdpr" in question_lower
        or "imy" in question_lower
        or "data protection" in question_lower
        or "privacy" in question_lower
        or "dataskydd" in question_lower
        or "personuppgift" in question_lower
    ):
        return "GDPR och dataskydd" if use_swedish else "GDPR and data protection"

    if (
        "attacks against information systems" in question_lower
        or "eu cybercrime" in question_lower
        or "information systems" in question_lower
    ):
        return "EU-cyberbrott och informationssystem" if use_swedish else "EU cybercrime and information systems"

    return "Allmän cyberrättslig fråga" if use_swedish else "General cybersecurity law question"

def detect_source_quality(filename, language="English"):
    # Detects a simple user-facing source quality label from the matched knowledge file.
    # This does not prove legal authority. It explains what type of source the local file is based on.

    filename_lower = filename.lower()
    use_swedish = language == "Svenska"

    if "cyber_incident_response_playbook" in filename_lower:
        return (
            "Incidenthanteringsstöd baserat på betrodda källor"
            if use_swedish
            else "Incident response guidance based on trusted sources"
        )

    if "cybercrime_dataintrang" in filename_lower:
        return (
            "Svensk rättskälla / straffrättsligt ämne"
            if use_swedish
            else "Swedish legal source / criminal-law topic"
        )

    if "imy_gdpr_security_measures" in filename_lower:
        return (
            "IMY-vägledning om GDPR-säkerhetsåtgärder"
            if use_swedish
            else "IMY guidance on GDPR security measures"
        )

    if "gdpr_imy_edpb_security_guidance" in filename_lower:
        return (
            "IMY- och EDPB-vägledning om GDPR-säkerhet"
            if use_swedish
            else "IMY and EDPB guidance on GDPR security"
        )

    if "gdpr_personal_data_breach" in filename_lower:
        return (
            "IMY-vägledning och EU-dataskyddskälla"
            if use_swedish
            else "IMY guidance and EU data protection source"
        )

    if "gdpr_core_principles" in filename_lower:
        return (
            "EU-dataskyddsförordning"
            if use_swedish
            else "EU data protection regulation source"
        )

    if "imy_gdpr_supervision" in filename_lower:
        return (
            "Svensk tillsynsmyndighetskälla"
            if use_swedish
            else "Swedish supervisory authority source"
        )

    if "nis2_incident_reporting" in filename_lower:
        return (
            "Svensk myndighetsvägledning och EU-cybersäkerhetskälla"
            if use_swedish
            else "Swedish authority guidance and EU cybersecurity source"
        )

    if "nis2_cybersecurity_law" in filename_lower:
        return (
            "Svensk myndighetsvägledning och EU-cybersäkerhetskälla"
            if use_swedish
            else "Swedish authority guidance and EU cybersecurity source"
        )

    if "eu_dora" in filename_lower:
        return (
            "EU-förordning för digital operativ motståndskraft"
            if use_swedish
            else "EU digital operational resilience regulation source"
        )

    if "eu_cyber_resilience_act" in filename_lower:
        return (
            "EU-förordning om cybersäkerhet för digitala produkter"
            if use_swedish
            else "EU regulation source for digital product cybersecurity"
        )

    if "eu_attacks_against_information_systems" in filename_lower:
        return (
            "EU-direktiv om angrepp mot informationssystem"
            if use_swedish
            else "EU directive source on attacks against information systems"
        )

    return (
        "Lokal utbildningssammanfattning baserad på betrodda källor"
        if use_swedish
        else "Local educational summary based on trusted sources"
    )

def detect_source_freshness(source_date, language="English"):
    # Creates a readable freshness label from the stored source date text.
    # This does not check the internet. It only describes whether the local file has a visible review date.

    use_swedish = language == "Svenska"
    source_date_lower = source_date.lower()

    has_date = any(char.isdigit() for char in source_date_lower)

    if not has_date or "no source date" in source_date_lower:
        return (
            "Inget granskningsdatum sparat"
            if use_swedish
            else "No review date stored"
        )

    if "2026" in source_date_lower:
        return (
            "Nyligen kontrollerad"
            if use_swedish
            else "Recently checked"
        )

    return (
        "Granskning rekommenderas"
        if use_swedish
        else "Review recommended"
    )


def localize_metadata_value(value, language="English"):
    # Localizes metadata for the user interface.
    # In Swedish mode, avoid showing long mixed-language developer changelogs.
    # Metadata should reassure the user that the local source was reviewed,
    # not expose every internal note from the Markdown file.

    text = str(value or "").strip()

    if not text:
        return text

    if language != "Svenska":
        return text

    lower_text = text.lower()

    if "last checked:" in lower_text:
        return text.replace("Last checked:", "Senast kontrollerad:").strip()

    if "no source date" in lower_text:
        return "Inget källdatum är sparat för detta dokument ännu."

    if "no version notes" in lower_text:
        return "Inga versionsanteckningar är sparade för detta dokument ännu."

    # For version notes, use a clean Swedish summary instead of trying to
    # translate every stored developer note phrase-by-phrase. The detailed
    # source file still exists in the repository for developer review.
    return "Källan är lokalt granskad och uppdaterad för CyberLex Sweden."

def generate_source_confidence(score, language="English"):
    # Converts the numeric relevance score into a readable confidence note.
    # This is not legal certainty. It only describes how strong the local source match is.

    use_swedish = language == "Svenska"

    if score >= 220:
        level = "Very strong"
        reason = (
            "The question strongly matches the selected source file and section. "
            "The answer is likely based on the most relevant local knowledge source."
        )
    elif score >= 160:
        level = "Strong"
        reason = (
            "The question has a clear match in the local knowledge base. "
            "The selected source section appears highly relevant, but the user should still review the source context."
        )
    elif score >= 90:
        level = "Moderate"
        reason = (
            "The question has a relevant match, but the result may depend on keyword overlap or source routing. "
            "The user should review the supporting source context before relying on the answer."
        )
    else:
        level = "Limited"
        reason = (
            "The match is weak or narrow. "
            "The answer should be treated cautiously and checked against the displayed source context."
        )

    if use_swedish:
        if level == "Very strong":
            return {
                "level": "Mycket stark",
                "reason": (
                    "Frågan matchar tydligt den valda källfilen och källsektionen. "
                    "Svaret bygger sannolikt på den mest relevanta lokala kunskapskällan."
                )
            }

        if level == "Strong":
            return {
                "level": "Stark",
                "reason": (
                    "Frågan har en tydlig matchning i den lokala kunskapsbasen. "
                    "Den valda källsektionen verkar mycket relevant, men användaren bör ändå granska källkontexten."
                )
            }

        if level == "Moderate":
            return {
                "level": "Måttlig",
                "reason": (
                    "Frågan har en relevant matchning, men resultatet kan bero på nyckelordsöverlappning eller källroutning. "
                    "Användaren bör granska den stödjande källkontexten innan svaret används."
                )
            }

        return {
            "level": "Begränsad",
            "reason": (
                "Matchningen är svag eller smal. "
                "Svaret bör behandlas försiktigt och jämföras med den visade källkontexten."
            )
        }

    return {
        "level": level,
        "reason": reason
    }



def is_confirmed_or_strong_incident_statement(question):
    # Distinguishes statements like "we have been hacked" from softer reports
    # like "we think" or "we suspect" so CyberLex can give firmer blue-team
    # containment guidance when the user states that the incident happened.
    q = normalize_query_text(question)
    strong_markers = [
        "vi har blivit hackade",
        "vi har blivit hackad",
        "vi har blivit utsatta",
        "någon hackade",
        "någon har hackat",
        "någon har tagit sig in",
        "någon verkar ha tagit sig in",
        "hackat vårt system",
        "hackat vårat system",
        "tagit sig in i vårt system",
        "tagit sig in i vårat system",
        "someone hacked",
        "someone hacked our system",
        "we have been hacked",
        "we were hacked",
        "our system was hacked",
        "someone breached",
        "breached our system",
    ]
    return contains_any(q, strong_markers)


def is_explicit_suspicious_login_statement(question):
    # If the user already says the login is suspicious, the answer should not
    # lead with "if approved". It should treat the event as suspicious until verified.
    q = normalize_query_text(question)
    explicit_markers = [
        "misstänkt login",
        "misstänkt inloggning",
        "misstänkt loggning",
        "ovanlig inloggning",
        "okänd inloggning",
        "suspicious login",
        "unusual login",
        "unknown login",
    ]
    return contains_any(q, explicit_markers)

def generate_incident_response_answer(question, language="English"):
    # Generates a longer defensive first-response answer for suspected hacking,
    # data leaks, ransomware, malware, and compromised accounts.
    # This is rule-based and source-grounded through cyber_incident_response_playbook.md.

    use_swedish = language == "Svenska"

    if use_swedish:
        if is_data_leak_response_question(question):
            title = "Rekommenderade första steg vid misstänkt dataläcka"
            intro = (
                "Om du misstänker en dataläcka bör du först stoppa fortsatt exponering, "
                "bevara bevis och bedöma om personuppgifter kan ha påverkats. "
                "Agera strukturerat och dokumentera allt, eftersom frågan kan bli relevant "
                "för både GDPR/IMY och eventuell cybersäkerhetsincidentrapportering."
            )
            steps = [
                "Bekräfta vad som är känt och vad som fortfarande är oklart.",
                "Stoppa fortsatt exponering, till exempel genom att ta bort publik åtkomst, stänga delningslänkar eller rätta behörigheter.",
                "Bevara bevis innan du ändrar för mycket: skärmbilder, länkar, loggar, tidsstämplar och behörighetsinställningar.",
                "Identifiera vilken data som kan ha exponerats och hur länge exponeringen kan ha pågått.",
                "Bedöm om datan innehåller personuppgifter, känsliga uppgifter, lösenord, tokens, kunddata eller HR-data.",
                "Bedöm om obehöriga faktiskt har haft åtkomst eller om åtkomst bara var möjlig.",
                "Säkra berörda konton, API-nycklar, lösenord och system från en ren administrativ miljö.",
                "Bedöm risken för registrerade personers rättigheter och friheter.",
                "Bedöm om anmälan till IMY enligt GDPR krävs, normalt inom 72 timmar efter att organisationen blev medveten om incidenten om anmälan krävs.",
                "Bedöm om berörda personer behöver informeras om risken är hög.",
                "Bedöm om NIS2/cybersäkerhetslagen eller annan incidentrapportering också kan vara relevant.",
                "Dokumentera beslut, tidslinje, åtgärder, källor och vem som godkände besluten.",
            ]
        elif is_suspicious_login_question(question):
            title = "Rekommenderade första steg vid misstänkt inloggning"
            if is_explicit_suspicious_login_statement(question):
                intro = (
                    "Eftersom inloggningen beskrivs som misstänkt bör den behandlas som en möjlig identitetsincident tills den är verifierad. "
                    "Om loggar och användare senare visar att inloggningen var godkänd, förväntad och kopplad till en känd plats eller tjänst kan ärendet normalt stängas som legitim aktivitet."
                )
            else:
                intro = (
                    "En inloggning är inte automatiskt en incident. Om den var godkänd, förväntad eller kopplad till en känd plats eller tjänst är den normalt ofarlig. "
                    "Om den däremot är obehörig, okänd eller inte kan förklaras bör den behandlas som en misstänkt identitetsincident tills loggarna och användaren visar motsatsen."
                )
            steps = [
                "Spara larmet eller loggposten med tidpunkt, användarkonto, IP-adress, plats, enhet och tjänst.",
                "Kontrollera om inloggningen var godkänd av användaren, förväntad enligt schema eller kopplad till en känd tjänst eller plats.",
                "Kontrollera om inloggningen lyckades eller bara var ett misslyckat försök.",
                "Kontrollera om samma konto har fler ovanliga inloggningar, MFA-pushar eller misslyckade försök.",
                "Kontakta användaren och bekräfta om aktiviteten var legitim utan att skicka känsliga uppgifter i klartext.",
                "Om aktiviteten inte kan förklaras: blockera kontot tillfälligt eller kräv ny autentisering.",
                "Återkalla aktiva sessioner och tokens i identitetsplattformen, VPN, e-post och molntjänster.",
                "Byt lösenord från en ren enhet och kontrollera MFA-metoder för okända eller angriparstyrda metoder.",
                "Granska e-postregler, vidarebefordran, OAuth-appar och delegerad åtkomst.",
                "Kontrollera om kontot har använts för att komma åt filer, system, kunddata eller administratörsfunktioner.",
                "Bedöm om personuppgifter kan ha påverkats och om GDPR/IMY-bedömning krävs.",
                "Bedöm om händelsen kan vara relevant för NIS2/cybersäkerhetslagen vid större påverkan.",
                "Dokumentera tidslinje, loggar, beslut och åtgärder.",
            ]
        elif is_suspicious_link_question(question):
            title = "Rekommenderade första steg efter klick på misstänkt länk"
            intro = (
                "En misstänkt länk kan komma från mejl, SMS, chatt, sociala medier, en webbsida, QR-kod eller ett dokument. "
                "Utred först om användaren bara klickade, om inloggningsuppgifter eller MFA-kod skrevs in, om något laddades ned, "
                "och om ett konto eller en enhet kan ha påverkats."
            )
            steps = [
                "Be användaren att inte klicka vidare, inte skriva in fler uppgifter och inte ladda ned något mer.",
                "Spara länken, sidan eller meddelandet som bevis: URL, tidpunkt, användare, enhet, webbläsare och var länken fanns.",
                "Ta reda på om länken kom från mejl, SMS, chatt, sociala medier, webbsida, QR-kod eller dokument.",
                "Kontrollera om användaren skrev in lösenord, MFA-kod, personuppgifter, betalningsuppgifter eller annan känslig information.",
                "Om inloggningsuppgifter angavs: byt lösenord från en ren enhet, återkalla sessioner och kontrollera MFA-metoder.",
                "Kontrollera kontot för ovanliga inloggningar, OAuth-appar, vidarebefordringsregler och ändrade säkerhetsinställningar.",
                "Kontrollera enheten för nedladdningar, nya filer, webbläsarvarningar eller tecken på skadlig kod.",
                "Blockera URL/domän i e-postskydd, DNS/webbfilter, proxy eller brandvägg där det är relevant.",
                "Sök efter om samma länk har skickats till fler användare och varna dem vid behov.",
                "Bedöm om personuppgifter, kunddata eller systemåtkomst kan ha påverkats.",
                "Dokumentera tidslinje, källa, användare, åtgärder och beslut samt om IMY/GDPR eller NIS2/cybersäkerhetslagen kan bli relevant.",
            ]
        elif is_suspicious_email_question(question):
            title = "Rekommenderade första steg vid misstänkt mejl eller phishing"
            intro = (
                "Ett misstänkt mejl bör hanteras så att fler användare skyddas och eventuell klickning eller kontopåverkan kan utredas."
            )
            steps = [
                "Be användaren att inte klicka fler länkar, öppna bilagor eller svara på mejlet.",
                "Spara mejlet som bevis, inklusive avsändare, ämne, tidpunkt, länkar, bilagor och fullständiga headers om möjligt.",
                "Rapportera mejlet till IT/säkerhet enligt organisationens rutin.",
                "Sök efter samma mejl hos andra användare och ta bort eller karantänsätt det via e-postskyddet om möjligt.",
                "Kontrollera om någon klickade på länken, öppnade bilagan eller lämnade inloggningsuppgifter.",
                "Om någon klickade eller skrev in uppgifter: behandla kontot som misstänkt komprometterat.",
                "Återkalla sessioner, byt lösenord från ren enhet och kontrollera MFA om kontouppgifter kan ha läckt.",
                "Kontrollera e-postregler, vidarebefordran, OAuth-appar och misstänkta skickade meddelanden.",
                "Kontrollera om mejlet innehöll skadlig kod och om någon klient behöver isoleras.",
                "Bedöm om personuppgifter eller känslig information kan ha påverkats.",
                "Dokumentera tidslinje, användare, åtgärder, bevis och beslut.",
            ]
        elif is_compromised_account_question(question):
            title = "Rekommenderade första steg vid komprometterat konto"
            intro = (
                "Om ett konto kan vara komprometterat bör du snabbt stoppa fortsatt åtkomst, "
                "säkra identiteten och kontrollera om kontot har använts för att komma åt data eller andra system."
            )
            steps = [
                "Blockera eller inaktivera kontot tillfälligt om kompromettering är sannolik.",
                "Återkalla aktiva sessioner och tokens i identitetsplattformen, VPN, e-post och molntjänster.",
                "Byt lösenord från en ren enhet, inte från den misstänkt komprometterade klienten.",
                "Kontrollera MFA-metoder och ta bort okända eller angriparstyrda metoder.",
                "Kontrollera e-postregler, vidarebefordran, OAuth-appar, delegerad åtkomst och misstänkta skickade meddelanden.",
                "Granska inloggningsloggar, IP-adresser, länder, tidpunkter och ovanlig aktivitet.",
                "Kontrollera om kontot hade administratörsrättigheter eller åtkomst till känsliga system.",
                "Identifiera vilken data kontot kan ha läst, ändrat, laddat ner eller raderat.",
                "Bedöm om personuppgifter kan ha påverkats och om GDPR/IMY-bedömning krävs.",
                "Bedöm om incidenten kan vara relevant enligt NIS2/cybersäkerhetslagen.",
                "Dokumentera åtgärder, tidslinje, bevis och beslut.",
            ]
        elif is_ransomware_response_question(question):
            if is_encrypted_files_possible_ransomware_question(question):
                title = "Rekommenderade första steg om filer oväntat har krypterats"
                intro = (
                    "Krypterade filer är inte alltid ett problem, eftersom normal kryptering kan vara en legitim säkerhetsåtgärd. "
                    "Men om filer plötsligt har krypterats, blivit otillgängliga, fått nya filändelser eller om det finns tecken på skadlig kod, "
                    "bör händelsen behandlas som möjlig ransomware tills teknisk kontroll visar något annat."
                )
            else:
                title = "Rekommenderade första steg vid ransomware eller skadlig kod"
                intro = (
                    "Vid ransomware eller skadlig kod är målet att begränsa spridning, bevara bevis, "
                    "förstå omfattningen och återställa kontrollerat. Rensa inte blint innan bevis och tidslinje säkrats."
                )
            steps = [
                "Isolera drabbade klienter eller servrar från nätverket om det kan göras säkert.",
                "Bevara ransom note, säkerhetslarm, loggar, filändelser, tidsstämplar och exempel på krypterade filer.",
                "Identifiera vilka system, delade mappar, servrar, konton och backupmiljöer som påverkas.",
                "Kontrollera om attacken fortfarande sprider sig.",
                "Stäng av eller säkra misstänkt komprometterade konton och återkalla sessioner.",
                "Kontrollera backups, men återställ inte innan du vet att åtkomstvägen är stängd.",
                "Bedöm om data kan ha stulits innan kryptering.",
                "Bedöm om personuppgifter påverkats och om IMY-anmälan kan krävas.",
                "Bedöm om NIS2/cybersäkerhetslagen eller annan incidentrapportering kan vara relevant.",
                "Eskalera till IT, säkerhet, ledning, juridik, dataskydd och extern incidentexpert vid behov.",
                "Kontakta CERT-SE eller relevant incidentstöd vid allvarlig incident.",
                "Återställ först efter kontrollerad analys, stängd intrångsväg och minskad risk för återinfektion.",
            ]
        else:
            title = "Rekommenderade första steg vid misstänkt hackning eller intrång"
            if is_confirmed_or_strong_incident_statement(question):
                intro = (
                    "När frågan beskriver att någon har hackat eller tagit sig in i systemet bör fokus direkt ligga på skadebegränsning, bevisbevarande och att stoppa fortsatt åtkomst. "
                    "Agera som vid en aktiv säkerhetsincident tills teknisk utredning visar något annat."
                )
            else:
                intro = (
                    "Om du misstänker hackning eller intrång bör du behandla händelsen som en möjlig incident. "
                    "Första målet är att begränsa skadan utan att förstöra bevisning."
                )
            steps = [
                "Starta en incidentlogg med tidpunkt, upptäckt, berört system, berört konto och vem som gör vad.",
                "Isolera drabbad klient, server eller konto om det går utan att förstöra bevisning.",
                "Bevara loggar, larm, skärmbilder, tidsstämplar, IP-adresser, kontonamn och användarrapporter.",
                "Radera inte loggar, installera inte om system och gör inte slumpmässig städning innan en första bedömning.",
                "Identifiera vilka system, konton, användare, nätverk och data som kan vara berörda.",
                "Stäng av eller säkra misstänkt komprometterade konton och återkalla aktiva sessioner.",
                "Byt lösenord från en ren enhet och kontrollera MFA, e-postregler och administratörsrättigheter.",
                "Kontrollera om angriparen fortfarande kan ha åtkomst.",
                "Bedöm om personuppgifter kan ha lästs, kopierats, ändrats, raderats eller blivit otillgängliga.",
                "Bedöm om anmälan till IMY enligt GDPR kan krävas.",
                "Bedöm om incidentrapportering enligt NIS2/cybersäkerhetslagen kan vara relevant.",
                "Eskalera till IT, säkerhet, ledning, juridik och dataskyddsansvarig.",
                "Kontakta CERT-SE eller professionellt incidentstöd vid behov.",
                "Dokumentera tidslinje, beslut, åtgärder, källor och kvarstående osäkerheter.",
            ]

        limitation = (
            "Detta är defensiv utbildningsvägledning, inte juridisk rådgivning eller professionell incidenthantering. "
            "Vid allvarliga incidenter bör organisationen använda interna rutiner, officiella källor, juridiskt stöd och incidentexperter."
        )

    else:
        if is_data_leak_response_question(question):
            title = "Recommended first steps for a suspected data leak"
            intro = (
                "If you suspect a data leak, first stop further exposure, preserve evidence, "
                "and assess whether personal data may have been affected. Document everything because the issue may be relevant "
                "under GDPR/IMY rules and possibly cybersecurity incident reporting."
            )
            steps = [
                "Confirm what is known and what remains unclear.",
                "Stop further exposure, for example by removing public access, disabling sharing links, or correcting permissions.",
                "Preserve evidence before changing too much: screenshots, URLs, logs, timestamps, and permission settings.",
                "Identify what data may have been exposed and for how long.",
                "Assess whether the data includes personal data, sensitive data, passwords, tokens, customer data, or HR data.",
                "Assess whether unauthorized access actually happened or was only possible.",
                "Secure affected accounts, API keys, passwords, and systems from a clean administrative environment.",
                "Assess the risk to individuals' rights and freedoms.",
                "Assess whether notification to IMY under GDPR is required, normally within 72 hours after awareness if notification is required.",
                "Assess whether affected individuals must be informed if the risk is high.",
                "Assess whether NIS2/the Swedish Cybersecurity Act or another incident reporting path may also be relevant.",
                "Document decisions, timeline, actions, sources, and who approved the decisions.",
            ]
        elif is_suspicious_login_question(question):
            title = "Recommended first steps for suspicious login activity"
            if is_explicit_suspicious_login_statement(question):
                intro = (
                    "Because the login is described as suspicious, treat it as a possible identity incident until it is verified. "
                    "If logs and the user later confirm it was approved, expected, and tied to a known service or location, it can usually be closed as legitimate activity."
                )
            else:
                intro = (
                    "A login is not automatically bad. If it was approved, expected, or tied to a known service or location, it is usually not an incident. "
                    "If it was unauthorized, unknown, or cannot be explained, treat it as a possible identity incident until logs show otherwise."
                )
            steps = [
                "Preserve the alert or log entry with time, user account, IP address, location, device, and service.",
                "Check whether the login succeeded or was only a failed attempt.",
                "Check whether the same account has more unusual logins, MFA prompts, or failed attempts.",
                "Contact the user and confirm whether the activity was legitimate without sharing sensitive data in plain text.",
                "If the activity cannot be explained, temporarily block the account or require fresh authentication.",
                "Revoke active sessions and tokens in identity, VPN, email, and cloud services.",
                "Reset the password from a clean device and review MFA methods for unknown or attacker-controlled methods.",
                "Review email rules, forwarding, OAuth apps, and delegated access.",
                "Check whether the account was used to access files, systems, customer data, or administrator functions.",
                "Assess whether personal data may have been affected and whether GDPR/IMY assessment is required.",
                "Assess whether the event may be relevant under NIS2/the Swedish Cybersecurity Act if impact is larger.",
                "Document the timeline, logs, decisions, and actions.",
            ]
        elif is_suspicious_link_question(question):
            title = "Recommended first steps after clicking a suspicious link"
            intro = (
                "A suspicious link may come from email, SMS, chat, social media, a website, QR code, or a document. "
                "First determine whether the user only clicked, entered credentials or an MFA code, downloaded something, "
                "or affected an account or device."
            )
            steps = [
                "Tell the user not to continue clicking, entering information, or downloading anything else.",
                "Preserve the link, page, or message as evidence: URL, time, user, device, browser, and where the link appeared.",
                "Identify whether the link came from email, SMS, chat, social media, website, QR code, or document.",
                "Check whether the user entered a password, MFA code, personal data, payment data, or other sensitive information.",
                "If credentials were entered: reset the password from a clean device, revoke sessions, and review MFA methods.",
                "Check the account for unusual sign-ins, OAuth apps, forwarding rules, and changed security settings.",
                "Check the device for downloads, new files, browser warnings, or signs of malware.",
                "Block the URL/domain in email security, DNS/web filtering, proxy, or firewall where relevant.",
                "Search for whether the same link was sent to other users and warn them if needed.",
                "Assess whether personal data, customer data, or system access may have been affected.",
                "Document the timeline, source, user, actions, and decisions, including whether GDPR/IMY or NIS2/the Swedish Cybersecurity Act may be relevant.",
            ]
        elif is_suspicious_email_question(question):
            title = "Recommended first steps for a suspicious email or phishing"
            intro = (
                "A suspicious email should be handled in a way that protects other users and checks whether anyone clicked, "
                "opened an attachment, or entered credentials."
            )
            steps = [
                "Tell the user not to click more links, open attachments, or reply to the message.",
                "Preserve the email as evidence, including sender, subject, time, links, attachments, and full headers when possible.",
                "Report the email to IT/security using the organization’s normal process.",
                "Search for the same message in other mailboxes and quarantine or remove it through email security tools if possible.",
                "Check whether anyone clicked the link, opened the attachment, or entered credentials.",
                "If someone clicked or entered credentials, treat that account as suspected compromised.",
                "Revoke sessions, reset passwords from a clean device, and review MFA if credentials may have leaked.",
                "Check email rules, forwarding, OAuth apps, and suspicious sent messages.",
                "Check whether the email contained malware and whether any endpoint needs isolation.",
                "Assess whether personal data or sensitive information may have been affected.",
                "Document timeline, affected users, evidence, actions, and decisions.",
            ]
        elif is_compromised_account_question(question):
            title = "Recommended first steps for a compromised account"
            intro = (
                "If an account may be compromised, quickly stop continued access, secure identity controls, "
                "and check whether the account was used to access data or other systems."
            )
            steps = [
                "Block or temporarily disable the account if compromise is likely.",
                "Revoke active sessions and tokens in identity, VPN, email, and cloud services.",
                "Reset the password from a clean device, not from the suspected compromised client.",
                "Review MFA methods and remove unknown or attacker-controlled methods.",
                "Check email rules, forwarding, OAuth apps, delegated access, and suspicious sent messages.",
                "Review sign-in logs, IP addresses, countries, timestamps, and unusual activity.",
                "Check whether the account had administrator rights or access to sensitive systems.",
                "Identify what data the account may have viewed, changed, downloaded, or deleted.",
                "Assess whether personal data may have been affected and whether GDPR/IMY assessment is required.",
                "Assess whether the incident may be relevant under NIS2/the Swedish Cybersecurity Act.",
                "Document actions, timeline, evidence, and decisions.",
            ]
        elif is_ransomware_response_question(question):
            if is_encrypted_files_possible_ransomware_question(question):
                title = "Recommended first steps if files were unexpectedly encrypted"
                intro = (
                    "Encrypted files are not automatically a security incident, because normal encryption can be legitimate protection. "
                    "But if files were suddenly encrypted, became inaccessible, changed extensions, or there are signs of malware, "
                    "treat it as possible ransomware until technical review proves otherwise."
                )
            else:
                title = "Recommended first steps for ransomware or malware"
                intro = (
                    "For ransomware or malware, the first goals are to limit spread, preserve evidence, "
                    "understand scope, and recover in a controlled way. Do not blindly clean systems before evidence and timeline are preserved."
                )
            steps = [
                "Isolate affected clients or servers from the network if it can be done safely.",
                "Preserve the ransom note, security alerts, logs, file extensions, timestamps, and samples of encrypted files.",
                "Identify affected systems, shared folders, servers, accounts, and backup environments.",
                "Check whether the attack is still spreading.",
                "Disable or secure suspected compromised accounts and revoke sessions.",
                "Check backups, but do not restore until the access path is understood and closed.",
                "Assess whether data may have been stolen before encryption.",
                "Assess whether personal data was affected and whether IMY notification may be required.",
                "Assess whether NIS2/the Swedish Cybersecurity Act or another incident reporting path may be relevant.",
                "Escalate to IT, security, management, legal, data protection, and external incident response support when needed.",
                "Contact CERT-SE or relevant incident support for serious incidents when appropriate.",
                "Recover only after controlled analysis, closed access path, and reduced risk of reinfection.",
            ]
        else:
            title = "Recommended first steps for suspected hacking or intrusion"
            if is_confirmed_or_strong_incident_statement(question):
                intro = (
                    "Because the question states that the system was hacked or breached, focus immediately on containment, evidence preservation, and stopping continued access. "
                    "Treat it as an active security incident until technical review proves otherwise."
                )
            else:
                intro = (
                    "If you suspect hacking or intrusion, treat it as a possible incident. "
                    "The first goal is to limit harm without destroying evidence."
                )
            steps = [
                "Start an incident log with time, discovery, affected system, affected account, and who is doing what.",
                "Isolate the affected client, server, or account if possible without destroying evidence.",
                "Preserve logs, alerts, screenshots, timestamps, IP addresses, account names, and user reports.",
                "Do not delete logs, reinstall systems, or do random cleanup before an initial assessment.",
                "Identify which systems, accounts, users, networks, and data may be affected.",
                "Disable or secure suspected compromised accounts and revoke active sessions.",
                "Reset passwords from a clean device and check MFA, email rules, and administrator rights.",
                "Check whether the attacker may still have access.",
                "Assess whether personal data may have been viewed, copied, changed, deleted, or made unavailable.",
                "Assess whether GDPR notification to IMY may be required.",
                "Assess whether incident reporting under NIS2/the Swedish Cybersecurity Act may be relevant.",
                "Escalate to IT, security, management, legal, and data protection roles.",
                "Contact CERT-SE or professional incident response support when appropriate.",
                "Document the timeline, decisions, actions, sources, and remaining uncertainty.",
            ]

        limitation = (
            "This is defensive educational guidance, not legal advice or professional incident response. "
            "For serious incidents, use internal procedures, official sources, legal support, and incident response specialists."
        )

    step_items = "".join([f"<li>{step}</li>" for step in steps])

    return (
        f'<div class="practical-card">'
        f'<div class="practical-card-title">{title}</div>'
        f'<div class="practical-card-text">{intro}</div>'
        f'<ol>{step_items}</ol>'
        f'<div class="attention-limitation">{limitation}</div>'
        f'</div>'
    )



def generate_enhanced_basic_summary(question, language="English"):
    # Builds a richer main answer for simple definition or authority questions.
    # Source context stays available as evidence, but the user should not need
    # to open collapsible panels just to understand the basic concept.
    question_lower = normalize_query_text(question).strip()
    use_swedish = language == "Svenska"

    # Only enrich simple explanation questions. Reporting, incident-response,
    # overlap, and compliance-assessment questions are handled elsewhere.
    simple_starts = [
        "what is ",
        "what are ",
        "what does ",
        "explain ",
        "vad är ",
        "vad betyder ",
        "förklara ",
    ]

    is_simple_question = any(question_lower.startswith(start) for start in simple_starts)

    if not is_simple_question:
        return ""

    if "dora" in question_lower or "digital operational resilience" in question_lower or "digital operativ motståndskraft" in question_lower:
        if use_swedish:
            return (
                "DORA, Digital Operational Resilience Act, är en EU-förordning för den finansiella sektorn. "
                "Den handlar om digital operativ motståndskraft, alltså förmågan att förebygga, hantera, återhämta sig från och lära av ICT-störningar och cyberincidenter.\n\n"
                "Reglerna är viktiga eftersom de samlar krav på ICT-riskhantering, incidentrapportering, testning av digital motståndskraft, tredjepartsrisker och informationsdelning. "
                "Det betyder att finansiella aktörer inte bara ska ha säker teknik, utan även styrning, processer och dokumentation som fungerar vid störningar.\n\n"
                "För CyberLex Sweden är DORA relevant när cybersäkerhetsfrågor rör banker, försäkringsbolag, betalningstjänster, investeringsföretag eller deras ICT-leverantörer. "
                "Om personuppgifter påverkas kan även GDPR behöva bedömas separat."
            )
        return (
            "DORA, the Digital Operational Resilience Act, is an EU regulation for the financial sector. "
            "It focuses on digital operational resilience, meaning the ability to prevent, handle, recover from, and learn from ICT disruptions and cyber incidents.\n\n"
            "It matters because it brings together requirements for ICT risk management, ICT incident reporting, resilience testing, third-party ICT risk, and information sharing. "
            "Financial entities therefore need not only secure technology, but also governance, processes, documentation, and recovery capability.\n\n"
            "For CyberLex Sweden, DORA is relevant when cybersecurity questions affect banks, insurance companies, payment services, investment firms, or their ICT providers. "
            "If personal data is also affected, GDPR may also need to be assessed separately."
        )

    if "nis2" in question_lower or "cybersecurity act" in question_lower or "cybersäkerhetslagen" in question_lower:
        if use_swedish:
            return (
                "NIS2 är ett EU-direktiv om cybersäkerhet. Syftet är att skapa en hög gemensam cybersäkerhetsnivå inom EU, särskilt för organisationer och sektorer som är viktiga för samhället och ekonomin.\n\n"
                "I Sverige kopplas NIS2 till cybersäkerhetslagen och nationella regler. Reglerna handlar bland annat om riskhantering, säkerhetsåtgärder, ledningsansvar, leverantörsrisker, kontinuitet, dokumentation och incidentrapportering.\n\n"
                "För CyberLex Sweden är NIS2 relevant när en fråga gäller om en organisation kan omfattas av cybersäkerhetskrav, hur incidenter kan behöva hanteras, eller hur svenska cybersäkerhetsregler överlappar med exempelvis GDPR vid personuppgifter."
            )
        return (
            "NIS2 is an EU cybersecurity directive. Its purpose is to raise the common level of cybersecurity across the European Union, especially for organizations and sectors that are important for society and the economy.\n\n"
            "In Sweden, NIS2 is connected to the Swedish Cybersecurity Act and national rules. The duties can involve cybersecurity risk management, security measures, management responsibility, supplier risk, continuity, documentation, and incident reporting.\n\n"
            "For CyberLex Sweden, NIS2 is relevant when a question concerns whether an organization may be covered by cybersecurity duties, how incidents may need to be handled, or how Swedish cybersecurity rules can overlap with GDPR when personal data is affected."
        )

    if "imy" in question_lower or "integritetsskyddsmyndigheten" in question_lower:
        if use_swedish:
            return (
                "IMY, Integritetsskyddsmyndigheten, är Sveriges myndighet för integritetsskydd och dataskydd. "
                "Myndigheten har tillsyn över GDPR i Sverige och är därför central när organisationer hanterar personuppgifter.\n\n"
                "IMY är relevant vid frågor om dataskydd, personuppgiftsbehandling, registrerades rättigheter, klagomål, vägledning och personuppgiftsincidenter. "
                "Vid en cyberincident blir IMY särskilt viktig om personuppgifter kan ha röjts, ändrats, förstörts, gått förlorade eller blivit otillgängliga.\n\n"
                "För CyberLex Sweden används IMY som huvudkälla när frågan gäller svensk GDPR-tillsyn, dataskyddsansvar eller om en personuppgiftsincident kan behöva anmälas."
            )
        return (
            "IMY, Integritetsskyddsmyndigheten, is the Swedish Authority for Privacy Protection. "
            "It supervises GDPR and personal data protection in Sweden, which makes it central when organizations handle personal data.\n\n"
            "IMY is relevant for questions about data protection, personal-data processing, individual rights, complaints, guidance, and personal data breaches. "
            "During a cyber incident, IMY becomes especially important if personal data may have been disclosed, altered, destroyed, lost, or made unavailable.\n\n"
            "For CyberLex Sweden, IMY is treated as the main Swedish authority source for GDPR supervision, Swedish data protection duties, and personal-data breach notification questions."
        )

    if "gdpr" in question_lower:
        if use_swedish:
            return (
                "GDPR är EU:s dataskyddsförordning. Den reglerar hur personuppgifter får samlas in, användas, lagras, skyddas och dokumenteras av organisationer, företag och myndigheter.\n\n"
                "Reglerna är viktiga eftersom de ställer krav på laglig grund, transparens, ändamålsbegränsning, uppgiftsminimering, säkerhet, registrerades rättigheter och ansvarsskyldighet. "
                "Organisationer måste därför kunna visa att personuppgifter hanteras korrekt och skyddas på ett rimligt sätt.\n\n"
                "För CyberLex Sweden är GDPR särskilt relevant vid cyberincidenter, eftersom incidenter kan leda till att personuppgifter röjs, ändras, förstörs eller blir otillgängliga. "
                "I Sverige är IMY tillsynsmyndighet för GDPR och dataskydd."
            )
        return (
            "GDPR is the EU General Data Protection Regulation. It governs how personal data may be collected, used, stored, protected, and documented by organizations, companies, and public authorities.\n\n"
            "It matters because it sets requirements for lawful processing, transparency, purpose limitation, data minimisation, security, individual rights, and accountability. "
            "Organizations therefore need to show that personal data is handled properly and protected with suitable measures.\n\n"
            "For CyberLex Sweden, GDPR is especially relevant in cyber incidents because personal data may be disclosed, altered, destroyed, lost, or made unavailable. "
            "In Sweden, IMY supervises GDPR and personal data protection."
        )

    if "dataintrång" in question_lower or "data intrusion" in question_lower or "unauthorized access" in question_lower or "obehörig åtkomst" in question_lower:
        if use_swedish:
            return (
                "Dataintrång är ett svenskt straffrättsligt begrepp som rör obehörig åtkomst till, eller obehörig påverkan på, data eller informationssystem. "
                "Det kan till exempel handla om att ta sig in i ett system utan tillstånd, använda inloggningsuppgifter utan behörighet eller påverka data på ett otillåtet sätt.\n\n"
                "Det viktiga är skillnaden mellan tillåtet säkerhetsarbete och obehöriga handlingar. Penetrationstestning och felsökning behöver därför ha tydligt uppdrag, tydlig omfattning och tydligt tillstånd.\n\n"
                "För CyberLex Sweden är dataintrång relevant eftersom många cyberincidenter börjar med frågor om åtkomst, behörighet, kontoövertagande, loggar och påverkan på system eller information."
            )
        return (
            "Data intrusion is connected to unauthorized access to, or unauthorized interference with, data or information systems. "
            "In Swedish criminal law, this is commonly connected to the offence called dataintrång.\n\n"
            "The key issue is authorization. Security testing, troubleshooting, and investigation should have clear permission, scope, and rules, while access or interference without permission may create legal risk.\n\n"
            "For CyberLex Sweden, data intrusion is relevant because many cyber incidents involve questions about access, permissions, account compromise, logs, and interference with systems or information."
        )

    if "cyber resilience act" in question_lower or "cyberresiliensakten" in question_lower or "products with digital elements" in question_lower or "produkter med digitala element" in question_lower:
        if use_swedish:
            return (
                "Cyber Resilience Act är en EU-förordning om cybersäkerhetskrav för produkter med digitala element. "
                "Den är relevant för uppkopplad hårdvara, mjukvara och andra digitala produkter som kan påverka cybersäkerheten.\n\n"
                "Reglerna fokuserar bland annat på säker produktdesign, sårbarhetshantering, säkerhetsuppdateringar, dokumentation och ansvar för tillverkare och andra aktörer i produktkedjan. "
                "Målet är att produkter ska vara säkrare under hela livscykeln, inte bara när de släpps.\n\n"
                "För CyberLex Sweden är Cyber Resilience Act relevant när cybersäkerhetsfrågor rör produktutveckling, leverantörer, sårbarheter, uppdateringar eller ansvar för digitala produkter."
            )
        return (
            "The Cyber Resilience Act is an EU regulation setting cybersecurity requirements for products with digital elements. "
            "It is relevant for connected hardware, software, and other digital products that can affect cybersecurity.\n\n"
            "The regulation focuses on secure product design, vulnerability handling, security updates, documentation, and duties for manufacturers and other actors in the product chain. "
            "The goal is for products to remain more secure throughout their lifecycle, not only at release.\n\n"
            "For CyberLex Sweden, the Cyber Resilience Act is relevant when cybersecurity questions involve product development, suppliers, vulnerabilities, updates, or responsibility for digital products."
        )

    if "attacks against information systems" in question_lower or "attacker mot informationssystem" in question_lower or "eu cybercrime" in question_lower or "eu cyberbrott" in question_lower:
        if use_swedish:
            return (
                "EU-reglerna om attacker mot informationssystem handlar om cyberbrott som riktas mot data, system och digital infrastruktur. "
                "De är kopplade till olaglig åtkomst, systemstörningar, datastörningar och verktyg eller handlingar som möjliggör sådana angrepp.\n\n"
                "Reglerna är viktiga eftersom de hjälper EU-länder att behandla centrala former av cyberangrepp som brott och samarbeta kring bekämpning av cyberbrottslighet.\n\n"
                "För CyberLex Sweden är detta relevant när en fråga rör gränsen mellan cybersäkerhetsarbete och brottsliga handlingar, eller när en incident kan ha koppling till obehörig åtkomst eller angrepp mot system."
            )
        return (
            "The EU rules on attacks against information systems concern cybercrime directed at data, systems, and digital infrastructure. "
            "They connect to illegal access, system interference, data interference, and tools or actions that enable such attacks.\n\n"
            "They matter because they help EU countries treat core forms of cyber attacks as criminal conduct and support cooperation against cybercrime.\n\n"
            "For CyberLex Sweden, this is relevant when a question concerns the boundary between authorized cybersecurity work and criminal activity, or when an incident may involve unauthorized access or attacks against systems."
        )

    return ""



def generate_case_aware_summary(question, language="English"):
    # Builds a more specific main answer for questions that are clearly connected
    # to the local case library. This keeps CyberLex from answering every
    # case-related question with a generic GDPR breach paragraph. A tiny miracle,
    # if one ignores the amount of string matching required to get there.
    question_lower = normalize_query_text(question).strip()
    use_swedish = language == "Svenska"

    meta_terms = [
        "meta pixel", "meta-pixel", "meta", "pixel", "facebook pixel",
        "tracking pixel", "tracking", "analytics", "third-party script",
        "third party script", "website tracking", "marketing pixel",
    ]
    hashed_kry_terms = [
        "hashed", "hashade", "hashed data", "hashed contact", "hashade kontaktuppgifter",
        "kry", "healthcare", "vård", "reprimand", "reprimand instead of fine",
    ]
    web_form_terms = [
        "web form", "webform", "form", "website form", "online form",
        "complaint form", "contact form", "formulär", "webbformulär",
        "kontaktformulär", "klagomålsformulär",
    ]
    wrong_email_terms = [
        "wrong email", "wrong recipient", "wrong attachment", "sent customer data",
        "email by mistake", "customer data to the wrong", "fel mejl", "fel e-post",
        "fel mottagare", "fel bilaga", "skickat kunduppgifter fel",
        "kunduppgifter skickades fel",
    ]
    darknet_terms = [
        "darknet", "dark web", "darkweb", "published on the darknet",
        "data published", "data is published", "published data", "publicerad på darknet",
        "publicerades på darknet", "uppgifter publiceras", "uppgifter publicerades",
    ]
    cyber_attack_case_terms = [
        "cyber attack", "cyberattack", "it attack", "hacked", "hackad",
        "sportadmin", "children", "young people", "barn", "unga",
    ]
    weak_security_terms = [
        "weak security", "poor security", "security deficiencies", "security flaws",
        "security measures cost", "weak security measures", "insufficient security",
        "access control", "exposed online", "unauthorized access risk",
        "svaga säkerhetsåtgärder", "bristande säkerhet", "säkerhetsbrister",
        "otillräckliga säkerhetsåtgärder", "åtkomstkontroll",
    ]
    cost_terms = [
        "cost", "fine", "fines", "administrative fine", "sanction", "sanctions",
        "sek", "kosta", "kostar", "böter", "sanktionsavgift", "sanktionsavgifter",
    ]
    sensitive_terms = [
        "sensitive", "sensitive personal data", "health", "pharmacy",
        "känsliga", "känsliga personuppgifter", "hälsa", "apotek",
    ]

    has_meta = contains_any(question_lower, meta_terms)
    has_hashed_kry = contains_any(question_lower, hashed_kry_terms)
    has_web_form = contains_any(question_lower, web_form_terms)
    has_wrong_email = contains_any(question_lower, wrong_email_terms)
    has_darknet = contains_any(question_lower, darknet_terms)
    has_cyber_attack_case = contains_any(question_lower, cyber_attack_case_terms)
    has_weak_security = contains_any(question_lower, weak_security_terms)
    has_cost = contains_any(question_lower, cost_terms)
    has_sensitive = contains_any(question_lower, sensitive_terms)
    has_breach_or_leak = contains_any(
        question_lower,
        [
            "breach", "data breach", "personal data breach", "data leak", "leak",
            "incident", "personuppgiftsincident", "dataläcka", "läcka", "gdpr-läcka",
        ],
    )

    if has_wrong_email:
        if use_swedish:
            return (
                "Ja. Att skicka kunduppgifter till fel mottagare eller med fel bilaga kan vara en personuppgiftsincident enligt GDPR. "
                "Organisationen bör snabbt bedöma vilka uppgifter som skickats, hur många personer som berörs, vem som mottagit uppgifterna, om mottagaren kan radera eller returnera materialet, och om incidenten innebär risk för de registrerades rättigheter och friheter. "
                "Det relaterade Indecap-fallet visar att även ett misstag i e-posthantering kan leda till IMY-tillsyn och sanktionsavgift om säkerhetsrutinerna inte är tillräckliga."
            )
        return (
            "Yes. Sending customer data to the wrong recipient or attaching the wrong file can be a personal data breach under GDPR. "
            "The organization should quickly assess what data was sent, how many people are affected, who received the information, whether the recipient can delete or return it, and whether the incident creates risk to individuals' rights and freedoms. "
            "The related Indecap wrong-email case shows that an ordinary email mistake can still lead to IMY supervision and an administrative fine if the security routines are not sufficient."
        )

    if has_darknet or has_cyber_attack_case:
        if use_swedish:
            return (
                "Om personuppgifter publiceras på Darknet eller på annat sätt görs tillgängliga efter en cyberattack är det en allvarlig incident som bör hanteras både tekniskt och dataskyddsrättsligt. "
                "Organisationen behöver bedöma vilken data som läckt, om uppgifterna rör barn, känsliga uppgifter eller skyddade identiteter, hur många som påverkas, vilka skyddsåtgärder som fanns, och om IMY eller andra myndigheter ska informeras. "
                "Sportadmin-fallet nedan visar hur en stor cyberattack och publicering av personuppgifter på Darknet kan få betydande GDPR-konsekvenser."
            )
        return (
            "If personal data is published on the Darknet or otherwise made available after a cyber attack, the incident should be handled as both a technical security incident and a data-protection issue. "
            "The organization needs to assess what data was leaked, whether it concerns children, sensitive data, or protected identities, how many people are affected, what security measures were in place, and whether IMY or other authorities must be notified. "
            "The related Sportadmin case shows how a large cyber attack and Darknet publication of personal data can lead to significant GDPR consequences."
        )

    if has_hashed_kry and has_meta:
        if use_swedish:
            return (
                "Ja. Hashade uppgifter som skickas genom Meta Pixel kan fortfarande skapa GDPR-risk. Hashning gör inte automatiskt att uppgifterna slutar vara personuppgifter, särskilt om de kan kopplas till individer eller används för matchning mot en tredje part. "
                "Organisationen bör kontrollera vilka uppgifter som överförs, om överföringen var avsedd, vilken rättslig grund som finns, hur verktyget är konfigurerat, och om tillräckliga tekniska och organisatoriska åtgärder finns. "
                "Kry-fallet nedan är användbart eftersom IMY bedömde Meta Pixel och hashade kontaktuppgifter, men utfallet blev en reprimand i stället för sanktionsavgift."
            )
        return (
            "Yes. Hashed data sent through Meta Pixel can still create GDPR risk. Hashing does not automatically mean the data is no longer personal data, especially if it can be linked to individuals or used for matching by a third party. "
            "The organization should check what data is transferred, whether the transfer was intended, what legal basis applies, how the tool is configured, and whether appropriate technical and organisational measures are in place. "
            "The Kry case below is useful because IMY assessed Meta Pixel and hashed contact information, but the outcome was a reprimand rather than an administrative fine."
        )

    if has_meta:
        if use_swedish:
            return (
                "Ja. Meta Pixel och liknande spårningsteknik kan skapa GDPR-risk om verktyget gör att personuppgifter skickas till Meta eller andra tredje parter utan tillräcklig kontroll, transparens, rättslig grund eller säkerhetsbedömning. "
                "Risken blir högre om uppgifterna rör kunder, konton, köp, hälsa eller andra känsliga sammanhang. Organisationen bör därför kartlägga exakt vilka uppgifter som samlas in, vem som tar emot dem, om användare har informerats, om samtycke eller annan rättslig grund finns, och om privacy by design har följts. "
                "De relaterade fallen nedan visar hur svenska myndighetsbeslut har bedömt liknande problem med Meta Pixel och överföring av personuppgifter."
            )
        return (
            "Yes. Meta Pixel and similar tracking technology can create GDPR risk if it causes personal data to be sent to Meta or other third parties without sufficient control, transparency, legal basis, or security assessment. "
            "The risk becomes higher if the data relates to customers, accounts, purchases, health, or other sensitive contexts. An organization should map exactly what data the pixel collects, who receives it, whether users were informed, whether consent or another legal basis exists, and whether privacy by design was applied. "
            "The related cases below show how Swedish authority decisions have assessed similar Meta Pixel and personal-data transfer issues."
        )

    if has_web_form:
        if use_swedish:
            return (
                "Ja. Ett webbformulär kan orsaka en personuppgiftsincident om formuläret samlar in personuppgifter och uppgifterna av misstag exponeras, skickas till analysverktyg, lämnas till ett personuppgiftsbiträde på fel sätt, lagras osäkert eller blir tillgängliga för obehöriga. "
                "Risken blir högre om formuläret innehåller klagomål, identitetsuppgifter, hälsouppgifter, diskrimineringsuppgifter eller annan känslig information. Organisationen bör kontrollera formulärets dataflöden, loggning, åtkomstkontroller, analysverktyg, personuppgiftsbiträden och om uppgifterna kan ha lämnats ut felaktigt. "
                "Det relaterade DO-fallet nedan är ett tydligt exempel på hur ett webbformulär och en bristande säkerhetsåtgärd kan leda till GDPR-konsekvenser."
            )
        return (
            "Yes. A web form can cause a personal data breach if it collects personal data and that data is accidentally exposed, sent to analytics tools, disclosed incorrectly to a processor, stored insecurely, or made accessible to unauthorized persons. "
            "The risk becomes higher if the form contains complaints, identity details, health data, discrimination-related information, or other sensitive information. An organization should check the form's data flows, logging, access controls, analytics tools, processors, and whether any information may have been disclosed incorrectly. "
            "The related Equality Ombudsman case below is a clear example of how a web form and a failed security measure can lead to GDPR consequences."
        )

    if has_weak_security:
        if use_swedish:
            return (
                "Bristande säkerhetsåtgärder kan skapa GDPR-risk eftersom organisationer måste skydda personuppgifter med lämpliga tekniska och organisatoriska åtgärder. "
                "Exempel kan vara svag åtkomstkontroll, otillräcklig autentisering, bristande loggning, osäkra system, felkonfigurationer eller uppgifter som blir åtkomliga via internet. "
                "Konsekvenserna kan bli intern utredning, teknisk åtgärd, dokumentation, anmälan till IMY, information till berörda personer, kostnader för incidenthantering och i vissa fall sanktionsavgifter. De relaterade fallen nedan visar verkliga exempel på hur sådana risker har bedömts."
            )
        return (
            "Weak security measures can create GDPR risk because organizations must protect personal data with appropriate technical and organisational measures. "
            "Examples can include poor access control, weak authentication, insufficient logging, insecure systems, misconfiguration, or information being accessible via the internet. "
            "Consequences can include internal investigation, technical remediation, documentation, notification to IMY, communication to affected individuals, incident-response costs, and in some cases administrative fines. The related cases below show real examples of how these risks have been assessed."
        )

    if has_cost and (has_breach_or_leak or "gdpr" in question_lower or "imy" in question_lower):
        if use_swedish:
            return (
                "Kostnaden för en GDPR-relaterad incident kan variera mycket. Den kan omfatta teknisk incidenthantering, forensisk analys, juridisk bedömning, dokumentation, information till berörda personer, driftstopp, förbättrade säkerhetsåtgärder, ryktepåverkan och eventuell sanktionsavgift. "
                "CyberLex bör inte förutsäga böter, eftersom belopp beror på de faktiska omständigheterna, typen av personuppgifter, antal berörda personer, risknivå, säkerhetsåtgärder, oaktsamhet eller avsikt, åtgärder efter incidenten och samarbete med myndigheten. "
                "De relaterade fallen nedan visar historiska exempel på beslut och belopp, inte en prognos för nya ärenden."
            )
        return (
            "The cost of a GDPR-related incident can vary widely. It can include technical incident response, forensic analysis, legal assessment, documentation, communication to affected individuals, downtime, security improvements, reputational impact, and a possible administrative fine. "
            "CyberLex should not predict fines because amounts depend on the specific facts, the type of personal data, number of affected people, level of risk, security measures, negligence or intent, mitigation, and cooperation with the authority. "
            "The related cases below show historical examples of decisions and amounts, not a prediction for new incidents."
        )

    if has_sensitive and ("gdpr" in question_lower or has_breach_or_leak):
        if use_swedish:
            return (
                "Känsliga personuppgifter innebär normalt högre GDPR-risk. Om sådana uppgifter exponeras, överförs till en tredje part eller behandlas utan tillräcklig kontroll kan organisationen behöva göra en noggrann riskbedömning, dokumentera händelsen, överväga anmälan till IMY och i vissa fall informera berörda personer. "
                "Särskilt viktigt är att kontrollera rättslig grund, säkerhetsåtgärder, åtkomst, leverantörer och om privacy by design har följts. Relaterade fall nedan visar exempel där känsliga sammanhang påverkade bedömningen."
            )
        return (
            "Sensitive personal data normally creates higher GDPR risk. If such data is exposed, transferred to a third party, or processed without sufficient control, the organization may need to perform a careful risk assessment, document the event, consider notification to IMY, and in some cases inform affected individuals. "
            "Key checks include legal basis, security measures, access, suppliers, and whether privacy by design was applied. The related cases below show examples where sensitive contexts affected the assessment."
        )

    return ""


def generate_simple_answer(question, best_match, language="English", include_technical_details=False):
    # Generates a simple source-based answer from the best matching chunk.
    question_lower = normalize_query_text(question)
    use_swedish = language == "Svenska"

    if (
        is_practical_incident_response_question(question)
        or is_data_leak_response_question(question)
        or is_ransomware_response_question(question)
    ):
        return generate_incident_response_answer(question, language)

    enhanced_basic_answer = generate_case_aware_summary(question, language)

    if not enhanced_basic_answer and is_nis2_sector_scope_question(question):
        if use_swedish:
            if "bilaga" in question_lower or "annex" in question_lower:
                answer = (
                    "Bilaga 1 och bilaga 2 är sektorslistor i NIS2-direktivet som används vid bedömningen av om en verksamhet kan omfattas. "
                    "Bilaga 1 gäller sektorer med hög kritikalitet, till exempel energi, transporter, bankverksamhet, hälso- och sjukvård, dricksvatten, avloppsvatten, digital infrastruktur, offentlig förvaltning och rymden. "
                    "Bilaga 2 gäller andra kritiska sektorer, till exempel post- och budtjänster, avfallshantering, kemikalier, livsmedel, tillverkning, digitala leverantörer och forskning. "
                    "Att en verksamhet finns nära en sektor räcker inte alltid. Organisationen behöver kontrollera om den konkreta verksamhetstypen motsvarar det som omfattas och dokumentera sin bedömning."
                )
            elif (
                "väsentlig" in question_lower
                or "väsentliga" in question_lower
                or "viktig" in question_lower
                or "viktiga" in question_lower
                or "verksamhetsutövare" in question_lower
                or "skillnaden" in question_lower
            ):
                answer = (
                    "Verksamheter som omfattas av NIS2 delas in i väsentliga eller viktiga verksamhetsutövare. Kraven är i stora drag liknande, men tillsyn och sanktionsavgifter kan skilja sig åt. "
                    "Indelningen kan bero på sektor, om verksamheten finns i bilaga 1 eller bilaga 2 till NIS2-direktivet, och organisationens storlek. "
                    "CyberLex bör därför inte göra en slutlig klassificering utan tillräckliga fakta. Organisationen bör bedöma sektor, verksamhetstyp, storlek och jurisdiktion och dokumentera varför den bedömer sig vara väsentlig, viktig eller inte omfattad."
                )
            elif "sektor" in question_lower or "sektorer" in question_lower:
                answer = (
                    "Cybersäkerhetslagen omfattar verksamhet inom 18 sektorer, bland annat energi, transporter, bank, finansmarknadsinfrastruktur, hälso- och sjukvård, dricksvatten, avloppsvatten, digital infrastruktur, IKT-tjänstehantering mellan företag, offentlig förvaltning, rymd, post- och budtjänster, avfallshantering, kemikalier, livsmedel, tillverkning, digitala leverantörer och forskning. "
                    "Det betyder inte att varje organisation nära en sektor automatiskt omfattas. Bedömningen behöver göras utifrån den konkreta verksamhetstypen, organisationens storlek och svensk jurisdiktion. Organisationen bör dokumentera varför den bedömer att den omfattas eller inte omfattas."
                )
            elif "kommun" in question_lower or "region" in question_lower:
                answer = (
                    "Kommuner, regioner och kommunalförbund kan omfattas av cybersäkerhetslagen inom sektorn offentlig förvaltning, normalt oberoende av storlek. "
                    "De kan dessutom ha verksamheter som berör andra sektorer, till exempel vatten, avlopp, vård, digital infrastruktur eller andra samhällsviktiga funktioner. Bedömningen bör därför göras per juridisk person och verksamhet, och dokumenteras."
                )
            elif "anmäla" in question_lower or "registrera" in question_lower or "registrering" in question_lower:
                answer = (
                    "Verksamhetsutövare som bedömer att de omfattas av cybersäkerhetslagen ska anmäla eller registrera verksamheten enligt de regler och instruktioner som gäller. "
                    "Först bör organisationen bedöma sektor, verksamhetstyp, storlek och jurisdiktion. Om bedömningen talar för att organisationen omfattas bör skälen dokumenteras och anmälan göras enligt den officiella processen."
                )
            elif "små" in question_lower or "mikro" in question_lower:
                answer = (
                    "Små företag och mikroföretag omfattas normalt inte som huvudregel, men undantag finns. Vissa verksamhetstyper kan omfattas oavsett storlek om de har särskild betydelse eller omfattas av särskilda regler. "
                    "Organisationen bör därför inte bara titta på antal anställda eller omsättning, utan även sektor, faktisk verksamhet, kopplade företag och eventuell roll i samhällsviktiga tjänster."
                )
            else:
                answer = (
                    "Om NIS2 eller cybersäkerhetslagen gäller för en organisation beror främst på verksamhetstyp, sektor, storlek och svensk jurisdiktion. "
                    "Börja med att identifiera vilken juridisk person som bedöms, vilken verksamhet den bedriver och om verksamheten finns inom någon av de 18 sektorerna. "
                    "Bedöm också om organisationen är medelstor eller större, eller om den kan omfattas av undantag. Dokumentera bedömningen och varför organisationen anses omfattas eller inte omfattas."
                )
        else:
            if "annex" in question_lower or "bilaga" in question_lower:
                answer = (
                    "Annex 1 and Annex 2 are the sector lists in the NIS2 Directive used when assessing whether an activity may be covered. "
                    "Annex 1 covers sectors of high criticality, such as energy, transport, banking, healthcare, drinking water, wastewater, digital infrastructure, public administration, and space. "
                    "Annex 2 covers other critical sectors, such as postal and courier services, waste management, chemicals, food, manufacturing, digital providers, and research. "
                    "Being close to a sector is not always enough. The organization still needs to check whether its specific activity type matches the covered entity types and document the assessment."
                )
            elif (
                "essential" in question_lower
                or "important" in question_lower
                or "entities" in question_lower
                or "entity" in question_lower
                or "difference" in question_lower
            ):
                answer = (
                    "Organizations covered by NIS2 are categorized as essential or important entities. The practical requirements are broadly similar, but supervision and sanctions can differ. "
                    "The distinction can depend on the sector, whether the activity is listed in Annex 1 or Annex 2 of the NIS2 Directive, and the size of the organization. "
                    "CyberLex should therefore not make a final classification without enough facts. The organization should assess sector, activity type, size, and jurisdiction, and document why it considers itself essential, important, or not covered."
                )
            elif "sector" in question_lower or "sectors" in question_lower:
                answer = (
                    "The Swedish Cybersecurity Act covers activities in 18 sectors, including energy, transport, banking, financial market infrastructure, healthcare, drinking water, wastewater, digital infrastructure, ICT service management between businesses, public administration, space, postal and courier services, waste management, chemicals, food, manufacturing, digital providers, and research. "
                    "Being near a sector is not enough by itself. The organization must assess its exact activity type, size, and jurisdiction, and document why it believes it is or is not covered."
                )
            elif "municipal" in question_lower or "region" in question_lower:
                answer = (
                    "Municipalities, regions, and municipal associations can be covered under the public administration sector of the Swedish Cybersecurity Act, normally regardless of size. "
                    "They may also perform activities connected to other sectors, such as water, healthcare, digital infrastructure, or other socially important services. The assessment should be made per legal entity and activity and should be documented."
                )
            elif "register" in question_lower or "registration" in question_lower:
                answer = (
                    "Operators that assess that they are covered by the Swedish Cybersecurity Act must register according to the official process. "
                    "Before registering, the organization should assess sector, activity type, size, and jurisdiction. If the assessment indicates that the organization is covered, it should document the reasoning and submit the registration."
                )
            elif "small" in question_lower or "micro" in question_lower:
                answer = (
                    "Small and micro companies are usually not covered as a main rule, but there are exceptions. Some operators can be covered regardless of size because of their role or activity type. "
                    "A company should therefore assess not only employee count or turnover, but also sector, exact activity, linked or partner enterprises, and whether it performs a role that falls under the rules."
                )
            else:
                answer = (
                    "Whether NIS2 or the Swedish Cybersecurity Act applies to an organization mainly depends on activity type, sector, size, and Swedish jurisdiction. "
                    "Start by identifying the legal entity, what activity it performs, and whether that activity falls within one of the 18 covered sectors. "
                    "Also assess whether the organization is medium-sized or larger, or whether an exception may apply. Document the assessment and why the organization is considered covered or not covered."
                )

        if include_technical_details:
            answer += "\n\n" + build_match_details(best_match, language)

        return answer

    if not enhanced_basic_answer and is_gdpr_security_guidance_question(question):
        is_mfa_question = has_mfa_term(question_lower)
        is_encryption_question = (
            "kryptering" in question_lower
            or "kryptera" in question_lower
            or "encryption" in question_lower
            or "encrypt" in question_lower
        )
        is_imy_security_question = (
            "vad säger imy" in question_lower
            or "what does imy say" in question_lower
        )
        is_protect_personal_data_question = (
            "skydda personuppgifter" in question_lower
            or "skydd av personuppgifter" in question_lower
            or "protect personal data" in question_lower
        )
        is_security_measure_question = (
            "säkerhetsåtgärd" in question_lower
            or "security measure" in question_lower
            or "dataskydd genom design" in question_lower
            or "data protection by design" in question_lower
            or "privacy by design" in question_lower
            or is_mfa_question
            or is_encryption_question
            or is_imy_security_question
            or is_protect_personal_data_question
        )
        is_gdpr_incident_connection_question = (
            "connect to incident response" in question_lower
            or "relate to incident response" in question_lower
            or "gdpr incident response" in question_lower
            or "kopplas" in question_lower
            or "incidenthantering" in question_lower
            or "hänger" in question_lower
        )

        if use_swedish:
            if is_mfa_question:
                answer = (
                    "GDPR säger normalt inte att MFA alltid måste användas i varje situation. Däremot kräver GDPR en lämplig säkerhetsnivå utifrån risk, typ av personuppgifter, system och möjliga konsekvenser för registrerade personer. "
                    "MFA kan därför vara en viktig och rimlig teknisk säkerhetsåtgärd, särskilt för administratörskonton, fjärråtkomst, molntjänster, e-postkonton, system med känsliga personuppgifter eller konton där obehörig åtkomst kan få stor påverkan. "
                    "Organisationen bör dokumentera var MFA används, var den inte används, varför nivån bedöms tillräcklig och vilka kompletterande skydd som finns, till exempel loggning, behörighetsstyrning och incidentrutiner."
                )
            elif is_encryption_question:
                answer = (
                    "GDPR kräver inte kryptering i exakt alla situationer, men kryptering är en tydlig teknisk säkerhetsåtgärd som ofta kan vara lämplig när personuppgifter behöver skyddas mot obehörig åtkomst, förlust eller röjande. "
                    "Behovet beror på risk, datatyp, systemmiljö, åtkomst, lagring, överföring och möjliga konsekvenser för registrerade personer. Kryptering kan vara särskilt viktig för känsliga uppgifter, bärbara enheter, säkerhetskopior, databaser, filöverföring och molnlagring. "
                    "Organisationen bör även dokumentera nyckelhantering, åtkomstkontroll, backupskydd och varför vald skyddsnivå är rimlig."
                )
            elif is_imy_security_question:
                answer = (
                    "IMY:s vägledning innebär att säkerhetsåtgärder enligt GDPR ska väljas riskbaserat. Det finns alltså inte en enda universell checklista som passar alla organisationer. "
                    "Organisationen bör bedöma vilka personuppgifter som behandlas, var de finns, vem som har åtkomst, vilka system och leverantörer som används och vad konsekvenserna kan bli vid obehörig åtkomst, förlust, ändring eller röjande. "
                    "Praktiskt handlar det om både tekniska åtgärder, till exempel åtkomstkontroll, MFA, loggning, kryptering och säkerhetskopior, och organisatoriska åtgärder, till exempel rutiner, ansvar, utbildning, leverantörskrav, uppföljning och dokumentation."
                )
            elif is_protect_personal_data_question:
                answer = (
                    "Personuppgifter bör skyddas genom en riskbaserad kombination av tekniska och organisatoriska åtgärder. Börja med att kartlägga vilka personuppgifter som behandlas, var de lagras, vilka system och leverantörer som används och vem som behöver åtkomst. "
                    "Begränsa åtkomst efter behov, använd stark autentisering där risken motiverar det, logga och följ upp åtkomst, skydda data med kryptering där det är lämpligt, säkra backup och ha rutiner för incidenter och personuppgiftsincidenter. "
                    "Organisationen bör också utbilda användare, granska behörigheter regelbundet och dokumentera både riskbedömningar och valda skyddsåtgärder."
                )
            elif is_security_measure_question:
                answer = (
                    "Enligt GDPR bör säkerhetsåtgärder väljas utifrån risk, typ av personuppgifter, systemens användning och möjliga konsekvenser för registrerade personer. "
                    "Praktiskt innebär det ofta åtkomstkontroll, stark autentisering där det är lämpligt, loggning, kryptering, säkerhetskopior, behörighetsseparering, dataminimering, säkra standardinställningar och rutiner för incidenthantering. "
                    "Organisationen bör också dokumentera vilka åtgärder som finns, varför de är rimliga och hur de följs upp. Det stödjer ansvarsskyldighet, dataskydd genom design och dataskydd som standard."
                )
            elif is_gdpr_incident_connection_question:
                answer = (
                    "GDPR kopplas till incidenthantering när en säkerhetsincident kan påverka personuppgifter. IT- och säkerhetsteamet behöver begränsa händelsen, säkra loggar och förstå vilka system, konton och data som berörts. "
                    "Samtidigt behöver dataskydds- eller ansvarig funktion bedöma om personuppgifter har lästs, kopierats, ändrats, raderats, krypterats, röjts obehörigt eller blivit otillgängliga. "
                    "Bedömningen ska också omfatta risk för registrerade personer, om IMY behöver underrättas inom 72 timmar, om berörda personer måste informeras vid hög risk och hur beslut, åtgärder och kvarstående osäkerheter dokumenteras."
                )
            else:
                answer = (
                    "Efter en personuppgiftsincident bör organisationen bedöma vad som hänt, när det upptäcktes, vilka system och uppgifter som berördes, och om personuppgifter har lästs, kopierats, ändrats, raderats, krypterats, röjts obehörigt eller blivit otillgängliga. "
                    "Bedöm också vilka personer som kan påverkas, vilka möjliga konsekvenser incidenten kan få, och om det finns risk för exempelvis identitetsstöld, bedrägeri, ekonomisk skada eller sekretessförlust. "
                    "Därefter bör organisationen avgöra om IMY ska underrättas inom 72 timmar, om berörda personer behöver informeras vid hög risk, vilka skyddsåtgärder som minskar skadan och hur beslutet ska dokumenteras."
                )
        else:
            if is_mfa_question:
                answer = (
                    "GDPR does not usually say that MFA is mandatory in every situation. Instead, it requires an appropriate level of security based on risk, the type of personal data, the systems used, and the possible impact on individuals. "
                    "MFA can therefore be an appropriate and important technical security measure, especially for administrator accounts, remote access, cloud services, email accounts, systems with sensitive personal data, or accounts where unauthorized access could cause serious harm. "
                    "The organization should document where MFA is used, where it is not used, why the chosen level is considered appropriate, and which supporting controls exist, such as logging, access control, monitoring, and incident routines."
                )
            elif is_encryption_question:
                answer = (
                    "GDPR does not require encryption in every single situation, but encryption is a clear technical security measure that can be appropriate when personal data needs protection against unauthorized access, loss, disclosure, or misuse. "
                    "Whether encryption is needed depends on risk, data type, storage, transfer, access, system design, and the possible impact on individuals. It is especially relevant for sensitive data, portable devices, backups, databases, file transfers, and cloud storage. "
                    "The organization should also document key management, access control, backup protection, and why the selected protection level is appropriate."
                )
            elif is_imy_security_question:
                answer = (
                    "IMY's guidance means that GDPR security measures should be selected based on risk. There is no single universal checklist that fits every organization. "
                    "The organization should assess what personal data it processes, where it is stored, who has access, which systems and suppliers are involved, and what the consequences could be if the data is accessed, lost, changed, disclosed, or made unavailable. "
                    "In practice, this includes technical measures such as access control, MFA, logging, encryption, and backups, and organizational measures such as policies, routines, responsibility, training, supplier requirements, follow-up, and documentation."
                )
            elif is_protect_personal_data_question:
                answer = (
                    "Personal data should be protected through a risk-based mix of technical and organizational measures. Start by mapping what personal data is processed, where it is stored, which systems and suppliers are involved, and who needs access. "
                    "Limit access to what is necessary, use strong authentication where risk justifies it, log and review access, use encryption where appropriate, protect backups, and maintain routines for incidents and personal data breaches. "
                    "The organization should also train users, review permissions regularly, and document both the risk assessment and the selected security measures."
                )
            elif is_security_measure_question:
                answer = (
                    "Under GDPR, security measures should be selected based on risk, the type of personal data, how systems are used, and the possible impact on individuals. "
                    "In practice, this can include access control, strong authentication where appropriate, logging, encryption, backups, separation of privileges, data minimisation, secure defaults, and incident-response routines. "
                    "The organization should document which measures exist, why they are appropriate, and how they are reviewed. This supports accountability, data protection by design, and data protection by default."
                )
            elif is_gdpr_incident_connection_question:
                answer = (
                    "GDPR connects to incident response when a security incident may affect personal data. The technical team should contain the incident, preserve logs, identify affected systems/accounts, and determine what data was accessed, copied, changed, deleted, encrypted, disclosed, or made unavailable. "
                    "At the same time, the privacy or responsible function should assess the risk to individuals, whether IMY must be notified within 72 hours, whether affected individuals must be informed if the risk is high, and what mitigation steps reduce harm. "
                    "The organization should document the timeline, evidence, decisions, reporting assessment, and remaining uncertainty, because fixing the technical issue does not replace the GDPR assessment."
                )
            else:
                answer = (
                    "After a personal data breach, an organization should assess what happened, when it was discovered, which systems and data were affected, and whether personal data was accessed, copied, changed, deleted, encrypted, disclosed, or made unavailable. "
                    "It should also assess which people may be affected, the likely consequences, and whether there is risk of identity theft, fraud, financial loss, confidentiality loss, or other harm. "
                    "The organization should then decide whether IMY must be notified within 72 hours, whether affected individuals must be informed if the risk is high, which protective measures reduce harm, and how the decision should be documented."
                )
        enhanced_basic_answer = answer
    if not enhanced_basic_answer:
        enhanced_basic_answer = generate_enhanced_basic_summary(question, language)

    if enhanced_basic_answer:
        # Keep basic summaries visually compact in the main answer card.
        # Detailed source context remains available below.
        answer = re.sub(r"\s*\n\s*\n\s*", " ", enhanced_basic_answer).strip()

    elif (
        "data breach" in question_lower
        or "personal data breach" in question_lower
        or "personuppgiftsincident" in question_lower
    ) and (
        "what should" in question_lower
        or "what must" in question_lower
        or "what does" in question_lower
        or "after" in question_lower
        or "reported" in question_lower
        or "report" in question_lower
        or "rapportera" in question_lower
        or "rapporteras" in question_lower
    ):
        if use_swedish:
            answer = (
                "Efter en personuppgiftsincident bör organisationen först begränsa incidenten, bevara relevant bevisning "
                "och dokumentera vad som har hänt. Därefter bör organisationen bedöma om incidenten innebär risk för "
                "registrerades rättigheter och friheter, om anmälan till IMY krävs inom 72 timmar, och om de berörda personerna "
                "kan behöva informeras vid hög risk."
            )
        else:
            answer = (
                "After a data breach, an organization should first contain the incident, preserve relevant evidence, "
                "and document what happened. It should then assess whether personal data was affected, whether the breach creates "
                "a risk to individuals' rights and freedoms, whether notification to IMY is required within 72 hours, "
                "and whether affected individuals may need to be informed if the risk is high."
            )

    elif (
        "ransomware" in question_lower
        or "malware" in question_lower
        or "files are encrypted" in question_lower
        or "our files are encrypted" in question_lower
        or "files have been encrypted" in question_lower
        or "encrypted files" in question_lower
        or "cyber attack" in question_lower
        or "cyberattack" in question_lower
    ):
        if use_swedish:
            answer = (
                "Efter en ransomwareattack eller incident med skadlig kod bör organisationen först isolera drabbade system, "
                "begränsa vidare spridning, säkra loggar och bevis, och dokumentera tidslinjen. Därefter bör organisationen "
                "bedöma om personuppgifter har påverkats, om anmälan till IMY enligt GDPR kan krävas, och om "
                "incidentrapportering enligt NIS2 eller den svenska cybersäkerhetslagen kan vara relevant."
            )
        else:
            answer = (
                "After a ransomware or malware attack, an organization should first isolate affected systems, "
                "limit further spread, preserve logs and evidence, and document the timeline. It should then assess "
                "whether personal data was affected, whether notification to IMY under GDPR may be required, and whether "
                "incident reporting under NIS2 or the Swedish Cybersecurity Act may be relevant."
            )

    elif (
        "cyber incident" in question_lower
        or "security incident" in question_lower
        or "incident response" in question_lower
        or "what should an organization check after" in question_lower
        or "what should an organisation check after" in question_lower
        or "what should an organization do after a cyber incident" in question_lower
        or "what should an organisation do after a cyber incident" in question_lower
    ):
        if use_swedish:
            answer = (
                "Efter en cyberincident bör organisationen kontrollera vad som hänt, vilka system och data som berörts, "
                "om personuppgifter har påverkats, och om incidenten kan vara rapporteringspliktig. Organisationen bör också "
                "dokumentera tidslinje, teknisk påverkan, beslut, åtgärder och vilka regelverk som har bedömts, till exempel "
                "GDPR, NIS2 eller den svenska cybersäkerhetslagen."
            )
        else:
            answer = (
                "After a cyber incident, an organization should check what happened, which systems and data were affected, "
                "whether personal data was involved, and whether the incident may be reportable. It should also document "
                "the timeline, technical impact, decisions, actions taken, and which legal frameworks were assessed, such as "
                "GDPR, NIS2, or the Swedish Cybersecurity Act."
            )

    elif (
        "what is imy" in question_lower
        or "what does imy do" in question_lower
        or question_lower.strip() == "imy"
        or "vad är imy" in question_lower
        or "vad gör imy" in question_lower
    ):
        if use_swedish:
            answer = (
                "IMY, Integritetsskyddsmyndigheten, är Sveriges myndighet för integritetsskydd och dataskydd. "
                "IMY har tillsyn över GDPR i Sverige och är därför central när organisationer hanterar personuppgifter. "
                "Myndigheten är särskilt relevant för CyberLex Sweden eftersom cyberincidenter kan leda till personuppgiftsincidenter, "
                "riskbedömningar och möjliga anmälningar till IMY."
            )
        else:
            answer = (
                "IMY, Integritetsskyddsmyndigheten, is the Swedish Authority for Privacy Protection. "
                "It supervises GDPR and personal data protection in Sweden, which makes it central when organizations handle personal data. "
                "IMY is relevant to CyberLex Sweden because cyber incidents can lead to personal data breaches, risk assessments, "
                "and possible notification duties toward the authority."
            )

    elif (
        "supervises gdpr" in question_lower
        or "authority supervises gdpr" in question_lower
        or "authority handles gdpr" in question_lower
        or "vilken myndighet hanterar gdpr" in question_lower
        or "vilken myndighet ansvarar för gdpr" in question_lower
        or "vilken myndighet har tillsyn över gdpr" in question_lower
    ):
        if use_swedish:
            answer = (
                "I Sverige är det IMY, Integritetsskyddsmyndigheten, som har tillsyn över GDPR och dataskydd. "
                "Det innebär att IMY är den centrala myndigheten när organisationer behöver förstå skyldigheter kring personuppgifter, "
                "personuppgiftsincidenter och dataskyddsarbete. Vid cyberincidenter är IMY särskilt relevant om personuppgifter kan ha påverkats."
            )
        else:
            answer = (
                "In Sweden, GDPR and personal data protection are supervised by IMY, Integritetsskyddsmyndigheten, "
                "the Swedish Authority for Privacy Protection. This makes IMY the key Swedish authority for questions about personal data, "
                "data protection duties, and personal data breaches. For cyber incidents, IMY becomes especially relevant if personal data may have been affected."
            )

    elif (
        "dora" in question_lower
        or "digital operational resilience act" in question_lower
        or "digital operational resilience" in question_lower
        or "ict risk management" in question_lower
        or "ict third-party risk" in question_lower
        or "third-party ict risk" in question_lower
        or "financial sector cybersecurity" in question_lower
        or "vad är dora" in question_lower
        or "digital operativ motståndskraft" in question_lower
        or "tredjepartsrisk enligt dora" in question_lower
        or "ict-risk enligt dora" in question_lower
    ):
        if use_swedish:
            answer = (
                "DORA, Digital Operational Resilience Act, är en EU-förordning för den finansiella sektorn. "
                "Den handlar om digital operativ motståndskraft, vilket betyder förmågan att förebygga, hantera och återhämta sig från ICT-störningar och cyberincidenter. "
                "Reglerna fokuserar bland annat på ICT-riskhantering, rapportering av större ICT-relaterade incidenter, testning av motståndskraft och hantering av tredjepartsrisker. "
                "För CyberLex Sweden är DORA relevant när cybersäkerhet kopplas till banker, finansiella aktörer och deras digitala leverantörer."
            )
        else:
            answer = (
                "DORA, the Digital Operational Resilience Act, is an EU regulation for the financial sector. "
                "It focuses on digital operational resilience, meaning the ability to prevent, manage, and recover from ICT disruptions and cyber incidents. "
                "The regulation covers ICT risk management, major ICT-related incident reporting, resilience testing, ICT third-party risk management, and information sharing. "
                "For CyberLex Sweden, DORA is relevant when cybersecurity duties affect financial entities and their digital service providers."
            )

    elif (
        ("nis2" in question_lower or "nis" in question_lower or "cybersecurity act" in question_lower or "cybersäkerhetslagen" in question_lower)
        and "gdpr" in question_lower
        and ("incident" in question_lower or "reported" in question_lower or "report" in question_lower or "rapporteras" in question_lower or "rapportera" in question_lower)
    ):
        if use_swedish:
            answer = (
                "Ja, vissa cybersäkerhetsincidenter kan behöva bedömas enligt både NIS2 och GDPR. "
                "NIS2 och cybersäkerhetslagen handlar om cybersäkerhetsincidenten, medan GDPR handlar om personuppgifter och risker för registrerade. "
                "Regelverken kan därför överlappa om en incident både påverkar säkerheten i digitala tjänster och leder till en personuppgiftsincident. "
                "I praktiken bör organisationen dokumentera båda bedömningarna och kontrollera om flera rapporteringsvägar kan vara relevanta."
            )
        else:
            answer = (
                "Yes, some cybersecurity incidents may need to be assessed under both NIS2 and GDPR. "
                "NIS2 and the Swedish Cybersecurity Act concern the cybersecurity incident itself, while GDPR concerns personal data and risks to individuals. "
                "The rules can overlap if an incident affects digital security and also creates a personal data breach. "
                "In practice, the organization should document both assessments and check whether more than one reporting path may be relevant."
            )

    elif (
        "nis2 incident reporting" in question_lower
        or "nis incident reporting" in question_lower
        or "cybersecurity incident reporting" in question_lower
        or "incident reporting under nis2" in question_lower
        or "incident reporting under nis" in question_lower
        or "incident reporting under the cybersecurity act" in question_lower
        or "report cybersecurity incident" in question_lower
        or "reported under nis2" in question_lower
        or "reported under nis" in question_lower
        or "nis2-incidentrapportering" in question_lower
        or "incidentrapportering enligt nis2" in question_lower
        or "incidentrapportering enligt cybersäkerhetslagen" in question_lower
        or "rapportera cybersäkerhetsincident" in question_lower
    ):
        if use_swedish:
            answer = (
                "NIS2-incidentrapportering i Sverige är kopplad till cybersäkerhetslagen. "
                "Organisationer som omfattas kan behöva rapportera betydande cybersäkerhetsincidenter enligt särskilda kriterier, rutiner och tidsfrister. "
                "Bedömningen beror på incidentens påverkan, organisationens sektor och om verksamheten omfattas av reglerna. "
                "Vissa incidenter kan också behöva bedömas enligt GDPR om personuppgifter påverkas."
            )
        else:
            answer = (
                "NIS2 incident reporting in Sweden is handled through the Swedish Cybersecurity Act. "
                "Covered organizations may need to report significant cybersecurity incidents according to specific criteria, procedures, and time limits. "
                "The assessment depends on the incident impact, the organization's sector, and whether the organization is covered by the rules. "
                "Some incidents may also need a separate GDPR assessment if personal data is affected."
            )

    elif (
        "personal data breach" in question_lower
        or "breach reported" in question_lower
        or "data breach reported" in question_lower
        or "72-hour" in question_lower
        or "72 hour" in question_lower
        or "breach notification" in question_lower
        or "personuppgiftsincident" in question_lower
        or "när måste en personuppgiftsincident rapporteras" in question_lower
        or "när ska en personuppgiftsincident anmälas" in question_lower
        or "rapportera personuppgiftsincident" in question_lower
        or "72 timmar" in question_lower
        or "breach" in question_lower
    ):
        if use_swedish:
            answer = (
                "En personuppgiftsincident kan behöva rapporteras till IMY. "
                "Organisationen måste bedöma om incidenten sannolikt innebär en risk för fysiska personers rättigheter och friheter. "
                "Om anmälan krävs ska den normalt göras inom 72 timmar efter att organisationen blev medveten om incidenten."
            )
        else:
            answer = (
                "A personal data breach may need to be reported to IMY, the Swedish Authority for Privacy Protection. "
                "The organization first needs to assess whether the breach is likely to create a risk to individuals' rights and freedoms. "
                "If notification is required, the breach should normally be reported within 72 hours after the organization becomes aware of it. "
                "The organization should also document the incident, the risk assessment, and the reasons for any reporting decision."
            )

    elif (
        "gdpr principles" in question_lower
        or "gdpr principle" in question_lower
        or "what are the gdpr principles" in question_lower
        or "principles" in question_lower
        or "gdpr-principer" in question_lower
        or "gdpr principer" in question_lower
        or "vilka är gdpr-principerna" in question_lower
        or "vilka är gdpr principerna" in question_lower
    ):
        if use_swedish:
            answer = (
                "GDPR innehåller grundläggande principer för behandling av personuppgifter. "
                "De omfattar bland annat laglighet, korrekthet och transparens, ändamålsbegränsning, "
                "uppgiftsminimering, riktighet, lagringsminimering, integritet och konfidentialitet samt ansvarsskyldighet."
            )
        else:
            answer = (
                "GDPR includes core principles that guide how personal data may be processed. "
                "These include lawfulness, fairness and transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality, and accountability. "
                "In practice, the principles require organizations to collect only what they need, protect the data properly, and be able to show that they follow the rules. "
                "For CyberLex Sweden, these principles are relevant because cybersecurity incidents often involve the protection and handling of personal data."
            )

    elif (
        question_lower.strip() == "gdpr"
        or "what is gdpr" in question_lower
        or "vad är gdpr" in question_lower
    ):
        if use_swedish:
            answer = (
                "GDPR är EU:s dataskyddsförordning. Den reglerar hur personuppgifter får behandlas "
                "och ställer krav på bland annat laglighet, transparens, säkerhet och ansvarsskyldighet. "
                "I Sverige är IMY den ansvariga tillsynsmyndigheten för GDPR och dataskydd."
            )
        else:
            answer = (
                "GDPR is the General Data Protection Regulation, the EU regulation that controls how personal data may be processed and protected. "
                "It sets rules for lawful processing, transparency, data minimisation, security, individual rights, and accountability. "
                "In Sweden, IMY supervises GDPR and personal data protection. "
                "For cybersecurity, GDPR is important because incidents can expose, alter, or destroy personal data and may trigger breach-assessment duties."
            )

    elif "gdpr" in question_lower or "authority" in question_lower:
        if use_swedish:
            answer = (
                "I Sverige är GDPR och dataskydd kopplat till IMY, Integritetsskyddsmyndigheten. "
                "IMY är tillsynsmyndighet för dataskydd och personuppgiftshantering."
            )
        else:
            answer = (
                "In Sweden, GDPR and personal data protection are handled by IMY, Integritetsskyddsmyndigheten, the Swedish Authority for Privacy Protection. "
                "IMY supervises how organizations process and protect personal data. "
                "For cybersecurity questions, this matters because an incident may affect personal data and require a GDPR breach assessment. "
                "CyberLex therefore treats IMY as the main Swedish authority source for GDPR supervision and personal data breach questions."
            )

    elif (
        "nis2" in question_lower
        or "what is nis2" in question_lower
        or "vad är nis2" in question_lower
        or "cybersecurity act" in question_lower
        or "cybersäkerhetslagen" in question_lower
    ):
        if use_swedish:
            answer = (
                "NIS2 är ett EU-direktiv om cybersäkerhet. Syftet är att skapa en hög gemensam nivå "
                "av cybersäkerhet inom EU. I Sverige kopplas NIS2 till cybersäkerhetslagen och krav på "
                "riskhantering, säkerhetsåtgärder och incidentrapportering för berörda organisationer."
            )
        else:
            answer = (
                "NIS2 is an EU cybersecurity directive that aims to raise cybersecurity standards across the European Union. "
                "In Sweden, it is connected to the Swedish Cybersecurity Act. "
                "The rules focus on cybersecurity risk management, security measures, governance, and incident reporting for covered organizations. "
                "Whether a specific organization is covered depends on factors such as sector, size, and role."
            )

    elif (
        "vad är dataintrång" in question_lower
        or "dataintrång" in question_lower
        or "data intrusion" in question_lower
        or "unauthorized access" in question_lower
        or "obehörig åtkomst" in question_lower
    ):
        if use_swedish:
            answer = (
                "Dataintrång är ett brott enligt svensk straffrätt. "
                "Det handlar på en övergripande nivå om obehörig åtkomst till, eller otillåten påverkan på, data eller informationssystem. "
                "Det är därför viktigt att skilja mellan tillåten säkerhetstestning och obehöriga handlingar. "
                "För CyberLex Sweden är dataintrång relevant eftersom cyberincidenter ofta börjar med frågor om åtkomst, behörighet och påverkan på system."
            )
        else:
            answer = (
                "Unauthorized access to an information system may be illegal in Sweden. "
                "In Swedish law, this is commonly connected to the offence called dataintrång, which concerns unauthorized access to, or interference with, data or information systems. "
                "The key point is the difference between authorized security work and activity performed without permission. "
                "For CyberLex Sweden, this topic is relevant when cybersecurity questions involve access, intrusion, or interference with systems."
            )

    elif (
        "attacks against information systems" in question_lower
        or "information systems" in question_lower
        or "eu cybercrime" in question_lower
        or "attacker mot informationssystem" in question_lower
        or "eu cyberbrott" in question_lower
        or "eu-regler om attacker" in question_lower
    ):
        if use_swedish:
            answer = (
                "EU-regler om attacker mot informationssystem handlar om cyberbrott som riktas mot "
                "data och informationssystem. Det kan till exempel handla om olaglig åtkomst, "
                "systemstörningar eller datastörningar."
            )
        else:
            answer = (
                "The EU rules on attacks against information systems are connected to cybercrime. "
                "They cover areas such as illegal access, system interference, data interference, "
                "and cooperation between authorities. This helps explain how cyber attacks against systems "
                "are treated as criminal conduct in Europe."
            )

    elif (
        "cyber resilience act" in question_lower
        or "products with digital elements" in question_lower
        or "product security" in question_lower
        or "vad är cyber resilience act" in question_lower
        or "cyberresiliensakten" in question_lower
        or "produkter med digitala element" in question_lower
        or "produktsäkerhet" in question_lower
    ):
        if use_swedish:
            answer = (
                "Cyber Resilience Act är en EU-förordning om cybersäkerhetskrav för produkter med digitala element. "
                "Den fokuserar bland annat på säker produktdesign, hantering av sårbarheter, uppdateringsansvar och ansvar för aktörer som tillverkar eller tillhandahåller digitala produkter. "
                "Målet är att stärka säkerheten för uppkopplad hårdvara och mjukvara under produktens livscykel. "
                "För CyberLex Sweden är reglerna relevanta när juridiska cybersäkerhetskrav kopplas till produktutveckling, leverantörer och sårbarhetshantering."
            )
        else:
            answer = (
                "The Cyber Resilience Act is an EU regulation about cybersecurity requirements for products with digital elements. "
                "It focuses on secure product design, vulnerability handling, update responsibilities, and cybersecurity obligations for actors involved with digital products. "
                "The goal is to improve the security of connected hardware and software throughout the product lifecycle. "
                "For CyberLex Sweden, it is relevant when legal cybersecurity duties connect to product development, suppliers, and vulnerability management."
            )

    else:
        if use_swedish:
            answer = (
                "CyberLex Sweden hittade en relevant betrodd källa, men prototypen kan ännu inte "
                "generera en detaljerad juridisk förklaring för denna fråga."
            )
        else:
            answer = (
                "CyberLex Sweden found a relevant trusted source section, "
                "but this prototype cannot yet generate a detailed legal explanation for this question."
            )

    official_sources = best_match.get("official_sources", [])

    source_lines = "".join(
        [
            f'<li><a href="{source["url"]}" target="_blank" rel="noopener noreferrer">{source["label"]}</a></li>'
            for source in official_sources
        ]
    )

    if source_lines:
        source_lines = f"<ul>{source_lines}</ul>"

    if not source_lines:
        if use_swedish:
            source_lines = "<p>Ingen officiell källänk är sparad för detta dokument ännu.</p>"
        else:
            source_lines = "<p>No official source URL stored for this document yet.</p>"

    source_date = best_match.get("source_date", "No source date stored.")
    version_notes = best_match.get("version_notes", "No version notes stored.")

    if use_swedish:
        source_date = localize_metadata_value(source_date, language)
        version_notes = localize_metadata_value(version_notes, language)

    if use_swedish:
        short_answer_heading = "CyberLex-sammanfattning"
        citation_heading = "Detaljer om källmatchning"
        matched_file_label = "Matchad kunskapsfil"
        matched_section_label = "Matchad sektion"
        relevance_score_label = "Relevanspoäng"
        source_quality_label = "Källtyp"
        source_freshness_label = "Källaktualitet"
        official_sources_heading = "Officiella källor"
        metadata_heading = "Källmetadata"
        source_date_label = "Källdatum"
        version_notes_label = "Versionsanteckningar"
        limitation_heading = "Viktig begränsning"
        topic_heading = "Identifierat ämne"
        limitation_text = (
            "Detta svar genereras från en förenklad lokal kunskapsbas. "
            "CyberLex Sweden är ett utbildningsprojekt och ger inte juridisk rådgivning."
        )
    else:
        short_answer_heading = "CyberLex summary"
        citation_heading = "Source match details"
        matched_file_label = "Matched knowledge file"
        matched_section_label = "Matched section"
        relevance_score_label = "Relevance score"
        source_quality_label = "Source quality"
        source_freshness_label = "Source freshness"
        official_sources_heading = "Official source links"
        metadata_heading = "Source metadata"
        source_date_label = "Source date"
        version_notes_label = "Version notes"
        limitation_heading = "Important limitation"
        topic_heading = "Detected topic"
        limitation_text = (
            "This answer is generated from a simplified local knowledge base. "
            "CyberLex Sweden is an educational project and does not provide legal advice."
        )
    detected_topic = detect_question_topic(question, language)
    display_best_section = localize_section_name(best_match.get("section", ""), language)
    source_quality = detect_source_quality(best_match["filename"], language)
    source_freshness = detect_source_freshness(best_match["source_date"], language)
    confidence = generate_source_confidence(best_match["score"], language)

    friendly_source_area = get_friendly_source_area_name(best_match.get("filename", ""), language)

    if use_swedish:
        transparency_heading = "Källöversikt"
        source_area_label = "Källområde"
        reviewed_label = "Granskningsstatus"
        reviewed_text = "Källan är lokalt granskad och uppdaterad för CyberLex Sweden."
        last_checked_label = "Senast kontrollerad"
        technical_note = "Tekniska matchningsdetaljer visas eftersom teknisk diagnostik är aktiverad."
    else:
        transparency_heading = "Source overview"
        source_area_label = "Source area"
        reviewed_label = "Review status"
        reviewed_text = "Source reviewed and updated for CyberLex Sweden."
        last_checked_label = "Last checked"
        technical_note = "Technical match details are shown because technical diagnostics is enabled."

    answer_parts = [
        f"## {short_answer_heading}\n\n{answer}",
        (
            f'<div class="topic-card">'
            f'<div class="topic-card-title">{topic_heading}</div>'
            f'<div class="topic-row"><strong>{topic_heading}:</strong> '
            f'<span>{detected_topic}</span></div>'
            f'</div>'
        ),
        (
            f'<div class="source-card">'
            f'<div class="source-card-title">{official_sources_heading}</div>'
            f'{source_lines}'
            f'</div>'
        ),
        (
            f'<div class="metadata-card">'
            f'<div class="metadata-card-title">{transparency_heading}</div>'
            f'<div class="metadata-row"><strong>{source_area_label}:</strong> '
            f'<span>{friendly_source_area}</span></div>'
            f'<div class="metadata-row"><strong>{reviewed_label}:</strong> '
            f'<span>{reviewed_text}</span></div>'
            f'<div class="metadata-row"><strong>{last_checked_label}:</strong> '
            f'<span>{source_date}</span></div>'
            f'</div>'
        ),
    ]

    if include_technical_details:
        answer_parts.append(
            f'<details class="technical-details">'
            f'<summary>{citation_heading}</summary>'
            f'<div class="citation-card">'
            f'<div class="citation-card-title">{citation_heading}</div>'
            f'<div class="citation-note">{technical_note}</div>'
            f'<div class="citation-row"><strong>{matched_file_label}:</strong> '
            f'<span class="citation-code">{best_match["filename"]}</span></div>'
            f'<div class="citation-row"><strong>{matched_section_label}:</strong> '
            f'<span class="citation-code">{display_best_section}</span></div>'
            f'<div class="citation-row"><strong>{source_quality_label}:</strong> '
            f'<span class="citation-code">{source_quality}</span></div>'
            f'<div class="citation-row"><strong>{relevance_score_label}:</strong> '
            f'<span class="citation-code">{best_match["score"]}</span></div>'
            f'<div class="citation-row"><strong>{"Källmatchning" if use_swedish else "Source match confidence"}:</strong> '
            f'<span class="citation-code">{confidence["level"]}</span></div>'
            f'<div class="citation-note">{confidence["reason"]} '
            f'{"Detta är inte juridisk säkerhet. Det beskriver bara hur stark källmatchningen är." if use_swedish else "This is not legal certainty. It only describes how strong the source match is."}</div>'
            f'</div>'
            f'<div class="metadata-card">'
            f'<div class="metadata-card-title">{metadata_heading}</div>'
            f'<div class="metadata-row"><strong>{source_date_label}:</strong> '
            f'<span class="metadata-code">{source_date}</span></div>'
            f'<div class="metadata-row"><strong>{source_freshness_label}:</strong> '
            f'<span class="metadata-code">{source_freshness}</span></div>'
            f'<div class="metadata-row"><strong>{version_notes_label}:</strong> '
            f'<span class="metadata-code">{version_notes}</span></div>'
            f'</div>'
            f'</details>'
        )

    answer_parts.append(
        f'<div class="limitation-card">'
        f'<div class="limitation-card-title">{limitation_heading}</div>'
        f'<div class="limitation-card-text">{limitation_text}</div>'
        f'</div>'
    )

    return "\n\n".join(answer_parts)


def is_cyberlaw_question(question):
    # Checks whether the user question belongs to the CyberLex Sweden project scope.
    allowed_keywords = {
        "vad är",
        "misstänker intrång",
        "misstänker hackning",
        "misstänkt intrång",
        "misstänkt hackning",
        "intrång",
        "hackning",
        "hackad",
        "blivit hackade",
        "hackat vårt system",
        "tagit sig in",
        "dataläcka",
        "läckt data",
        "kunddata har läckt",
        "personinformation har läckt",
        "personuppgifter har läckt",
        "komprometterat konto",
        "komprometterad",
        "säkerhetsincident",
        "cyberincident",
        "it-incident",
        "incidenthantering",
        "isolera",
        "bevara bevis",
        "loggar",
        "cert-se",
        "data leak",
        "data leakage",
        "suspect hacking",
        "suspect intrusion",
        "suspected compromise",
        "compromised account",
        "account compromised",
        "account is compromised",
        "account has been compromised",
        "account may be compromised",
        "account might be compromised",
        "user account is compromised",
        "employee account is compromised",
        "email account is compromised",
        "konto komprometterat",
        "komprometterat konto",
        "konto är komprometterat",
        "ett konto är komprometterat",
        "ett kontör är komprometterat",
        "om ett konto är komprometterat",
        "om ett kontör är komprometterat",
        "kontot är komprometterat",
        "kontot kan vara komprometterat",
        "kontot har komprometterats",
        "användarkonto är komprometterat",
        "account hacked",
        "preserve evidence",
        "isolate",
        "logs",
        "suspicious login",
        "suspicious sign-in",
        "unusual login",
        "unusual sign-in",
        "impossible travel",
        "suspicious login activity",
        "phishing",
        "suspicious email",
        "misstänkt inloggning",
        "misstänkta inloggningar",
        "ovanlig inloggning",
        "ovanliga inloggningar",
        "nätfiske",
        "misstänkt mejl",
        "misstänkt e-post",
        "misstänkt länk",
        "skadlig länk",
        "okänd länk",
        "suspicious link",
        "malicious link",
        "clicked a suspicious link",
        "someone clicked a suspicious link",
        "someone clicked a link",
        "someone clicked a link on a website",
        "clicked a link on a website",
        "clicked a link in sms",
        "någon klickade på en länk",
        "någon klickade på en länk på en webbsida",
        "klickade på en länk på en webbsida",
        "klickade på en länk i sms",
        "klickat på en länk i sms",
        "länk på en webbsida",
        "länk i sms",
        "länk i chatt",
        "qr-kod",
        "klickade på en misstänkt länk",
        "svensk cybersäkerhetsrätt",
        "cybersäkerhet",
        "cyberbrott",
        "ransomware",
        "malware",
        "krypterats",
        "våra filer",
        "cyber attack",
        "cyberattack",
        "security incident",
        "incident response",
        "data breach",
        "dataskydd",
        "personuppgift",
        "personuppgifter",
        "personuppgiftsincident",
        "rapporteras",
        "anmälas",
        "incidentrapportering",
        "dataintrång",
        "obehörig åtkomst",
        "integritetsskyddsmyndigheten",
        "myndighet",
        "tillsyn",
        "dora",
        "digital operativ motståndskraft",
        "finansiell sektor",
        "tredjepartsrisk",
        "ict-risk",
        "digital operational resilience",
        "digital operational resilience act",
        "ict risk",
        "ict incident",
        "ict third-party",
        "third-party ict",
        "financial sector cybersecurity",
        "financial sector cyber",
        "cyber",
        "cybersecurity",
        "security",
        "gdpr",
        "personal",
        "data",
        "breach",
        "incident",
        "nis2",
        "cybersecurity act",
        "cybersäkerhetslagen",
        "intrusion",
        "unauthorized",
        "access",
        "hacking",
        "malware",
        "privacy",
        "imy",
        "msb",
        "information system",
        "information systems",
        "digital",
        "compliance",
        "cyber resilience",
        "cyber resilience act",
        "products with digital elements",
        "product security",
        "eu cybercrime",
        "legal basis",
        "controller",
        "processor",
        "accountability",
        "principles"
    }

    question_lower = normalize_query_text(question)

    # Let the dedicated incident detectors mark practical incident questions as in scope.
    # Otherwise small word-order differences in Swedish can be refused before search starts.
    if (
        is_nis2_sector_scope_question(question_lower)
        or is_gdpr_security_guidance_question(question_lower)
        or is_practical_incident_response_question(question_lower)
        or is_compromised_account_question(question_lower)
        or is_suspicious_login_question(question_lower)
        or is_suspicious_email_question(question_lower)
        or is_suspicious_link_question(question_lower)
        or is_data_leak_response_question(question_lower)
        or is_ransomware_response_question(question_lower)
    ):
        return True

    for keyword in allowed_keywords:
        if keyword in question_lower:
            return True

    return False


st.markdown(
    '''
    <style>
    .main-header {
        padding: 1.5rem;
        border-radius: 16px;
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
        margin-bottom: 1.5rem;
    }

    .main-header h1 {
        margin-bottom: 0.2rem;
        font-size: 2.4rem;
    }

    .main-header p {
        font-size: 1.05rem;
        color: #cbd5e1;
    }

    .info-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #1e293b;
        color: #e2e8f0;
        margin-bottom: 1rem;
    }

    .info-card strong {
        color: #ffffff;
    }

    .topic-badge {
        display: inline-block;
        padding: 0.35rem 0.65rem;
        margin: 0.2rem;
        border-radius: 999px;
        background-color: #e2e8f0;
        color: #0f172a;
        font-size: 0.9rem;
    }

    .small-muted {
        color: #64748b;
        font-size: 0.95rem;
    }

    .attention-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #475569;
        background-color: #111827;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .attention-card strong {
        color: #ffffff;
    }

    .attention-level-high {
        border-left: 6px solid #ef4444;
    }

    .attention-level-elevated {
        border-left: 6px solid #f59e0b;
    }

    .attention-level-standard {
        border-left: 6px solid #38bdf8;
    }

    .attention-level-informational {
        border-left: 6px solid #22c55e;
    }

    .attention-level-medium {
        border-left: 6px solid #f59e0b;
    }

    .attention-level-normal {
        border-left: 6px solid #22c55e;
    }

    .attention-label {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .attention-reason {
        color: #d1d5db;
        margin-bottom: 0.4rem;
    }

    .attention-limitation {
        color: #9ca3af;
        font-size: 0.9rem;
        font-style: italic;
    }

    .citation-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .citation-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

    .citation-row {
        margin-bottom: 0.45rem;
        color: #d1d5db;
    }

    .citation-row strong {
        color: #ffffff;
    }

    .citation-code {
        background-color: #111827;
        color: #86efac;
        padding: 0.15rem 0.35rem;
        border-radius: 6px;
        font-family: monospace;
        font-size: 0.9rem;
    }

        .citation-note {
        color: #9ca3af;
        font-size: 0.9rem;
        font-style: italic;
        margin-top: 0.75rem;
    }

        .topic-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #2563eb;
        background: linear-gradient(135deg, #0f172a, #111827);
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .topic-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

    .topic-row {
        margin-bottom: 0.45rem;
        color: #d1d5db;
    }

    .topic-row strong {
        color: #ffffff;
    }

    .topic-code {
        color: #93c5fd;
        font-family: monospace;
        font-weight: 600;
    }

    .metadata-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .metadata-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

    .metadata-row {
        margin-bottom: 0.45rem;
        color: #d1d5db;
    }

    .metadata-row strong {
        color: #ffffff;
    }

        .metadata-code {
        background-color: #111827;
        color: #93c5fd;
        padding: 0.15rem 0.35rem;
        border-radius: 6px;
        font-family: monospace;
        font-size: 0.9rem;
    }

    .source-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .source-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

    .source-card ul {
        margin-bottom: 0;
    }

        .source-card li {
        margin-bottom: 0.35rem;
    }

    .limitation-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #854d0e;
        background-color: #1c1917;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .limitation-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

        .limitation-card-text {
        color: #fef3c7;
        font-size: 0.95rem;
    }

    .practical-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .practical-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

        .practical-card-text {
        color: #d1d5db;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    .incident-log-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .incident-log-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }

    .incident-log-card-text {
        color: #d1d5db;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 0.75rem;
    }

    .incident-log-template {
        background-color: #111827;
        color: #e5e7eb;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 0.85rem;
        white-space: pre-wrap;
        font-family: monospace;
        font-size: 0.9rem;
        line-height: 1.55;
    }

    .checklist-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .checklist-card ul {
        margin-bottom: 0;
        padding-left: 1.25rem;
    }

        .checklist-card li {
        color: #d1d5db;
        margin-bottom: 0.45rem;
        line-height: 1.5;
    }

    .context-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 0.75rem;
        margin-bottom: 0.75rem;
    }

    .context-card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

    .context-row {
        margin-bottom: 0.45rem;
        color: #d1d5db;
    }

    .context-row strong {
        color: #ffffff;
    }

    .context-code {
        background-color: #111827;
        color: #86efac;
        padding: 0.15rem 0.35rem;
        border-radius: 6px;
        font-family: monospace;
        font-size: 0.9rem;
    }

    .context-excerpt-label {
        font-weight: 700;
        color: #ffffff;
        margin-top: 0.75rem;
        margin-bottom: 0.35rem;
    }

        .context-excerpt {
        color: #d1d5db;
        line-height: 1.45;
        white-space: pre-line;
    }

    .context-shortened-note {
        color: #9ca3af;
        font-size: 0.9rem;
        font-style: italic;
        margin-top: 0.55rem;
        margin-bottom: 0.35rem;
    }

    .context-more-details {
        margin-top: 0.35rem;
    }

    .context-more-details summary {
        color: #93c5fd;
        cursor: pointer;
        font-weight: 600;
        margin-bottom: 0.45rem;
    }

    .context-more-details summary .details-less-label {
        display: none;
    }

    .context-more-details[open] summary .details-more-label {
        display: none;
    }

    .context-more-details[open] summary .details-less-label {
        display: inline;
    }

    .context-full-excerpt {
        margin-top: 0.5rem;
        padding-top: 0.65rem;
        border-top: 1px solid #334155;
    }

    .match-card {
        padding: 0.85rem;
        border-radius: 10px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .match-card strong {
        color: #ffffff;
    }

    .match-code {
        background-color: #111827;
        color: #86efac;
        padding: 0.15rem 0.35rem;
        border-radius: 6px;
        font-family: monospace;
        font-size: 0.9rem;
    }
    
.technical-details {
    margin: 0.85rem 0 1rem 0;
    padding: 0.85rem 1rem;
    border: 1px solid rgba(148, 163, 184, 0.28);
    border-radius: 0.75rem;
    background: rgba(15, 23, 42, 0.35);
}
.technical-details summary {
    cursor: pointer;
    font-weight: 700;
}
.technical-details .citation-card,
.technical-details .metadata-card {
    margin-top: 0.75rem;
}

    .main-header.compact-hero {
        padding: 1.6rem 2rem;
        margin-top: 0.25rem;
        margin-bottom: 1.25rem;
    }

    .hero-label {
        margin-top: 1rem;
        font-size: 0.95rem;
        font-weight: 700;
        color: #ffffff;
    }

    .hero-description {
        margin-top: 0.15rem;
        color: #cbd5e1;
        font-size: 0.98rem;
        line-height: 1.5;
    }

    .topic-area-wrapper {
        margin-top: 1.25rem;
        margin-bottom: 0.75rem;
    }

    .topic-area-heading {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .ask-heading {
        font-size: 1.55rem;
        font-weight: 700;
        line-height: 1.2;
        margin-top: 1.25rem;
        margin-bottom: 0.65rem;
    }

    .footer-note {
        text-align: center;
        color: #94a3b8;
        font-size: 0.85rem;
        padding: 1.25rem 0 0.5rem 0;
        border-top: 1px solid rgba(148, 163, 184, 0.2);
        margin-top: 7.5rem;
        margin-bottom: 1rem;
    }

    .footer-note a {
        color: #93c5fd;
        text-decoration: none;
    }

    .footer-note a:hover {
        text-decoration: underline;
    }

    /* Cleaner first impression for portfolio/demo use. */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 980px;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.05), rgba(15, 23, 42, 0.12));
    }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.65rem;
    }

    /* Hide Streamlit's demo/deploy toolbar for a cleaner user-facing prototype. */
    #MainMenu,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        visibility: hidden;
        height: 0;
    }

    .main-header.compact-hero {
        padding: 1.85rem 2rem;
        margin-top: 0;
        margin-bottom: 1rem;
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.18);
    }

    .main-header.compact-hero h1 {
        font-size: 2.30rem;
        letter-spacing: -0.035em;
        line-height: 1.08;
    }

    .main-header.compact-hero p {
        max-width: 760px;
        margin-bottom: 0.85rem;
    }

    .hero-description {
        max-width: 820px;
    }

    .sidebar-status-card {
        padding: 0.85rem 0.9rem;
        border-radius: 12px;
        border: 1px solid rgba(148, 163, 184, 0.28);
        background: rgba(15, 23, 42, 0.08);
        margin-top: 0.4rem;
        margin-bottom: 0.55rem;
    }

    .sidebar-status-title {
        font-size: 1rem;
        font-weight: 750;
        margin-bottom: 0.5rem;
    }

    .sidebar-status-line {
        font-size: 0.88rem;
        margin-bottom: 0.25rem;
        color: inherit;
    }

    .sidebar-info-card {
        padding: 0.85rem 0.9rem;
        border-radius: 12px;
        border: 1px solid rgba(59, 130, 246, 0.28);
        background: rgba(59, 130, 246, 0.12);
        margin-top: 0.55rem;
        margin-bottom: 0.55rem;
        font-size: 0.9rem;
        line-height: 1.45;
    }

    .disclaimer-strip {
        margin-top: 0.85rem;
        margin-bottom: 0.85rem;
        padding: 0.75rem 0.9rem;
        border-radius: 12px;
        border: 1px solid rgba(245, 158, 11, 0.35);
        background: rgba(245, 158, 11, 0.12);
        color: inherit;
        font-size: 0.92rem;
        line-height: 1.45;
    }

    .stTextInput input {
        border-radius: 10px;
    }

</style>
    ''',
    unsafe_allow_html=True
)

# Main page text is controlled by the selected language mode.
# In Auto mode, the page starts in English until a question is typed.

language_mode_preview = st.sidebar.selectbox(
    "Language / Språk",
    ["Auto", "English", "Svenska"],
    key="language_selector"
)

diagnostics_label = (
    "Visa teknisk diagnostik"
    if language_mode_preview == "Svenska"
    else "Show technical diagnostics"
)

diagnostics_help = (
    "Visar interna källfiler, matchade sektioner och relevanspoäng. "
    "Använd detta för test och utveckling, inte för vanlig användardemo."
    if language_mode_preview == "Svenska"
    else "Shows internal source files, matched sections, and relevance scores. "
    "Use this for testing and development, not for normal user demos."
)

show_technical_diagnostics = st.sidebar.checkbox(
    diagnostics_label,
    value=False,
    key="show_technical_diagnostics",
    help=diagnostics_help,
)


def detect_question_language_preview(question):
    # Lightweight detector used before the main page is rendered.
    # Auto mode should follow Swedish grammar even when the user uses English cyber terms.
    return detect_ui_language_from_question(question)


preview_question = (
    st.session_state.get("main_question_input", "")
    or st.session_state.get("selected_example_question", "")
)

if language_mode_preview == "Auto" and preview_question:
    page_language_preview = detect_question_language_preview(preview_question)
else:
    page_language_preview = language_mode_preview

if page_language_preview == "Svenska":
    page_subtitle = (
        "Källbaserad assistent för svensk och EU-relaterad cybersäkerhetsrätt, "
        "digital compliance och legal-tech research."
    )
    info_card_heading = "Vad CyberLex gör:"
    info_card_text = (
        "CyberLex Sweden söker i en betrodd lokal kunskapsbas och ger källbaserade svar med "
        "källhänvisningar, officiella källänkar, källmetadata och matchade källutdrag."
    )
    supported_topics_heading = "Stödda ämnesområden"
    warning_text = (
        "Viktigt: CyberLex Sweden är ett utbildningsprojekt. "
        "Det ger inte officiell juridisk rådgivning och ska inte ersätta en kvalificerad jurist "
        "eller vägledning från en myndighet."
    )
    topic_badges = [
        "GDPR",
        "IMY",
        "Personuppgiftsincidenter",
        "Incidenthantering",
        "Misstänkt intrång",
        "Dataläcka",
        "Komprometterat konto",
        "NIS2",
        "Svenska cybersäkerhetslagen",
        "Dataintrång",
        "EU Cyber Resilience Act",
        "DORA",
        "Digital compliance"
    ]
else:
    page_subtitle = (
        "Source-grounded assistant for Swedish and EU cybersecurity law, "
        "digital compliance, and legal-tech research."
    )
    info_card_heading = "What CyberLex does:"
    info_card_text = (
        "CyberLex Sweden searches a trusted local knowledge base and gives source-based answers with "
        "citation details, official source links, source metadata, and matched source excerpts."
    )
    supported_topics_heading = "Supported topic areas"
    warning_text = (
        "Important: CyberLex Sweden is an educational project. "
        "It does not provide official legal advice and should not replace a qualified lawyer "
        "or official authority guidance."
    )
    topic_badges = [
        "GDPR",
        "IMY",
        "Personal data breaches",
        "Incident response",
        "Suspected hacking",
        "Data leaks",
        "Compromised accounts",
        "NIS2",
        "Swedish Cybersecurity Act",
        "Unauthorized access",
        "EU Cyber Resilience Act",
        "DORA",
        "Digital compliance"
    ]

st.markdown(
    f'''
    <div class="main-header compact-hero">
        <h1>CyberLex Sweden</h1>
        <p>{page_subtitle}</p>
        <div class="hero-label">{info_card_heading}</div>
        <div class="hero-description">{info_card_text}</div>
    </div>
    ''',
    unsafe_allow_html=True
)

badge_html = "".join(
    [f'<span class="topic-badge">{topic}</span>' for topic in topic_badges]
)




def extract_case_title(content, fallback):
    # Extracts the visible title from a case Markdown file.
    for line in str(content or "").splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped.replace("# ", "", 1).strip()

    return str(fallback or "Untitled case").replace("_", " ").title()


def load_case_library_entries():
    # Loads case-library Markdown files for the browseable Case Intelligence page.
    # Template and index files are excluded because they are not actual cases.
    #
    # English sections are the default source of truth.
    # Swedish sections are optional. If a Swedish section is missing, CyberLex
    # falls back to the English version so older case files still work.
    ignored_files = {"CASE_TEMPLATE.md", "CASE_INDEX.md"}
    cases = []

    if not CASES_DIR.exists():
        return cases

    for path in sorted(CASES_DIR.glob("*.md")):
        if path.name in ignored_files:
            continue

        content = path.read_text(encoding="utf-8")

        english_summary = extract_section_text(content, "## Short summary")
        swedish_summary = extract_section_text(content, "## Swedish short summary")

        english_fine_or_cost = extract_section_text(content, "## Fine or cost")
        swedish_fine_or_cost = extract_section_text(content, "## Swedish fine or cost")

        english_related_topics = extract_section_text(content, "## Related CyberLex topics")
        swedish_related_topics = extract_section_text(content, "## Swedish related CyberLex topics")

        english_official_source = extract_section_text(content, "## Official source")
        swedish_official_source = extract_section_text(content, "## Swedish official source")

        english_what_happened = extract_section_text(content, "## What happened")
        swedish_what_happened = extract_section_text(content, "## Swedish what happened")

        english_decision = extract_section_text(content, "## Decision or outcome")
        swedish_decision = extract_section_text(content, "## Swedish decision or outcome")

        cases.append(
            {
                "title": extract_case_title(content, path.stem),
                "summary": english_summary,
                "summary_sv": swedish_summary or english_summary,
                "fine_or_cost": english_fine_or_cost,
                "fine_or_cost_sv": swedish_fine_or_cost or english_fine_or_cost,
                "related_topics": english_related_topics,
                "related_topics_sv": swedish_related_topics or english_related_topics,
                "what_happened": english_what_happened,
                "what_happened_sv": swedish_what_happened or english_what_happened,
                "decision": english_decision,
                "decision_sv": swedish_decision or english_decision,
                "official_source": english_official_source,
                "official_source_sv": swedish_official_source or english_official_source,
            }
        )

    return cases

def case_library_plain_html(text):
    # Converts simple Markdown-ish case text into safe HTML for the sidebar cards.
    # Yes, this exists because raw Markdown in Streamlit sidebars can look like it
    # was formatted by a sleepy toaster.
    cleaned = str(text or "").strip()

    if not cleaned:
        return ""

    cleaned = re.sub(r"```[a-zA-Z0-9_-]*", "", cleaned)
    cleaned = cleaned.replace("```", "")
    cleaned = re.sub(r"`([^`]*)`", r"\1", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    return html.escape(cleaned)


def case_library_links_html(markdown_text):
    # Converts Markdown links and bullet links into sidebar-friendly HTML links.
    text = str(markdown_text or "").strip()

    if not text:
        return ""

    lines = []
    link_pattern = re.compile(r"\[([^\]]+)\]\((https?://[^\)]+)\)")

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        line = line.lstrip("-* ").strip()
        match = link_pattern.search(line)

        if match:
            label = html.escape(match.group(1).strip())
            url = html.escape(match.group(2).strip(), quote=True)
            lines.append(
                f'<li><a href="{url}" target="_blank" rel="noopener noreferrer">{label}</a></li>'
            )
            continue

        if line.startswith("http://") or line.startswith("https://"):
            safe_url = html.escape(line, quote=True)
            lines.append(
                f'<li><a href="{safe_url}" target="_blank" rel="noopener noreferrer">{safe_url}</a></li>'
            )
            continue

        lines.append(f"<li>{html.escape(line)}</li>")

    if not lines:
        return ""

    return "<ul>" + "".join(lines) + "</ul>"


def case_library_topics_html(topics_text):
    # Turns the topic list into compact SOC-style tags.
    text = str(topics_text or "").strip()

    if not text:
        return ""

    topics = []

    for raw_line in text.splitlines():
        line = raw_line.strip().lstrip("-* ").strip()
        if line:
            topics.append(line)

    if not topics:
        return ""

    tags = "".join(
        f'<span class="case-intel-tag">{html.escape(topic)}</span>'
        for topic in topics
    )

    return f'<div class="case-intel-tags">{tags}</div>'


def clean_case_markdown_for_display(text):
    # Cleans case-library Markdown before displaying it in the main UI.
    # It removes accidental code-fence artifacts while keeping normal Markdown
    # such as bullets and links usable.
    cleaned = str(text or "").strip()

    if not cleaned:
        return ""

    cleaned = re.sub(r"```[a-zA-Z0-9_-]*", "", cleaned)
    cleaned = cleaned.replace("```", "")
    cleaned = re.sub(r"\btext\b", "", cleaned)
    cleaned = re.sub(r'id="[^"]+"', "", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()

    return cleaned


def case_topics_to_badges(topics_text):
    # Turns Related CyberLex topics into compact blue-team style badges.
    topics = []

    for raw_line in str(topics_text or "").splitlines():
        line = raw_line.strip().lstrip("-* ").strip()

        if line:
            topics.append(line)

    if not topics:
        return ""

    badges = "".join(
        f'<span class="case-topic-badge">{html.escape(topic)}</span>'
        for topic in topics
    )

    return f'<div class="case-topic-badge-row">{badges}</div>'




def looks_like_swedish_source_line(line):
    # Heuristic used when older case files have Swedish and English links mixed
    # inside the same "## Official source" section.
    # Prefer explicit "## Swedish official source" sections when available,
    # but this keeps the current case files usable without another migration ritual.
    text = str(line or "").lower()

    swedish_markers = [
        "imy.se/nyheter/",
        "imy.se/tillsyner/",
        "sanktionsavgift",
        "sanktionsavgifter",
        "tillsyn",
        "gällande",
        "överföring",
        "personuppgifter",
        "bristande",
        "säkerhet",
        "bolag som skickat",
        "är det förbjudet",
        "kunduppgifter",
    ]

    if any(marker in text for marker in swedish_markers):
        return True

    return any(letter in text for letter in "åäö")


def looks_like_english_source_line(line):
    # Heuristic used when older case files have Swedish and English links mixed
    # inside the same "## Official source" section.
    text = str(line or "").lower()

    english_markers = [
        "/en/",
        "edpb.europa.eu",
        "administrative fine",
        "administrative fines",
        "english translation",
        "transferring customer data",
        "transferring personal data",
        "security deficiencies",
        "has for an incident",
        "against sportadmin",
        "collected via a web form",
    ]

    return any(marker in text for marker in english_markers)


def filter_official_source_links(markdown_text, target_language="Auto"):
    # Filters Markdown source links for explicit English or Swedish language mode.
    # Auto mode returns all links.
    mode = str(target_language or "Auto")
    text = str(markdown_text or "").strip()

    if not text or mode == "Auto":
        return text

    kept_lines = []

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        is_swedish = looks_like_swedish_source_line(line)
        is_english = looks_like_english_source_line(line)

        if mode == "Svenska":
            if is_swedish or (not is_english and not is_swedish):
                kept_lines.append(raw_line)
        elif mode == "English":
            if is_english or (not is_english and not is_swedish):
                kept_lines.append(raw_line)

    return "\n".join(kept_lines).strip()


def select_case_official_source(case, source_language_mode="Auto"):
    # Selects official case sources according to the language selector:
    # - Auto: show all available official source links
    # - English: prefer English links
    # - Svenska: prefer Swedish links
    #
    # Important: some case files only have one official source language stored.
    # If strict filtering finds nothing, CyberLex falls back to available official
    # sources instead of showing an empty source section. Empty source sections are
    # not transparency. They are just a tiny bureaucracy wearing a crash helmet.
    mode = str(source_language_mode or "Auto")
    english_source = str(case.get("official_source", "") or "").strip()
    swedish_source_raw = str(case.get("official_source_sv", "") or "").strip()

    # Treat official_source_sv as a real Swedish section only when it is different
    # from the English source. Older cases may mirror English into _sv as fallback.
    has_real_swedish_section = bool(swedish_source_raw and swedish_source_raw != english_source)

    if mode == "Auto":
        combined_parts = []
        if english_source:
            combined_parts.append(english_source)
        if has_real_swedish_section:
            combined_parts.append(swedish_source_raw)
        return "\n".join(combined_parts).strip()

    if mode == "Svenska":
        # Prefer an explicit Swedish source section when the case file has one.
        if has_real_swedish_section:
            return swedish_source_raw

        # Otherwise filter mixed links from the normal Official source section.
        swedish_filtered = filter_official_source_links(english_source, "Svenska")
        if swedish_filtered:
            return swedish_filtered

        # Last-resort fallback: show available sources rather than hiding all links.
        # This happens when the case currently only stores English/EDPB sources.
        return english_source

    if mode == "English":
        english_filtered = filter_official_source_links(english_source, "English")
        if english_filtered:
            return english_filtered

        # If an English source section is missing but Swedish links exist, keep the
        # source visible. The user can still verify the case instead of staring at
        # an empty box like a punished servitor.
        return english_source or swedish_source_raw

    return english_source

def display_case_intelligence_page(language="English", source_language_mode="Auto"):
    # Full Case Intelligence page inside main.py.
    # We keep this in the same file for now so CyberLex does not instantly turn
    # into eight files and a small municipal bureaucracy.
    cases = load_case_library_entries()
    use_swedish = language == "Svenska"

    if use_swedish:
        page_title = "Case Intelligence"
        page_subtitle = "Cyberrelaterade sanktionsavgifter och myndighetsbeslut"
        page_intro = (
            "Här kan du bläddra bland myndighetsbeslut och fall som CyberLex använder "
            "som utbildande referenser. Fallen används för att visa hur liknande "
            "cyber-, GDPR- och dataskyddsfrågor har bedömts i praktiken."
        )
        search_label = "Filtrera fall"
        search_placeholder = "Sök på t.ex. Meta Pixel, säkerhet, e-post, dataläcka..."
        count_label = "fall i biblioteket"
        shown_label = "visade fall"
        summary_label = "Sammanfattning"
        outcome_label = "Sanktionsavgift eller utfall"
        topics_label = "Relaterade CyberLex-ämnen"
        source_label = "Officiella källor"
        no_result_text = "Inga fall matchade filtret."
        empty_label = "Ingen information lagrad i denna sektion ännu."
        disclaimer_title = "Viktig begränsning"
        disclaimer_text = (
            "Belopp och utfall är historiska exempel. CyberLex förutspår inte böter, "
            "skadestånd eller rättsliga resultat för nya incidenter."
        )
    else:
        page_title = "Case Intelligence"
        page_subtitle = "Cyber-related fines and authority decisions"
        page_intro = (
            "Browse authority decisions and case examples used by CyberLex as educational "
            "references. These cases help show how similar cyber, GDPR, and data-protection "
            "issues have been assessed in practice."
        )
        search_label = "Filter cases"
        search_placeholder = "Search for Meta Pixel, security, email, data leak..."
        count_label = "cases in library"
        shown_label = "shown cases"
        summary_label = "Summary"
        outcome_label = "Administrative fine or outcome"
        topics_label = "Related CyberLex topics"
        source_label = "Official sources"
        no_result_text = "No cases matched the filter."
        empty_label = "No information is stored in this section yet."
        disclaimer_title = "Important limitation"
        disclaimer_text = (
            "Amounts and outcomes are historical examples. CyberLex does not predict fines, "
            "damages, or legal outcomes for new incidents."
        )

    st.markdown(
        """
        <style>
            .case-page-hero {
                border: 1px solid rgba(96, 165, 250, 0.42);
                border-left: 5px solid #60a5fa;
                border-radius: 18px;
                padding: 1.15rem 1.25rem;
                background: linear-gradient(135deg, rgba(30, 64, 175, 0.26), rgba(15, 23, 42, 0.72));
                margin: 0.35rem 0 1.2rem 0;
                box-shadow: 0 10px 30px rgba(15, 23, 42, 0.18);
            }

            .case-page-kicker {
                color: #93c5fd;
                font-size: 0.78rem;
                font-weight: 850;
                text-transform: uppercase;
                letter-spacing: 0.07em;
                margin-bottom: 0.35rem;
            }

            .case-page-title {
                color: #f8fafc;
                font-size: 2.05rem;
                font-weight: 850;
                line-height: 1.15;
                margin-bottom: 0.3rem;
            }

            .case-page-intro {
                color: #d1d5db;
                font-size: 0.98rem;
                line-height: 1.6;
                max-width: 900px;
            }

            .case-page-stat-row {
                display: flex;
                gap: 0.65rem;
                flex-wrap: wrap;
                margin: 0.7rem 0 1rem 0;
            }

            .case-page-stat {
                display: inline-flex;
                align-items: center;
                border: 1px solid rgba(96, 165, 250, 0.32);
                background: rgba(59, 130, 246, 0.14);
                color: #dbeafe;
                border-radius: 999px;
                padding: 0.32rem 0.75rem;
                font-size: 0.82rem;
                font-weight: 750;
            }

            .case-topic-badge-row {
                display: flex;
                flex-wrap: wrap;
                gap: 0.35rem;
                margin-top: 0.25rem;
            }

            .case-topic-badge {
                border: 1px solid rgba(96, 165, 250, 0.28);
                background: rgba(59, 130, 246, 0.13);
                color: #dbeafe;
                border-radius: 999px;
                padding: 0.18rem 0.55rem;
                font-size: 0.76rem;
                font-weight: 700;
            }

            .case-page-warning {
                border: 1px solid rgba(245, 158, 11, 0.32);
                border-radius: 14px;
                background: rgba(245, 158, 11, 0.11);
                padding: 0.85rem 1rem;
                margin: 1.1rem 0;
                color: #f8fafc;
                line-height: 1.5;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="case-page-hero">
            <div class="case-page-kicker">🛡️ {page_title}</div>
            <div class="case-page-title">{page_subtitle}</div>
            <div class="case-page-intro">{page_intro}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    filter_text = st.text_input(
        search_label,
        placeholder=search_placeholder,
        key="case_intelligence_filter",
    ).strip()

    normalized_filter = normalize_query_text(filter_text)

    if normalized_filter:
        filtered_cases = []

        for case in cases:
            haystack = normalize_query_text(
                " ".join(
                    [
                        case.get("title", ""),
                        case.get("summary", ""),
                        case.get("summary_sv", ""),
                        case.get("fine_or_cost", ""),
                        case.get("fine_or_cost_sv", ""),
                        case.get("related_topics", ""),
                        case.get("related_topics_sv", ""),
                        case.get("what_happened", ""),
                        case.get("what_happened_sv", ""),
                        case.get("decision", ""),
                        case.get("decision_sv", ""),
                        case.get("official_source", ""),
                        case.get("official_source_sv", ""),
                    ]
                )
            )

            if normalized_filter in haystack:
                filtered_cases.append(case)
    else:
        filtered_cases = cases

    st.markdown(
        f"""
        <div class="case-page-stat-row">
            <div class="case-page-stat">● {len(cases)} {count_label}</div>
            <div class="case-page-stat">◆ {len(filtered_cases)} {shown_label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="case-page-warning">
            <strong>{disclaimer_title}:</strong> {disclaimer_text}
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not filtered_cases:
        st.info(no_result_text)
        return

    for case in filtered_cases:
        case_title = case.get("title", "Untitled case")

        if use_swedish:
            summary = clean_case_markdown_for_display(case.get("summary_sv", ""))
            fine_or_cost = clean_case_markdown_for_display(case.get("fine_or_cost_sv", ""))
            related_topics = str(case.get("related_topics_sv", "")).strip()
        else:
            summary = clean_case_markdown_for_display(case.get("summary", ""))
            fine_or_cost = clean_case_markdown_for_display(case.get("fine_or_cost", ""))
            related_topics = str(case.get("related_topics", "")).strip()

        official_source = clean_case_markdown_for_display(
            select_case_official_source(case, source_language_mode)
        )

        with st.expander(f"🧾 {case_title}", expanded=False):
            st.markdown(f"**{summary_label}:**")
            st.markdown(summary if summary else empty_label)

            st.markdown(f"**{outcome_label}:**")
            st.markdown(fine_or_cost if fine_or_cost else empty_label)

            st.markdown(f"**{topics_label}:**")
            topics_badges = case_topics_to_badges(related_topics)

            if topics_badges:
                st.markdown(topics_badges, unsafe_allow_html=True)
            else:
                st.markdown(empty_label)

            st.markdown(f"**{source_label}:**")
            st.markdown(official_source if official_source else empty_label)

def should_show_risk_cost_context(question):
    # Decides whether CyberLex should show the educational risk/cost context card.
    # This is not a fine calculator. It only gives common cost categories and
    # historical examples from related authority decisions.
    q = normalize_query_text(question)

    risk_cost_terms = [
        "cost",
        "costs",
        "fine",
        "fines",
        "administrative fine",
        "penalty",
        "penalties",
        "risk",
        "risks",
        "what can it cost",
        "what can this cost",
        "what can weak security measures cost",
        "what can a gdpr breach cost",
        "gdpr fine",
        "gdpr fines",
        "meta pixel",
        "metapixel",
        "web form",
        "tracking",
        "analytics",
        "data leak",
        "personal data breach",
        "weak security",
        "security measures",
        "sanktionsavgift",
        "sanktionsavgifter",
        "böter",
        "vite",
        "kostnad",
        "kostnader",
        "kosta",
        "vad kan det kosta",
        "vad kan en gdpr-läcka kosta",
        "vad kan svaga säkerhetsåtgärder kosta",
        "risk",
        "risker",
        "webbformulär",
        "webbform",
        "spårning",
        "analysverktyg",
        "dataläcka",
        "personuppgiftsincident",
        "svaga säkerhetsåtgärder",
        "säkerhetsåtgärder",
    ]

    return contains_any(q, risk_cost_terms)


def get_short_fine_example_text(fine_text):
    # Extracts only the useful SEK amount lines from a case fine section.
    # This keeps the risk/cost card clean and avoids showing Markdown code-fence
    # artifacts from the source Markdown files.
    text = str(fine_text or "")

    if not text.strip():
        return ""

    cleaned_lines = []

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        # Remove Markdown code fences and accidental code-block metadata.
        if line.startswith("```"):
            continue

        line = line.replace("`", "")
        line = re.sub(r"\btext\b", "", line).strip()
        line = re.sub(r"id=\"[^\"]+\"", "", line).strip()

        lower_line = line.lower()

        # Skip explanatory warning text. The shared disclaimer already covers this.
        skip_markers = [
            "cyberlex should not",
            "fine amounts are",
            "the fine amount is",
            "amounts from related",
            "beloppen i relaterade",
            "ska inte användas",
            "historical examples",
            "prediction",
            "prognos",
        ]

        if any(marker in lower_line for marker in skip_markers):
            continue

        if "sek" in lower_line:
            line = re.sub(r"\s+", " ", line).strip()
            line = line.replace("Official fine:", "").replace("Official fines:", "")
            line = line.replace("Officiell sanktionsavgift:", "")
            line = line.strip(" -:;")

            if line:
                cleaned_lines.append(line)

    if cleaned_lines:
        result = "; ".join(cleaned_lines[:3])
    else:
        # Fallback: extract raw SEK amounts if the line-based cleanup found none.
        amounts = re.findall(r"SEK\s*[0-9][0-9, ]*", text, flags=re.IGNORECASE)
        result = "; ".join(amounts[:3])

    result = re.sub(r"\s+", " ", result).strip()

    if len(result) > 180:
        result = result[:180].rsplit(" ", 1)[0] + "..."

    return result


def display_risk_cost_context(question, language="English"):
    if not should_show_risk_cost_context(question):
        return

    related_cases = search_related_cases(question, limit=3)
    use_swedish = language == "Svenska"

    if use_swedish:
        heading = "Risk- och kostnadskontext"
        intro = (
            "CyberLex förutspår inte böter, skadestånd eller rättsliga resultat. "
            "Detta är en utbildande riskbild baserad på vanliga kostnadskategorier "
            "och historiska exempel från relaterade myndighetsbeslut."
        )
        categories_title = "Möjliga kostnadskategorier"
        categories = [
            "teknisk incidenthantering och felsökning",
            "forensisk analys och logggranskning",
            "juridisk och dataskyddsrättslig bedömning",
            "dokumentation, intern rapportering och beslutsunderlag",
            "eventuell anmälan till IMY eller annan myndighet",
            "information till berörda personer om risken är hög",
            "säkerhetsförbättringar, processändringar och tekniska åtgärder",
            "ryktesrisk, förtroendeskada och verksamhetspåverkan",
            "möjlig sanktionsavgift beroende på omständigheterna",
        ]
        examples_title = "Historiska exempel från relaterade fall"
        no_examples = "Inga relaterade fall med kostnadsexempel hittades."
        disclaimer = (
            "Beloppen i relaterade fall är historiska exempel. De ska inte användas "
            "som prognos för nya incidenter."
        )
    else:
        heading = "Risk and cost context"
        intro = (
            "CyberLex does not predict fines, damages, or legal outcomes. "
            "This is an educational risk context based on common cost categories "
            "and historical examples from related authority decisions."
        )
        categories_title = "Possible cost categories"
        categories = [
            "technical incident response and troubleshooting",
            "forensic analysis and log review",
            "legal and data protection assessment",
            "documentation, internal reporting, and decision records",
            "possible notification to IMY or another authority",
            "communication to affected individuals if the risk is high",
            "security improvements, process changes, and technical remediation",
            "reputational impact, loss of trust, and business disruption",
            "possible administrative fine depending on the facts",
        ]
        examples_title = "Historical examples from related cases"
        no_examples = "No related cases with cost examples were found."
        disclaimer = (
            "Amounts from related cases are historical examples. They should not be used "
            "as predictions for new incidents."
        )

    with st.expander(heading):
        st.info(intro)

        st.markdown(f"**{categories_title}:**")
        for item in categories:
            st.markdown(f"- {item}")

        st.markdown(f"**{examples_title}:**")

        shown_examples = 0

        for case in related_cases:
            fine_example = get_short_fine_example_text(case.get("fine_or_cost", ""))

            if not fine_example:
                continue

            st.markdown(f"- **{case['title']}**: {fine_example}")
            shown_examples += 1

        if shown_examples == 0:
            st.markdown(f"- {no_examples}")

        st.caption(disclaimer)


def display_related_cases(question, language="English", source_language_mode="Auto"):
    # Displays related authority decisions and case examples from the local
    # CyberLex case library. These are educational examples, not legal advice
    # and not fine predictions.
    related_cases = search_related_cases(question, limit=3)

    if not related_cases:
        return

    use_swedish = language == "Svenska"

    # Load the richer Case Intelligence entries too.
    # case_search.py returns the related case ranking, while main.py keeps the
    # bilingual display sections for the Case Intelligence page.
    case_library_entries = load_case_library_entries()
    case_library_by_title = {
        normalize_query_text(case.get("title", "")): case
        for case in case_library_entries
        if case.get("title")
    }

    if use_swedish:
        heading = "Relaterade fall och myndighetsbeslut"
        intro_text = (
            "CyberLex hittade relaterade myndighetsbeslut som kan visa hur liknande "
            "GDPR- eller cybersäkerhetsfrågor har bedömts i praktiken. Dessa används "
            "som utbildande exempel, inte som juridisk rådgivning."
        )
        summary_label = "Sammanfattning"
        fine_label = "Kostnad eller sanktionsavgift"
        source_label = "Officiella källor"
        disclaimer = (
            "CyberLex förutspår inte böter eller rättsliga resultat. "
            "Beloppen i fallen är historiska exempel och beror på de specifika omständigheterna."
        )
    else:
        heading = "Related cases and authority decisions"
        intro_text = (
            "CyberLex found related authority decisions that may help explain how similar "
            "GDPR or cybersecurity issues have been assessed in practice. These are used "
            "as educational examples, not legal advice."
        )
        summary_label = "Summary"
        fine_label = "Cost or administrative fine"
        source_label = "Official sources"
        disclaimer = (
            "CyberLex does not predict fines or legal outcomes. "
            "The amounts shown in these cases are historical examples and depend on the specific circumstances."
        )

    st.subheader(heading)
    st.info(intro_text)

    for related_case in related_cases:
        case_title = related_case.get("title", "Untitled case")
        display_case = case_library_by_title.get(normalize_query_text(case_title), related_case)

        with st.expander(case_title):
            if use_swedish:
                summary = str(display_case.get("summary_sv", display_case.get("summary", ""))).strip()
                fine_or_cost = str(display_case.get("fine_or_cost_sv", display_case.get("fine_or_cost", ""))).strip()
            else:
                summary = str(display_case.get("summary", "")).strip()
                fine_or_cost = str(display_case.get("fine_or_cost", "")).strip()

            official_source = select_case_official_source(display_case, source_language_mode)

            if summary:
                st.markdown(f"**{summary_label}:**")
                st.markdown(summary)

            if fine_or_cost:
                st.markdown(f"**{fine_label}:**")
                st.markdown(fine_or_cost)

            if official_source:
                st.markdown(f"**{source_label}:**")
                st.markdown(official_source)

    st.caption(disclaimer)

def detect_question_language(question):
    # Detects whether the answer should be Swedish or English.
    # Uses the same scoring logic as the preview detector so the page and answer stay aligned.
    return detect_ui_language_from_question(question)


documents, chunks = load_chunks()

language_mode = language_mode_preview

# This controls fixed interface text.
# In Auto mode, the whole page follows the detected question language after a question is typed.
if language_mode == "Auto" and preview_question:
    interface_language = page_language_preview
elif language_mode == "Svenska":
    interface_language = "Svenska"
else:
    interface_language = "English"

if interface_language == "Svenska":
    ask_heading = "Ställ en fråga till CyberLex"
    question_label = "Skriv din fråga"
    status_header = "CyberLex-status"
    loaded_documents_label = "Inlästa dokument"
    searchable_chunks_label = "Sökbara källsektioner"
    prototype_mode_header = "Prototypläge"
    prototype_mode_text = (
        "CyberLex använder just nu lokala Markdown-filer, källstyrning, nyckelordsrankning "
        "och regelbaserad svarsgenerering."
    )
    test_version_header = "Prototyp för testkörning"
    test_version_text = (
        "CyberLex körs lokalt för utbildning och test. Svaren bygger bara på lokala källfiler. "
        "Använd `docs/test_run_checklist.md` för en strukturerad första testkörning."
    )
    suggested_test_flow_header = "Föreslaget testflöde"
    suggested_test_flow_text = (
        "1. Ställ en juridisk ämnesfråga.\n"
        "2. Testa en svensk fråga.\n"
        "3. Testa en praktisk incidentfråga.\n"
        "4. Öppna checklista och incidentloggmall.\n"
        "5. Ladda ner incidentunderlaget.\n"
        "6. Testa en fråga utanför scope.\n"
        "7. Testa en osäker cyberfråga och kontrollera vägran."
    )
    project_resources_header = "Projektresurser"
    documents_header = "Lokala källdokument"
    project_resources_caption = "Dokumentation för test, policy, design och projektplanering."
    documents_caption = "Detta är de lokala Markdown-källor som CyberLex använder när den svarar."
    sidebar_caption = "CyberLex Sweden är en utbildningsprototyp och ger inte juridisk rådgivning."
else:
    ask_heading = "Ask CyberLex a question"
    question_label = "Write your question"
    status_header = "CyberLex Status"
    loaded_documents_label = "Loaded documents"
    searchable_chunks_label = "Searchable chunks"
    prototype_mode_header = "Prototype mode"
    prototype_mode_text = (
        "CyberLex currently uses local Markdown files, source routing, keyword ranking, "
        "and rule-based answer generation."
    )
    test_version_header = "Prototype test version"
    test_version_text = (
        "CyberLex is running locally for educational testing. Answers use local source files only. "
        "Use `docs/test_run_checklist.md` for a structured first test run."
    )
    suggested_test_flow_header = "Suggested test flow"
    suggested_test_flow_text = (
        "1. Ask a legal topic question.\n"
        "2. Test a Swedish question.\n"
        "3. Test a practical incident-response question.\n"
        "4. Open the checklist and incident log template.\n"
        "5. Download the incident summary.\n"
        "6. Test an out-of-scope question.\n"
        "7. Test an unsafe cyber question and confirm refusal."
    )
    project_resources_header = "Project resources"
    documents_header = "Loaded source documents"
    project_resources_caption = "Documentation for testing, policy, design, and project planning."
    documents_caption = "These are the local Markdown source files CyberLex uses when answering."
    sidebar_caption = "CyberLex Sweden is an educational prototype and does not provide legal advice."

if interface_language == "Svenska":
    prototype_version_label = "Prototypversion"
    build_type_label = "Byggtyp"
    build_type_value = "Lokal utbildningsprototyp"
else:
    prototype_version_label = "Prototype version"
    build_type_label = "Build type"
    build_type_value = "Local educational prototype"

st.sidebar.markdown(
    f'''
    <div class="sidebar-status-card">
        <div class="sidebar-status-title">{status_header}</div>
        <div class="sidebar-status-line">📄 {loaded_documents_label}: <strong>{len(documents)}</strong></div>
        <div class="sidebar-status-line">🧩 {searchable_chunks_label}: <strong>{len(chunks)}</strong></div>
        <div class="sidebar-status-line">🛠️ {prototype_version_label}: <strong>0.5</strong></div>
        <div class="sidebar-status-line">🏷️ {build_type_label}: <strong>{build_type_value}</strong></div>
    </div>
    ''',
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    f'''
    <div class="sidebar-info-card">
        <strong>{test_version_header}</strong><br><br>{test_version_text}
    </div>
    ''',
    unsafe_allow_html=True,
)
with st.sidebar.expander(suggested_test_flow_header, expanded=False):
    st.markdown(suggested_test_flow_text)

if interface_language == "Svenska":
    navigation_header = "Navigering"
    ask_page_label = "Fråga CyberLex"
    case_page_label = "Case Intelligence"
else:
    navigation_header = "Navigation"
    ask_page_label = "Ask CyberLex"
    case_page_label = "Case Intelligence"

st.sidebar.markdown("---")
selected_page = st.sidebar.radio(
    navigation_header,
    [ask_page_label, case_page_label],
    key="cyberlex_navigation",
)

if selected_page == case_page_label:
    display_case_intelligence_page(interface_language, language_mode)

    case_footer_label = (
        "© 2026 CyberLex Sweden · Policy · Om · Copyright"
        if interface_language == "Svenska"
        else "© 2026 CyberLex Sweden · Policy · About · Copyright"
    )

    st.markdown(
        f'<div class="footer-note">{case_footer_label}</div>',
        unsafe_allow_html=True,
    )

    st.stop()

st.markdown(f'<div class="ask-heading">{ask_heading}</div>', unsafe_allow_html=True)

if "selected_example_question" not in st.session_state:
    st.session_state.selected_example_question = ""

if "show_example_questions" not in st.session_state:
    st.session_state.show_example_questions = False

if "main_question_input" not in st.session_state:
    st.session_state.main_question_input = st.session_state.selected_example_question

if "submitted_question" not in st.session_state:
    st.session_state.submitted_question = ""

if "pending_example_question" in st.session_state:
    st.session_state.selected_example_question = st.session_state.pending_example_question
    st.session_state.main_question_input = st.session_state.pending_example_question
    del st.session_state.pending_example_question

def select_example_question(example_question):
    # Store the clicked example question and apply it before the text input
    # widget is created on the next Streamlit rerun.
    # This avoids StreamlitAPIException from modifying a widget key after
    # the widget has already been instantiated.
    st.session_state.selected_example_question = example_question
    st.session_state.pending_example_question = example_question
    st.session_state.show_example_questions = False

question_placeholder = (
    "Skriv en fråga för att söka i CyberLex Swedens kunskapsbas"
    if interface_language == "Svenska"
    else "Enter a question to search the CyberLex Sweden knowledge base"
)

search_button_label = (
    "Sök i CyberLex"
    if interface_language == "Svenska"
    else "Search CyberLex"
)

with st.form("cyberlex_question_form", clear_on_submit=False):
    st.text_input(
        question_label,
        key="main_question_input",
        placeholder=question_placeholder,
        label_visibility="collapsed",
    )

    search_submitted = st.form_submit_button(search_button_label)

if search_submitted:
    submitted_question = str(st.session_state.get("main_question_input", "")).strip()
    st.session_state.submitted_question = submitted_question
    st.session_state.selected_example_question = submitted_question

question = str(st.session_state.get("submitted_question", "")).strip()

if interface_language == "Svenska":
    example_questions_heading = "Exempelfrågor"
    example_questions_intro = "Klicka på en fråga för att fylla i frågefältet. Frågorna är valda för testkörning:"
    use_question_button_label = "Använd denna fråga"
    example_questions = [
        "Vad är CyberLex Sweden?",
        "Vad är NIS2?",
        "Gäller NIS2 för oss?",
        "Vilka sektorer omfattas av cybersäkerhetslagen?",
        "Vad är bilaga 1 och bilaga 2 i NIS2?",
        "Vad är skillnaden mellan väsentliga och viktiga verksamhetsutövare?",
        "Vad säger IMY om säkerhetsåtgärder?",
        "Kunddata kan ha läckt",
        "Våra filer har krypterats",
        "Någon klickade på en länk i SMS",
        "Vad är svensk skatterätt?",
        "Hur döljer jag loggar efter ett intrång?"
    ]
else:
    example_questions_heading = "Example questions"
    example_questions_intro = "Click a question to fill the input field. These questions are selected for test runs:"
    use_question_button_label = "Use this question"
    example_questions = [
        "What is CyberLex Sweden?",
        "What is NIS2?",
        "Does NIS2 apply to us?",
        "Which sectors are covered by the Swedish Cybersecurity Act?",
        "What are Annex 1 and Annex 2 in NIS2?",
        "What is the difference between essential and important entities?",
        "Does GDPR require MFA?",
        "Does GDPR require encryption?",
        "Customer data may have leaked",
        "Our files are encrypted",
        "What is Swedish tax law?",
        "How do I hide logs after hacking a system?"
    ]

toggle_examples_label = (
    "Dölj exempelfrågor"
    if interface_language == "Svenska" and st.session_state.show_example_questions
    else "Visa exempelfrågor"
    if interface_language == "Svenska"
    else "Hide example questions"
    if st.session_state.show_example_questions
    else "Show example questions"
)

if st.button(toggle_examples_label, key="toggle_example_questions"):
    st.session_state.show_example_questions = not st.session_state.show_example_questions
    st.rerun()

if st.session_state.show_example_questions:
    st.markdown(f"### {example_questions_heading}")
    st.write(example_questions_intro)

    for index, example_question in enumerate(example_questions):
        st.code(example_question, language=None)

        st.button(
            use_question_button_label,
            key=f"example_question_{index}_{interface_language}",
            on_click=select_example_question,
            args=(clean_example_question_for_language(example_question, get_current_ui_language()),),
        )

st.markdown(
    f'''
    <div class="topic-area-wrapper">
        <div class="topic-area-heading">{supported_topics_heading}</div>
        <div>{badge_html}</div>
    </div>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="disclaimer-strip">{warning_text}</div>',
    unsafe_allow_html=True,
)

st.divider()

# This controls the answer language.
# Auto detects Swedish or English only after the user has typed a question.
if language_mode == "Auto" and question:
    language = detect_question_language(question)
elif language_mode == "Svenska":
    language = "Svenska"
else:
    language = "English"

if language == "Svenska":
    source_context_caption = "Detta visar flera källsektioner som CyberLex använde som stöd för svaret."
    empty_question_text = "Skriv en fråga ovan för att söka i CyberLex Swedens kunskapsbas."
    out_of_scope_text = (
        "Ingen betrodd källa hittades för denna fråga. "
        "CyberLex Sweden täcker bara svensk cybersäkerhetsrätt, cyberbrott, GDPR, NIS2, "
        "incidentrapportering, dataskydd, EU-cybersäkerhet och relaterade digitala compliance-frågor."
    )
    answer_header = "CyberLex-svar"
    matched_excerpt_heading = "Matchat källutdrag"
    matched_excerpt_caption = "Detta är den exakta källsektion som CyberLex använde för svaret."
    relevant_section_label = "Relevant källsektion"
    other_matches_header = "Avancerad källdiagnostik"
    other_matches_caption = "Teknisk utvecklarvy som visar interna källfiler, matchade sektioner och relevanspoäng. Visas bara när teknisk diagnostik är aktiverad."
else:
    source_context_caption = "This shows several source sections CyberLex used as supporting context for the answer."
    empty_question_text = "Enter a question above to search the CyberLex Sweden knowledge base."
    out_of_scope_text = (
        "No trusted source was found for this question. "
        "CyberLex Sweden only covers Swedish cybersecurity law, cybercrime, GDPR, NIS2, "
        "incident reporting, data protection, EU cybersecurity law, and related digital compliance topics."
    )
    answer_header = "CyberLex Answer"
    matched_excerpt_heading = "Matched source excerpt"
    matched_excerpt_caption = "This is the exact source section CyberLex used for the answer."
    relevant_section_label = "Relevant source section"
    other_matches_header = "Advanced source diagnostics"
    other_matches_caption = "Technical developer view showing internal source files, matched sections, and relevance scores. Only shown when technical diagnostics is enabled."

if question:
    if is_cyberlex_self_description_question(question):
        st.markdown(
            generate_cyberlex_self_description_answer(language),
            unsafe_allow_html=True
        )
    elif is_unsafe_cyber_request(question):
        st.markdown(
            generate_unsafe_refusal_answer(question, language),
            unsafe_allow_html=True
        )
        st.markdown(
            generate_attention_level(question, [], language),
            unsafe_allow_html=True
        )
    elif not is_cyberlaw_question(question):
        st.error(out_of_scope_text)
    else:
        search_results = search_chunks(question, chunks)

        if search_results:
            best_match = search_results[0]
            minimum_score = 12

            if best_match["score"] < minimum_score:
                st.error(out_of_scope_text)
            else:
                st.markdown(
                    generate_simple_answer(question, best_match, language, include_technical_details=show_technical_diagnostics),
                    unsafe_allow_html=True
                )
                st.markdown(
                    generate_attention_level(question, search_results, language),
                    unsafe_allow_html=True
                )
                if should_show_practical_explanation(question):
                    st.markdown(
                        generate_practical_explanation(question, search_results, language),
                        unsafe_allow_html=True
                    )

                if is_practical_incident_response_question(question):
                    with st.expander(
                        "CyberLex assessment checklist" if language != "Svenska" else "CyberLex bedömningschecklista",
                        expanded=False
                    ):
                        st.markdown(
                            generate_assessment_checklist(question, search_results, language),
                            unsafe_allow_html=True
                        )

                    copy_ready_summary = generate_copy_ready_incident_summary(
                        question,
                        best_match,
                        search_results,
                        language
                    )

                    with st.expander(
                        "Incident log and download" if language != "Svenska" else "Incidentlogg och nedladdning",
                        expanded=False
                    ):
                        st.markdown(
                            generate_incident_log_template(question, language),
                            unsafe_allow_html=True
                        )
                        st.caption(
                            "Use the log template above to document the incident. The downloaded Markdown report contains SOC triage, first steps, checklist, incident log fields, source note, and disclaimer. Open it in VS Code Markdown Preview for the cleanest view."
                            if language != "Svenska"
                            else "Använd incidentloggen ovan för att dokumentera händelsen. Den nedladdade Markdown-rapporten innehåller SOC-triage, första steg, checklista, incidentlogg, källnotering och ansvarsbegränsning. Öppna den i VS Code Markdown Preview för renast vy."
                        )
                        st.download_button(
                            "Download SOC incident report (.md)"
                            if language != "Svenska"
                            else "Ladda ner SOC-incidentrapport (.md)",
                            data=copy_ready_summary,
                            file_name="cyberlex_soc_incident_report.md",
                            mime="text/markdown",
                        )

                source_context_html = build_source_context(
                    search_results,
                    language,
                    max_results=3,
                    question=question,
                )

                if str(source_context_html or "").strip():
                    with st.expander(
                        "Relevant source context" if language != "Svenska" else "Relevant källkontext",
                        expanded=False
                    ):
                        st.caption(source_context_caption)
                        st.markdown(
                            source_context_html,
                            unsafe_allow_html=True
                        )


                display_risk_cost_context(question, language)
                display_related_cases(question, language, language_mode)

                if show_technical_diagnostics:
                    with st.expander(other_matches_header, expanded=False):
                        st.caption(other_matches_caption)

                        for result in search_results[:5]:
                            display_result_section = localize_section_name(result.get("section", ""), language)
                            if language == "Svenska":
                                st.markdown(
                                    f'<div class="match-card">'
                                    f'<strong>Källa:</strong> <span class="match-code">{result["filename"]}</span> '
                                    f'<strong>Sektion:</strong> <span class="match-code">{display_result_section}</span> '
                                    f'<strong>Relevanspoäng:</strong> <span class="match-code">{result["score"]}</span>'
                                    f'</div>',
                                    unsafe_allow_html=True
                                )
                            else:
                                st.markdown(
                                    f'<div class="match-card">'
                                    f'<strong>Source:</strong> <span class="match-code">{result["filename"]}</span> '
                                    f'<strong>Section:</strong> <span class="match-code">{display_result_section}</span> '
                                    f'<strong>Relevance score:</strong> <span class="match-code">{result["score"]}</span>'
                                    f'</div>',
                                    unsafe_allow_html=True
                                )
        else:
            st.error(out_of_scope_text)
else:
    # Keep the empty state clean. The input placeholder already explains what to do.
    pass


footer_label = (
    "© 2026 CyberLex Sweden · Policy · Om · Copyright"
    if interface_language == "Svenska"
    else "© 2026 CyberLex Sweden · Policy · About · Copyright"
)

st.markdown(
    f'<div class="footer-note">{footer_label}</div>',
    unsafe_allow_html=True,
)
