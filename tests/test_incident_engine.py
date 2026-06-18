import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1] / "app"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

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
)


def test_ransomware_question_is_practical_incident():
    question = "Our files are encrypted, what should we do?"

    assert is_practical_incident_response_question(question) is True
    assert is_ransomware_response_question(question) is True
    assert is_encrypted_files_possible_ransomware_question(question) is True


def test_swedish_ransomware_statement_is_practical_incident():
    question = "Våra filer har krypterats"

    assert is_practical_incident_response_question(question) is True
    assert is_ransomware_response_question(question) is True


def test_suspicious_login_question_is_practical_incident():
    question = "Vi har fått en misstänkt login på ett konto, vad ska vi göra?"

    assert is_practical_incident_response_question(question) is True
    assert is_suspicious_login_question(question) is True


def test_suspicious_link_question_is_practical_incident():
    question = "Someone clicked a suspicious link, what should we do?"

    assert is_practical_incident_response_question(question) is True
    assert is_suspicious_link_question(question) is True


def test_swedish_suspicious_sms_link_is_practical_incident():
    question = "Någon klickade på en länk i SMS"

    assert is_practical_incident_response_question(question) is True
    assert is_suspicious_link_question(question) is True


def test_compromised_account_question_is_detected():
    question = "What should we do if an account is compromised?"

    assert is_practical_incident_response_question(question) is True
    assert is_compromised_account_question(question) is True


def test_data_leak_question_is_detected():
    question = "Customer data may have leaked"

    assert is_practical_incident_response_question(question) is True
    assert is_data_leak_response_question(question) is True


def test_suspected_hacking_question_is_detected():
    question = "We suspect intrusion in our system, what should we do?"

    assert is_practical_incident_response_question(question) is True
    assert is_suspected_hacking_question(question) is True


def test_definition_question_is_not_practical_incident():
    question = "What is ransomware?"

    assert is_practical_incident_response_question(question) is False


def test_case_context_question_is_not_practical_incident():
    question = "Can Meta Pixel create GDPR risk?"

    assert is_practical_incident_response_question(question) is False


def test_app_bug_question_is_not_practical_incident():
    question = "Can an app bug expose customer data?"

    assert is_practical_incident_response_question(question) is False


def test_suspicious_email_question_is_detected():
    question = "We received a suspicious email"

    assert is_suspicious_email_question(question) is True
