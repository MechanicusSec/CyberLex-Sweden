from pathlib import Path
import streamlit as st
from vector_search import build_chunk_index, search_chunks as experimental_search_chunks

st.set_page_config(
    page_title="CyberLex Sweden",
    page_icon="💻",
    layout="wide"
)

DATA_DIR = Path("data")


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
        "malware infection first steps": "Första steg vid malware",
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
        "legal reference": "Rättslig koppling",
        "practical explanation": "Praktisk förklaring",
        "cybersecurity connection": "Cybersäkerhetskoppling",
        "swedish connection": "Svensk koppling",
        "third-party ict risk": "ICT-tredjepartsrisk",
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
    }

    if use_swedish:
        if normalized in swedish_names:
            return swedish_names[normalized]

        # Remove leading language markers if a source heading contains them.
        if normalized.startswith("swedish "):
            stripped = raw_section[8:].strip()
            return stripped[:1].upper() + stripped[1:]
        if normalized.startswith("english "):
            stripped = raw_section[8:].strip()
            return stripped[:1].upper() + stripped[1:]

        return raw_section

    if normalized in english_names:
        return english_names[normalized]

    if normalized.startswith("swedish "):
        stripped = raw_section[8:].strip()
        return stripped[:1].upper() + stripped[1:]
    if normalized.startswith("english "):
        stripped = raw_section[8:].strip()
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
        "misstänker hackning",
        "misstänkt hackning",
        "suspect intrusion",
        "suspected intrusion",
        "intrusion",
        "intrång",
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
        "filer har krypterats",
        "data leak",
        "data leakage",
        "dataläcka",
        "läckt data",
        "data har läckt",
        "customer data exposed",
        "kunddata har exponerats",
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
        "misstänkt inloggning",
        "ovanlig inloggning",
        "misstänkta inloggningar",
        "ovanliga inloggningar",
        "phishing",
        "nätfiske",
        "suspicious email",
        "misstänkt mejl",
        "misstänkt e-post",
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
        "misstänker",
        "misstänkt",
    ]

    return contains_any(question_lower, incident_terms) and contains_any(question_lower, action_terms)


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
            "intrång",
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
            "personal data exposed",
            "exposed data",
            "dataläcka",
            "data har läckt",
            "läckt data",
            "kunddata har exponerats",
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
            "ovanlig inloggning",
            "ovanliga inloggningar",
            "okänd inloggning",
            "inloggning från okänt land",
            "inloggning från annat land",
            "misslyckade inloggningar",
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
            "klickat på phishinglänk",
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
            "filer har krypterats",
            "encrypted files",
            "krypterade filer",
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


def get_target_source_file(question):
    # Routes clear questions to a specific knowledge file.
    question_lower = normalize_query_text(question).strip()


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
        "evidence preservation examples"
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
                score += 100
            else:
                score -= 100

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

        if "nis2" in question_lower or "cybersecurity act" in question_lower or "cybersäkerhetslagen" in question_lower:
            if "nis2" in filename_lower:
                score += 50
            if "key idea" in section_text:
                score += 15
            if "important points" in section_text:
                score += 15
            if "incident reporting" in section_text:
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

    if is_suspicious_login_question(question):
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


def clean_source_excerpt(content, section_name="", language="English", max_chars=700):
    # Creates a cleaner preview for "Relevant source context".
    # It removes source-routing examples such as "Use this section when the user asks:"
    # and skips straight to the actual guidance.
    lines = str(content or "").splitlines()

    # Remove leading Markdown heading.
    if lines and lines[0].strip().startswith("#"):
        lines = lines[1:]

    cleaned = []
    skip_question_examples = False

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

    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()
        lower = stripped.lower()

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
        for raw_line in lines:
            stripped = raw_line.strip()
            lower = stripped.lower()
            if not stripped:
                continue
            if any(marker in lower for marker in routing_markers):
                continue
            if stripped.startswith("- ") and stripped.endswith("?"):
                continue
            fallback_lines.append(raw_line.rstrip())
        excerpt = "\n".join(fallback_lines).strip()

    if len(excerpt) > max_chars:
        excerpt = excerpt[:max_chars].rsplit(" ", 1)[0] + "..."

    return excerpt

