import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1] / "app"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from language import detect_ui_language_from_question


def test_english_meta_pixel_question_stays_english():
    question = "Can Meta Pixel create GDPR risk?"

    assert detect_ui_language_from_question(question) == "English"


def test_swedish_meta_pixel_question_detects_swedish():
    question = "Kan Meta Pixel skapa GDPR-risk?"

    assert detect_ui_language_from_question(question) == "Svenska"


def test_english_app_bug_question_stays_english():
    question = "Can an app bug expose customer data?"

    assert detect_ui_language_from_question(question) == "English"


def test_swedish_app_bug_question_detects_swedish():
    question = "Kan ett appfel exponera kunduppgifter?"

    assert detect_ui_language_from_question(question) == "Svenska"


def test_english_nis2_question_stays_english():
    question = "What is NIS2?"

    assert detect_ui_language_from_question(question) == "English"


def test_swedish_nis2_question_detects_swedish():
    question = "Vad är NIS2?"

    assert detect_ui_language_from_question(question) == "Svenska"


def test_swedish_incident_question_with_english_login_detects_swedish():
    question = "Vi har fått en misstänkt login på ett konto, vad ska vi göra?"

    assert detect_ui_language_from_question(question) == "Svenska"


def test_english_risk_word_does_not_force_swedish():
    question = "Can Meta Pixel create GDPR risk?"

    assert detect_ui_language_from_question(question) == "English"


def test_swedish_ransomware_question_detects_swedish():
    question = "Vad ska vi göra om våra filer har krypterats?"

    assert detect_ui_language_from_question(question) == "Svenska"


def test_empty_question_defaults_to_english():
    question = ""

    assert detect_ui_language_from_question(question) == "English"
