"""
Language detection and localization helpers for CyberLex Sweden.

This module keeps Swedish/English UI logic separate from the main Streamlit app.
"""

import re
import streamlit as st

from text_utils import clean_words, normalize_query_text, contains_any

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
        "appfel", "kunduppgifter", "exponera", "exponerar", "exponerade",
        "exponering", "användare", "uppgifter", "kontoseparering",
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

def get_effective_ui_language(selected_language, question):
    # Resolves the active UI language.
    # If the user selected Auto, the UI follows the detected language of the question.
    if selected_language in ("English", "Svenska"):
        return selected_language

    detected_language = detect_ui_language_from_question(question)
    if detected_language in ("English", "Svenska"):
        return detected_language

    return "English"


def localize_case_title(title, language="English"):
    # Converts known case-library titles into the active UI language.
    # The Markdown case titles are often English, but the UI should follow the
    # user's question language when Auto mode is used.
    raw_title = str(title or "").strip()

    if language != "Svenska":
        return raw_title

    key = re.sub(r"[^a-zåäö0-9]+", " ", raw_title.lower()).strip()
    key = re.sub(r"\s+", " ", key)

    swedish_titles = {
        "klarna app data exposure 2021": "Klarna appdataexponering 2021",
        "wrong email customer data case": "Kunduppgifter skickade till fel e-postmottagare",
        "wrong email customer data": "Kunduppgifter skickade till fel e-postmottagare",
        "trygg hansa security deficiencies": "Trygg-Hansa: säkerhetsbrister",
        "apoteket and apohem meta pixel": "Apoteket och Apohem: Meta Pixel",
        "avanza bank and meta pixel": "Avanza Bank och Meta Pixel",
        "imy kry meta pixel": "Kry: Meta Pixel",
        "kry meta pixel": "Kry: Meta Pixel",
        "equality ombudsman web form": "Diskrimineringsombudsmannen: webbformulär",
        "sportadmin security breach": "Sportadmin: säkerhetsincident",
    }

    if key in swedish_titles:
        return swedish_titles[key]

    if "wrong email" in key and "customer data" in key:
        return "Kunduppgifter skickade till fel e-postmottagare"
    if "klarna" in key and "data exposure" in key:
        return "Klarna appdataexponering 2021"
    if "trygg hansa" in key and "security" in key:
        return "Trygg-Hansa: säkerhetsbrister"

    return raw_title


def localize_source_label(label, language="English"):
    # Converts known official-source labels into the active UI language.
    # The URL remains unchanged; only the visible label is localized.
    raw_label = str(label or "").strip()

    if language != "Svenska":
        return raw_label

    key = re.sub(r"[^a-zåäö0-9]+", " ", raw_label.lower()).strip()
    key = re.sub(r"\s+", " ", key)

    swedish_labels = {
        "imy personal data breach guidance": "IMY: vägledning om personuppgiftsincidenter",
        "imy notification of a personal data breach": "IMY: anmälan av personuppgiftsincident",
        "imy do we have to report all personal data breaches to imy": "IMY: måste alla personuppgiftsincidenter anmälas?",
        "eu gdpr regulation": "EU: dataskyddsförordningen GDPR",
        "edpb notify a personal data breach": "EDPB: anmälan av personuppgiftsincident",
        "edpb guidelines 01 2021 on examples regarding personal data breach notification": "EDPB: riktlinjer med exempel på anmälan av personuppgiftsincidenter",
        "edpb guidelines 4 2019 on article 25 data protection by design and by default": "EDPB: riktlinjer om dataskydd genom design och som standard",
        "cert se the national csirt of sweden": "CERT-SE: Sveriges nationella CSIRT",
        "msb hantera pågående it incident": "MSB: hantera pågående it-incident",
        "msb frivillig rapportering av it incident": "MSB: frivillig rapportering av it-incident",
        "msb incidentrapportering enligt cybersäkerhetslagen": "MSB: incidentrapportering enligt cybersäkerhetslagen",
        "cisa ransomware response checklist": "CISA: checklista för ransomware-respons",
        "cisa i ve been hit by ransomware": "CISA: jag har drabbats av ransomware",
    }

    if key in swedish_labels:
        return swedish_labels[key]

    # Extra robust fallbacks for labels that may contain punctuation, wording
    # changes, or source-title variants.
    if "do we have to report all personal data breaches" in key:
        return "IMY: måste alla personuppgiftsincidenter anmälas?"
    if "personal data breach guidance" in key:
        return "IMY: vägledning om personuppgiftsincidenter"
    if "notification of a personal data breach" in key:
        return "IMY: anmälan av personuppgiftsincident"
    if "gdpr regulation" in key:
        return "EU: dataskyddsförordningen GDPR"

    return raw_label