def build_source_context(search_results, language="English", max_results=3, question=None):
    # Builds a short source context summary from the top matched source sections.
    # The context should support the answer, not repeat the CyberLex checklist.
    # Therefore checklist sections are hidden unless no non-checklist source context exists.

    use_swedish = language == "Svenska"

    if use_swedish:
        file_label = "Källa"
        section_label = "Sektion"
        score_label = "Relevanspoäng"
        excerpt_label = "Kort utdrag"
    else:
        file_label = "Source"
        section_label = "Section"
        score_label = "Relevance score"
        excerpt_label = "Short excerpt"

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

    filtered_results = prioritize_source_context_results(
        filtered_results,
        question=question,
        language=language
    )

    # Avoid duplicating the visible CyberLex assessment checklist.
    non_checklist_results = [
        result for result in filtered_results
        if not is_checklist_section(result.get("section", ""))
    ]

    if non_checklist_results:
        filtered_results = non_checklist_results

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

        if len(selected_results) >= max_results:
            break

    for result in selected_results:
        display_section = localize_section_name(result.get("section", ""), language)
        excerpt = clean_source_excerpt(
            result.get("content", ""),
            section_name=result.get("section", ""),
            language=language,
            max_chars=700
        )

        context_blocks.append(
            f'<div class="context-card">'
            f'<div class="context-card-title">{display_section}</div>'
            f'<div class="context-row"><strong>{file_label}:</strong> '
            f'<span class="context-code">{result["filename"]}</span></div>'
            f'<div class="context-row"><strong>{section_label}:</strong> '
            f'<span class="context-code">{display_section}</span></div>'
            f'<div class="context-row"><strong>{score_label}:</strong> '
            f'<span class="context-code">{result["score"]}</span></div>'
            f'<div class="context-excerpt-label">{excerpt_label}:</div>'
            f'<div class="context-excerpt">{excerpt}</div>'
            f'</div>'
        )

    return "\n".join(context_blocks)


