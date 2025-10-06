"""
UI Module for AI Prompt Generator

This module contains all user interface components and handles user interactions.
It provides a clean separation between UI logic and business logic.

Author: AI Assistant
Date: October 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyperclip


class AIPromptGeneratorUI:
    """UI class for the AI Prompt Generator application"""

    def __init__(self, root, prompt_generator):
        """
        Initialize the UI with the main window and prompt generator

        Args:
            root: Tkinter root window
            prompt_generator: Instance of PromptGenerator class
        """
        self.root = root
        self.prompt_generator = prompt_generator
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        """Configure the main window properties"""
        self.root.title("KI Prompt Generator für Bildungsaufgaben")
        self.root.geometry("700x600")
        self.root.resizable(True, True)

        # Configure style
        style = ttk.Style()
        style.theme_use("clam")

    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights for responsive design
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # Title
        title_label = ttk.Label(main_frame, text="KI Prompt Generator", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Input fields
        self.create_input_fields(main_frame)

        # Generate button
        generate_btn = ttk.Button(
            main_frame, text="Generate Prompt", command=self.generate_prompt, style="Accent.TButton"
        )
        generate_btn.grid(row=6, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))

        # Output section
        self.create_output_section(main_frame)

        # Copy button
        copy_btn = ttk.Button(main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_btn.grid(row=9, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    def create_input_fields(self, parent):
        """Create all input fields with labels"""
        # Grade/Class - German school system
        ttk.Label(parent, text="Klasse/Jahrgangsstufe:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.grade_var = tk.StringVar()
        grade_combo = ttk.Combobox(parent, textvariable=self.grade_var, width=40)
        grade_combo["values"] = (
            "1. Klasse",
            "2. Klasse",
            "3. Klasse",
            "4. Klasse",
            "5. Klasse",
            "6. Klasse",
            "7. Klasse",
            "8. Klasse",
            "9. Klasse",
            "10. Klasse",
            "11. Klasse",
            "12. Klasse",
            "13. Klasse",
            "Oberstufe",
            "Universität",
        )
        grade_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Subject - German school subjects
        ttk.Label(parent, text="Fach:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.subject_var = tk.StringVar()
        subject_combo = ttk.Combobox(parent, textvariable=self.subject_var, width=40)
        subject_combo["values"] = (
            "Mathematik",
            "Deutsch",
            "Englisch",
            "Französisch",
            "Spanisch",
            "Latein",
            "Physik",
            "Chemie",
            "Biologie",
            "Geschichte",
            "Geographie",
            "Politik/Wirtschaft",
            "Sozialwissenschaften",
            "Religion",
            "Ethik",
            "Philosophie",
            "Kunst",
            "Musik",
            "Sport",
            "Informatik",
            "Technik",
            "Wirtschaft",
        )
        subject_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Topic
        ttk.Label(parent, text="Thema:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.topic_var = tk.StringVar()
        topic_entry = ttk.Entry(parent, textvariable=self.topic_var, width=40)
        topic_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Exercise Type - German terms
        ttk.Label(parent, text="Aufgabentyp:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.exercise_type_var = tk.StringVar()
        exercise_combo = ttk.Combobox(parent, textvariable=self.exercise_type_var, width=40)
        exercise_combo["values"] = (
            "Multiple Choice",
            "Offene Fragen",
            "Richtig/Falsch",
            "Lückentext",
            "Kurze Antworten",
            "Aufsatzfragen",
            "Problemlösung",
            "Rechenaufgaben",
            "Analyseaufgaben",
            "Interpretationsaufgaben",
            "Erörterung",
        )
        exercise_combo.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Number of Questions
        ttk.Label(parent, text="Anzahl der Aufgaben:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.num_questions_var = tk.StringVar(value="5")
        num_spinbox = ttk.Spinbox(parent, from_=1, to=50, textvariable=self.num_questions_var, width=38)
        num_spinbox.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

    def create_output_section(self, parent):
        """Create the output section with generated prompt display"""
        # Output label
        output_label = ttk.Label(parent, text="Generierter Prompt:", font=("Arial", 12, "bold"))
        output_label.grid(row=7, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))

        # Output text area with scrollbar
        self.output_text = scrolledtext.ScrolledText(parent, height=8, width=70, wrap=tk.WORD, font=("Consolas", 10))
        self.output_text.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Configure text area to expand
        parent.rowconfigure(8, weight=1)

    def generate_prompt(self):
        """Generate the AI prompt based on user inputs"""
        # Get values from input fields
        grade = self.grade_var.get()
        subject = self.subject_var.get()
        topic = self.topic_var.get()
        exercise_type = self.exercise_type_var.get()
        num_questions = self.num_questions_var.get()

        # Validate inputs using the prompt generator
        is_valid, error_message = self.prompt_generator.validate_inputs(
            grade, subject, topic, exercise_type, num_questions
        )

        if not is_valid:
            messagebox.showerror("Eingabefehler", error_message)
            return

        # Generate the prompt using the prompt generator
        prompt = self.prompt_generator.create_prompt_template(num_questions, grade, subject, topic, exercise_type)

        # Display the prompt in the output area
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, prompt)

        # Show success message
        messagebox.showinfo("Erfolg", "Prompt erfolgreich generiert!")

    def copy_to_clipboard(self):
        """Copy the generated prompt to clipboard"""
        prompt_text = self.output_text.get(1.0, tk.END).strip()

        if not prompt_text:
            messagebox.showwarning(
                "Warnung", "Kein Prompt zum Kopieren vorhanden. Bitte generieren Sie zuerst einen Prompt."
            )
            return

        try:
            pyperclip.copy(prompt_text)
            messagebox.showinfo("Erfolg", "Prompt in die Zwischenablage kopiert!")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Kopieren in die Zwischenablage: {str(e)}")
