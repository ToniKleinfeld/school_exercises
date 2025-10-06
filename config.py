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

# Prompt Template - can be easily modified without changing code logic
PROMPT_TEMPLATE = """SCHRITT 1: RECHERCHE & INTEGRATION (nicht separat ausgeben)

Recherchiere im Internet nach existierenden Aufgaben zu: {topic_text}
(Klassenstufe: {grade}, Fach: {subject}, Aufgabentypen: {exercise_types_text})

→ Verwende die gefundenen Informationen direkt zur Erstellung eigener, inspiriert-abgewandelter Aufgaben.
→ Gib die Rechercheergebnisse nicht separat aus, sondern arbeite sie vollständig in die Aufgaben ein (Schwierigkeitsgrad, Fragetypen, Wortwahl).
→ Integriere automatisch typische Fragestellungen, bewährte Aufgabenformate und erkannte Fehlerquellen.

SCHRITT 2: AUFGABENERSTELLUNG

{distribution_info}

{language_instruction}

Strukturierung nach Unterthemen:
{subtopic_instructions}

Für jede Aufgabe: klare, einfache Formulierungen mit angemessenem Schwierigkeitsgrad

Danach: vollständige Lösung und kurze {grade_level} Erklärung

WICHTIG: Erstelle tiefgreifende, durchdachte Aufgaben die verschiedene Aspekte des jeweiligen Unterthemas abdecken und zum Nachdenken anregen.

SCHRITT 3: PDF-ERSTELLUNG

Erstelle zwei PDF-Dateien im DIN A4-Format, Arial 12 pt:

1. Übungsblatt (ohne Lösungen) – Titel, Name-/Datumsfeld, übersichtliche Gliederung, Absätze zwischen Unterthemen
2. Lösungsblatt (mit Antworten + Erklärungen) – gleiche Struktur, aber mit Lösungen direkt unter jeder Aufgabe

Layoutanforderungen:
- Überschriften klar abgesetzt
- Jede Aufgabe nummeriert
- Zwischenräume zwischen den Aufgaben
- kindgerechtes, sauberes Layout

AUSGABE:
Erstelle direkt zwei PDFs (Übungsblatt ohne Lösungen und Lösungsblatt mit Lösungen und kindgerechten Erklärungen) im DIN-A4-Format, Arial 12 pt. Gib die Dateien ohne Rückfrage aus.

ZUSATZ:
Wenn du zusätzliche Informationen aus der Recherche verwendest (z. B. typische Fehlerquellen oder Aufgabentypen), integriere sie automatisch in die Aufgaben — ohne sie separat aufzuführen."""
