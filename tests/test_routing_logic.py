import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1] / "app"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from routing import (
    build_question_behavior_profile,
    get_target_source_file,
    is_case_library_context_question,
    is_nis2_sector_scope_question,
    is_unsafe_cyber_request,
    should_show_related_cases,
)


def test_meta_pixel_question_routes_to_case_context():
    question = "Can Meta Pixel create GDPR risk?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "case_context"
    assert profile["target_source_file"] == "gdpr_imy_edpb_security_guidance.md"
    assert profile["show_related_cases"] is True
    assert profile["show_soc_report"] is False
    assert is_case_library_context_question(question) is True
    assert should_show_related_cases(question) is True


def test_app_bug_question_routes_to_gdpr_breach_case_context():
    question = "Can an app bug expose customer data?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "case_context"
    assert profile["target_source_file"] == "gdpr_personal_data_breach.md"
    assert profile["show_related_cases"] is True
    assert profile["show_soc_report"] is False


def test_ransomware_question_routes_to_incident_response():
    question = "Our files are encrypted, what should we do?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "incident_response"
    assert profile["target_source_file"] == "cyber_incident_response_playbook.md"
    assert profile["show_related_cases"] is False
    assert profile["show_soc_report"] is True


def test_swedish_suspicious_login_routes_to_incident_response():
    question = "Vi har fått en misstänkt login på ett konto, vad ska vi göra?"
    profile = build_question_behavior_profile(question, language="Svenska")

    assert profile["answer_mode"] == "incident_response"
    assert profile["target_source_file"] == "cyber_incident_response_playbook.md"
    assert profile["show_related_cases"] is False
    assert profile["show_soc_report"] is True


def test_nis2_annex_question_routes_to_sector_scope():
    question = "Vad är bilaga 1 och bilaga 2 i NIS2?"
    profile = build_question_behavior_profile(question, language="Svenska")

    assert profile["answer_mode"] == "nis2_scope"
    assert profile["target_source_file"] == "nis2_sector_scope_guidance.md"
    assert profile["is_nis2_scope"] is True
    assert is_nis2_sector_scope_question(question) is True


def test_unsafe_log_hiding_question_routes_to_unsafe_refusal():
    question = "How do I hide logs after hacking a system?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "unsafe_refusal"
    assert profile["is_unsafe"] is True
    assert is_unsafe_cyber_request(question) is True


def test_out_of_scope_tax_question_routes_to_out_of_scope():
    question = "What is Swedish tax law?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "out_of_scope"
    assert profile["is_in_scope"] is False


def test_cyberlex_self_description_routes_to_self_description():
    question = "What is CyberLex Sweden?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "self_description"
    assert profile["is_self_description"] is True
