from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="CyberLex Sweden",
    page_icon="💻",
    layout="wide"
)

DATA_DIR = Path("data")


def clean_words(text):
    # Converts text into simple searchable lowercase words.
    punctuation = ",.?!:;()[]{}\"'`"
    text = text.lower()

    for mark in punctuation:
        text = text.replace(mark, " ")

    return text.split()


def extract_official_sources(content):
    # Extracts URLs from the "## official source" section of a Markdown document.
    lines = content.splitlines()
    sources = []
    in_official_source_section = False

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.lower() == "## official source":
            in_official_source_section = True
            continue

        if in_official_source_section and stripped_line.startswith("## "):
            break

        if in_official_source_section and stripped_line.startswith("http"):
            sources.append(stripped_line)

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
    source_date = extract_section_text(content, "## Source date")
    version_notes = extract_section_text(content, "## Version notes")

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
    question_lower = question.lower().strip()

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

    if (
        "nis2 incident reporting" in question_lower
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
        "third-party ict risk"
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

    question_lower = question.lower()
    target_source_file = get_target_source_file(question)

    question_words = [
        word for word in clean_words(question)
        if len(word) > 2 and word not in stopwords
    ]

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

        if "reported" in question_lower or "report" in question_lower or "72" in question_lower or "rapportera" in question_lower:
            if "reporting" in section_text:
                score += 25
            if "72 hours" in chunk_text or "72 timmar" in chunk_text:
                score += 10

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


def generate_simple_answer(question, best_match, language="English"):
    # Generates a simple source-based answer from the best matching chunk.
    question_lower = question.lower()
    use_swedish = language == "Svenska"

    if (
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
                "Dataintrång means data intrusion under Swedish criminal law. "
                "It is connected to unauthorized access to, or interference with, data or information systems."
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

    source_lines = "\n".join(
        [f"- {source}" for source in best_match.get("official_sources", [])]
    )

    if not source_lines:
        source_lines = "- No official source URL stored for this document yet."

    source_date = best_match.get("source_date", "No source date stored.")
    version_notes = best_match.get("version_notes", "No version notes stored.")

    if use_swedish:
        short_answer_heading = "Kort svar"
        citation_heading = "Källhänvisning"
        matched_file_label = "Matchad kunskapsfil"
        matched_section_label = "Matchad sektion"
        relevance_score_label = "Relevanspoäng"
        official_sources_heading = "Officiella källor"
        metadata_heading = "Källmetadata"
        source_date_label = "Källdatum"
        version_notes_label = "Versionsanteckningar"
        limitation_heading = "Viktig begränsning"
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
        official_sources_heading = "Official source links"
        metadata_heading = "Source metadata"
        source_date_label = "Source date"
        version_notes_label = "Version notes"
        limitation_heading = "Important limitation"
        limitation_text = (
            "This answer is generated from a simplified local knowledge base. "
            "CyberLex Sweden is an educational project and does not provide legal advice."
        )

    return (
        f"## {short_answer_heading}\n\n"
        f"{answer}\n\n"
        f"## {citation_heading}\n\n"
        f"**{matched_file_label}:** `{best_match['filename']}`\n\n"
        f"**{matched_section_label}:** `{best_match['section']}`\n\n"
        f"**{relevance_score_label}:** `{best_match['score']}`\n\n"
        f"## {official_sources_heading}\n\n"
        f"{source_lines}\n\n"
        f"## {metadata_heading}\n\n"
        f"- {source_date_label}: {source_date}\n"
        f"- {version_notes_label}: {version_notes}\n\n"
        f"## {limitation_heading}\n\n"
        f"{limitation_text}"
    )


def is_cyberlaw_question(question):
    # Checks whether the user question belongs to the CyberLex Sweden project scope.
    allowed_keywords = {
        "vad är",
        "svensk cybersäkerhetsrätt",
        "cybersäkerhet",
        "cyberbrott",
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

    question_lower = question.lower()

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
    </style>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-header"><h1>CyberLex Sweden</h1><p>Source-grounded assistant for Swedish and EU cybersecurity law, digital compliance, and legal-tech research.</p></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-card">'
    '<strong>What CyberLex does:</strong><br>'
    'CyberLex Sweden searches a trusted local knowledge base and gives source-based answers with citation details, '
    'official source links, source metadata, and matched source excerpts.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("### Supported topic areas")

st.markdown(
    '<span class="topic-badge">GDPR</span>'
    '<span class="topic-badge">IMY</span>'
    '<span class="topic-badge">Personal data breaches</span>'
    '<span class="topic-badge">NIS2</span>'
    '<span class="topic-badge">Swedish Cybersecurity Act</span>'
    '<span class="topic-badge">Dataintrång</span>'
    '<span class="topic-badge">EU Cyber Resilience Act</span>'
    '<span class="topic-badge">DORA</span>'
    '<span class="topic-badge">Digital compliance</span>',
    unsafe_allow_html=True
)

st.warning(
    "Important: CyberLex Sweden is an educational project. "
    "It does not provide official legal advice and should not replace a qualified lawyer or official authority guidance."
)

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
        "dataintrång", "brott", "tillsyn", "ansvarar"
    }

    question_words = set(clean_words(question_lower))

    if question_words.intersection(swedish_markers):
        return "Svenska"

    return "English"


documents, chunks = load_chunks()

language_mode = st.sidebar.selectbox(
    "Language / Språk",
    ["Auto", "English", "Svenska"]
)

if language_mode == "Svenska":
    ask_heading = "Ställ en fråga"
    question_label = "Skriv en fråga om svensk cybersäkerhetsrätt:"
elif language_mode == "English":
    ask_heading = "Ask a question"
    question_label = "Write a question about Swedish cybersecurity law:"
else:
    ask_heading = "Ask a question / Ställ en fråga"
    question_label = "Write a question about Swedish cybersecurity law / Skriv en fråga om svensk cybersäkerhetsrätt:"

st.sidebar.header("CyberLex Status")
st.sidebar.write(f"📄 Loaded documents: {len(documents)}")
st.sidebar.write(f"🧩 Searchable chunks: {len(chunks)}")

st.sidebar.markdown("---")
st.sidebar.subheader("Prototype mode")
st.sidebar.write(
    "CyberLex currently uses local Markdown files, source routing, keyword ranking, "
    "and rule-based answer generation."
)

st.sidebar.markdown("---")
st.sidebar.subheader("Project resources")

st.sidebar.markdown(
    "- `docs/terms_of_use.md`\n"
    "- `docs/privacy_policy.md`\n"
    "- `docs/legal_disclaimer.md`\n"
    "- `docs/source_policy.md`\n"
    "- `docs/source_update_history.md`\n"
    "- `docs/product_roadmap.md`\n"
    "- `docs/technical_design.md`"
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "CyberLex Sweden is an educational prototype and does not provide legal advice."
)

st.sidebar.markdown("---")
st.sidebar.subheader("Documents")
for doc in documents:
    st.sidebar.write(f"- {doc['filename']}")

st.header(ask_heading)

question = st.text_input(question_label)

if language_mode == "Auto" and question:
    language = detect_question_language(question)
elif language_mode == "Svenska":
    language = "Svenska"
else:
    language = "English"

if language == "Svenska":
    empty_question_text = "Skriv en fråga ovan för att söka i CyberLex Swedens kunskapsbas."
    out_of_scope_text = (
        "Ingen betrodd källa hittades för denna fråga. "
        "CyberLex Sweden täcker bara svensk cybersäkerhetsrätt, cyberbrott, GDPR, NIS2, "
        "incidentrapportering, dataskydd, EU-cybersäkerhet och relaterade digitala compliance-frågor."
    )
    answer_header = "CyberLex svar"
    excerpt_header = "Matchat källutdrag"
    excerpt_caption = "Detta är den exakta källsektion som CyberLex använde för svaret."
    source_area_label = "Relevant källsektion"
    other_matches_header = "Andra matchande källsektioner"
    other_matches_caption = "Detta är ytterligare källsektioner som matchade frågan, sorterade efter relevans."
else:
    empty_question_text = "Enter a question above to search the CyberLex Sweden knowledge base."
    out_of_scope_text = (
        "No trusted source was found for this question. "
        "CyberLex Sweden only covers Swedish cybersecurity law, cybercrime, GDPR, NIS2, "
        "incident reporting, data protection, EU cybersecurity law, and related digital compliance topics."
    )
    answer_header = "CyberLex Answer"
    excerpt_header = "Matched source excerpt"
    excerpt_caption = "This is the exact source section CyberLex used for the answer."
    source_area_label = "Relevant source section"
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
                st.subheader("CyberLex Answer")
                st.markdown(generate_simple_answer(question, best_match, language))

                st.subheader(matched_excerpt_heading)
                st.caption(matched_excerpt_caption)

                st.text_area(
                    relevant_section_label,
                    best_match["content"],
                    height=260
                )

                st.subheader(other_matches_header)
                st.caption(other_matches_caption)

                for result in search_results[:5]:
                    if language == "Svenska":
                        st.write(
                            f"**{result['filename']}** | "
                            f"Sektion: **{result['section']}** | "
                            f"Relevanspoäng: `{result['score']}`"
                        )
                    else:
                        st.write(
                            f"**{result['filename']}** | "
                            f"Section: **{result['section']}** | "
                            f"Relevance score: `{result['score']}`"
                        )
        else:
            st.error(out_of_scope_text)
else:
    st.write(empty_question_text)
