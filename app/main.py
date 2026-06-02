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
    # Extracts official source links from the "## Official source" section.
    # Supports both raw URLs and Markdown links:
    # https://example.com
    # [Source name](https://example.com)

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

        if not in_official_source_section:
            continue

        if stripped_line.startswith("[") and "](" in stripped_line and stripped_line.endswith(")"):
            label = stripped_line.split("](", 1)[0].replace("[", "").strip()
            url = stripped_line.split("](", 1)[1].replace(")", "").strip()

            if label and url.startswith("http"):
                sources.append(
                    {
                        "label": label,
                        "url": url
                    }
                )

        elif stripped_line.startswith("http"):
            sources.append(
                {
                    "label": stripped_line,
                    "url": stripped_line
                }
            )

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

def build_source_context(search_results, language="English", max_results=3):
    # Builds a short source context summary from the top matched source sections.
    # This helps CyberLex show useful supporting material without using an AI model.
    # It also removes repeated Markdown headings from excerpts to avoid duplicate titles.

    use_swedish = language == "Svenska"

    if use_swedish:
        context_heading = "Relevant källkontext"
        file_label = "Källa"
        section_label = "Sektion"
        score_label = "Relevanspoäng"
        excerpt_label = "Kort utdrag"
    else:
        context_heading = "Relevant source context"
        file_label = "Source"
        section_label = "Section"
        score_label = "Relevance score"
        excerpt_label = "Short excerpt"

    context_blocks = []

    for result in search_results[:max_results]:
        excerpt_lines = result["content"].strip().splitlines()

        # Remove the first Markdown heading if the excerpt already starts with one.
        # Example: "## Reporting to IMY" is removed because the section title is already shown.
        if excerpt_lines and excerpt_lines[0].strip().startswith("#"):
            excerpt_lines = excerpt_lines[1:]

        excerpt = "\n".join(excerpt_lines).strip()

        if len(excerpt) > 700:
            excerpt = excerpt[:700].rsplit(" ", 1)[0] + "..."

        context_blocks.append(
            f"### {result['section']}\n\n"
            f"- **{file_label}:** `{result['filename']}`\n"
            f"- **{section_label}:** `{result['section']}`\n"
            f"- **{score_label}:** `{result['score']}`\n\n"
            f"**{excerpt_label}:**\n\n"
            f"{excerpt}\n"
        )

    return "\n".join(context_blocks)

def generate_practical_explanation(question, search_results, language="English"):
    # Generates a practical explanation based on the question and matched source sections.
    # This is still rule-based and source-grounded. It does not use an external AI model.

    question_lower = question.lower()
    use_swedish = language == "Svenska"

    if use_swedish:
        heading = "Praktisk förklaring"

        if "personal data breach" in question_lower or "personuppgiftsincident" in question_lower or "72" in question_lower:
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

        if "personal data breach" in question_lower or "breach" in question_lower or "72" in question_lower:
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

    return f"## {heading}\n\n{explanation}"

