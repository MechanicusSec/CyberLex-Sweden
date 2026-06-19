"""
Routing and question-behavior helpers for CyberLex Sweden.

This module contains pure routing/search logic that can be tested without
launching the Streamlit interface.
"""

from text_utils import clean_words, normalize_query_text, contains_any
from incident_engine import (
    is_practical_incident_response_question,
    is_suspected_hacking_question,
    is_data_leak_response_question,
    is_suspicious_login_question,
    is_suspicious_link_question,
    is_suspicious_email_question,
    is_compromised_account_question,
    is_ransomware_response_question,
    is_ransomware_or_malware_question,
)


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
        "app bug": [
            "personal data breach",
            "customer data exposure",
            "data protection",
            "gdpr",
            "imy",
            "security measures",
            "privacy by design",
        ],
        "appfel": [
            "personuppgiftsincident",
            "kunduppgifter",
            "exponerade personuppgifter",
            "gdpr",
            "imy",
            "säkerhetsåtgärder",
        ],
        "users see other users data": [
            "customer data exposure",
            "personal data breach",
            "session handling",
            "account separation",
            "gdpr",
        ],
        "användare se andra användares uppgifter": [
            "kunduppgifter",
            "personuppgiftsincident",
            "kontoseparering",
            "sessioner",
            "gdpr",
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
        "app bug", "app incident", "app error", "application error",
        "appfel", "appincident", "appuppdatering",
        "customer data exposure", "customer data exposed", "exposed customer data",
        "users see other users data", "users could see other users data",
        "other users data", "see other users data",
        "kunduppgifter", "kunduppgifter exponerades", "exponera kunduppgifter",
        "användare se andra användares uppgifter", "andra användares uppgifter",
        "account separation", "session handling", "kontoseparering",
        "klarna", "finansinspektionen",
        "administrative fine", "sanktionsavgift", "gdpr fine", "fine",
    ]

    return contains_any(q, terms)

def should_show_related_cases(question):
    # Shows related cases only when the question is about legal/compliance
    # examples, case-library context, fines, data exposure, Meta Pixel, app bugs,
    # wrong-recipient disclosures, or similar historical/compliance examples.
    #
    # Practical incident-response questions should focus on first steps, evidence,
    # containment, and reporting assessment. Showing old cases during ransomware
    # or suspicious-login triage can make the answer feel less relevant.
    if is_practical_incident_response_question(question):
        return False

    return is_case_library_context_question(question)

def build_question_behavior_profile(question, language="English"):
    """
    Builds one central behavior profile for the current question.

    CyberLex is still a rule-based, source-grounded prototype. This profile
    simply makes the existing rules behave more consistently by deciding once
    what kind of question the user asked, then reusing that decision in the
    answer flow.
    """

    question_text = str(question or "").strip()

    is_self_description = is_cyberlex_self_description_question(question_text)
    is_unsafe = is_unsafe_cyber_request(question_text)
    is_in_scope = is_cyberlaw_question(question_text)

    is_practical_incident = is_practical_incident_response_question(question_text)
    is_case_context = is_case_library_context_question(question_text)
    is_nis2_scope = is_nis2_sector_scope_question(question_text)
    is_gdpr_security = is_gdpr_security_guidance_question(question_text)
    is_imy_security = is_imy_gdpr_security_measures_question(question_text)

    # Practical incident-response questions should stay operational.
    # Old case examples and fine examples can be useful later, but not while the
    # user is asking what to do about ransomware, phishing, suspicious login, etc.
    show_related_cases = False
    show_risk_cost_context = False

    if not is_practical_incident:
        show_related_cases = is_case_context
        show_risk_cost_context = is_case_context

    show_practical_explanation = should_show_practical_explanation(question_text)
    show_assessment_checklist = is_practical_incident
    show_soc_report = is_practical_incident

    source_context_max_results = 3

    if is_practical_incident:
        source_context_max_results = 2

    if is_nis2_scope:
        source_context_max_results = get_nis2_scope_max_context_cards(question_text)

    if is_case_context:
        source_context_max_results = 2

    target_source_file = get_target_source_file(question_text)

    # Final guardrail: practical incident-response questions must stay on the
    # incident playbook even if other broad GDPR/security rules also match.
    if is_practical_incident:
        target_source_file = "cyber_incident_response_playbook.md"

    if is_self_description:
        answer_mode = "self_description"
    elif is_unsafe:
        answer_mode = "unsafe_refusal"
    elif not is_in_scope:
        answer_mode = "out_of_scope"
    elif is_practical_incident:
        answer_mode = "incident_response"
    elif is_case_context:
        answer_mode = "case_context"
    elif is_nis2_scope:
        answer_mode = "nis2_scope"
    elif is_imy_security:
        answer_mode = "imy_security"
    elif is_gdpr_security:
        answer_mode = "gdpr_security"
    else:
        answer_mode = "source_answer"

    return {
        "answer_mode": answer_mode,
        "language": language,
        "target_source_file": target_source_file,
        "is_self_description": is_self_description,
        "is_unsafe": is_unsafe,
        "is_in_scope": is_in_scope,
        "is_practical_incident": is_practical_incident,
        "is_case_context": is_case_context,
        "is_nis2_scope": is_nis2_scope,
        "is_gdpr_security": is_gdpr_security,
        "is_imy_security": is_imy_security,
        "show_practical_explanation": show_practical_explanation,
        "show_assessment_checklist": show_assessment_checklist,
        "show_soc_report": show_soc_report,
        "show_related_cases": show_related_cases,
        "show_risk_cost_context": show_risk_cost_context,
        "source_context_max_results": source_context_max_results,
    }

