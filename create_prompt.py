"""
Prompt Generator Module

This module handles the creation and formatting of AI prompts for educational exercises.
It contains the business logic for generating prompts based on user inputs.

Author: AI Assistant
Date: October 2025
"""


class PromptGenerator:
    """Class responsible for generating AI prompts based on input parameters"""

    def __init__(self):
        """Initialize the prompt generator"""
        pass

    def create_prompt_template(self, num_questions, grade, subject, topic, exercise_types):
        """
        Create the formatted prompt template

        Args:
            num_questions (str): Number of questions to generate
            grade (str): Grade/class level
            subject (str): Subject area
            topic (str): Specific topic
            exercise_types (list): List of exercise types

        Returns:
            str: Formatted prompt for AI
        """
        # Handle both list and string input for backwards compatibility
        if isinstance(exercise_types, list):
            # Calculate distribution of exercises
            total_exercises = int(num_questions)
            exercises_per_type = total_exercises // len(exercise_types)
            remaining = total_exercises % len(exercise_types)

            # Create distribution text
            distribution_parts = []
            for i, exercise_type in enumerate(exercise_types):
                count = exercises_per_type + (1 if i < remaining else 0)
                distribution_parts.append(f"{count} {exercise_type}")

            distribution_text = ", ".join(distribution_parts)
        else:
            distribution_text = f"{num_questions} {exercise_types}"

        # Determine age-appropriate language level
        grade_level = self._get_grade_level(grade)
        language_instruction = self._get_language_instruction(subject, grade_level)

        prompt = f"""Erstelle {num_questions} Übungen für Schüler der {grade} zum Thema „{topic}".

Übungstypen: {distribution_text}

{language_instruction}

Für jede Aufgabe: klare, einfache Formulierungen

Danach: vollständige Lösung und kurze {grade_level} Erklärung

Ausgabeanforderungen:

Erstelle zwei PDF-Dateien:

1. Übungsblatt (Fragen ohne Lösungen) für Schüler
2. Lösungsblatt (mit Antworten und Erklärungen) für Lehrkräfte

Verwende übersichtliches Layout (DIN A4, Arial 12 pt)

Trenne Abschnitte mit klaren Überschriften und Abständen

Titel, Name- und Datumsfelder auf Seite 1 des Übungsblatts

Mehrseitiges Layout, falls nötig

Keine weiteren Erklärungen oder Zwischenausgaben – direkt PDFs zum Download erstellen

Formatierungshinweis: Gib beide Dateien direkt als Downloadlink aus."""

        return prompt

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

    def validate_inputs(self, grade, subject, topic, exercise_type, num_questions):
        """
        Validate all input parameters

        Args:
            grade (str): Grade/class level
            subject (str): Subject area
            topic (str): Specific topic
            exercise_type (str): Type of exercise
            num_questions (str): Number of questions

        Returns:
            tuple: (is_valid, error_message)
        """
        # Check for empty fields
        required_fields = [
            (grade.strip(), "Klasse/Jahrgangsstufe"),
            (subject.strip(), "Fach"),
            (topic.strip(), "Thema"),
            (exercise_type.strip(), "Aufgabentyp"),
            (num_questions.strip(), "Anzahl der Aufgaben"),
        ]

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
