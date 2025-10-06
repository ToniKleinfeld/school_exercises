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

    def create_prompt_template(self, num_questions, grade, subject, topic, exercise_type):
        """
        Create the formatted prompt template

        Args:
            num_questions (str): Number of questions to generate
            grade (str): Grade/class level
            subject (str): Subject area
            topic (str): Specific topic
            exercise_type (str): Type of exercise

        Returns:
            str: Formatted prompt for AI
        """
        prompt = f"""Generate {num_questions} exercises for {grade} grade students in {subject} on the topic "{topic}".
The exercises should be of type {exercise_type}.
Include answers and short explanations.
Format the output in JSON."""

        return prompt

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