def get_target_source_file(question):
    # Routes clear questions to a specific knowledge file.
    question_lower = normalize_query_text(question).strip()

    # Practical incident-response questions should use the incident playbook before
    # any broader GDPR/IMY security routing. This prevents encrypted-file or
    # ransomware questions from being pulled into GDPR guidance instead of
    # operational first-step guidance.
    if is_practical_incident_response_question(question):
        return "cyber_incident_response_playbook.md"

    # Case-library-style questions should use GDPR/data protection source context,
    # while the actual real-world examples are shown in the related-cases section.
    # This avoids weird combinations like a Meta Pixel question using the generic
    # incident-response playbook as the main source card.
    if is_case_library_context_question(question_lower):
        if contains_any(
            question_lower,
            [
                "app bug", "app incident", "app error", "application error",
                "appfel", "appincident", "appuppdatering",
                "customer data exposure", "customer data exposed", "exposed customer data",
                "users see other users data", "users could see other users data",
                "other users data", "see other users data",
                "kunduppgifter", "kunduppgifter exponerades", "exponera kunduppgifter",
                "användare se andra användares uppgifter", "andra användares uppgifter",
                "account separation", "session handling", "kontoseparering",
                "klarna", "finansinspektionen",
            ],
        ):
            return "gdpr_personal_data_breach.md"

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

    # Practical incident-response questions should use the incident playbook
    # before broader GDPR/IMY security guidance. Otherwise questions such as
    # Swedish ransomware/encrypted-file incidents can be pulled into GDPR
    # security guidance instead of operational first-step guidance.
    if is_practical_incident_response_question(question):
        return "cyber_incident_response_playbook.md"

    # IMY/GDPR security-measure questions should use the dedicated IMY security file
    # instead of the general breach/incident guidance source.
    if is_imy_gdpr_security_measures_question(question_lower):
        return "imy_gdpr_security_measures.md"

    # GDPR assessment/security questions are informational or compliance questions,
    # not generic incident playbook questions.
    if is_gdpr_security_guidance_question(question_lower):
        return "gdpr_imy_edpb_security_guidance.md"

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
        "app bug",
        "app incident",
        "app error",
        "appfel",
        "appincident",
        "kunduppgifter",
        "exponera kunduppgifter",
        "andra användares uppgifter",
        "users see other users data",
        "other users data",
        "customer data exposure",
        "account separation",
        "session handling",
        "klarna",
        "principles"
    }

    question_lower = normalize_query_text(question)

    # Let the dedicated incident detectors mark practical incident questions as in scope.
    # Otherwise small word-order differences in Swedish can be refused before search starts.
    if (
        is_nis2_sector_scope_question(question_lower)
        or is_case_library_context_question(question_lower)
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