def generate_assessment_checklist(question, search_results, language="English"):
    # Generates a simple assessment checklist based on the user's question.
    # This is not legal advice. It gives the user a structured way to review the issue.

    question_lower = question.lower()
    use_swedish = language == "Svenska"

    if use_swedish:
        heading = "CyberLex bedömningschecklista"

        if "personal data breach" in question_lower or "personuppgiftsincident" in question_lower or "72" in question_lower:
            items = [
                "Identifiera om incidenten berör personuppgifter.",
                "Bedöm om incidenten kan innebära risk för registrerade personers rättigheter och friheter.",
                "Kontrollera när organisationen blev medveten om incidenten.",
                "Bedöm om anmälan till IMY kan vara relevant.",
                "Dokumentera beslut, tidslinje, åtgärder och källor."
            ]

        elif ("nis2" in question_lower or "cybersäkerhetslagen" in question_lower) and "gdpr" in question_lower:
            items = [
                "Bedöm om incidenten är en cybersäkerhetsincident.",
                "Bedöm om incidenten även påverkar personuppgifter.",
                "Kontrollera om NIS2/cybersäkerhetslagen och GDPR kan vara relevanta samtidigt.",
                "Identifiera vilka myndigheter eller rapporteringsvägar som kan behöva bedömas.",
                "Dokumentera varför incidenten omfattas eller inte omfattas av respektive regelverk."
            ]

        elif "nis2" in question_lower or "cybersäkerhetslagen" in question_lower:
            items = [
                "Identifiera om organisationen kan omfattas av NIS2 eller svensk cybersäkerhetslag.",
                "Bedöm om incidenten är betydande eller rapporteringspliktig enligt relevanta kriterier.",
                "Kontrollera sektor, verksamhetstyp och ansvarig funktion.",
                "Dokumentera teknisk påverkan, tidslinje och vidtagna åtgärder.",
                "Jämför bedömningen med aktuella MSB-källor."
            ]

        elif "dora" in question_lower or "digital operational resilience" in question_lower:
            items = [
                "Identifiera om verksamheten tillhör den finansiella sektorn.",
                "Bedöm om frågan gäller ICT-risk, incidenthantering, testning eller tredjepartsleverantörer.",
                "Kontrollera om en ICT-relaterad incident eller störning föreligger.",
                "Dokumentera påverkan på digital operativ motståndskraft.",
                "Jämför bedömningen med DORA-källor och relevanta tillsynsmyndigheter."
            ]

        elif "dataintrång" in question_lower or "unauthorized access" in question_lower or "obehörig åtkomst" in question_lower:
            items = [
                "Identifiera vilken åtkomst eller påverkan som skett.",
                "Bedöm om åtkomsten var behörig eller obehörig.",
                "Skilj mellan tillåten säkerhetstestning och otillåten aktivitet.",
                "Dokumentera system, konton, loggar och tidslinje.",
                "Jämför situationen med svenska straffrättsliga källor."
            ]

        elif "cyber resilience act" in question_lower or "cyberresiliensakten" in question_lower:
            items = [
                "Identifiera om frågan gäller en produkt med digitala element.",
                "Bedöm om produktdesign, säkerhetskrav eller sårbarhetshantering påverkas.",
                "Kontrollera ansvar för tillverkare, leverantör eller annan aktör.",
                "Dokumentera säkerhetsåtgärder, uppdateringar och sårbarhetsprocesser.",
                "Jämför bedömningen med Cyber Resilience Act-källor."
            ]

        else:
            items = [
                "Identifiera vilken cyberrättslig eller compliance-fråga som ställs.",
                "Kontrollera vilka källsektioner CyberLex matchade.",
                "Läs den praktiska förklaringen tillsammans med källkontexten.",
                "Kontrollera officiella källor och källdatum.",
                "Sök juridisk eller myndighetsbaserad vägledning vid viktiga beslut."
            ]

    else:
        heading = "CyberLex assessment checklist"

        if "personal data breach" in question_lower or "breach" in question_lower or "72" in question_lower:
            items = [
                "Identify whether the incident involves personal data.",
                "Assess whether the incident may create risk to individuals' rights and freedoms.",
                "Check when the organization became aware of the incident.",
                "Assess whether notification to IMY may be relevant.",
                "Document the decision, timeline, actions, and sources."
            ]

        elif ("nis2" in question_lower or "cybersecurity act" in question_lower) and "gdpr" in question_lower:
            items = [
                "Assess whether the incident is a cybersecurity incident.",
                "Assess whether the incident also affects personal data.",
                "Check whether NIS2/the Swedish Cybersecurity Act and GDPR may both be relevant.",
                "Identify which authorities or reporting paths may need to be considered.",
                "Document why each legal framework is or is not relevant."
            ]

        elif "nis2" in question_lower or "cybersecurity act" in question_lower:
            items = [
                "Identify whether the organization may be covered by NIS2 or Swedish cybersecurity rules.",
                "Assess whether the incident may be significant or reportable under relevant criteria.",
                "Check the sector, organization type, and responsible internal function.",
                "Document technical impact, timeline, and actions taken.",
                "Compare the assessment with current MSB source material."
            ]

        elif "dora" in question_lower or "digital operational resilience" in question_lower:
            items = [
                "Identify whether the organization belongs to the financial sector.",
                "Assess whether the issue concerns ICT risk, incident handling, testing, or third-party providers.",
                "Check whether an ICT-related incident or disruption exists.",
                "Document the impact on digital operational resilience.",
                "Compare the assessment with DORA sources and relevant supervisory guidance."
            ]

        elif "dataintrång" in question_lower or "unauthorized access" in question_lower or "data intrusion" in question_lower:
            items = [
                "Identify what access or interference occurred.",
                "Assess whether the access was authorized or unauthorized.",
                "Separate authorized security testing from unauthorized activity.",
                "Document systems, accounts, logs, and timeline.",
                "Compare the situation with Swedish criminal-law source material."
            ]

        elif "cyber resilience act" in question_lower or "products with digital elements" in question_lower:
            items = [
                "Identify whether the question concerns a product with digital elements.",
                "Assess whether product design, security requirements, or vulnerability handling are affected.",
                "Check responsibility for the manufacturer, supplier, or other actor.",
                "Document security measures, updates, and vulnerability processes.",
                "Compare the assessment with Cyber Resilience Act sources."
            ]

        else:
            items = [
                "Identify the cybersecurity law or compliance issue.",
                "Check which source sections CyberLex matched.",
                "Read the practical explanation together with the source context.",
                "Check official sources and source dates.",
                "Use legal or authority-based guidance for important decisions."
            ]

    checklist_lines = "\n".join([f"- {item}" for item in items])

    return checklist_lines

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
        "dora"
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

    official_sources = best_match.get("official_sources", [])

    source_lines = "\n".join(
        [
            f"- [{source['label']}]({source['url']})"
            for source in official_sources
        ]
    )

    if not source_lines:
        if use_swedish:
            source_lines = "- Ingen officiell källänk är sparad för detta dokument ännu."
        else:
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
        "dataintrång", "brott", "tillsyn", "ansvarar"
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
    st.sidebar.write("🛠️ Prototypversion: `0.4`")
    st.sidebar.write("🏷️ Byggtyp: Lokal utbildningsprototyp")
else:
    st.sidebar.write("🛠️ Prototype version: `0.4`")
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
        "Vad är Cyber Resilience Act?"
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
        "What is the Cyber Resilience Act?"
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
                st.markdown(generate_simple_answer(question, best_match, language))
                st.markdown(
                    generate_attention_level(question, search_results, language),
                    unsafe_allow_html=True
                )
                st.markdown(generate_practical_explanation(question, search_results, language))

                with st.expander(
                    "CyberLex assessment checklist" if language != "Svenska" else "CyberLex bedömningschecklista",
                    expanded=False
                ):
                    st.markdown(generate_assessment_checklist(question, search_results, language))

                with st.expander(
                    "Relevant source context" if language != "Svenska" else "Relevant källkontext",
                    expanded=False
                ):
                    st.caption(source_context_caption)
                    st.markdown(build_source_context(search_results, language, max_results=3))

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
