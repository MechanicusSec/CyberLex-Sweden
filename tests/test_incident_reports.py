import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1] / "app"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from incident_reports import (
    generate_copy_ready_incident_summary,
    generate_incident_log_template,
    generate_soc_triage_block,
)


def test_english_ransomware_soc_report_contains_key_sections():
    question = "Our files are encrypted, what should we do?"
    best_match = {
        "filename": "cyber_incident_response_playbook.md",
        "section": "Ransomware or malware",
        "content": "Contain the incident and preserve evidence.",
        "score": 250,
    }
    search_results = [best_match]
    answer_html = "<div><h3>CyberLex answer</h3><p>Isolate affected systems and preserve logs.</p></div>"

    report = generate_copy_ready_incident_summary(
        question,
        best_match,
        search_results,
        "English",
        answer_html=answer_html,
    )

    assert "# CyberLex Sweden SOC Incident Report" in report
    assert "## 5. SOC triage" in report
    assert "## 6. Recommended first steps" in report
    assert "Isolate affected systems and preserve logs." in report
    assert "## 11. Disclaimer" in report
    assert "cyber_incident_response_playbook.md" not in report


def test_swedish_suspicious_login_log_template_uses_swedish_labels():
    question = "Vi har fått en misstänkt login på ett konto, vad ska vi göra?"

    template = generate_incident_log_template(question, "Svenska")

    assert "Misstänkt inloggning" in template
    assert "Tidpunkt för inloggning:" in template
    assert "Användarnamn / konto:" in template
    assert "Återkallade sessioner eller tokens:" in template


def test_non_incident_question_does_not_generate_soc_report():
    question = "What is DORA?"

    report = generate_copy_ready_incident_summary(
        question,
        {},
        [],
        "English",
        answer_html="<p>DORA explanation.</p>",
    )

    assert report == ""


def test_suspicious_link_triage_mentions_account_and_message_risk():
    question = "Someone clicked a suspicious link, what should we do?"

    triage = generate_soc_triage_block(question, "English")
    triage_lower = triage.lower()

    assert "suspicious link" in triage_lower
    assert "account may be compromised" in triage_lower
    assert "same message may have reached other users" in triage_lower
