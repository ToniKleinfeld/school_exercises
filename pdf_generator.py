"""
PDF Generator Module

This module handles the creation of PDF files from structured exercise data.
Supports both exercise sheets (without solutions) and solution sheets.

Author: Toni Kleinfeld
Date: October 2025
"""

import json
from datetime import datetime

# Check if reportlab is available
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    from reportlab.lib.enums import TA_LEFT, TA_CENTER
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False


class PDFGenerator:
    """Class responsible for generating PDF files from exercise data"""

    def __init__(self):
        """Initialize the PDF generator with styles"""
        if not REPORTLAB_AVAILABLE:
            raise ImportError("reportlab ist nicht installiert. Bitte installiere es mit: pip install reportlab")
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()

    def _setup_custom_styles(self):
        """Setup custom paragraph styles for the PDF"""
        # Title style
        self.styles.add(
            ParagraphStyle(
                name="CustomTitle",
                parent=self.styles["Heading1"],
                fontSize=16,
                textColor="#333333",
                spaceAfter=30,
                alignment=TA_CENTER,
                fontName="Helvetica-Bold",
            )
        )

        # Subtitle style
        self.styles.add(
            ParagraphStyle(
                name="CustomSubtitle",
                parent=self.styles["Heading2"],
                fontSize=14,
                textColor="#555555",
                spaceAfter=20,
                spaceBefore=20,
                fontName="Helvetica-Bold",
            )
        )

        # Question style
        self.styles.add(
            ParagraphStyle(
                name="Question",
                parent=self.styles["Normal"],
                fontSize=12,
                textColor="#000000",
                spaceAfter=8,
                fontName="Helvetica",
            )
        )

        # Answer style
        self.styles.add(
            ParagraphStyle(
                name="Answer",
                parent=self.styles["Normal"],
                fontSize=11,
                textColor="#006600",
                spaceAfter=6,
                leftIndent=20,
                fontName="Helvetica-Bold",
            )
        )

        # Explanation style
        self.styles.add(
            ParagraphStyle(
                name="Explanation",
                parent=self.styles["Normal"],
                fontSize=10,
                textColor="#666666",
                spaceAfter=15,
                leftIndent=20,
                fontName="Helvetica-Oblique",
            )
        )

    def generate_pdfs_from_json(self, json_data, output_prefix="exercise"):
        """
        Generate both exercise and solution PDFs from JSON data

        Args:
            json_data (dict or str): Exercise data as dictionary or JSON string
            output_prefix (str): Prefix for output filenames

        Returns:
            tuple: (exercise_pdf_path, solution_pdf_path)
        """
        # Parse JSON if string
        if isinstance(json_data, str):
            try:
                data = json.loads(json_data)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON format: {str(e)}")
        else:
            data = json_data

        # Validate data structure
        self._validate_json_structure(data)

        # Generate filenames with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        exercise_path = f"{output_prefix}_uebungsblatt_{timestamp}.pdf"
        solution_path = f"{output_prefix}_loesungsblatt_{timestamp}.pdf"

        # Generate PDFs
        self._generate_exercise_sheet(data, exercise_path)
        self._generate_solution_sheet(data, solution_path)

        return exercise_path, solution_path

    def _validate_json_structure(self, data):
        """Validate that JSON has required structure"""
        if not isinstance(data, dict):
            raise ValueError("JSON data must be a dictionary")

        if "metadata" not in data:
            raise ValueError("JSON must contain 'metadata' field")

        if "exercises" not in data:
            raise ValueError("JSON must contain 'exercises' field")

        if not isinstance(data["exercises"], list):
            raise ValueError("'exercises' must be a list")

        # Validate metadata
        required_metadata = ["topic", "grade", "subject"]
        for field in required_metadata:
            if field not in data["metadata"]:
                raise ValueError(f"Metadata must contain '{field}' field")

        # Validate exercises
        for i, exercise in enumerate(data["exercises"], 1):
            required_fields = ["id", "type", "question", "answer"]
            for field in required_fields:
                if field not in exercise:
                    raise ValueError(f"Exercise {i} must contain '{field}' field")

    def _generate_exercise_sheet(self, data, output_path):
        """Generate exercise sheet (without solutions)"""
        doc = SimpleDocTemplate(
            output_path, pagesize=A4, rightMargin=2 * cm, leftMargin=2 * cm, topMargin=2 * cm, bottomMargin=2 * cm
        )

        story = []
        metadata = data["metadata"]

        # Title
        title = f"{metadata['topic']} – Übungsblatt ({metadata['grade']} {metadata['subject']})"
        story.append(Paragraph(title, self.styles["CustomTitle"]))
        story.append(Spacer(1, 0.5 * cm))

        # Name and Date fields
        story.append(Paragraph("Name: _______________________________", self.styles["Normal"]))
        story.append(Spacer(1, 0.3 * cm))
        story.append(Paragraph("Datum: _______________________________", self.styles["Normal"]))
        story.append(Spacer(1, 1 * cm))

        # Group exercises by subtopic
        exercises_by_subtopic = {}
        for exercise in data["exercises"]:
            subtopic = exercise.get("subtopic", "Allgemein")
            if subtopic not in exercises_by_subtopic:
                exercises_by_subtopic[subtopic] = []
            exercises_by_subtopic[subtopic].append(exercise)

        # Add exercises
        for subtopic, exercises in exercises_by_subtopic.items():
            # Subtopic header
            story.append(Paragraph(f"<b>{subtopic}</b>", self.styles["CustomSubtitle"]))
            story.append(Spacer(1, 0.3 * cm))

            for exercise in exercises:
                # Question number and text
                question_text = f"<b>{exercise['id']}.</b> {exercise['question']}"
                story.append(Paragraph(question_text, self.styles["Question"]))

                # Add options for Multiple Choice
                if exercise.get("options") and isinstance(exercise["options"], list):
                    for option in exercise["options"]:
                        story.append(Paragraph(f"   ☐ {option}", self.styles["Normal"]))

                # Add space for answer
                story.append(Spacer(1, 0.8 * cm))

            story.append(Spacer(1, 0.5 * cm))

        doc.build(story)

    def _generate_solution_sheet(self, data, output_path):
        """Generate solution sheet (with answers and explanations)"""
        doc = SimpleDocTemplate(
            output_path, pagesize=A4, rightMargin=2 * cm, leftMargin=2 * cm, topMargin=2 * cm, bottomMargin=2 * cm
        )

        story = []
        metadata = data["metadata"]

        # Title
        title = f"{metadata['topic']} – Lösungsblatt ({metadata['grade']} {metadata['subject']})"
        story.append(Paragraph(title, self.styles["CustomTitle"]))
        story.append(Spacer(1, 1 * cm))

        # Group exercises by subtopic
        exercises_by_subtopic = {}
        for exercise in data["exercises"]:
            subtopic = exercise.get("subtopic", "Allgemein")
            if subtopic not in exercises_by_subtopic:
                exercises_by_subtopic[subtopic] = []
            exercises_by_subtopic[subtopic].append(exercise)

        # Add exercises with solutions
        for subtopic, exercises in exercises_by_subtopic.items():
            # Subtopic header
            story.append(Paragraph(f"<b>{subtopic}</b>", self.styles["CustomSubtitle"]))
            story.append(Spacer(1, 0.3 * cm))

            for exercise in exercises:
                # Question
                question_text = f"<b>{exercise['id']}.</b> {exercise['question']}"
                story.append(Paragraph(question_text, self.styles["Question"]))

                # Show options for Multiple Choice
                if exercise.get("options") and isinstance(exercise["options"], list):
                    for option in exercise["options"]:
                        marker = "✓" if option == exercise["answer"] else "☐"
                        story.append(Paragraph(f"   {marker} {option}", self.styles["Normal"]))

                # Answer
                answer_text = f"<b>Lösung:</b> {exercise['answer']}"
                story.append(Paragraph(answer_text, self.styles["Answer"]))

                # Explanation
                if exercise.get("explanation"):
                    explanation_text = f"<i>Erklärung:</i> {exercise['explanation']}"
                    story.append(Paragraph(explanation_text, self.styles["Explanation"]))

                story.append(Spacer(1, 0.5 * cm))

            story.append(Spacer(1, 0.3 * cm))

        doc.build(story)


