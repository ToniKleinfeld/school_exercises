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

# German school subjects (focused on core subjects)
SUBJECTS = (
    "Mathematik",
    "Deutsch",
    "Englisch",
    "Französisch",
    "Spanisch",
    "Latein",
)

# Exercise type mappings for each subject with detailed descriptions
# Each type includes pedagogical guidance for better task generation
EXERCISE_MAPPINGS = {
    "Mathematik": [
        "Rechenaufgaben",
        "Ankreuzen (Multiple Choice)",
        "Problemlösung",
        "Kurzantwort",
    ],
    "Deutsch": [
        "Erkennen/Unterstreichen",
        "Ankreuzen (Multiple Choice)",
        "Lückentext (Wort einsetzen)",
        "Lückentext (Form ergänzen)",
        "Formbildung/Variation",
        "Groß-/Kleinschreibung korrigieren",
        "Wortart unterscheiden/Ausschließen",
        "Sortieren/Zuordnen",
        "Freies Vervollständigen",
        "Kurzantwort: Bestimme Eigenschaften",
    ],
    "Englisch": [
        "Erkennen/Unterstreichen",
        "Ankreuzen (Multiple Choice)",
        "Lückentext (Wort einsetzen)",
        "Lückentext (Form ergänzen)",
        "Formbildung/Variation",
        "Sortieren/Zuordnen",
        "Freies Vervollständigen",
        "Kurzantwort",
    ],
    "Französisch": [
        "Erkennen/Unterstreichen",
        "Ankreuzen (Multiple Choice)",
        "Lückentext (Wort einsetzen)",
        "Lückentext (Form ergänzen)",
        "Formbildung/Variation",
        "Sortieren/Zuordnen",
        "Freies Vervollständigen",
        "Kurzantwort",
    ],
    "Spanisch": [
        "Erkennen/Unterstreichen",
        "Ankreuzen (Multiple Choice)",
        "Lückentext (Wort einsetzen)",
        "Lückentext (Form ergänzen)",
        "Formbildung/Variation",
        "Sortieren/Zuordnen",
        "Freies Vervollständigen",
        "Kurzantwort",
    ],
    "Latein": [
        "Erkennen/Unterstreichen",
        "Ankreuzen (Multiple Choice)",
        "Lückentext (Form ergänzen)",
        "Formbildung/Variation",
        "Sortieren/Zuordnen",
        "Kurzantwort: Bestimme Eigenschaften",
    ],
}

# Detailed exercise type descriptions for prompt generation
EXERCISE_TYPE_DESCRIPTIONS = {
    "Erkennen/Unterstreichen": "Bestimmte Wörter/Elemente in einem Satz/Text finden und unterstreichen. Formulierung: 'Unterstreiche alle [Zielwörter] in diesem Satz.' Achte auf: Verwechslung mit ähnlichen Wortarten; zusammengesetzte Wörter. Gestaltung: Beispiele vorgeben; Leerzeilen lassen; Ablenker einbauen.",
    "Ankreuzen (Multiple Choice)": "Richtige Eigenschaft, Form oder Kategorie auswählen. Formulierung: 'Welche Antwort ist richtig? Kreuze an.' Achte auf: plausible Ablenkungen. Gestaltung: 3-4 Optionen, eine richtige, sinnvolle Ablenker, eindeutige Wortwahl.",
    "Lückentext (Wort einsetzen)": "Passendes Wort/Begriff in Kontext einsetzen. Formulierung: 'Setze in jede Lücke ein passendes Wort und achte auf die richtige Schreibweise.' Achte auf: falsche Wortart; Klein-/Großschreibung. Gestaltung: Kontext klar machen; Platz für Einträge.",
    "Lückentext (Form ergänzen)": "Richtige Form (Artikel, Endung, Präposition) einsetzen. Formulierung: 'Schreibe in jede Lücke die richtige Form.' Achte auf: Fall/Beziehung im Satz. Gestaltung: Beispiele geben; nur eine korrekte Lösung.",
    "Formbildung/Variation": "Wortform korrekt bilden (Plural, Zeitform, Steigerung). Formulierung: 'Bilde die passende Form von: ___ → ______.' Achte auf: reguläre Endungen, Umlautwechsel. Gestaltung: Unregelmäßige Beispiele einbauen; Lösungsmuster zeigen.",
    "Groß-/Kleinschreibung korrigieren": "Orthografie in ganzen Sätzen überprüfen. Formulierung: 'Schreibe die Sätze richtig: Achte auf Groß- und Kleinschreibung.' Achte auf: Namen/Schlüsselwörter; Satzanfang. Gestaltung: mehrere kurze Sätze, klare Markierungen.",
    "Wortart unterscheiden/Ausschließen": "Wörter in Kategorien zuordnen oder falsches Element finden. Formulierung: 'Kreuze an, welches Wort nicht in diese Gruppe gehört.' Achte auf: Wörter mit mehreren Funktionen. Gestaltung: Ablenker mit ähnlichen Formen wählen.",
    "Sortieren/Zuordnen": "Wörter in Gruppen ordnen. Formulierung: 'Sortiere die Wörter in die Spalten: [Kategorie A] / [Kategorie B].' Achte auf: uneindeutige Wörter. Gestaltung: klare Kategorien; Platz für mehrere Einträge.",
    "Freies Vervollständigen": "Eigene passende Wörter oder Sätze bilden. Formulierung: 'Vervollständige den Satz mit einem passenden Wort: Im ___ sehe ich ___.' Achte auf: ungeeignete Wortart; Rechtschreibfehler. Gestaltung: Beispiele als Hilfe; mehrere Lösungen zulassen.",
    "Kurzantwort: Bestimme Eigenschaften": "Kurze Fakten zu einem Wort angeben. Formulierung: 'Schreibe zu jedem Wort: 1) Eigenschaft A 2) Eigenschaft B.' Achte auf: fehlende Angaben; falsche Reihenfolge. Gestaltung: Tabellarisches Layout; ausgefülltes Beispiel zeigen.",
    "Kurzantwort": "Kurze, präzise Antworten auf spezifische Fragen. Gestaltung: Klare Fragestellung; ausreichend Platz für Antwort.",
    "Rechenaufgaben": "Mathematische Berechnungen durchführen. Gestaltung: Klare Aufgabenstellung; Platz für Rechenweg; eindeutiges Ergebnis.",
    "Problemlösung": "Mathematische Probleme analysieren und lösen. Gestaltung: Sachbezug herstellen; Lösungsweg nachvollziehbar; mehrere Schritte möglich.",
}

