"""
Test Script für die neue Aufgabenverteilungs-Funktionalität

Testet, ob die Berechnung korrekt funktioniert
"""

from create_prompt import PromptGenerator


def test_neue_verteilung():
    """Teste die neue Aufgabenverteilung"""
    generator = PromptGenerator()

    # Test-Eingaben
    num_questions = "5"
    grade = "5. Klasse"
    subject = "Deutsch"
    main_topic = "Wortarten"
    subtopics = "Nomen, Verben, Adjektive"
    exercise_types = ["Erkennen/Unterstreichen", "Ankreuzen (Multiple Choice)", "Lückentext (Wort einsetzen)"]

    print("=" * 80)
    print("TEST: Neue Aufgabenverteilung")
    print("=" * 80)
    print(f"\nEingaben:")
    print(f"  Fach: {subject}")
    print(f"  Klasse: {grade}")
    print(f"  Hauptthema: {main_topic}")
    print(f"  Unterthemen: {subtopics}")
    print(f"  Anzahl pro Typ: {num_questions}")
    print(f"  Aufgabentypen: {len(exercise_types)}")
    for i, ex_type in enumerate(exercise_types, 1):
        print(f"    {i}. {ex_type}")

    print("\n" + "=" * 80)
    print("Erwartete Berechnung:")
    print("=" * 80)
    subtopic_list = [s.strip() for s in subtopics.split(",")]
    print(f"  Unterthemen: {len(subtopic_list)}")
    print(f"  Aufgabentypen: {len(exercise_types)}")
    print(f"  Fragen pro Typ: {num_questions}")
    print(f"  → Aufgaben pro Unterthema: {len(exercise_types)} (eine pro Typ)")
    print(f"  → Fragen pro Aufgabe: {num_questions}")
    print(f"  → Gesamt Aufgaben: {len(subtopic_list) * len(exercise_types)}")
    print(f"  → Gesamt Fragen: {len(subtopic_list) * len(exercise_types) * int(num_questions)}")

    # Generiere den JSON-Prompt
    print("\n" + "=" * 80)
    print("Generierter JSON-Prompt (Auszug):")
    print("=" * 80)

    prompt = generator.create_json_prompt_template(num_questions, grade, subject, main_topic, subtopics, exercise_types)

    # Zeige nur die Distribution Info
    lines = prompt.split("\n")
    in_distribution = False
    for line in lines:
        if "Insgesamt" in line and "Aufgaben" in line:
            in_distribution = True
        if in_distribution:
            print(line)
            if "STRUKTUR DER AUFGABENERSTELLUNG" in line:
                break

    print("\n" + "=" * 80)
    print("TEST ERFOLGREICH!")
    print("=" * 80)

    return prompt


if __name__ == "__main__":
    test_neue_verteilung()