def create_sample_json():
    """Create a sample JSON structure for testing"""
    return {
        "metadata": {
            "topic": "Nomen",
            "grade": "4. Klasse",
            "subject": "Deutsch",
            "subtopics": ["Plural", "Artikel", "Merkwörter"],
        },
        "exercises": [
            {
                "id": 1,
                "type": "Lückentext",
                "subtopic": "Plural",
                "question": "Setze die richtige Pluralform ein: Das Haus → Die ___",
                "options": None,
                "answer": "Häuser",
                "explanation": "Bei 'Haus' wird der Umlaut verwendet und -er angehängt.",
            },
            {
                "id": 2,
                "type": "Multiple Choice",
                "subtopic": "Artikel",
                "question": "Welcher Artikel passt? ___ Baum",
                "options": ["der", "die", "das"],
                "answer": "der",
                "explanation": "Baum ist maskulin, daher 'der'.",
            },
        ],
    }


if __name__ == "__main__":
    # Test the PDF generator
    generator = PDFGenerator()
    sample_data = create_sample_json()

    try:
        exercise_pdf, solution_pdf = generator.generate_pdfs_from_json(sample_data, "test")
        print(f"✓ Exercise sheet created: {exercise_pdf}")
        print(f"✓ Solution sheet created: {solution_pdf}")
    except Exception as e:
        print(f"✗ Error: {str(e)}")
