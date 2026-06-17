"""
Incident-detection helpers for CyberLex Sweden.

This module contains defensive incident-response classifiers used by the main
app and search routing. It identifies questions about suspected hacking,
data leaks, ransomware, suspicious links, suspicious logins, compromised
accounts, and related practical response scenarios.
"""

from text_utils import normalize_query_text, contains_any

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

