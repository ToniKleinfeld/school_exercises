"""
Prompt Generator Module

This module handles the creation and formatting of AI prompts for educational exercises.
It contains the business logic for generating prompts based on user inputs.

Author: Toni Kleinfeld
Date: October 2025
"""

from config import JSON_PROMPT_TEMPLATE, EXERCISE_TYPE_DESCRIPTIONS


class PromptGenerator:
    """Class responsible for generating AI prompts based on input parameters"""

    def __init__(self):
        """Initialize the prompt generator"""
        pass

    def create_json_prompt_template(self, num_questions, grade, subject, main_topic, subtopics, exercise_types):
        """
        Create the JSON-formatted prompt template for AI models that output JSON

        Args:
            num_questions (str): Number of questions per exercise type
            grade (str): Grade/class level
            subject (str): Subject area
            main_topic (str): Main topic
            subtopics (str): Subtopics separated by commas
            exercise_types (list): List of exercise types

        Returns:
            str: Formatted JSON prompt for AI
        """
        # Create structured topic text and subtopic analysis
        topic_text, subtopic_list = self._format_topic_structure_with_list(main_topic, subtopics)

        # num_questions = Anzahl der Fragen PRO Aufgabentyp
        questions_per_type = int(num_questions)

        # Handle both list and string input for backwards compatibility
        if isinstance(exercise_types, list) and subtopic_list:
            # Create distribution text based on subtopics and exercise types
            distribution_info = self._create_subtopic_distribution(subtopic_list, questions_per_type, exercise_types)
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

        # Determine age-appropriate language level
        grade_level = self._get_grade_level(grade)
        language_instruction = self._get_language_instruction(subject, grade_level)

        # Create exercise type list with detailed descriptions
        exercise_type_details = self._format_exercise_type_details(exercise_types)

        # Prepare subtopic instructions
        subtopic_instructions = self._create_subtopic_instructions(subtopic_list, questions_per_type, exercise_types)

        # Use JSON template from config with all dynamic values
        prompt = JSON_PROMPT_TEMPLATE.format(
            topic_text=topic_text,
            grade=grade,
            subject=subject,
            exercise_type_details=exercise_type_details,
            distribution_info=distribution_info,
            language_instruction=language_instruction,
            subtopic_instructions=subtopic_instructions,
            grade_level=grade_level,
            num_questions=num_questions,
        )

        return prompt

    def _format_exercise_type_details(self, exercise_types):
        """Format exercise types with their detailed descriptions"""
        if not isinstance(exercise_types, list):
            return exercise_types

        details = []
        for ex_type in exercise_types:
            if ex_type in EXERCISE_TYPE_DESCRIPTIONS:
                details.append(f"• {ex_type}: {EXERCISE_TYPE_DESCRIPTIONS[ex_type]}")
            else:
                details.append(f"• {ex_type}")

        return "\n".join(details)

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
        """Create distribution text based on subtopics and exercise types"""
        if not isinstance(exercise_types, list):
            exercise_types = [exercise_types]

        num_exercise_types = len(exercise_types)
        num_subtopics = len(subtopic_list)
        exercises_per_subtopic_total = exercises_per_subtopic  # Anzahl Aufgaben PRO Unterthema
        total_exercises = num_subtopics * exercises_per_subtopic_total

        distribution_text = f"Insgesamt {total_exercises} Aufgaben verteilt auf {num_subtopics} Unterthemen:\n"
        distribution_text += f"Pro Unterthema: {exercises_per_subtopic_total} Aufgaben\n"
        distribution_text += "Jede Aufgabe enthält 3-5 Unteraufgaben/Teilfragen\n"
        distribution_text += f"\nGewählte Aufgabentypen: {', '.join(exercise_types)}\n"
        distribution_text += f"Unterthemen: {', '.join(subtopic_list)}\n"

        distribution_text += "\nWICHTIG - Struktur pro Unterthema:\n"
        distribution_text += f"• Jedes Unterthema bekommt genau {exercises_per_subtopic_total} Aufgaben\n"
        distribution_text += f"• Die {exercises_per_subtopic_total} Aufgaben werden gleichmäßig auf die {num_exercise_types} Aufgabentypen verteilt\n"
        distribution_text += "• Jede Hauptaufgabe enthält 3-5 konkrete Unteraufgaben/Beispiele\n"
        distribution_text += "• Multiple Choice sollte höchstens 30% aller Aufgaben ausmachen\n"
        distribution_text += "• Bevorzuge Aufgaben mit sub_questions für mehr Übungsvielfalt"

        return distribution_text

    def _create_subtopic_instructions(self, subtopic_list, exercises_per_subtopic, exercise_types):
        """Create detailed instructions for subtopic-based exercise creation"""
        if not subtopic_list:
            return "Erstelle die Aufgaben thematisch strukturiert."

        if not isinstance(exercise_types, list):
            exercise_types = [exercise_types]

        instructions = []
        instructions.append("STRUKTUR DER AUFGABENERSTELLUNG:\n")
        instructions.append(f"Erstelle insgesamt {len(subtopic_list) * exercises_per_subtopic} Aufgaben:")
        instructions.append(f"• {exercises_per_subtopic} Aufgaben pro Unterthema")
        instructions.append(f"• {len(subtopic_list)} Unterthemen: {', '.join(subtopic_list)}")
        instructions.append(f"• Verfügbare Aufgabentypen: {', '.join(exercise_types)}")
        instructions.append("")
        instructions.append("DETAILLIERTE VERTEILUNG PRO UNTERTHEMA:")

        # Erstelle detaillierte Anweisungen für jedes Unterthema
        for i, subtopic in enumerate(subtopic_list, 1):
            instructions.append(f"\nUnterthema {i}: {subtopic}")
            instructions.append(f"   → Erstelle genau {exercises_per_subtopic} Aufgaben für dieses Unterthema")
            instructions.append(
                f"   → Verteile die {exercises_per_subtopic} Aufgaben gleichmäßig auf die Aufgabentypen:"
            )

            # Berechne Verteilung der Aufgabentypen für dieses Unterthema
            exercises_per_type = exercises_per_subtopic // len(exercise_types)
            remainder = exercises_per_subtopic % len(exercise_types)

            for j, ex_type in enumerate(exercise_types):
                count = exercises_per_type + (1 if j < remainder else 0)
                if count > 0:
                    instructions.append(f"     • {count}x {ex_type}")

            instructions.append("   → Jede Aufgabe enthält 3-5 konkrete Unteraufgaben/Beispiele")
            instructions.append(f"   → Fokus: {subtopic} (alle Beispiele sollen zu diesem Thema passen)")

        instructions.append("")
        instructions.append("WICHTIGE QUALITÄTSREGELN:")
        instructions.append("• Jede Hauptaufgabe MUSS 3-5 sub_questions enthalten")
        instructions.append("• Multiple Choice nur in Maßen verwenden (max. 30%)")
        instructions.append("• Alle Beispiele müssen zum jeweiligen Unterthema passen")
        instructions.append("• Schwierigkeitsgrad altersgerecht anpassen")

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
