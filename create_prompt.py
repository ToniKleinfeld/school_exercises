"""
Prompt Generator Module

This module handles the creation and formatting of AI prompts for educational exercises.
It contains the business logic for generating prompts based on user inputs.

Author: Toni Kleinfeld
Date: October 2025
"""


class PromptGenerator:
    """Class responsible for generating AI prompts based on input parameters"""

    def __init__(self):
        """Initialize the prompt generator"""
        pass

    def create_prompt_template(self, num_questions, grade, subject, main_topic, subtopics, exercise_types):
        """
        Create the formatted prompt template

        Args:
            num_questions (str): Number of questions per exercise type
            grade (str): Grade/class level
            subject (str): Subject area
            main_topic (str): Main topic
            subtopics (str): Subtopics separated by commas
            exercise_types (list): List of exercise types

        Returns:
            str: Formatted prompt for AI
        """
        # Create structured topic text and subtopic analysis
        topic_text, subtopic_list = self._format_topic_structure_with_list(main_topic, subtopics)

        # Handle both list and string input for backwards compatibility
        if isinstance(exercise_types, list) and subtopic_list:
            # Calculate exercises per subtopic
            exercises_per_subtopic = int(num_questions)
            total_exercises = exercises_per_subtopic * len(subtopic_list)

            # Create distribution text based on subtopics
            distribution_info = self._create_subtopic_distribution(
                subtopic_list, exercises_per_subtopic, exercise_types
            )
        else:
            # Fallback for old behavior
            if isinstance(exercise_types, list):
                total_exercises = int(num_questions) * len(exercise_types)
                distribution_parts = []
                for exercise_type in exercise_types:
                    distribution_parts.append(f"{num_questions} {exercise_type}")
                distribution_text = ", ".join(distribution_parts)
                distribution_info = f"Insgesamt {total_exercises} Aufgaben: {distribution_text}"
            else:
                distribution_info = f"{num_questions} {exercise_types}"
                total_exercises = int(num_questions)

        # Determine age-appropriate language level
        grade_level = self._get_grade_level(grade)
        language_instruction = self._get_language_instruction(subject, grade_level)

        # Create exercise type list for research
        exercise_types_text = ", ".join(exercise_types) if isinstance(exercise_types, list) else exercise_types

        prompt = f"""SCHRITT 1: RECHERCHE & INTEGRATION (nicht separat ausgeben)

Recherchiere im Internet nach existierenden Aufgaben zu: {topic_text}
(Klassenstufe: {grade}, Fach: {subject}, Aufgabentypen: {exercise_types_text})

→ Verwende die gefundenen Informationen direkt zur Erstellung eigener, inspiriert-abgewandelter Aufgaben.
→ Gib die Rechercheergebnisse nicht separat aus, sondern arbeite sie vollständig in die Aufgaben ein (Schwierigkeitsgrad, Fragetypen, Wortwahl).
→ Integriere automatisch typische Fragestellungen, bewährte Aufgabenformate und erkannte Fehlerquellen.

SCHRITT 2: AUFGABENERSTELLUNG

{distribution_info}

{language_instruction}

Strukturierung nach Unterthemen:
{self._create_subtopic_instructions(subtopic_list, exercises_per_subtopic if subtopic_list else int(num_questions), exercise_types)}

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
Erstelle zwei PDF-Dateien (Übungsblatt & Lösungsblatt) im DIN-A4-Format, Schriftart Arial 12 pt.
Kein Text ausgeben, nur die beiden PDFs.

ZUSATZ:
Wenn du zusätzliche Informationen aus der Recherche verwendest (z. B. typische Fehlerquellen oder Aufgabentypen), integriere sie automatisch in die Aufgaben — ohne sie separat aufzuführen."""

        return prompt

    def _format_topic_structure_with_list(self, main_topic, subtopics):
        """Format the topic structure and return both formatted text and subtopic list"""
        if not main_topic.strip():
            if subtopics.strip():
                subtopic_list = [sub.strip() for sub in subtopics.split(",") if sub.strip()]
                return subtopics.strip(), subtopic_list
            else:
                return "Unbekanntes Thema", []

        if not subtopics.strip():
            return f'„{main_topic.strip()}"', []

        # Clean and format subtopics
        subtopic_list = [sub.strip() for sub in subtopics.split(",") if sub.strip()]
        if subtopic_list:
            subtopic_text = ", ".join(subtopic_list)
            formatted_topic = f'„{main_topic.strip()}" (Schwerpunkte: {subtopic_text})'
            return formatted_topic, subtopic_list
        else:
            return f'„{main_topic.strip()}"', []

    def _create_subtopic_distribution(self, subtopic_list, exercises_per_subtopic, exercise_types):
        """Create distribution text based on subtopics"""
        total_exercises = exercises_per_subtopic * len(subtopic_list)

        distribution_text = f"Insgesamt {total_exercises} Aufgaben ({exercises_per_subtopic} pro Unterthema):"

        for i, subtopic in enumerate(subtopic_list, 1):
            distribution_text += f"\n- Unterthema {i} ({subtopic}): {exercises_per_subtopic} Aufgaben"

        exercise_types_text = ", ".join(exercise_types) if isinstance(exercise_types, list) else exercise_types
        distribution_text += f"\n\nAufgabentypen: {exercise_types_text} (zufällig auf Unterthemen verteilt)"

        return distribution_text

    def _create_subtopic_instructions(self, subtopic_list, exercises_per_subtopic, exercise_types):
        """Create detailed instructions for subtopic-based exercise creation"""
        if not subtopic_list:
            return "Erstelle die Aufgaben thematisch strukturiert."

        instructions = []
        exercise_types_text = ", ".join(exercise_types) if isinstance(exercise_types, list) else exercise_types

        for i, subtopic in enumerate(subtopic_list, 1):
            instructions.append(f"Unterthema {i}: '{subtopic}' - {exercises_per_subtopic} Aufgaben")
            instructions.append(f"   → Verwende zufällig die Aufgabentypen: {exercise_types_text}")
            instructions.append(f"   → Fokussiere spezifisch auf die Aspekte von '{subtopic}'")
            instructions.append("")

        return "\n".join(instructions)

    def _format_topic_structure(self, main_topic, subtopics):
        """Format the topic structure for better clarity (legacy method)"""
        formatted_topic, _ = self._format_topic_structure_with_list(main_topic, subtopics)
        return formatted_topic

    def _get_grade_level(self, grade):
        """Determine appropriate language level based on grade"""
        grade_lower = grade.lower()
        if any(x in grade_lower for x in ["1.", "2.", "3.", "4."]):
            return "kindgerechte"
        elif any(x in grade_lower for x in ["5.", "6.", "7.", "8."]):
            return "altersgerechte"
        elif any(x in grade_lower for x in ["9.", "10.", "11.", "12.", "13.", "oberstufe"]):
            return "angemessene"
        else:
            return "verständliche"

    def _get_language_instruction(self, subject, grade_level):
        """Get subject-specific language instructions"""
        subject_lower = subject.lower()

        if "deutsch" in subject_lower:
            if grade_level == "kindgerechte":
                return f"Sprache: Deutsch ({grade_level} Niveau für Grundschule)"
            else:
                return f"Sprache: Deutsch ({grade_level} Niveau)"
        elif any(lang in subject_lower for lang in ["englisch", "französisch", "spanisch", "latein"]):
            return f"Sprache: {subject} ({grade_level} Sprachniveau)"
        else:
            return f"Sprache: Deutsch ({grade_level} Fachsprache für {subject})"

    def validate_inputs(self, grade, subject, main_topic, subtopics, exercise_type, num_questions):
        """
        Validate all input parameters

        Args:
            grade (str): Grade/class level
            subject (str): Subject area
            main_topic (str): Main topic
            subtopics (str): Subtopics
            exercise_type (str): Type of exercise
            num_questions (str): Number of questions

        Returns:
            tuple: (is_valid, error_message)
        """
        # Check for empty fields
        required_fields = [
            (grade.strip(), "Klasse/Jahrgangsstufe"),
            (subject.strip(), "Fach"),
            (exercise_type.strip(), "Aufgabentyp"),
            (num_questions.strip(), "Anzahl der Aufgaben"),
        ]

        # At least one topic field must be filled
        if not main_topic.strip() and not subtopics.strip():
            return False, "Bitte füllen Sie mindestens das Hauptthema oder die Unterthemen aus."

        for value, field_name in required_fields:
            if not value:
                return False, f"Bitte füllen Sie das Feld '{field_name}' aus."

        # Validate number of questions is a positive integer
        try:
            num = int(num_questions)
            if num <= 0:
                raise ValueError()
        except ValueError:
            return False, "Die Anzahl der Aufgaben muss eine positive Zahl sein."

        return True, ""
