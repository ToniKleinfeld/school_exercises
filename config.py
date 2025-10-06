"""
Configuration module for AI Prompt Generator

This module contains all configuration data including subjects, grades,
and exercise type mappings for better organization and maintainability.

Author: Toni Kleinfeld
Date: October 2025
"""

# German school grades
GRADES = (
    "1. Klasse",
    "2. Klasse",
    "3. Klasse",
    "4. Klasse",
    "5. Klasse",
    "6. Klasse",
    "7. Klasse",
    "8. Klasse",
    "9. Klasse",
    "10. Klasse",
    "11. Klasse",
    "12. Klasse",
    "13. Klasse",
    "Oberstufe",
    "Universität",
)

# German school subjects
SUBJECTS = (
    "Mathematik",
    "Deutsch",
    "Englisch",
    "Französisch",
    "Spanisch",
    "Latein",
    "Physik",
    "Chemie",
    "Biologie",
    "Geschichte",
    "Geographie",
    "Politik/Wirtschaft",
    "Sozialwissenschaften",
    "Religion",
    "Ethik",
    "Philosophie",
    "Kunst",
    "Musik",
    "Sport",
    "Informatik",
    "Technik",
    "Wirtschaft",
)

# Exercise type mappings for each subject
# Only includes sensible combinations based on pedagogical considerations
EXERCISE_MAPPINGS = {
    "Mathematik": ["Multiple Choice", "Rechenaufgaben", "Problemlösung", "Kurze Antworten", "Analyseaufgaben"],
    "Deutsch": [
        "Multiple Choice",
        "Offene Fragen",
        "Lückentext",
        "Aufsatzfragen",
        "Interpretationsaufgaben",
        "Erörterung",
        "Analyseaufgaben",
    ],
    "Englisch": [
        "Multiple Choice",
        "Lückentext",
        "Kurze Antworten",
        "Aufsatzfragen",
        "Offene Fragen",
        "Richtig/Falsch",
    ],
    "Französisch": [
        "Multiple Choice",
        "Lückentext",
        "Kurze Antworten",
        "Aufsatzfragen",
        "Offene Fragen",
        "Richtig/Falsch",
    ],
    "Spanisch": [
        "Multiple Choice",
        "Lückentext",
        "Kurze Antworten",
        "Aufsatzfragen",
        "Offene Fragen",
        "Richtig/Falsch",
    ],
    "Latein": [
        "Multiple Choice",
        "Lückentext",
        "Kurze Antworten",
        "Interpretationsaufgaben",
        "Analyseaufgaben",
    ],
    "Physik": ["Multiple Choice", "Rechenaufgaben", "Problemlösung", "Kurze Antworten", "Analyseaufgaben"],
    "Chemie": ["Multiple Choice", "Rechenaufgaben", "Problemlösung", "Kurze Antworten", "Analyseaufgaben"],
    "Biologie": ["Multiple Choice", "Offene Fragen", "Kurze Antworten", "Analyseaufgaben", "Richtig/Falsch"],
    "Geschichte": [
        "Multiple Choice",
        "Offene Fragen",
        "Aufsatzfragen",
        "Analyseaufgaben",
        "Interpretationsaufgaben",
        "Erörterung",
    ],
    "Geographie": ["Multiple Choice", "Offene Fragen", "Kurze Antworten", "Analyseaufgaben", "Richtig/Falsch"],
    "Politik/Wirtschaft": [
        "Multiple Choice",
        "Offene Fragen",
        "Aufsatzfragen",
        "Analyseaufgaben",
        "Erörterung",
    ],
    "Sozialwissenschaften": [
        "Multiple Choice",
        "Offene Fragen",
        "Aufsatzfragen",
        "Analyseaufgaben",
        "Erörterung",
    ],
    "Religion": ["Multiple Choice", "Offene Fragen", "Aufsatzfragen", "Erörterung", "Interpretationsaufgaben"],
    "Ethik": ["Multiple Choice", "Offene Fragen", "Aufsatzfragen", "Erörterung", "Analyseaufgaben"],
    "Philosophie": [
        "Multiple Choice",
        "Offene Fragen",
        "Aufsatzfragen",
        "Erörterung",
        "Interpretationsaufgaben",
        "Analyseaufgaben",
    ],
    "Kunst": [
        "Multiple Choice",
        "Offene Fragen",
        "Analyseaufgaben",
        "Interpretationsaufgaben",
        "Kurze Antworten",
    ],
    "Musik": ["Multiple Choice", "Offene Fragen", "Analyseaufgaben", "Kurze Antworten", "Richtig/Falsch"],
    "Sport": ["Multiple Choice", "Offene Fragen", "Kurze Antworten", "Richtig/Falsch"],
    "Informatik": ["Multiple Choice", "Problemlösung", "Kurze Antworten", "Analyseaufgaben", "Rechenaufgaben"],
    "Technik": ["Multiple Choice", "Problemlösung", "Kurze Antworten", "Analyseaufgaben", "Rechenaufgaben"],
    "Wirtschaft": ["Multiple Choice", "Offene Fragen", "Rechenaufgaben", "Analyseaufgaben", "Problemlösung"],
}

# Default exercise types for unknown subjects
DEFAULT_EXERCISE_TYPES = ["Multiple Choice", "Offene Fragen", "Kurze Antworten"]

# UI Configuration
WINDOW_TITLE = "KI Prompt Generator für Übungsaufgaben zum Lernen"
MAIN_TITLE = "Übungsaufgaben Prompt Generator"
WINDOW_SIZE = "600x900"
MAIN_FONT = ("Arial", 18, "bold")
LABEL_FONT = ("Arial", 12, "bold")
HELP_FONT = ("Arial", 9)
OUTPUT_FONT = ("Consolas", 10)

# Button texts (keeping English as requested)
GENERATE_BUTTON_TEXT = "Generate Prompt"
COPY_BUTTON_TEXT = "Copy to Clipboard"

# Default values
DEFAULT_NUM_QUESTIONS = "5"
MIN_QUESTIONS = 1
MAX_QUESTIONS = 50
