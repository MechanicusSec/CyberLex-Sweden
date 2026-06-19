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
    assert get_target_source_file(question) == "gdpr_imy_edpb_security_guidance.md"


def test_swedish_meta_pixel_question_routes_to_case_context():
    question = "Kan Meta Pixel skapa GDPR-risk?"
    profile = build_question_behavior_profile(question, language="Svenska")

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
    assert get_target_source_file(question) == "gdpr_personal_data_breach.md"


def test_swedish_app_bug_question_routes_to_gdpr_breach_case_context():
    question = "Kan ett appfel exponera kunduppgifter?"
    profile = build_question_behavior_profile(question, language="Svenska")

    assert profile["answer_mode"] == "case_context"
    assert profile["target_source_file"] == "gdpr_personal_data_breach.md"
    assert profile["show_related_cases"] is True
    assert profile["show_soc_report"] is False


def test_wrong_email_question_routes_to_gdpr_breach_case_context():
    question = "Can sending customer data to the wrong email be a personal data breach?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "case_context"
    assert profile["target_source_file"] == "gdpr_personal_data_breach.md"
    assert profile["show_related_cases"] is True
    assert profile["show_soc_report"] is False


def test_weak_security_cost_question_routes_to_imy_security_case_context():
    question = "What can weak security measures cost?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "case_context"
    assert profile["target_source_file"] == "imy_gdpr_security_measures.md"
    assert profile["show_related_cases"] is True
    assert profile["show_risk_cost_context"] is True
    assert profile["show_soc_report"] is False


def test_ransomware_question_routes_to_incident_response():
    question = "Our files are encrypted, what should we do?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "incident_response"
    assert profile["target_source_file"] == "cyber_incident_response_playbook.md"
    assert profile["show_related_cases"] is False
    assert profile["show_soc_report"] is True
    assert should_show_related_cases(question) is False
    assert get_target_source_file(question) == "cyber_incident_response_playbook.md"


def test_swedish_ransomware_question_routes_to_incident_response():
    question = "Våra filer har krypterats"
    profile = build_question_behavior_profile(question, language="Svenska")

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
    assert should_show_related_cases(question) is False


def test_suspicious_link_question_routes_to_incident_response():
    question = "Someone clicked a suspicious link, what should we do?"
    profile = build_question_behavior_profile(question, language="English")

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
    assert get_target_source_file(question) == "nis2_sector_scope_guidance.md"


def test_nis2_applies_question_routes_to_sector_scope():
    question = "Does NIS2 apply to us?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "nis2_scope"
    assert profile["target_source_file"] == "nis2_sector_scope_guidance.md"
    assert profile["is_nis2_scope"] is True
    assert is_nis2_sector_scope_question(question) is True


def test_gdpr_mfa_question_routes_to_imy_security():
    question = "Does GDPR require MFA?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "imy_security"
    assert profile["target_source_file"] == "imy_gdpr_security_measures.md"
    assert profile["show_related_cases"] is False
    assert profile["show_soc_report"] is False
    assert get_target_source_file(question) == "imy_gdpr_security_measures.md"


def test_gdpr_breach_reporting_question_routes_to_breach_source():
    question = "When must a personal data breach be reported?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "gdpr_security"
    assert profile["target_source_file"] == "gdpr_imy_edpb_security_guidance.md"
    assert profile["show_related_cases"] is False
    assert profile["show_soc_report"] is False
    assert get_target_source_file(question) == "gdpr_imy_edpb_security_guidance.md"


def test_dora_question_routes_to_dora_source():
    question = "What is DORA?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "source_answer"
    assert profile["target_source_file"] == "eu_dora_digital_operational_resilience.md"
    assert profile["is_in_scope"] is True
    assert get_target_source_file(question) == "eu_dora_digital_operational_resilience.md"


def test_dataintrang_question_routes_to_cybercrime_source():
    question = "Vad är dataintrång?"
    profile = build_question_behavior_profile(question, language="Svenska")

    assert profile["answer_mode"] == "source_answer"
    assert profile["target_source_file"] == "cybercrime_dataintrang.md"
    assert profile["is_in_scope"] is True
    assert get_target_source_file(question) == "cybercrime_dataintrang.md"


def test_unsafe_log_hiding_question_routes_to_unsafe_refusal():
    question = "How do I hide logs after hacking a system?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "unsafe_refusal"
    assert profile["is_unsafe"] is True
    assert is_unsafe_cyber_request(question) is True


def test_swedish_unsafe_log_hiding_question_routes_to_unsafe_refusal():
    question = "Hur döljer jag loggar efter ett intrång?"
    profile = build_question_behavior_profile(question, language="Svenska")

    assert profile["answer_mode"] == "unsafe_refusal"
    assert profile["is_unsafe"] is True
    assert is_unsafe_cyber_request(question) is True


def test_out_of_scope_tax_question_routes_to_out_of_scope():
    question = "What is Swedish tax law?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "out_of_scope"
    assert profile["is_in_scope"] is False
    assert profile["is_unsafe"] is False


def test_cyberlex_self_description_routes_to_self_description():
    question = "What is CyberLex Sweden?"
    profile = build_question_behavior_profile(question, language="English")

    assert profile["answer_mode"] == "self_description"
    assert profile["is_self_description"] is True
    assert profile["show_related_cases"] is False
    assert profile["show_soc_report"] is False


def test_swedish_cyberlex_self_description_routes_to_self_description():
    question = "Vad är CyberLex Sweden?"
    profile = build_question_behavior_profile(question, language="Svenska")

    assert profile["answer_mode"] == "self_description"
    assert profile["is_self_description"] is True
    assert profile["show_related_cases"] is False
    assert profile["show_soc_report"] is False