def generate_practical_explanation(question, search_results, language="English"):
    # Generates a practical explanation based on the question and matched source sections.
    # This is still rule-based and source-grounded. It does not use an external AI model.

    question_lower = question.lower()
    use_swedish = language == "Svenska"

    if use_swedish:
        heading = "Praktisk förklaring"

        if is_practical_incident_response_question(question):
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

        if is_practical_incident_response_question(question):
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
        "dataläcka",
        "läckt data",
        "exponerad data",
        "kunddata",
    ]

    ransomware_terms = [
        "ransomware",
        "malware",
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
                "Har vi kontrollerat om mejlet innehöll malware och om någon klient behöver isoleras?",
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
        incident_type_sv = "Ransomware eller malware"
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
            "Malwareprov eller larm sparat:",
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

def generate_attention_level(question, search_results, language="English"):
    # Generates a simple CyberLex attention level.
    # This is not a legal risk rating. It is an educational signal based on topic and matched sources.

    question_lower = question.lower()
    use_swedish = language == "Svenska"

    best_score = 0
    if search_results:
        best_score = search_results[0].get("score", 0)

    high_terms = [
        "personal data breach",
        "personuppgiftsincident",
        "72",
        "incident reporting",
        "incidentrapportering",
        "reported",
        "rapportera",
        "rapporteras",
        "nis2",
        "cybersecurity act",
        "cybersäkerhetslagen",
        "dora",
        "ransomware",
        "malware",
        "cyber attack",
        "cyberattack",
        "security incident",
        "incident response",
        "suspect hacking",
        "suspect intrusion",
        "data leak",
        "compromised account",
        "misstänker intrång",
        "misstänker hackning",
        "dataläcka",
        "komprometterat konto",
        "cyberincident",
        "säkerhetsincident"
    ]

    medium_terms = [
        "gdpr",
        "imy",
        "dataintrång",
        "unauthorized access",
        "obehörig åtkomst",
        "cyber resilience act",
        "cyberresiliensakten",
        "products with digital elements"
    ]

    if any(term in question_lower for term in high_terms) or best_score >= 180:
        level = "High"

        if use_swedish:
            reason = (
                "Frågan kan beröra incidentrapportering, tidsfrister, personuppgifter, "
                "cybersäkerhetskrav eller regler som kräver noggrann bedömning."
            )
        else:
            reason = (
                "The question may involve incident reporting, timelines, personal data, "
                "cybersecurity duties, or rules that require careful assessment."
            )

    elif any(term in question_lower for term in medium_terms) or best_score >= 100:
        level = "Medium"

        if use_swedish:
            reason = (
                "Frågan verkar vara relevant för dataskydd, cybersäkerhetsrätt eller digital compliance, "
                "men den verkar inte nödvändigtvis vara en akut incidentfråga."
            )
        else:
            reason = (
                "The question appears relevant to data protection, cybersecurity law, or digital compliance, "
                "but does not necessarily appear to be an urgent incident issue."
            )

    else:
        level = "Normal"

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

        if level == "High":
            translated_level = "Hög"
        elif level == "Medium":
            translated_level = "Medel"
        else:
            translated_level = "Normal"

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

    question_lower = question.lower()
    use_swedish = language == "Svenska"

    if is_practical_incident_response_question(question):
        return "Incidenthantering och första åtgärder" if use_swedish else "Incident response and first steps"

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
        return "Ransomware- eller malwareincident" if use_swedish else "Ransomware or malware incident"

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
            intro = (
                "En misstänkt inloggning betyder inte alltid att kontot är helt komprometterat, "
                "men den ska behandlas som en möjlig identitetsincident tills loggarna visar motsatsen."
            )
            steps = [
                "Spara larmet eller loggposten med tidpunkt, användarkonto, IP-adress, plats, enhet och tjänst.",
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
                "Kontrollera om mejlet innehöll malware och om någon klient behöver isoleras.",
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
            title = "Rekommenderade första steg vid ransomware eller malware"
            intro = (
                "Vid ransomware eller malware är målet att begränsa spridning, bevara bevis, "
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
            intro = (
                "A suspicious login does not always mean full compromise, but it should be treated as a possible identity incident "
                "until the logs show otherwise."
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


def generate_simple_answer(question, best_match, language="English"):
    # Generates a simple source-based answer from the best matching chunk.
    question_lower = question.lower()
    use_swedish = language == "Svenska"

    if is_practical_incident_response_question(question):
        return generate_incident_response_answer(question, language)

    if (
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
        or "cyber attack" in question_lower
        or "cyberattack" in question_lower
    ):
        if use_swedish:
            answer = (
                "Efter en ransomwareattack eller malwareincident bör organisationen först isolera drabbade system, "
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
                "IMY, Integritetsskyddsmyndigheten, är Sveriges myndighet för integritetsskydd. "
                "IMY har tillsyn över GDPR och dataskydd i Sverige. IMY är relevant för cybersäkerhet "
                "eftersom cyberincidenter kan leda till personuppgiftsincidenter eller andra risker för personuppgifter."
            )
        else:
            answer = (
                "IMY, Integritetsskyddsmyndigheten, is the Swedish Authority for Privacy Protection. "
                "It supervises GDPR and personal data protection in Sweden. IMY is relevant to cybersecurity "
                "because cyber incidents can involve personal data breaches or other personal data risks."
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
                "I Sverige är det IMY, Integritetsskyddsmyndigheten, som har tillsyn över GDPR "
                "och dataskydd."
            )
        else:
            answer = (
                "In Sweden, GDPR and personal data protection are supervised by IMY, "
                "Integritetsskyddsmyndigheten, the Swedish Authority for Privacy Protection."
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
                "Den handlar om digital operativ motståndskraft, ICT-riskhantering, rapportering av större ICT-relaterade incidenter, "
                "testning av digital motståndskraft och hantering av tredjepartsrisker kopplade till ICT-tjänster."
            )
        else:
            answer = (
                "DORA, the Digital Operational Resilience Act, is an EU regulation for the financial sector. "
                "It focuses on ICT risk management, major ICT-related incident reporting, digital operational resilience testing, "
                "ICT third-party risk management, and information sharing. Its purpose is to help financial entities withstand, "
                "respond to, and recover from ICT disruptions and cyber incidents."
            )

    elif (
        ("nis2" in question_lower or "nis" in question_lower or "cybersecurity act" in question_lower or "cybersäkerhetslagen" in question_lower)
        and "gdpr" in question_lower
        and ("incident" in question_lower or "reported" in question_lower or "report" in question_lower or "rapporteras" in question_lower or "rapportera" in question_lower)
    ):
        if use_swedish:
            answer = (
                "Ja, vissa cybersäkerhetsincidenter kan behöva bedömas enligt både NIS2 och GDPR. "
                "NIS2-incidentrapportering och GDPR-anmälan av personuppgiftsincidenter är olika rättsområden, "
                "men de kan överlappa om en cybersäkerhetsincident även påverkar personuppgifter."
            )
        else:
            answer = (
                "Yes, some cybersecurity incidents may need to be considered under both NIS2 and GDPR. "
                "NIS2 incident reporting and GDPR personal data breach notification are different legal areas, "
                "but they can overlap if a cybersecurity incident also affects personal data."
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
                "Organisationer som omfattas kan behöva rapportera betydande cybersäkerhetsincidenter enligt "
                "särskilda kriterier, rutiner och tidsfrister. Vissa incidenter kan också behöva bedömas enligt GDPR "
                "om personuppgifter påverkas."
            )
        else:
            answer = (
                "NIS2 incident reporting in Sweden is handled through the Swedish Cybersecurity Act. "
                "Covered organizations may need to report significant cybersecurity incidents according to reporting criteria, "
                "procedures, and time limits. Some incidents may also need separate GDPR reporting if personal data is affected."
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
                "If notification is required, the breach should normally be reported within 72 hours after the organization becomes aware of it."
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
                "GDPR includes core principles such as lawfulness, fairness and transparency, "
                "purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality, "
                "and accountability."
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
                "GDPR is the General Data Protection Regulation. It is an EU regulation that controls how personal data "
                "may be processed and protected. In Sweden, IMY supervises GDPR and personal data protection."
            )

    elif "gdpr" in question_lower or "authority" in question_lower:
        if use_swedish:
            answer = (
                "I Sverige är GDPR och dataskydd kopplat till IMY, Integritetsskyddsmyndigheten. "
                "IMY är tillsynsmyndighet för dataskydd och personuppgiftshantering."
            )
        else:
            answer = (
                "In Sweden, GDPR and personal data protection are handled by IMY, "
                "Integritetsskyddsmyndigheten, the Swedish Authority for Privacy Protection."
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
                "NIS2 is an EU cybersecurity directive. In Sweden, it is connected to the Swedish Cybersecurity Act. "
                "The rules focus on cybersecurity risk management, security measures, and incident reporting for covered organizations."
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
                "Det handlar på en övergripande nivå om obehörig åtkomst till, eller otillåten påverkan på, "
                "data eller informationssystem."
            )
        else:
            answer = (
                "Unauthorized access to an information system may be illegal in Sweden. "
                "In Swedish law, this is commonly connected to the offence called dataintrång, "
                "which concerns unauthorized access to, or interference with, data or information systems."
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
                "Den fokuserar bland annat på säker produktdesign, hantering av sårbarheter och ansvar för aktörer "
                "som tillverkar eller tillhandahåller digitala produkter."
            )
        else:
            answer = (
                "The Cyber Resilience Act is an EU regulation about cybersecurity requirements for products with digital elements. "
                "It focuses on secure product design, vulnerability handling, and cybersecurity responsibilities for actors involved "
                "with digital products."
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
        short_answer_heading = "Kort svar"
        citation_heading = "Källhänvisning"
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
        short_answer_heading = "Short answer"
        citation_heading = "Citation details"
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

    return (
        f"## {short_answer_heading}\n\n"
        f"{answer}\n\n"
        f'<div class="topic-card">'
        f'<div class="topic-card-title">{topic_heading}</div>'
        f'<div class="topic-row"><strong>{topic_heading}:</strong> '
        f'<span class="topic-code">{detected_topic}</span></div>'
        f'</div>\n\n'
        f'<div class="citation-card">'
        f'<div class="citation-card-title">{citation_heading}</div>'
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
        f'</div>\n\n'
        f'<div class="source-card">'
        f'<div class="source-card-title">{official_sources_heading}</div>'
        f'{source_lines}'
        f'</div>\n\n'
        f'<div class="metadata-card">'
        f'<div class="metadata-card-title">{metadata_heading}</div>'
        f'<div class="metadata-row"><strong>{source_date_label}:</strong> '
        f'<span class="metadata-code">{source_date}</span></div>'
        f'<div class="metadata-row"><strong>{source_freshness_label}:</strong> '
        f'<span class="metadata-code">{source_freshness}</span></div>'
        f'<div class="metadata-row"><strong>{version_notes_label}:</strong> '
        f'<span class="metadata-code">{version_notes}</span></div>'
        f'</div>\n\n'
        f'<div class="limitation-card">'
        f'<div class="limitation-card-title">{limitation_heading}</div>'
        f'<div class="limitation-card-text">{limitation_text}</div>'
        f'</div>'
    )


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
        "dataläcka",
        "läckt data",
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
        "svensk cybersäkerhetsrätt",
        "cybersäkerhet",
        "cyberbrott",
        "ransomware",
        "malware",
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
        is_practical_incident_response_question(question_lower)
        or is_compromised_account_question(question_lower)
        or is_suspicious_login_question(question_lower)
        or is_suspicious_email_question(question_lower)
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
        line-height: 1.6;
        white-space: pre-wrap;
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

if language_mode_preview == "Svenska":
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
        "Dataintrång",
        "EU Cyber Resilience Act",
        "DORA",
        "Digital compliance"
    ]

st.markdown(
    f'<div class="main-header"><h1>CyberLex Sweden</h1><p>{page_subtitle}</p></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-card">'
    f'<strong>{info_card_heading}</strong><br>'
    f'{info_card_text}'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(f"### {supported_topics_heading}")

badge_html = "".join(
    [f'<span class="topic-badge">{topic}</span>' for topic in topic_badges]
)

st.markdown(
    badge_html,
    unsafe_allow_html=True
)

st.warning(warning_text)

st.divider()

def detect_question_language(question):
    # Detects whether the user question is likely Swedish or English.
    question_lower = question.lower().strip()

    swedish_markers = {
        "vad", "är", "när", "vilken", "vilka", "hur", "varför",
        "svensk", "svenska", "sverige", "myndighet", "lag",
        "cybersäkerhet", "dataskydd", "personuppgift",
        "personuppgifter", "personuppgiftsincident",
        "rapporteras", "anmälas", "incidentrapportering",
        "dataintrång", "brott", "tillsyn", "ansvarar",
        "misstänker", "intrång", "hackning", "hackad", "dataläcka", "läckt",
        "komprometterat", "komprometterad", "isolera", "bevara", "loggar",
        "cyberincident", "säkerhetsincident", "it-incident", "incidenthantering",
    }

    question_words = set(clean_words(question_lower))

    if question_words.intersection(swedish_markers):
        return "Svenska"

    return "English"


documents, chunks = load_chunks()

language_mode = language_mode_preview

# This controls fixed interface text before the user asks a question.
# In Auto mode, the interface starts in English until a question is typed.
if language_mode == "Svenska":
    interface_language = "Svenska"
else:
    interface_language = "English"

if interface_language == "Svenska":
    ask_heading = "Ställ en fråga"
    question_label = "Skriv en fråga om svensk cybersäkerhetsrätt:"
    status_header = "CyberLex-status"
    loaded_documents_label = "Inlästa dokument"
    searchable_chunks_label = "Sökbara källsektioner"
    prototype_mode_header = "Prototypläge"
    prototype_mode_text = (
        "CyberLex använder just nu lokala Markdown-filer, källstyrning, nyckelordsrankning "
        "och regelbaserad svarsgenerering."
    )
    project_resources_header = "Projektresurser"
    documents_header = "Dokument"
    sidebar_caption = "CyberLex Sweden är en utbildningsprototyp och ger inte juridisk rådgivning."
else:
    ask_heading = "Ask a question"
    question_label = "Write a question about Swedish cybersecurity law:"
    status_header = "CyberLex Status"
    loaded_documents_label = "Loaded documents"
    searchable_chunks_label = "Searchable chunks"
    prototype_mode_header = "Prototype mode"
    prototype_mode_text = (
        "CyberLex currently uses local Markdown files, source routing, keyword ranking, "
        "and rule-based answer generation."
    )
    project_resources_header = "Project resources"
    documents_header = "Documents"
    sidebar_caption = "CyberLex Sweden is an educational prototype and does not provide legal advice."

st.sidebar.header(status_header)
st.sidebar.write(f"📄 {loaded_documents_label}: {len(documents)}")
st.sidebar.write(f"🧩 {searchable_chunks_label}: {len(chunks)}")

if interface_language == "Svenska":
    st.sidebar.write("🛠️ Prototypversion: `0.5`")
    st.sidebar.write("🏷️ Byggtyp: Lokal utbildningsprototyp")
else:
    st.sidebar.write("🛠️ Prototype version: `0.5`")
    st.sidebar.write("🏷️ Build type: Local educational prototype")

st.sidebar.markdown("---")
st.sidebar.subheader(prototype_mode_header)
st.sidebar.write(prototype_mode_text)

if interface_language == "Svenska":
    ai_roadmap_header = "Framtida AI-läge"
    ai_roadmap_text = (
        "**Nuvarande version:** lokala Markdown-filer, källstyrning, nyckelordsrankning "
        "och regelbaserade svar.\n\n"
        "**Framtida version:** vektorsökning, RAG och AI-genererade svar baserade på betrodda källor."
    )
else:
    ai_roadmap_header = "Future AI mode"
    ai_roadmap_text = (
        "**Current version:** local Markdown files, source routing, keyword ranking, "
        "and rule-based answers.\n\n"
        "**Future version:** vector search, RAG, and AI-generated answers based on trusted sources."
    )

with st.sidebar.expander(ai_roadmap_header, expanded=False):
    st.markdown(ai_roadmap_text)

st.sidebar.markdown("---")

if interface_language == "Svenska":
    experimental_search_header = "Experimentell AI-sökning"
    experimental_search_caption = (
        "Detta testfält använder den experimentella sökmodulen. "
        "Det ersätter inte CyberLex huvudsvar ännu."
    )
    experimental_search_label = "Testa experimentell sökning"
    experimental_search_placeholder = "Skriv en testfråga..."
    experimental_matches_label = "Toppmatchningar från experimentell sökning:"
    no_experimental_matches_text = "Inga experimentella sökmatchningar hittades."
    experimental_source_label = "Källa"
    experimental_section_label = "Sektion"
    experimental_score_label = "Poäng"
else:
    experimental_search_header = "Experimental AI search"
    experimental_search_caption = (
        "This test panel uses the experimental search module. "
        "It does not replace the main CyberLex answer yet."
    )
    experimental_search_label = "Test experimental search"
    experimental_search_placeholder = "Type a test question..."
    experimental_matches_label = "Top experimental matches:"
    no_experimental_matches_text = "No experimental search matches found."
    experimental_source_label = "Source"
    experimental_section_label = "Section"
    experimental_score_label = "Score"

st.sidebar.subheader(experimental_search_header)
st.sidebar.caption(experimental_search_caption)

experimental_question = st.sidebar.text_input(
    experimental_search_label,
    placeholder=experimental_search_placeholder,
    key="experimental_search_question",
)

if experimental_question:
    experimental_chunks = load_experimental_search_index()
    experimental_results = experimental_search_chunks(
        experimental_question,
        experimental_chunks,
        limit=3,
    )

    if experimental_results:
        st.sidebar.markdown(f"**{experimental_matches_label}**")

        for result in experimental_results:
            experimental_card = f"""
                <div class="match-card">
                    <strong>{experimental_source_label}:</strong> <code>{result["filename"]}</code><br>
                    <strong>{experimental_section_label}:</strong> <code>{result["section"]}</code><br>
                    <strong>{experimental_score_label}:</strong> <code>{result["score"]}</code>
                </div>
                """
            st.sidebar.markdown(experimental_card, unsafe_allow_html=True)
    else:
        st.sidebar.info(no_experimental_matches_text)

st.sidebar.markdown("---")
st.sidebar.subheader(project_resources_header)

st.sidebar.markdown(
    "- `docs/terms_of_use.md`\n"
    "- `docs/privacy_policy.md`\n"
    "- `docs/legal_disclaimer.md`\n"
    "- `docs/source_policy.md`\n"
    "- `docs/source_update_history.md`\n"
    "- `docs/ai_rag_plan.md`\n"
    "- `docs/product_roadmap.md`\n"
    "- `docs/technical_design.md`"
)

st.sidebar.markdown("---")
st.sidebar.caption(sidebar_caption)

st.sidebar.markdown("---")
st.sidebar.subheader(documents_header)
for doc in documents:
    st.sidebar.write(f"- {doc['filename']}")

st.header(ask_heading)

if "selected_example_question" not in st.session_state:
    st.session_state.selected_example_question = ""

if "show_example_questions" not in st.session_state:
    st.session_state.show_example_questions = False

question = st.text_input(
    question_label,
    value=st.session_state.selected_example_question
)

if language_mode == "Svenska":
    example_questions_heading = "Exempelfrågor"
    example_questions_intro = "Klicka på en fråga för att fylla i frågefältet:"
    use_question_button_label = "Använd denna fråga"
    example_questions = [
        "Vad är GDPR?",
        "Vilka är GDPR-principerna?",
        "När måste en personuppgiftsincident rapporteras?",
        "Kan en incident behöva rapporteras enligt både NIS2 och GDPR?",
        "Vad är NIS2?",
        "Vad är DORA?",
        "Vad är dataintrång?",
        "Vad är Cyber Resilience Act?",
        "Vad ska jag göra om jag misstänker intrång?",
        "Vad gör vi efter en dataläcka?",
        "Vad gör vi om ett konto är komprometterat?",
        "Vad ska ett företag göra efter en ransomwareattack?",
        "Vad gör vi om vi ser misstänkt inloggning?"
    ]
else:
    example_questions_heading = "Example questions"
    example_questions_intro = "Click a question to fill the input field:"
    use_question_button_label = "Use this question"
    example_questions = [
        "What is GDPR?",
        "What are the GDPR principles?",
        "When must a personal data breach be reported?",
        "Can an incident need to be reported under both NIS2 and GDPR?",
        "What is NIS2?",
        "What is DORA?",
        "What is dataintrång?",
        "What is the Cyber Resilience Act?",
        "What should I do if I suspect hacking?",
        "What should we do after a data leak?",
        "What should we do if an account is compromised?",
        "What should a company do after a ransomware attack?",
        "What should we do after suspicious login activity?"
    ]

toggle_examples_label = (
    "Dölj exempelfrågor"
    if language_mode == "Svenska" and st.session_state.show_example_questions
    else "Visa exempelfrågor"
    if language_mode == "Svenska"
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

        if st.button(
            use_question_button_label,
            key=f"example_question_{index}_{language_mode}"
        ):
            st.session_state.selected_example_question = example_question
            st.session_state.show_example_questions = False
            st.rerun()

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
    other_matches_header = "Andra matchande källsektioner"
    other_matches_caption = "Detta är ytterligare källsektioner som matchade frågan, sorterade efter relevans."
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
    other_matches_header = "Other matching source sections"
    other_matches_caption = "These are additional source sections that matched the question, ranked by relevance."

if question:
    if not is_cyberlaw_question(question):
        st.error(out_of_scope_text)
    else:
        search_results = search_chunks(question, chunks)

        if search_results:
            best_match = search_results[0]
            minimum_score = 12

            if best_match["score"] < minimum_score:
                st.error(out_of_scope_text)
            else:
                st.subheader(answer_header)
                st.markdown(
                    generate_simple_answer(question, best_match, language),
                    unsafe_allow_html=True
                )
                st.markdown(
                    generate_attention_level(question, search_results, language),
                    unsafe_allow_html=True
                )
                st.markdown(
                    generate_practical_explanation(question, search_results, language),
                    unsafe_allow_html=True
                )

                with st.expander(
                    "CyberLex assessment checklist" if language != "Svenska" else "CyberLex bedömningschecklista",
                    expanded=False
                ):
                    st.markdown(
                        generate_assessment_checklist(question, search_results, language),
                        unsafe_allow_html=True
                    )

                if is_practical_incident_response_question(question):
                    with st.expander(
                        "Incident log template" if language != "Svenska" else "Incidentloggmall",
                        expanded=False
                    ):
                        st.markdown(
                            generate_incident_log_template(question, language),
                            unsafe_allow_html=True
                        )

                with st.expander(
                    "Relevant source context" if language != "Svenska" else "Relevant källkontext",
                    expanded=False
                ):
                    st.caption(source_context_caption)
                    st.markdown(
                        build_source_context(search_results, language, max_results=3, question=question),
                        unsafe_allow_html=True
                    )

                st.subheader(other_matches_header)
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
    st.write(empty_question_text)
