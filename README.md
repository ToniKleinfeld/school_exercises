# AI Prompt Generator for Educational Exercises

Eine Python-Anwendung mit GUI zur Generierung von KI-Prompts für Bildungsaufgaben.

## Features

- ✅ Einfache Tkinter-GUI
- ✅ Eingabefelder für Klasse, Fach, Thema, Aufgabentyp und Anzahl
- ✅ Automatische Prompt-Generierung im gewünschten Format
- ✅ Copy-to-Clipboard Funktionalität
- ✅ Eingabevalidierung
- ✅ Responsive Design
- ✅ Erweiterbar für zukünftige KI-API Integration

## Installation

1. Stelle sicher, dass Python 3.7+ installiert ist
2. Installiere die erforderlichen Abhängigkeiten:

```bash
pip install -r requirements.txt
```

## Nutzung

1. Starte die Anwendung:

```bash
python ai_prompt_generator.py
```

2. Fülle die Eingabefelder aus:
   - **Grade/Class**: Wähle die Klassenstufe
   - **Subject**: Wähle das Fach
   - **Topic**: Gib das spezifische Thema ein
   - **Exercise Type**: Wähle den Aufgabentyp
   - **Number of Questions**: Anzahl der gewünschten Aufgaben

3. Klicke auf "Generate Prompt"

4. Der fertige Prompt wird angezeigt und kann mit "Copy to Clipboard" kopiert werden

## Beispiel-Output

```
Generate 5 exercises for 10th grade students in Mathematics on the topic "Quadratic Equations".
The exercises should be of type Multiple Choice.
Include answers and short explanations.
Format the output in JSON.
```

## Struktur

- `ai_prompt_generator.py`: Hauptanwendung
- `requirements.txt`: Python-Abhängigkeiten
- `README.md`: Diese Dokumentation

## Erweiterbarkeit

Die Anwendung ist darauf ausgelegt, leicht erweitert zu werden:

- **KI-API Integration**: Füge einfach API-Calls in der `generate_prompt()` Methode hinzu
- **Neue Eingabefelder**: Erweitere die `create_input_fields()` Methode
- **Template-Anpassungen**: Modifiziere die `create_prompt_template()` Methode
- **Export-Funktionen**: Füge weitere Output-Formate hinzu

## Technische Details

- **Framework**: Tkinter (Standard Python GUI)
- **Dependencies**: pyperclip für Zwischenablage-Funktionalität
- **Python Version**: 3.7+
- **Plattform**: Windows, macOS, Linux