import html
import re

from incident_engine import (
    is_practical_incident_response_question,
    is_suspected_hacking_question,
    is_data_leak_response_question,
    is_suspicious_login_question,
    is_suspicious_link_question,
    is_suspicious_email_question,
    is_compromised_account_question,
    is_ransomware_response_question,
    is_encrypted_files_possible_ransomware_question,
    is_ransomware_or_malware_question,
)
from language import localize_section_name
from text_utils import normalize_query_text


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


def generate_copy_ready_incident_summary(question, best_match, search_results, language="English", answer_html=None):
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

    answer_source = answer_html or ""
    answer_text = strip_download_answer_heading(
        clean_answer_for_download(
            html_to_plain_text(answer_source),
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

