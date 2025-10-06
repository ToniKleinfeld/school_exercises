# KI Prompt Generator für Bildungsaufgaben

Eine Python-Anwendung mit GUI zur Gene## Beispiel-Output

````
Generate 8 exercises for 10. Klasse students in Mathematik on the topic "Quadratische Gleichungen".
The exercises should include the following types: Multiple Choice, Rechenaufgaben und Problemlösung.
Distribute the questions evenly across the selected exercise types.
Include detailed answers and explanations for each question.

Output requirements:
- Create two separate PDFs:
  1. Exercise sheet (questions only) - multi-page format suitable for students
  2. Answer sheet (questions with solutions and explanations) - for teachers

Format the response as structured text that can be easily converted to PDF format.
```von KI-Prompts für Bildungsaufgaben, speziell angepasst für das deutsche Schulsystem.

## Features

- ✅ Einfache Tkinter-GUI auf Deutsch
- ✅ Deutsche Schulfächer und Klassenstufen
- ✅ **Fachspezifische Aufgabentypen** - nur sinnvolle Kombinationen werden angezeigt
- ✅ **Mehrfachauswahl von Aufgabentypen** - Checkboxes für flexible Auswahl
- ✅ Automatische Prompt-Generierung mit PDF-Ausgabe-Anforderung
- ✅ Copy-to-Clipboard Funktionalität
- ✅ Intelligente Eingabevalidierung
- ✅ Modulare Struktur für bessere Wartbarkeit
- ✅ Erweiterbar für zukünftige KI-API Integration

## Struktur

Das Projekt ist in vier Module aufgeteilt:

- **`ai_prompt_generator.py`**: Hauptanwendung - koordiniert UI und Prompt-Generierung
- **`ui.py`**: Benutzeroberfläche - alle GUI-Komponenten und Interaktionen
- **`create_prompt.py`**: Prompt-Generierung - Geschäftslogik für Prompt-Erstellung
- **`config.py`**: Konfiguration - alle Konstanten, Fächer, Aufgabentypen und UI-Einstellungen

## Installation

1. Stelle sicher, dass Python 3.7+ installiert ist
2. Installiere die erforderlichen Abhängigkeiten:

```bash
pip install -r requirements.txt
````

## Nutzung

Starte die Anwendung:

```bash
python ai_prompt_generator.py
```

## Deutsche Schulfächer

Die Anwendung unterstützt folgende Fächer des deutschen Schulsystems:

- Mathematik, Deutsch, Englisch, Französisch, Spanisch, Latein
- Physik, Chemie, Biologie
- Geschichte, Geographie, Politik/Wirtschaft, Sozialwissenschaften
- Religion, Ethik, Philosophie
- Kunst, Musik, Sport
- Informatik, Technik, Wirtschaft

## Klassenstufen

- 1. Klasse bis 13. Klasse
- Oberstufe
- Universität

## Eingabefelder

1. **Klasse/Jahrgangsstufe**: Wähle die Klassenstufe
2. **Fach**: Wähle das Schulfach
3. **Thema**: Gib das spezifische Thema ein
4. **Aufgabentypen**: Wähle einen oder mehrere passende Aufgabentypen (erscheinen nach Fachauswahl)
5. **Anzahl der Aufgaben**: Anzahl der gewünschten Aufgaben

## Intelligente Aufgabentyp-Zuordnung

Die App zeigt nur sinnvolle Aufgabentypen für das gewählte Fach an:

- **Mathematik/Physik/Chemie**: Rechenaufgaben, Problemlösung, Multiple Choice, etc.
- **Deutsch/Geschichte**: Aufsatzfragen, Interpretationsaufgaben, Erörterung, etc.
- **Fremdsprachen**: Lückentext, Multiple Choice, Aufsatzfragen, etc.
- **Naturwissenschaften**: Analyseaufgaben, Multiple Choice, Kurze Antworten, etc.

## Neue Prompt-Funktionen (Version 2.0)

Der generierte Prompt ist jetzt deutlich präziser und kindgerechter:

### ✅ **Intelligente Aufgabenverteilung**

- Automatische gleichmäßige Verteilung der Fragen auf gewählte Aufgabentypen
- Beispiel: 10 Aufgaben → "5 Multiple Choice, 5 Lückentext"

### ✅ **Altersgerechte Sprache**

- **Grundschule (1.-4. Klasse)**: Kindgerechte Formulierungen
- **Mittelstufe (5.-8. Klasse)**: Altersgerechte Sprache
- **Oberstufe (9.-13. Klasse)**: Angemessene Fachsprache

### ✅ **Professionelle PDF-Anforderungen**

- Klare Layout-Vorgaben (DIN A4, Arial 12pt)
- Name- und Datumsfelder auf Übungsblatt
- Direkte PDF-Download-Links
- Mehrseitiges Layout bei Bedarf

### ✅ **Deutsche Prompts**

- Kompletter Wechsel zu deutscher Prompt-Sprache
- Fachspezifische Sprachangaben je nach Unterrichtsfach

## Beispiel-Output (Version 2.0)

```
Erstelle 10 Übungen für Schüler der 4. Klasse zum Thema „Nomen Merkmale,Verändern sich Merkwörter mit ß".

Übungstypen: 5 Multiple Choice, 5 Lückentext

Sprache: Deutsch (kindgerechte Niveau für Grundschule)

Für jede Aufgabe: klare, einfache Formulierungen

Danach: vollständige Lösung und kurze kindgerechte Erklärung

Ausgabeanforderungen:

Erstelle zwei PDF-Dateien:

1. Übungsblatt (Fragen ohne Lösungen) für Schüler
2. Lösungsblatt (mit Antworten und Erklärungen) für Lehrkräfte

Verwende übersichtliches Layout (DIN A4, Arial 12 pt)

Trenne Abschnitte mit klaren Überschriften und Abständen

Titel, Name- und Datumsfelder auf Seite 1 des Übungsblatts

Mehrseitiges Layout, falls nötig

Keine weiteren Erklärungen oder Zwischenausgaben – direkt PDFs zum Download erstellen

Formatierungshinweis: Gib beide Dateien direkt als Downloadlink aus.
```

## Erweiterbarkeit

Die modulare Struktur macht Erweiterungen sehr einfach:

- **`config.py`**: Neue Fächer, Aufgabentypen oder UI-Texte hinzufügen
- **`create_prompt.py`**: KI-API Integration oder neue Prompt-Templates
- **`ui.py`**: Neue UI-Elemente oder Interaktionen
- **Neue Sprachen**: Einfach neue config-Dateien für andere Länder erstellen

### Beispiel: Neues Fach hinzufügen

```python
# In config.py
SUBJECTS = SUBJECTS + ("Neues Fach",)

EXERCISE_MAPPINGS["Neues Fach"] = [
    "Multiple Choice",
    "Spezielle Aufgaben für dieses Fach"
]
```

## Technische Details

- **Framework**: Tkinter (Standard Python GUI)
- **Dependencies**: pyperclip für Zwischenablage-Funktionalität
- **Python Version**: 3.7+
- **Plattform**: Windows, macOS, Linux
- **Architektur**: Modulare MVC-ähnliche Struktur
