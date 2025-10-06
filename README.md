# KI Prompt Generator für Bildungsaufgaben

Eine Python-Anwendung mit deutscher GUI zur Generierung von KI-Prompts für Übungsaufgaben, für das deutsche Schulsystem.

## Zweck der Anwendung

Diese App soll helfen Übungen zum lernen mit, **strukturiertem AI-Prompt** zu erstellen, die:

- **Qualitativ hochwertige Übungsblätter** mit PDF-Ausgabe generieren
- **Altersgerechte Aufgaben** für deutsche Klassenstufen (1. Klasse bis Universität) erstellen
- **Fachspezifische Aufgabentypen** verwenden (nur sinnvolle Kombinationen)
- **Unterthema-basierte Verteilung** für fokussierte Inhalte ermöglichen

## Installation und Ausführung

### Voraussetzungen

- **Python 3.7+**

### Setup

1. **Repository klonen oder herunterladen**
2. **Virtuelles Environment erstellen (empfohlen):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # oder: source venv/bin/activate  # macOS/Linux
   ```
3. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Anwendung starten:**
   ```bash
   python ai_prompt_generator.py
   ```

## Verwendete Technologien

- **Python 3.7+** (Standard-Installation)
- **Tkinter** (GUI-Framework, in Python enthalten)
- **pyperclip 1.8+** (Zwischenablage-Funktionalität)

## Hauptfunktionen

- **Deutsche Schulfächer** (Mathematik, Deutsch, Englisch, Naturwissenschaften, etc.)
- **Klassenstufen** (1. Klasse bis Universität)
- **Intelligente Aufgabentyp-Zuordnung** (nur passende Typen pro Fach)
- **Strukturierte Themeneingabe** (Hauptthema + Unterthemen)
- **Automatische Prompt-Generierung** mit 3-Schritt-Prozess
- **Copy-to-Clipboard** mit visuellem Feedback
- **Modulare Architektur** für einfache Erweiterungen

## Projektstruktur

```
school_exercises/
├── ai_prompt_generator.py    # Hauptanwendung
├── ui.py                     # Benutzeroberfläche
├── create_prompt.py          # Prompt-Generierung
├── config.py                 # Konfiguration und Templates
└── README.md
```

## Zusatz

Sollten diese Prompts dauerhaft gute Ergebnisse zum lernen hervorbringen, wird evtl eine web version folgen , im idealfall mit direkter ausgabe von PDF. 

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
