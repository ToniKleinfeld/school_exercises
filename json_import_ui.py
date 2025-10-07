"""
JSON Import and PDF Generation UI Module

This module provides a user interface for importing JSON exercise data
and generating PDF files.

Author: Toni Kleinfeld
Date: October 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import json

# Check if PDF generation is available
try:
    from pdf_generator import PDFGenerator, REPORTLAB_AVAILABLE
except ImportError:
    REPORTLAB_AVAILABLE = False
    PDFGenerator = None


class JSONImportUI:
    """UI class for JSON import and PDF generation"""

    def __init__(self, parent_frame):
        """
        Initialize the JSON import UI

        Args:
            parent_frame: Parent tkinter frame
        """
        self.parent = parent_frame
        self.pdf_generator = None
        if REPORTLAB_AVAILABLE and PDFGenerator:
            try:
                self.pdf_generator = PDFGenerator()
            except ImportError:
                self.pdf_generator = None
        self.create_widgets()

    def create_widgets(self):
        """Create all UI widgets"""
        # Title
        title_label = ttk.Label(self.parent, text="JSON Import & PDF Generator", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)

        # Warning if reportlab is not available
        if not REPORTLAB_AVAILABLE or not self.pdf_generator:
            warning_label = ttk.Label(
                self.parent,
                text="⚠️ WARNUNG: reportlab ist nicht installiert. PDF-Generierung nicht verfügbar.\n"
                "Installiere mit: pip install reportlab",
                font=("Arial", 10, "bold"),
                foreground="red",
                justify=tk.CENTER,
            )
            warning_label.pack(pady=5)

        # Instructions
        instructions = (
            "1. Kopiere das JSON-Format von der AI\n"
            "2. Füge es unten ein\n"
            "3. Klicke auf 'Validate JSON' zum Testen\n"
            "4. Klicke auf 'Generate PDFs' (benötigt reportlab)"
        )
        instructions_label = ttk.Label(self.parent, text=instructions, font=("Arial", 9), justify=tk.LEFT)
        instructions_label.pack(pady=5)

        # JSON Input Area
        input_label = ttk.Label(self.parent, text="JSON-Daten:", font=("Arial", 11, "bold"))
        input_label.pack(anchor=tk.W, padx=10, pady=(10, 5))

        self.json_text = scrolledtext.ScrolledText(
            self.parent, height=20, width=80, wrap=tk.WORD, font=("Consolas", 10)
        )
        self.json_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Buttons Frame
        button_frame = ttk.Frame(self.parent)
        button_frame.pack(pady=10)

        # Validate JSON Button
        self.validate_button = tk.Button(
            button_frame,
            text="Validate JSON",
            command=self.validate_json,
            font=("Arial", 11, "bold"),
            relief="raised",
            bd=2,
        )
        self.validate_button.pack(side=tk.LEFT, padx=5)

        # Generate PDFs Button
        self.generate_button = tk.Button(
            button_frame,
            text="Generate PDFs",
            command=self.generate_pdfs,
            font=("Arial", 11, "bold"),
            relief="raised",
            bd=2,
            bg="#4CAF50",
            fg="white",
        )
        self.generate_button.pack(side=tk.LEFT, padx=5)

        # Clear Button
        self.clear_button = tk.Button(
            button_frame, text="Clear", command=self.clear_input, font=("Arial", 11, "bold"), relief="raised", bd=2
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Load Sample Button
        self.sample_button = tk.Button(
            button_frame,
            text="Load Sample",
            command=self.load_sample,
            font=("Arial", 11, "bold"),
            relief="raised",
            bd=2,
        )
        self.sample_button.pack(side=tk.LEFT, padx=5)

        # Status Label
        self.status_label = ttk.Label(self.parent, text="", font=("Arial", 10), foreground="gray")
        self.status_label.pack(pady=5)

    def validate_json(self):
        """Validate the JSON input"""
        json_string = self.json_text.get(1.0, tk.END).strip()

        if not json_string:
            messagebox.showwarning("Warnung", "Bitte fügen Sie JSON-Daten ein.")
            return False

        try:
            data = json.loads(json_string)

            # Basic validation even without reportlab
            if not isinstance(data, dict):
                raise ValueError("JSON muss ein Objekt sein")
            if "metadata" not in data or "exercises" not in data:
                raise ValueError("JSON muss 'metadata' und 'exercises' enthalten")
            if not isinstance(data["exercises"], list):
                raise ValueError("'exercises' muss eine Liste sein")

            # Advanced validation if reportlab is available
            if self.pdf_generator:
                self.pdf_generator._validate_json_structure(data)

            # Show success feedback
            self.show_validation_success()
            messagebox.showinfo(
                "Erfolg", f"✓ JSON ist valide!\n\n" f"Gefunden: {len(data.get('exercises', []))} Aufgaben"
            )
            return True

        except json.JSONDecodeError as e:
            messagebox.showerror("JSON-Fehler", f"Ungültiges JSON-Format:\n\n{str(e)}")
            return False
        except ValueError as e:
            messagebox.showerror("Validierungsfehler", f"JSON-Struktur ist ungültig:\n\n{str(e)}")
            return False

    def generate_pdfs(self):
        """Generate PDF files from JSON input"""
        # Check if PDF generator is available
        if not self.pdf_generator:
            messagebox.showerror(
                "Fehler",
                "PDF-Generierung nicht verfügbar!\n\n"
                "reportlab ist nicht installiert.\n"
                "Installiere es mit:\n\n"
                "pip install reportlab",
            )
            return

        json_string = self.json_text.get(1.0, tk.END).strip()

        if not json_string:
            messagebox.showwarning("Warnung", "Bitte fügen Sie JSON-Daten ein.")
            return

        # Validate first
        if not self.validate_json():
            return

        try:
            data = json.loads(json_string)

            # Ask for output directory
            output_dir = filedialog.askdirectory(title="Wähle Speicherort für PDFs")

            if not output_dir:
                return

            # Generate filename prefix from metadata
            topic = data["metadata"].get("topic", "exercise")
            safe_topic = "".join(c for c in topic if c.isalnum() or c in (" ", "_")).strip()
            safe_topic = safe_topic.replace(" ", "_")

            output_prefix = f"{output_dir}/{safe_topic}"

            # Generate PDFs
            self.status_label.config(text="Generiere PDFs...", foreground="blue")
            self.parent.update()

            exercise_pdf, solution_pdf = self.pdf_generator.generate_pdfs_from_json(data, output_prefix)

            # Show success message
            self.show_generate_success()
            messagebox.showinfo(
                "Erfolg",
                f"✓ PDFs erfolgreich erstellt!\n\n" f"Übungsblatt: {exercise_pdf}\n" f"Lösungsblatt: {solution_pdf}",
            )

            self.status_label.config(text=f"✓ PDFs erstellt: {exercise_pdf}", foreground="green")

        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Generieren der PDFs:\n\n{str(e)}")
            self.status_label.config(text="✗ Fehler beim Generieren", foreground="red")

    def clear_input(self):
        """Clear the JSON input field"""
        self.json_text.delete(1.0, tk.END)
        self.status_label.config(text="", foreground="gray")

    def load_sample(self):
        """Load sample JSON for testing"""
        sample_json = {
            "metadata": {
                "topic": "Nomen und Artikel",
                "grade": "4. Klasse",
                "subject": "Deutsch",
                "subtopics": ["Plural", "Artikel", "Merkwörter"],
            },
            "exercises": [
                {
                    "id": 1,
                    "type": "Unterstreichen",
                    "subtopic": "Plural",
                    "question": "Unterstreiche alle Pluralformen in diesem Satz:",
                    "sub_questions": [
                        {
                            "question": '"Die Katzen jagen Mäuse, und die Hunde bellen laut."',
                            "answer": "Katzen, Mäuse, Hunde (unterstrichen)",
                            "explanation": "Diese Wörter stehen im Plural.",
                        },
                        {
                            "question": '"Die Kinder spielen mit ihren Bällen im Garten."',
                            "answer": "Kinder, Bällen (unterstrichen)",
                            "explanation": "Kinder und Bällen sind Pluralformen.",
                        },
                    ],
                    "explanation": "Pluralformen erkennt man oft an der Endung und dem Artikel 'die'.",
                },
                {
                    "id": 2,
                    "type": "Ankreuzen (Multiple Choice)",
                    "subtopic": "Artikel",
                    "question": "Welcher Artikel passt zu 'Baum'?",
                    "options": ["der", "die", "das"],
                    "answer": "der",
                    "explanation": "Baum ist maskulin, daher verwendet man den Artikel 'der'.",
                },
                {
                    "id": 3,
                    "type": "Formbildung/Variation",
                    "subtopic": "Plural",
                    "question": "Bilde die Pluralform:",
                    "sub_questions": [
                        {
                            "question": "Der Apfel → ___",
                            "answer": "Die Äpfel",
                            "explanation": "Bei 'Apfel' wird ein Umlaut verwendet: a → ä.",
                        },
                        {
                            "question": "Das Kind → ___",
                            "answer": "Die Kinder",
                            "explanation": "Bei 'Kind' wird -er angehängt.",
                        },
                    ],
                },
            ],
        }

        json_string = json.dumps(sample_json, indent=2, ensure_ascii=False)
        self.json_text.delete(1.0, tk.END)
        self.json_text.insert(1.0, json_string)
        self.status_label.config(text="Beispiel-JSON mit neuer Struktur geladen", foreground="blue")

    def show_validation_success(self):
        """Show visual feedback for successful validation"""
        original_bg = self.json_text.cget("bg")
        self.json_text.configure(bg="#e8f5e9")
        self.parent.after(1500, lambda: self.json_text.configure(bg=original_bg))

    def show_generate_success(self):
        """Show visual feedback for successful PDF generation"""
        original_bg = self.generate_button.cget("bg")
        self.generate_button.configure(bg="#2ecc71")
        self.parent.after(2000, lambda: self.generate_button.configure(bg=original_bg))