# Default exercise types for unknown subjects
DEFAULT_EXERCISE_TYPES = ["Ankreuzen (Multiple Choice)", "Kurzantwort", "Lückentext (Wort einsetzen)"]

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

# JSON Prompt Template for generating structured exercise data
JSON_PROMPT_TEMPLATE = """Ziel:
Erstelle strukturierte Übungsaufgaben zum Thema {topic_text} für {grade} {subject} im JSON-Format.

Anweisung (automatischer Ablauf, keine Rückfragen):

Führe intern eine kurze Internetrecherche durch, um typische Aufgaben und Aufgabenformate zu diesem Thema zu erkennen. Verwende diese Recherche ausschließlich zur Orientierung für Schwierigkeitsgrad, Wortwahl und Aufgabentypen. Zeige keine Quellen oder Rechercheergebnisse an.

------------------------------------------------------------
AUFGABENERSTELLUNG
------------------------------------------------------------

{distribution_info}

WICHTIG - Klare Struktur pro Unterthema:
• Jedes Unterthema bekommt eine festgelegte Anzahl von Aufgaben
• Pro Unterthema: {num_questions} Aufgaben gleichmäßig auf die Aufgabentypen verteilt
• Jede Hauptaufgabe enthält 3-5 konkrete Unteraufgaben/Beispiele
• Ausgewogene Mischung der Aufgabentypen innerhalb jedes Unterthemas

NEU: Strukturiere jede Aufgabe mit einer Hauptfrage und mehreren Unteraufgaben:
• Hauptfrage: z.B. "Unterstreiche alle Pluralformen in diesem Satz:"
• Unteraufgaben: 3-5 konkrete Beispiele als Bullet Points

Verfügbare Aufgabentypen mit Beschreibungen:

{exercise_type_details}

{subtopic_instructions}

Gestaltungshinweise:
• Klare, {grade_level} Formulierung
• {language_instruction}
• Typische Fehlerquellen gezielt einbauen
• Kurze, präzise Aufgabenstellungen
• Pro Hauptaufgabe 3-5 Unteraufgaben erstellen
• VARIATION: Wechsele regelmäßig zwischen verschiedenen Aufgabentypen innerhalb jedes Unterthemas

------------------------------------------------------------
AUSGABEFORMAT: JSON
------------------------------------------------------------

Gib die Aufgaben im folgenden JSON-Format aus (nur das JSON, keine weiteren Texte):

Für Aufgaben mit Unteraufgaben (BEVORZUGT für Rechenaufgaben, Lückentexte, etc.):
{{
  "metadata": {{
    "topic": "{topic_text}",
    "grade": "{grade}",
    "subject": "{subject}",
    "subtopics": [Liste der Übungsbereiche]
  }},
  "exercises": [
    {{
      "id": 1,
      "type": "Aufgabentyp",
      "subtopic": "Übungsbereich",
      "question": "Die Hauptfrage/Anweisung",
      "sub_questions": [
        {{
          "question": "Konkrete Beispielaufgabe 1",
          "answer": "Die korrekte Antwort",
          "explanation": "Kurze Erklärung"
        }},
        {{
          "question": "Konkrete Beispielaufgabe 2",
          "answer": "Die korrekte Antwort",
          "explanation": "Kurze Erklärung"
        }},
        {{
          "question": "Konkrete Beispielaufgabe 3",
          "answer": "Die korrekte Antwort",
          "explanation": "Kurze Erklärung"
        }},
        ... (3-5 Unteraufgaben pro Hauptaufgabe)
      ],
      "explanation": "Allgemeine Erklärung für die ganze Aufgabe (optional)"
    }},
    ... weitere Aufgaben
  ]
}}

Für einfache Aufgaben (nur für Multiple Choice und ähnliche):
{{
  "exercises": [
    {{
      "id": 2,
      "type": "Multiple Choice",
      "subtopic": "Übungsbereich",
      "question": "Die Aufgabenstellung",
      "options": ["Option 1", "Option 2", "Option 3"],
      "answer": "Die korrekte Antwort",
      "explanation": "Kurze Erklärung"
    }}
  ]
}}

WICHTIG - Qualitätskontrolle:
• Verwende Multiple Choice SPARSAM (höchstens 30% aller Aufgaben)
• Bevorzuge das Format mit sub_questions für bessere Strukturierung und mehr Übung
• Gib NUR valides JSON aus
• Keine zusätzlichen Texte vor oder nach dem JSON
• Alle Strings müssen in Anführungszeichen
• Jede Hauptaufgabe sollte 3-5 Unteraufgaben haben
• Gleichmäßige Verteilung pro Unterthema ist wichtiger als strikte Aufgabentyp-Reihenfolge"""
