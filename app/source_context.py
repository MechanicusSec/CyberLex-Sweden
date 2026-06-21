import re

from language import localize_section_name
from routing import (
    is_imy_gdpr_security_measures_question,
    is_gdpr_security_guidance_question,
    is_gdpr_assessment_or_security_file,
    is_nis2_sector_scope_question,
    filter_source_context_by_incident_type,
    is_nis2_scope_allowed_context_section,
    get_nis2_scope_max_context_cards,
    get_nis2_scope_source_context_priority,
    prioritize_source_context_results,
)


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





