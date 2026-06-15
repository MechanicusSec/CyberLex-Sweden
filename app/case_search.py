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
    text = str(text or "").lower()

    replacements = {
        "meta-pixel": "meta pixel",
        "metapixel": "meta pixel",
        "e mail": "email",
        "e-mail": "email",
        "e-post": "email",
        "dark net": "darknet",
        "dark-web": "darkweb",
        "dark web": "darkweb",
        "trygg-hansa": "trygg hansa",
        "sport admin": "sportadmin",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"[^a-zåäö0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def contains_phrase(text, phrases):
    clean = clean_text(text)
    return any(clean_text(phrase) in clean for phrase in phrases)


def get_case_profile(case):
    filename = clean_text(case.get("filename", ""))
    title = clean_text(case.get("title", ""))
    combined = filename + " " + title + " " + clean_text(case.get("content", ""))

    if "kry" in combined:
        return "kry_meta_pixel"

    if "sportadmin" in combined:
        return "sportadmin_security_breach"

    if "wrong email" in combined or "wrong recipient" in combined or "indecap" in combined or "wrong email customer" in filename:
        return "wrong_email_customer_data"

    if "equality ombudsman" in combined or "web form" in title or "web form" in filename:
        return "equality_ombudsman_web_form"

    if "trygg hansa" in combined or "security deficiencies" in title:
        return "trygg_hansa_security_deficiencies"

    if "avanza" in combined:
        return "avanza_meta_pixel"

    if "apoteket" in combined or "apohem" in combined:
        return "apoteket_apohem_meta_pixel"

    return "generic_case"


def get_keywords(question):
    stopwords = {
        "a", "an", "and", "are", "as", "at", "be", "but", "by",
        "can", "could", "do", "does", "for", "from", "how", "if",
        "in", "into", "is", "it", "may", "might", "of", "on", "or",
        "our", "the", "their", "this", "to", "under", "was", "we",
        "what", "when", "where", "which", "who", "why", "with",
        "är", "att", "av", "de", "det", "en", "ett", "för", "från",
        "hur", "i", "kan", "med", "och", "om", "på", "som", "till",
        "vad", "var", "varför", "vi", "vår", "vårt", "våra",
    }

    words = clean_text(question).split()
    keywords = []

    for word in words:
        if len(word) > 2 and word not in stopwords:
            keywords.append(word)

    expansions = {
        # Tracking / Meta Pixel
        "meta": ["meta", "pixel", "meta pixel", "tracking", "analytics", "third party", "facebook"],
        "pixel": ["meta", "pixel", "meta pixel", "tracking", "analytics", "third party", "facebook"],
        "tracking": ["tracking", "pixel", "analytics", "website", "third party"],
        "analytics": ["analytics", "tracking", "website", "processor"],
        "spårning": ["tracking", "pixel", "analytics", "meta"],
        "analysverktyg": ["analytics", "tracking", "pixel", "meta"],

        # Kry / hashed-data context
        "hashed": ["hashed", "hash", "contact information", "kry", "meta pixel", "reprimand"],
        "hash": ["hashed", "hash", "contact information", "kry", "meta pixel", "reprimand"],
        "hashade": ["hashed", "hash", "contact information", "kry", "meta pixel", "reprimand"],
        "reprimand": ["reprimand", "kry", "meta pixel"],
        "vård": ["healthcare", "health", "kry", "meta pixel"],
        "healthcare": ["healthcare", "health", "kry", "meta pixel"],

        # Security / breach
        "security": ["security", "security measures", "measures", "access", "article 32"],
        "säkerhet": ["säkerhet", "säkerhetsåtgärder", "security", "article 32"],
        "säkerhetsåtgärder": ["säkerhetsåtgärder", "security measures", "article 32", "security"],
        "weak": ["weak", "deficiencies", "flaws", "security"],
        "bristande": ["bristande", "deficiencies", "säkerhet", "security"],

        # Data leaks / breaches
        "leak": ["leak", "breach", "incident", "exposure", "disclosure"],
        "läcka": ["läcka", "leak", "breach", "incident", "exposure"],
        "dataläcka": ["dataläcka", "data leak", "breach", "incident", "exposure"],
        "breach": ["breach", "leak", "incident", "exposure", "personal data"],
        "incident": ["incident", "breach", "security", "personal data"],
        "personuppgiftsincident": ["personuppgiftsincident", "personal data breach", "gdpr", "imy"],

        # Email / wrong recipient
        "email": ["email", "wrong recipient", "wrong attachment", "customer data", "excel", "indecap"],
        "mail": ["email", "wrong recipient", "wrong attachment", "customer data", "indecap"],
        "mejl": ["email", "wrong recipient", "wrong attachment", "kunduppgifter", "indecap"],
        "recipient": ["recipient", "wrong recipient", "email", "disclosure"],
        "attachment": ["attachment", "wrong attachment", "email", "excel"],
        "bilaga": ["attachment", "wrong attachment", "email", "excel"],
        "kunduppgifter": ["customer data", "kunduppgifter", "email", "wrong recipient"],
        "customer": ["customer", "customer data", "email", "wrong recipient"],

        # Darknet / cyber attack
        "darknet": ["darknet", "darkweb", "published", "cyber attack", "sportadmin"],
        "darkweb": ["darknet", "darkweb", "published", "cyber attack", "sportadmin"],
        "published": ["published", "darknet", "leak", "data breach", "sportadmin"],
        "publicerad": ["published", "darknet", "leak", "data breach", "sportadmin"],
        "attack": ["attack", "cyber attack", "breach", "security", "sportadmin"],
        "hacked": ["hacked", "cyber attack", "breach", "unauthorized access"],
        "hackad": ["hacked", "cyber attack", "breach", "unauthorized access"],

        # GDPR / authority / fines
        "gdpr": ["gdpr", "imy", "personal data", "personuppgifter"],
        "imy": ["imy", "gdpr", "administrative fine", "sanktionsavgift"],
        "fine": ["fine", "cost", "sek", "administrative fine", "sanktionsavgift"],
        "fines": ["fine", "cost", "sek", "administrative fine", "sanktionsavgift"],
        "cost": ["cost", "fine", "sek", "administrative fine", "sanktionsavgift"],
        "kostnad": ["cost", "fine", "sek", "sanktionsavgift"],
        "kosta": ["cost", "fine", "sek", "sanktionsavgift"],
        "sanktionsavgift": ["sanktionsavgift", "fine", "sek", "imy"],

        # Sensitive / health / children
        "sensitive": ["sensitive", "health", "children", "protected identity"],
        "känsliga": ["sensitive", "health", "children", "protected identity"],
        "health": ["health", "sensitive", "kry", "apoteket", "sportadmin"],
        "children": ["children", "young people", "sportadmin"],
        "barn": ["children", "young people", "sportadmin"],

        # Named cases
        "sportadmin": ["sportadmin", "cyber attack", "darknet", "children", "security"],
        "trygg": ["trygg hansa", "security deficiencies", "customer data", "accessible"],
        "hansa": ["trygg hansa", "security deficiencies", "customer data", "accessible"],
        "avanza": ["avanza", "meta pixel", "bank", "tracking"],
        "kry": ["kry", "meta pixel", "hashed", "healthcare", "reprimand"],
        "apoteket": ["apoteket", "apohem", "meta pixel", "sensitive personal data"],
        "apohem": ["apoteket", "apohem", "meta pixel", "sensitive personal data"],
        "indecap": ["indecap", "email", "customer data", "wrong attachment"],
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
        if path.name.upper() in {"CASE_TEMPLATE.MD", "CASE_INDEX.MD"}:
            continue

        content = read_markdown_file(path)

        cases.append(
            {
                "filename": path.name,
                "title": get_title(content, path.stem),
                "case_type": get_section(content, "## Case type"),
                "topic": get_section(content, "## Topic"),
                "summary": get_section(content, "## Short summary"),
                "what_happened": get_section(content, "## What happened"),
                "legal_issue": get_section(content, "## Legal issue"),
                "outcome": get_section(content, "## Decision or outcome"),
                "fine_or_cost": get_section(content, "## Fine or cost"),
                "why_it_matters": get_section(content, "## Why it matters for CyberLex"),
                "similar_questions": get_section(content, "## Similar CyberLex questions"),
                "related_topics": get_section(content, "## Related CyberLex topics"),
                "official_source": get_section(content, "## Official source"),
                "content": content,
            }
        )

    return cases




def get_case_priority(question, case):
    # Deterministic ranking layer for obvious case-library intents.
    # Keyword scoring is useful, but for a tiny curated case library we can be
    # clearer: a hashed Meta Pixel question should not rank Kry third like a
    # bureaucratic coin toss.
    question_clean = clean_text(question)
    profile = get_case_profile(case)

    asks_meta = contains_phrase(
        question_clean,
        ["meta pixel", "meta", "pixel", "tracking", "analytics", "spårning"],
    )
    asks_hashed_kry = contains_phrase(
        question_clean,
        [
            "hashed", "hash", "hashade", "hashed data", "hashed contact",
            "contact information", "kry", "healthcare", "vård", "reprimand",
        ],
    )
    asks_web_form = contains_phrase(
        question_clean,
        [
            "web form", "webform", "form", "complaint form", "tips",
            "complaints", "webbformulär", "formulär",
        ],
    )
    asks_wrong_email = contains_phrase(
        question_clean,
        [
            "wrong email", "wrong recipient", "wrong attachment",
            "sent customer data", "email by mistake", "customer data to the wrong",
            "fel mejl", "fel e-post", "fel mottagare", "fel bilaga",
            "skickat kunduppgifter fel",
        ],
    )
    asks_darknet = contains_phrase(
        question_clean,
        [
            "darknet", "darkweb", "published on the darknet",
            "publicerad på darknet", "data published", "data is published",
            "published data",
        ],
    )
    asks_cyber_attack = contains_phrase(
        question_clean,
        [
            "cyber attack", "it attack", "hacked", "hackad",
            "children", "young people", "barn", "unga",
        ],
    )
    asks_weak_security = contains_phrase(
        question_clean,
        [
            "weak security", "security measures", "security deficiencies",
            "security flaws", "bristande säkerhet", "säkerhetsåtgärder",
            "article 32",
        ],
    )
    asks_sensitive = contains_phrase(
        question_clean,
        [
            "sensitive personal data", "sensitive", "health data",
            "känsliga", "hälsa", "protected identity",
        ],
    )

    # Very specific intents first.
    if asks_hashed_kry and asks_meta:
        if profile == "kry_meta_pixel":
            return 1000
        if profile in {"apoteket_apohem_meta_pixel", "avanza_meta_pixel"}:
            return 600
        return 0

    if asks_wrong_email:
        if profile == "wrong_email_customer_data":
            return 1000
        return 0

    if asks_darknet or asks_cyber_attack:
        if profile == "sportadmin_security_breach":
            return 1000
        if profile == "trygg_hansa_security_deficiencies":
            return 500
        return 0

    if asks_web_form:
        if profile == "equality_ombudsman_web_form":
            return 1000
        return 0

    if asks_weak_security:
        if profile == "trygg_hansa_security_deficiencies":
            return 950
        if profile == "sportadmin_security_breach":
            return 900
        if profile == "equality_ombudsman_web_form":
            return 500
        return 0

    # General Meta Pixel questions.
    if asks_meta:
        if asks_sensitive and profile == "apoteket_apohem_meta_pixel":
            return 950
        if profile == "apoteket_apohem_meta_pixel":
            return 900
        if profile == "avanza_meta_pixel":
            return 850
        if profile == "kry_meta_pixel":
            return 800
        return 0

    return 0

def score_case(question, case):
    keywords = get_keywords(question)

    question_clean = clean_text(question)
    title_clean = clean_text(case.get("title", ""))
    filename_clean = clean_text(case.get("filename", ""))
    profile = get_case_profile(case)

    topic_clean = clean_text(case.get("topic", ""))
    summary_clean = clean_text(case.get("summary", ""))
    fine_clean = clean_text(case.get("fine_or_cost", ""))
    related_topics_clean = clean_text(case.get("related_topics", ""))
    similar_questions_clean = clean_text(case.get("similar_questions", ""))
    why_clean = clean_text(case.get("why_it_matters", ""))
    content_clean = clean_text(case.get("content", ""))

    searchable_text = " ".join(
        [
            filename_clean,
            title_clean,
            topic_clean,
            summary_clean,
            fine_clean,
            related_topics_clean,
            similar_questions_clean,
            why_clean,
            content_clean,
        ]
    )

    score = 0

    for keyword in keywords:
        cleaned_keyword = clean_text(keyword)

        if not cleaned_keyword:
            continue

        if cleaned_keyword in filename_clean:
            score += 14

        if cleaned_keyword in title_clean:
            score += 12

        if cleaned_keyword in topic_clean:
            score += 8

        if cleaned_keyword in related_topics_clean:
            score += 7

        if cleaned_keyword in similar_questions_clean:
            score += 6

        if cleaned_keyword in summary_clean:
            score += 5

        if cleaned_keyword in why_clean:
            score += 4

        if cleaned_keyword in fine_clean:
            score += 3

        if cleaned_keyword in searchable_text:
            score += 1

    # Strong profile-based boosts.
    # This is intentionally explicit. It keeps the case-library results useful
    # until CyberLex later gets real semantic/vector search. Yes, the future is
    # apparently held together by if-statements. Civilization had a good run.

    asks_meta = contains_phrase(question_clean, ["meta pixel", "meta", "pixel", "tracking", "analytics", "spårning"])
    asks_hashed_kry = contains_phrase(
        question_clean,
        ["hashed", "hash", "hashade", "hashed data", "hashed contact", "kry", "healthcare", "vård", "reprimand"],
    )
    asks_web_form = contains_phrase(
        question_clean,
        ["web form", "webform", "form", "complaint form", "tips", "complaints", "webbformulär", "formulär"],
    )
    asks_wrong_email = contains_phrase(
        question_clean,
        [
            "wrong email", "wrong recipient", "wrong attachment", "sent customer data",
            "email by mistake", "customer data to the wrong", "fel mejl", "fel e-post",
            "fel mottagare", "fel bilaga", "skickat kunduppgifter fel",
        ],
    )
    asks_darknet = contains_phrase(
        question_clean,
        ["darknet", "darkweb", "published on the darknet", "publicerad på darknet", "data published", "data is published"],
    )
    asks_cyber_attack = contains_phrase(
        question_clean,
        ["cyber attack", "it attack", "hacked", "hackad", "children", "young people", "barn", "unga"],
    )
    asks_weak_security = contains_phrase(
        question_clean,
        [
            "weak security", "security measures", "security deficiencies", "security flaws",
            "bristande säkerhet", "säkerhetsåtgärder", "article 32",
        ],
    )
    asks_cost = contains_phrase(
        question_clean,
        ["cost", "fine", "fines", "sanktionsavgift", "kostnad", "kosta", "sek"],
    )
    asks_breach = contains_phrase(
        question_clean,
        ["personal data breach", "data breach", "data leak", "dataläcka", "personuppgiftsincident", "personal data exposed", "leak"],
    )
    asks_sensitive = contains_phrase(
        question_clean,
        ["sensitive personal data", "sensitive", "health data", "känsliga", "hälsa", "protected identity"],
    )

    # Kry must win when the question says hashed + Meta Pixel.
    if asks_hashed_kry and asks_meta:
        if profile == "kry_meta_pixel":
            score += 500
        elif profile in {"apoteket_apohem_meta_pixel", "avanza_meta_pixel"}:
            score += 25
            score -= 40
        elif profile == "equality_ombudsman_web_form":
            score -= 80

    # General Meta Pixel cluster.
    elif asks_meta:
        if profile in {"apoteket_apohem_meta_pixel", "avanza_meta_pixel", "kry_meta_pixel"}:
            score += 45

        if asks_sensitive and profile == "apoteket_apohem_meta_pixel":
            score += 25

    # Web form should not drag in Meta Pixel unless it truly matches.
    if asks_web_form:
        if profile == "equality_ombudsman_web_form":
            score += 110
        elif profile in {"apoteket_apohem_meta_pixel", "avanza_meta_pixel", "kry_meta_pixel"}:
            score -= 20

    # Wrong email should clearly route to the wrong-email case.
    if asks_wrong_email:
        if profile == "wrong_email_customer_data":
            score += 120
        else:
            score -= 15

    # Darknet and large cyberattack questions should lead with Sportadmin.
    if asks_darknet or asks_cyber_attack:
        if profile == "sportadmin_security_breach":
            score += 120
        elif profile == "trygg_hansa_security_deficiencies":
            score += 15
        else:
            score -= 10

    # Weak security should prioritize Trygg-Hansa and Sportadmin.
    if asks_weak_security:
        if profile in {"trygg_hansa_security_deficiencies", "sportadmin_security_breach"}:
            score += 85
        elif profile == "equality_ombudsman_web_form":
            score += 35

    # Fine/cost questions should prefer cases with clear amounts.
    if asks_cost:
        if "sek" in fine_clean or "administrative fine" in fine_clean or "sanktionsavgift" in fine_clean:
            score += 20

        if profile == "kry_meta_pixel" and "reprimand" in fine_clean:
            score += 8

    # Personal-data breach generally should prefer actual breach/disclosure cases.
    if asks_breach:
        if profile in {
            "sportadmin_security_breach",
            "wrong_email_customer_data",
            "equality_ombudsman_web_form",
            "trygg_hansa_security_deficiencies",
        }:
            score += 35

        if contains_phrase(content_clean, ["personal data breach", "data leak", "personuppgiftsincident"]):
            score += 10

    # Sensitive data should prioritize sensitive-data cases.
    if asks_sensitive:
        if profile in {"apoteket_apohem_meta_pixel", "sportadmin_security_breach", "kry_meta_pixel"}:
            score += 35

    return max(score, 0)


def search_related_cases(question, limit=3):
    results = []

    for case in load_cases():
        score = score_case(question, case)
        priority = get_case_priority(question, case)

        if score > 0 or priority > 0:
            results.append(
                {
                    "score": score,
                    "priority": priority,
                    "title": case["title"],
                    "filename": case["filename"],
                    "summary": case["summary"],
                    "fine_or_cost": case["fine_or_cost"],
                    "official_source": case["official_source"],
                    "related_topics": case.get("related_topics", ""),
                }
            )

    results.sort(
        key=lambda item: (
            item["priority"],
            item["score"],
            item["title"],
        ),
        reverse=True,
    )

    # Keep the public result shape stable for main.py.
    for result in results:
        result.pop("priority", None)

    return results[:limit]


if __name__ == "__main__":
    questions = [
        "Can Meta Pixel create GDPR risk?",
        "What can weak security measures cost?",
        "Can a web form cause a personal data breach?",
        "Vad kan en GDPR-läcka kosta?",
        "Can sending customer data to the wrong email be a personal data breach?",
        "What happens if data is published on the Darknet?",
        "Can hashed data sent through Meta Pixel be a GDPR issue?",
        "Kan ett företag få sanktionsavgift efter ett dataintrång?",
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
