import streamlit as st

APP_CSS = r"""<style>
    .main-header {
        padding: 1.5rem;
        border-radius: 16px;
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
        margin-bottom: 1.5rem;
    }

    .main-header h1 {
        margin-bottom: 0.2rem;
        font-size: 2.4rem;
    }

    .main-header p {
        font-size: 1.05rem;
        color: #cbd5e1;
    }

    .info-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #1e293b;
        color: #e2e8f0;
        margin-bottom: 1rem;
    }

    .info-card strong {
        color: #ffffff;
    }

    .topic-badge {
        display: inline-block;
        padding: 0.35rem 0.65rem;
        margin: 0.2rem;
        border-radius: 999px;
        background-color: #e2e8f0;
        color: #0f172a;
        font-size: 0.9rem;
    }

    .small-muted {
        color: #64748b;
        font-size: 0.95rem;
    }

    .attention-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #475569;
        background-color: #111827;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .attention-card strong {
        color: #ffffff;
    }

    .attention-level-high {
        border-left: 6px solid #ef4444;
    }

    .attention-level-elevated {
        border-left: 6px solid #f59e0b;
    }

    .attention-level-standard {
        border-left: 6px solid #38bdf8;
    }

    .attention-level-informational {
        border-left: 6px solid #22c55e;
    }

    .attention-level-medium {
        border-left: 6px solid #f59e0b;
    }

    .attention-level-normal {
        border-left: 6px solid #22c55e;
    }

    .attention-label {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .attention-reason {
        color: #d1d5db;
        margin-bottom: 0.4rem;
    }

    .attention-limitation {
        color: #9ca3af;
        font-size: 0.9rem;
        font-style: italic;
    }

    .citation-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .citation-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

    .citation-row {
        margin-bottom: 0.45rem;
        color: #d1d5db;
    }

    .citation-row strong {
        color: #ffffff;
    }

    .citation-code {
        background-color: #111827;
        color: #86efac;
        padding: 0.15rem 0.35rem;
        border-radius: 6px;
        font-family: monospace;
        font-size: 0.9rem;
    }

        .citation-note {
        color: #9ca3af;
        font-size: 0.9rem;
        font-style: italic;
        margin-top: 0.75rem;
    }

        .topic-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #2563eb;
        background: linear-gradient(135deg, #0f172a, #111827);
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .topic-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

    .topic-row {
        margin-bottom: 0.45rem;
        color: #d1d5db;
    }

    .topic-row strong {
        color: #ffffff;
    }

    .topic-code {
        color: #93c5fd;
        font-family: monospace;
        font-weight: 600;
    }

    .metadata-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .metadata-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

    .metadata-row {
        margin-bottom: 0.45rem;
        color: #d1d5db;
    }

    .metadata-row strong {
        color: #ffffff;
    }

        .metadata-code {
        background-color: #111827;
        color: #93c5fd;
        padding: 0.15rem 0.35rem;
        border-radius: 6px;
        font-family: monospace;
        font-size: 0.9rem;
    }

    .source-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .source-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

    .source-card ul {
        margin-bottom: 0;
    }

        .source-card li {
        margin-bottom: 0.35rem;
    }

    .limitation-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #854d0e;
        background-color: #1c1917;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .limitation-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

        .limitation-card-text {
        color: #fef3c7;
        font-size: 0.95rem;
    }

    .practical-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .practical-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

        .practical-card-text {
        color: #d1d5db;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    .incident-log-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .incident-log-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }

    .incident-log-card-text {
        color: #d1d5db;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 0.75rem;
    }

    .incident-log-template {
        background-color: #111827;
        color: #e5e7eb;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 0.85rem;
        white-space: pre-wrap;
        font-family: monospace;
        font-size: 0.9rem;
        line-height: 1.55;
    }

    .checklist-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .checklist-card ul {
        margin-bottom: 0;
        padding-left: 1.25rem;
    }

        .checklist-card li {
        color: #d1d5db;
        margin-bottom: 0.45rem;
        line-height: 1.5;
    }

    .context-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 0.75rem;
        margin-bottom: 0.75rem;
    }

    .context-card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }

    .context-row {
        margin-bottom: 0.45rem;
        color: #d1d5db;
    }

    .context-row strong {
        color: #ffffff;
    }

    .context-code {
        background-color: #111827;
        color: #86efac;
        padding: 0.15rem 0.35rem;
        border-radius: 6px;
        font-family: monospace;
        font-size: 0.9rem;
    }

    .context-excerpt-label {
        font-weight: 700;
        color: #ffffff;
        margin-top: 0.75rem;
        margin-bottom: 0.35rem;
    }

        .context-excerpt {
        color: #d1d5db;
        line-height: 1.45;
        white-space: pre-line;
    }

    .context-shortened-note {
        color: #9ca3af;
        font-size: 0.9rem;
        font-style: italic;
        margin-top: 0.55rem;
        margin-bottom: 0.35rem;
    }

    .context-more-details {
        margin-top: 0.35rem;
    }

    .context-more-details summary {
        color: #93c5fd;
        cursor: pointer;
        font-weight: 600;
        margin-bottom: 0.45rem;
    }

    .context-more-details summary .details-less-label {
        display: none;
    }

    .context-more-details[open] summary .details-more-label {
        display: none;
    }

    .context-more-details[open] summary .details-less-label {
        display: inline;
    }

    .context-full-excerpt {
        margin-top: 0.5rem;
        padding-top: 0.65rem;
        border-top: 1px solid #334155;
    }

    .match-card {
        padding: 0.85rem;
        border-radius: 10px;
        border: 1px solid #334155;
        background-color: #0f172a;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .match-card strong {
        color: #ffffff;
    }

    .match-code {
        background-color: #111827;
        color: #86efac;
        padding: 0.15rem 0.35rem;
        border-radius: 6px;
        font-family: monospace;
        font-size: 0.9rem;
    }
    
.technical-details {
    margin: 0.85rem 0 1rem 0;
    padding: 0.85rem 1rem;
    border: 1px solid rgba(148, 163, 184, 0.28);
    border-radius: 0.75rem;
    background: rgba(15, 23, 42, 0.35);
}
.technical-details summary {
    cursor: pointer;
    font-weight: 700;
}
.technical-details .citation-card,
.technical-details .metadata-card {
    margin-top: 0.75rem;
}

    .main-header.compact-hero {
        padding: 1.6rem 2rem;
        margin-top: 0.25rem;
        margin-bottom: 1.25rem;
    }

    .hero-label {
        margin-top: 1rem;
        font-size: 0.95rem;
        font-weight: 700;
        color: #ffffff;
    }

    .hero-description {
        margin-top: 0.15rem;
        color: #cbd5e1;
        font-size: 0.98rem;
        line-height: 1.5;
    }

    .topic-area-wrapper {
        margin-top: 1.25rem;
        margin-bottom: 0.75rem;
    }

    .topic-area-heading {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .ask-heading {
        font-size: 1.55rem;
        font-weight: 700;
        line-height: 1.2;
        margin-top: 1.25rem;
        margin-bottom: 0.65rem;
    }

    .footer-note {
        text-align: center;
        color: #94a3b8;
        font-size: 0.85rem;
        padding: 1.25rem 0 0.5rem 0;
        border-top: 1px solid rgba(148, 163, 184, 0.2);
        margin-top: 7.5rem;
        margin-bottom: 1rem;
    }

    .footer-note a {
        color: #93c5fd;
        text-decoration: none;
    }

    .footer-note a:hover {
        text-decoration: underline;
    }

    /* Cleaner first impression for portfolio/demo use. */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 980px;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.05), rgba(15, 23, 42, 0.12));
    }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.65rem;
    }

    /* Hide Streamlit's demo/deploy toolbar for a cleaner user-facing prototype. */
    #MainMenu,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        visibility: hidden;
        height: 0;
    }

    .main-header.compact-hero {
        padding: 1.85rem 2rem;
        margin-top: 0;
        margin-bottom: 1rem;
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.18);
    }

    .main-header.compact-hero h1 {
        font-size: 2.30rem;
        letter-spacing: -0.035em;
        line-height: 1.08;
    }

    .main-header.compact-hero p {
        max-width: 760px;
        margin-bottom: 0.85rem;
    }

    .hero-description {
        max-width: 820px;
    }

    .sidebar-status-card {
        padding: 0.85rem 0.9rem;
        border-radius: 12px;
        border: 1px solid rgba(148, 163, 184, 0.28);
        background: rgba(15, 23, 42, 0.08);
        margin-top: 0.4rem;
        margin-bottom: 0.55rem;
    }

    .sidebar-status-title {
        font-size: 1rem;
        font-weight: 750;
        margin-bottom: 0.5rem;
    }

    .sidebar-status-line {
        font-size: 0.88rem;
        margin-bottom: 0.25rem;
        color: inherit;
    }

    .sidebar-info-card {
        padding: 0.85rem 0.9rem;
        border-radius: 12px;
        border: 1px solid rgba(59, 130, 246, 0.28);
        background: rgba(59, 130, 246, 0.12);
        margin-top: 0.55rem;
        margin-bottom: 0.55rem;
        font-size: 0.9rem;
        line-height: 1.45;
    }

    .disclaimer-strip {
        margin-top: 0.85rem;
        margin-bottom: 0.85rem;
        padding: 0.75rem 0.9rem;
        border-radius: 12px;
        border: 1px solid rgba(245, 158, 11, 0.35);
        background: rgba(245, 158, 11, 0.12);
        color: inherit;
        font-size: 0.92rem;
        line-height: 1.45;
    }

    .stTextInput input {
        border-radius: 10px;
    }

</style>
"""


def apply_app_styles():
    """Injects the CyberLex Sweden CSS into the Streamlit page."""
    st.markdown(APP_CSS, unsafe_allow_html=True)
