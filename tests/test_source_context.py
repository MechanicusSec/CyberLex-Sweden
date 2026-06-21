import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1] / "app"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from source_context import (
    clean_source_excerpt,
    get_friendly_source_area_name,
    split_source_excerpt_for_display,
)


def test_clean_source_excerpt_removes_internal_helper_text():
    content = """
# Suspicious login guidance

Use this section when the user asks:
- What should we do about a suspicious login?

Start by preserving sign-in logs and confirming whether the activity was legitimate.
Document the account, source IP, device, and timestamp.
"""

    excerpt = clean_source_excerpt(content, section_name="Suspicious login", language="English")

    assert "Use this section when" not in excerpt
    assert "What should we do" not in excerpt
    assert "preserving sign-in logs" in excerpt


def test_source_excerpt_display_shortens_long_excerpt():
    excerpt = "\n".join([f"Line {number}" for number in range(1, 12)])

    display = split_source_excerpt_for_display(excerpt, language="English", max_visible_lines=4)

    assert display["was_shortened"] is True
    assert "Line 1" in display["short_excerpt"]
    assert "Line 5" not in display["short_excerpt"]
    assert display["details_label"] == "Show more source text"


def test_friendly_source_area_name_handles_incident_playbook_swedish():
    source_area = get_friendly_source_area_name(
        "cyber_incident_response_playbook.md",
        language="Svenska",
    )

    assert source_area == "Cyberincidenthantering"
