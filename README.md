# KI Prompt Generator für Bildungsaufgaben

Eine Python-Anwendung mit GUI zur Generierung von KI-Prompts für Bildungsaufgaben, speziell angepasst für das deutsche Schulsystem.

## Features

- ✅ Einfache Tkinter-GUI auf Deutsch
- ✅ Deutsche Schulfächer und Klassenstufen
- ✅ Eingabefelder für Klasse, Fach, Thema, Aufgabentyp und Anzahl
- ✅ Automatische Prompt-Generierung im gewünschten Format
- ✅ Copy-to-Clipboard Funktionalität
- ✅ Eingabevalidierung auf Deutsch
- ✅ Modulare Struktur für bessere Wartbarkeit
- ✅ Erweiterbar für zukünftige KI-API Integration

## Struktur

Das Projekt ist in drei Module aufgeteilt:

- **`ai_prompt_generator.py`**: Hauptanwendung - koordiniert UI und Prompt-Generierung
- **`ui.py`**: Benutzeroberfläche - alle GUI-Komponenten und Interaktionen
- **`create_prompt.py`**: Prompt-Generierung - Geschäftslogik für Prompt-Erstellung

## Installation

1. Stelle sicher, dass Python 3.7+ installiert ist
2. Installiere die erforderlichen Abhängigkeiten:

```bash
pip install -r requirements.txt
```

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
4. **Aufgabentyp**: Wähle den Aufgabentyp (Multiple Choice, Offene Fragen, etc.)
5. **Anzahl der Aufgaben**: Anzahl der gewünschten Aufgaben

## Beispiel-Output

```
Generate 5 exercises for 10. Klasse grade students in Mathematik on the topic "Quadratische Gleichungen".
The exercises should be of type Multiple Choice.
Include answers and short explanations.
Format the output in JSON.
```

## Erweiterbarkeit

Die modulare Struktur macht Erweiterungen einfach:

- **KI-API Integration**: Erweitere `create_prompt.py` um API-Calls
- **Neue UI-Elemente**: Modifiziere `ui.py`
- **Zusätzliche Validierung**: Erweitere die Validierungsmethoden
- **Export-Funktionen**: Füge neue Output-Formate hinzu

## Technische Details

- **Framework**: Tkinter (Standard Python GUI)
- **Dependencies**: pyperclip für Zwischenablage-Funktionalität
- **Python Version**: 3.7+
- **Plattform**: Windows, macOS, Linux
- **Architektur**: Modulare MVC-ähnliche Struktur
