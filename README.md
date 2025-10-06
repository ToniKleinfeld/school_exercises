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

## Eingabefelder (Version 2.2)

1. **Klasse/Jahrgangsstufe**: Wähle die Klassenstufe
2. **Fach**: Wähle das Schulfach
3. **Hauptthema**: Das übergeordnete Thema (z.B. "Nomen")
4. **Unterthemen**: Spezifische Aspekte, getrennt durch Kommas (z.B. "Merkmale, Veränderung, Merkwörter mit ß")
5. **Aufgabentypen**: Wähle einen oder mehrere passende Aufgabentypen (erscheinen nach Fachauswahl)
6. **Anzahl der Aufgaben**: Anzahl der Aufgaben **pro Unterthema** (wird zufällig auf Aufgabentypen verteilt)

## Intelligente Aufgabentyp-Zuordnung

Die App zeigt nur sinnvolle Aufgabentypen für das gewählte Fach an:

- **Mathematik/Physik/Chemie**: Rechenaufgaben, Problemlösung, Multiple Choice, etc.
- **Deutsch/Geschichte**: Aufsatzfragen, Interpretationsaufgaben, Erörterung, etc.
- **Fremdsprachen**: Lückentext, Multiple Choice, Aufsatzfragen, etc.
- **Naturwissenschaften**: Analyseaufgaben, Multiple Choice, Kurze Antworten, etc.

## Neue Features (Version 2.2)

### ✅ **Unterthema-basierte Aufgabenverteilung**

- **Pro Unterthema**: 10 Aufgaben bedeutet 10 Aufgaben für "Merkmale" + 10 für "Veränderung" + 10 für "Merkwörter mit ß"
- **Zufällige Verteilung**: Aufgabentypen werden zufällig auf Unterthemen verteilt
- **Fokussierte Inhalte**: Jede Aufgabe konzentriert sich spezifisch auf ihr Unterthema

### ✅ **Internet-Recherche für bessere Qualität**

- **Schritt 1**: KI sucht zuerst nach vergleichbaren Aufgaben im Internet
- **Inspiration**: Orientierung an bewährten Beispielen und Formaten
- **Qualitätssteigerung**: Erkennung von angemessenem Schwierigkeitsgrad
- **Fehlerprävention**: Identifikation häufiger Fehlerquellen

### ✅ **Strukturierte 3-Schritt-Anweisung**

- **Schritt 1**: Recherche und Inspiration
- **Schritt 2**: Aufgabenerstellung pro Unterthema
- **Schritt 3**: PDF-Erstellung mit Layout

### ✅ **Strukturierte Themenangabe**

- **Hauptthema**: Übergeordnetes Thema (z.B. "Nomen", "Quadratische Gleichungen")
- **Unterthemen**: Spezifische Aspekte, kommagetrennt
- **Automatische Formatierung**: "Nomen" (Schwerpunkte: Merkmale, Veränderung, Merkwörter mit ß)

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

## Beispiel-Output (Version 2.2)

```
SCHRITT 1: RECHERCHE UND INSPIRATION

Suche zuerst im Internet nach vergleichbaren Aufgaben für das Thema: „Nomen" (Schwerpunkte: Merkmale, Veränderung, Merkwörter mit ß)
Klassenstufe: 4. Klasse, Fach: Deutsch
Aufgabentypen: Multiple Choice, Lückentext

Orientiere dich an existierenden Beispielen, um:
- Typische Fragestellungen zu verstehen
- Angemessenen Schwierigkeitsgrad zu erkennen
- Bewährte Aufgabenformate zu übernehmen
- Häufige Fehlerquellen zu identifizieren

SCHRITT 2: AUFGABENERSTELLUNG

Insgesamt 30 Aufgaben (10 pro Unterthema):
- Unterthema 1 (Merkmale): 10 Aufgaben
- Unterthema 2 (Veränderung): 10 Aufgaben
- Unterthema 3 (Merkwörter mit ß): 10 Aufgaben

Aufgabentypen: Multiple Choice, Lückentext (zufällig auf Unterthemen verteilt)

Strukturierung nach Unterthemen:
Unterthema 1: 'Merkmale' - 10 Aufgaben
   → Verwende zufällig die Aufgabentypen: Multiple Choice, Lückentext
   → Fokussiere spezifisch auf die Aspekte von 'Merkmale'

Unterthema 2: 'Veränderung' - 10 Aufgaben
   → Verwende zufällig die Aufgabentypen: Multiple Choice, Lückentext
   → Fokussiere spezifisch auf die Aspekte von 'Veränderung'

Unterthema 3: 'Merkwörter mit ß' - 10 Aufgaben
   → Verwende zufällig die Aufgabentypen: Multiple Choice, Lückentext
   → Fokussiere spezifisch auf die Aspekte von 'Merkwörter mit ß'

WICHTIG: Erstelle tiefgreifende, durchdachte Aufgaben die verschiedene Aspekte des jeweiligen Unterthemas abdecken und zum Nachdenken anregen.

SCHRITT 3: PDF-ERSTELLUNG
[...Layout-Anforderungen...]
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
