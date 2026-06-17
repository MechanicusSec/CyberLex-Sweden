"""
Shared text helpers for CyberLex Sweden.

This module contains small normalization and phrase-matching functions used by
search, routing, language detection, and UI logic.
"""

def clean_words(text):

    # Converts text into simple searchable lowercase words.
    punctuation = ",.?!:;()[]{}\"'`"
    text = text.lower()

    for mark in punctuation:
        text = text.replace(mark, " ")

    return text.split()


def normalize_query_text(text):
    # Normalizes common wording and small typos before intent matching.
    # This keeps CyberLex from refusing a good question because of one tiny human typo.
    text_lower = str(text or "").lower()

    replacements = {
        "kontör": "konto",
        "kontr": "konto",
        "kontot": "konto",
        "e post": "e-post",
        "epost": "e-post",
        "mail": "mejl",
        "vårat": "vårt",
        "inlogning": "inloggning",
        "ransomewere": "ransomware",
        "ransomwere": "ransomware",
        "kryptats": "krypterats",
        "kund data": "kunddata",
        "customerdata": "customer data",
        "app-fel": "appfel",
        "app fel": "appfel",
        "app error": "app bug",
        "application error": "app bug",
        "users' data": "users data",
        "user data": "users data",
        "kontoseparation": "kontoseparering",
    }

    for wrong, right in replacements.items():
        text_lower = text_lower.replace(wrong, right)

    return text_lower


def contains_any(text, terms):
    # Returns True if any phrase in terms exists in text.
    # CyberLex uses this for simple intent detection.
    text_lower = normalize_query_text(text)
    normalized_terms = [normalize_query_text(term) for term in terms]
    return any(term in text_lower for term in normalized_terms)

