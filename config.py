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
PROMPT_TEMPLATE = """Ziel:
Erstelle ein vollständiges, {grade_level} Übungs- und Lösungsblatt zum Thema {topic_text} für {grade} {subject}.

SCHRITT 1 – Recherche & Integration (nicht separat ausgeben):
Suche im Internet nach typischen, frei zugänglichen Aufgaben und Aufgabenformaten zu {topic_text}.
Verwende die Rechercheergebnisse ausschließlich als inhaltliche und sprachliche Orientierung – also um Schwierigkeitsgrad, Wortwahl, Aufgabentypen und typische Fehlerquellen zu erkennen.
Die gefundenen Inhalte dürfen nicht direkt übernommen oder zitiert, sondern müssen vollständig neu formuliert und abgewandelt werden.
Gib keine Rechercheergebnisse oder Quellen separat aus.
Integriere sie automatisch in die Aufgaben (z. B. in der Formulierung, im Schwierigkeitsgrad oder in typischen Antwortoptionen).

SCHRITT 2 – Aufgabenerstellung:
{distribution_info}

Aufgabentypen: {exercise_types_text} (abwechslungsreich gemischt)

{subtopic_instructions}

Anforderungen:
• {language_instruction}
• Kurze, klare Aufgabenstellungen
• Aufgabentypen abwechslungsreich gemischt
• Aufgaben sollen unterschiedliche Aspekte abdecken und zum Nachdenken anregen
• Typische Fehlerquellen oder Missverständnisse gezielt einbauen

Für jede Aufgabe:
• Eine klar formulierte Fragestellung
• Falls Multiple Choice: drei Antwortoptionen (eine richtig)
• Falls Lückentext: vollständiger Satz mit Lücke
• Falls Analyseaufgabe: kleine Denksituation mit Aufforderung zur Erklärung

Nach den Aufgaben:
• Vollständige Lösungen
• Kurze, {grade_level} Erklärungen („Warum ist das richtig?")

SCHRITT 3 – PDF-Erstellung:
Erstelle direkt zwei PDF-Dateien im DIN-A4-Format, Schriftart Arial 12 pt:

1. Übungsblatt (ohne Lösungen)
   • Titel: „{topic_text} – Übungsblatt ({grade} {subject})"
   • Felder für Name und Datum
   • Überschriften für jedes Unterthema klar abgesetzt
   • Jede Aufgabe nummeriert
   • Zwischenräume zwischen den Aufgaben
   • {grade_level}, sauberes Layout

2. Lösungsblatt (mit Lösungen und Erklärungen)
   • Gleiche Struktur
   • Lösungen und kurze {grade_level} Erklärungen direkt unter jeder Aufgabe

Layoutanforderungen:
• Arial, 12 pt
• Deutliche Überschriften
• Ausreichend Abstand zwischen Aufgaben
• {grade_level} Layout, klar und freundlich

AUSGABE:
Erstelle die beiden PDF-Dateien (Übungsblatt & Lösungsblatt) direkt, ohne Zwischenschritt oder Rückfrage.
Verwende alle integrierten Rechercheinformationen ausschließlich zur Qualität der Aufgaben.
Gib keine Quellen, Links oder Rechercheergebnisse im Text oder Anhang aus.

ZUSATZ:
Falls du während der Recherche zusätzliche Muster, typische Fehler oder bewährte Formate erkennst, integriere sie automatisch in die Aufgaben — ohne sie gesondert zu erwähnen oder offenzulegen."""
