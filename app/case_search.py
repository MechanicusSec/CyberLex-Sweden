from pathlib import Path
import re

CASES_DIR = Path("cases")


def read_markdown_file(path):
    return path.read_text(encoding="utf-8")


def get_title(content, fallback):
    for line in content.splitlines():
        if line.startswith("# "):
            return line.replace("# ", "", 1).strip()

    return fallback.replace("_", " ").title()


def get_section(content, heading):
    lines = content.splitlines()
    in_section = False
    section = []

    for line in lines:
        stripped = line.strip()

        if stripped.lower() == heading.lower():
            in_section = True
            continue

        if in_section and stripped.startswith("## "):
            break

        if in_section:
            section.append(line)

    return "\n".join(section).strip()


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zåäö0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def get_keywords(question):
    stopwords = {
        "a", "an", "and", "are", "can", "do", "does", "for", "from",
        "how", "in", "is", "it", "of", "on", "or", "the", "to",
        "under", "was", "we", "what", "when", "where", "why", "with",
        "är", "att", "av", "de", "det", "en", "ett", "för", "från",
        "hur", "i", "kan", "med", "och", "om", "på", "som", "till",
        "vad", "var", "varför", "vi",
    }

    words = clean_text(question).split()
    keywords = []

    for word in words:
        if len(word) > 2 and word not in stopwords:
            keywords.append(word)

    expansions = {
        "meta": ["meta", "pixel", "tracking"],
        "pixel": ["meta", "pixel", "tracking"],
        "tracking": ["tracking", "pixel", "analytics"],
        "säkerhet": ["säkerhet", "säkerhetsåtgärder", "security"],
        "security": ["security", "measures", "access"],
        "läcka": ["läcka", "leak", "breach", "incident"],
        "breach": ["breach", "leak", "incident"],
        "fine": ["fine", "cost", "sek", "sanktionsavgift"],
        "cost": ["cost", "fine", "sek"],
        "gdpr": ["gdpr", "imy", "personuppgifter"],
        "web": ["web", "form", "website"],
        "form": ["form", "web"],
    }

    expanded = []

    for keyword in keywords:
        expanded.append(keyword)

        if keyword in expansions:
            expanded.extend(expansions[keyword])

    return sorted(set(expanded))


def load_cases():
    if not CASES_DIR.exists():
        return []

    cases = []

    for path in sorted(CASES_DIR.glob("*.md")):
        if path.name in ["CASE_TEMPLATE.md", "CASE_INDEX.md"]:
            continue

        content = read_markdown_file(path)

        cases.append(
            {
                "filename": path.name,
                "title": get_title(content, path.stem),
                "summary": get_section(content, "## Short summary"),
                "fine_or_cost": get_section(content, "## Fine or cost"),
                "official_source": get_section(content, "## Official source"),
                "content": content,
            }
        )

    return cases


def score_case(question, case):
    keywords = get_keywords(question)

    question_clean = clean_text(question)
    title_clean = clean_text(case["title"])
    summary_clean = clean_text(case["summary"])
    fine_clean = clean_text(case["fine_or_cost"])
    content_clean = clean_text(case["content"])

    searchable_text = (
        title_clean
        + " "
        + summary_clean
        + " "
        + fine_clean
        + " "
        + content_clean
    )

    score = 0

    for keyword in keywords:
        cleaned_keyword = clean_text(keyword)

        if not cleaned_keyword:
            continue

        if cleaned_keyword in title_clean:
            score += 8

        if cleaned_keyword in summary_clean:
            score += 4

        if cleaned_keyword in searchable_text:
            score += 1

    # Strong phrase-based boosts.
    # This helps CyberLex prefer the most obviously relevant case.
    if "web form" in question_clean or "form" in question_clean:
        if "web form" in title_clean or "web form" in summary_clean or "web form" in content_clean:
            score += 20

    if "meta pixel" in question_clean or "meta" in question_clean or "pixel" in question_clean:
        if "meta pixel" in title_clean or "meta pixel" in summary_clean or "meta pixel" in content_clean:
            score += 20

    if "security measures" in question_clean or "weak security" in question_clean or "security" in question_clean:
        if "security deficiencies" in title_clean or "security measures" in summary_clean or "security flaws" in summary_clean:
            score += 20

    if "tracking" in question_clean or "analytics" in question_clean:
        if "tracking" in summary_clean or "analytics" in content_clean or "meta pixel" in content_clean:
            score += 10

    if "sensitive personal data" in question_clean or "sensitive" in question_clean:
        if "sensitive personal data" in summary_clean or "sensitive personal data" in content_clean:
            score += 12

    return score


def search_related_cases(question, limit=3):
    results = []

    for case in load_cases():
        score = score_case(question, case)

        if score > 0:
            results.append(
                {
                    "score": score,
                    "title": case["title"],
                    "filename": case["filename"],
                    "summary": case["summary"],
                    "fine_or_cost": case["fine_or_cost"],
                    "official_source": case["official_source"],
                }
            )

    results.sort(key=lambda item: item["score"], reverse=True)

    return results[:limit]


if __name__ == "__main__":
    questions = [
        "Can Meta Pixel create GDPR risk?",
        "What can weak security measures cost?",
        "Can a web form cause a personal data breach?",
        "Vad kan en GDPR-läcka kosta?",
    ]

    for question in questions:
        print()
        print("Question:", question)

        matches = search_related_cases(question)

        if not matches:
            print("No related cases found.")
            continue

        for match in matches:
            print("-", match["title"])
            print("  File:", match["filename"])
            print("  Score:", match["score"])