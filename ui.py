"""
UI Module for AI Prompt Generator

This module contains all user interface components and handles user interactions.
It provides a clean separation between UI logic and business logic.

Author: Toni Kleinfeld
Date: October 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyperclip
from config import (
    GRADES,
    SUBJECTS,
    EXERCISE_MAPPINGS,
    DEFAULT_EXERCISE_TYPES,
    WINDOW_TITLE,
    MAIN_TITLE,
    WINDOW_SIZE,
    MAIN_FONT,
    LABEL_FONT,
    HELP_FONT,
    OUTPUT_FONT,
    GENERATE_BUTTON_TEXT,
    COPY_BUTTON_TEXT,
    DEFAULT_NUM_QUESTIONS,
    MIN_QUESTIONS,
    MAX_QUESTIONS,
)


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
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
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
        title_label = ttk.Label(main_frame, text=MAIN_TITLE, font=MAIN_FONT)
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Input fields
        self.create_input_fields(main_frame)

        # Generate button
        generate_btn = ttk.Button(
            main_frame, text=GENERATE_BUTTON_TEXT, command=self.generate_prompt, style="Accent.TButton"
        )
        generate_btn.grid(row=8, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))

        # Output section
        self.create_output_section(main_frame)

        # Copy button - placed after output section
        self.copy_button = ttk.Button(main_frame, text=COPY_BUTTON_TEXT, command=self.copy_to_clipboard)
        self.copy_button.grid(row=11, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    def create_input_fields(self, parent):
        """Create all input fields with labels"""
        # Grade/Class - German school system
        ttk.Label(parent, text="Klasse/Jahrgangsstufe:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.grade_var = tk.StringVar()
        grade_combo = ttk.Combobox(parent, textvariable=self.grade_var, width=40)
        grade_combo["values"] = GRADES
        grade_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Subject - German school subjects
        ttk.Label(parent, text="Fach:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.subject_var = tk.StringVar()
        subject_combo = ttk.Combobox(parent, textvariable=self.subject_var, width=40)
        subject_combo["values"] = SUBJECTS
        subject_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        subject_combo.bind("<<ComboboxSelected>>", self.on_subject_changed)

        # Topic structure with main topic and subtopics
        ttk.Label(parent, text="Hauptthema:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.main_topic_var = tk.StringVar()
        main_topic_entry = ttk.Entry(parent, textvariable=self.main_topic_var, width=40)
        main_topic_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Subtopics
        ttk.Label(parent, text="Unterthemen:").grid(row=4, column=0, sticky=(tk.W, tk.N), pady=5)
        self.subtopics_var = tk.StringVar()
        subtopics_entry = ttk.Entry(parent, textvariable=self.subtopics_var, width=40)
        subtopics_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Help text for subtopics
        help_text = ttk.Label(
            parent,
            text="(Getrennt durch Kommas)",
            font=("Arial", 8),
            foreground="gray",
        )
        help_text.grid(row=5, column=1, sticky=tk.W, padx=(10, 0))

        # Exercise Types - Multiple selection with checkboxes
        self.create_exercise_type_section(parent)

        # Number of Questions per Type
        ttk.Label(parent, text="Aufgaben pro Typ:").grid(row=7, column=0, sticky=tk.W, pady=5)
        ttk.Label(parent, text="Anzahl der Aufgaben:").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.num_questions_var = tk.StringVar(value=DEFAULT_NUM_QUESTIONS)
        num_spinbox = ttk.Spinbox(
            parent, from_=MIN_QUESTIONS, to=MAX_QUESTIONS, textvariable=self.num_questions_var, width=38
        )
        num_spinbox.grid(row=7, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

    def create_exercise_type_section(self, parent):
        """Create exercise type selection with checkboxes"""
        ttk.Label(parent, text="Aufgabentypen:").grid(row=6, column=0, sticky=(tk.W, tk.N), pady=5)

        # Frame for checkboxes
        self.exercise_frame = ttk.Frame(parent)
        self.exercise_frame.grid(row=6, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Dictionary to store checkbox variables
        self.exercise_type_vars = {}

        # Initially empty - will be populated when subject is selected
        self.exercise_checkboxes = []

        # Help label
        help_label = ttk.Label(
            self.exercise_frame,
            text="Bitte wählen Sie zuerst ein Fach aus, um verfügbare Aufgabentypen zu sehen.",
            font=HELP_FONT,
            foreground="gray",
        )
        help_label.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=5)
        self.exercise_checkboxes.append(help_label)  # Add to list so it gets cleared

    def get_exercise_types_for_subject(self, subject):
        """Get appropriate exercise types for the selected subject"""
        return EXERCISE_MAPPINGS.get(subject, DEFAULT_EXERCISE_TYPES)

    def on_subject_changed(self, event=None):
        """Handle subject selection change"""
        selected_subject = self.subject_var.get()
        if not selected_subject:
            return

        # Clear existing checkboxes
        for checkbox in self.exercise_checkboxes:
            checkbox.destroy()
        self.exercise_checkboxes.clear()
        self.exercise_type_vars.clear()

        # Get exercise types for selected subject
        exercise_types = self.get_exercise_types_for_subject(selected_subject)

        # Create new checkboxes
        for i, exercise_type in enumerate(exercise_types):
            var = tk.BooleanVar()
            self.exercise_type_vars[exercise_type] = var

            checkbox = ttk.Checkbutton(self.exercise_frame, text=exercise_type, variable=var)

            # Arrange in columns for better layout
            row = i // 2
            col = i % 2
            checkbox.grid(row=row, column=col, sticky=tk.W, padx=(0, 20), pady=2)

            self.exercise_checkboxes.append(checkbox)

    def create_output_section(self, parent):
        """Create the output section with generated prompt display"""
        # Output label
        output_label = ttk.Label(parent, text="Generierter Prompt:", font=LABEL_FONT)
        output_label.grid(row=9, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))

        # Output text area with scrollbar
        self.output_text = scrolledtext.ScrolledText(parent, height=8, width=70, wrap=tk.WORD, font=OUTPUT_FONT)
        self.output_text.grid(row=10, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Configure text area to expand
        parent.rowconfigure(10, weight=1)

    def generate_prompt(self):
        """Generate the AI prompt based on user inputs"""
        # Get values from input fields
        grade = self.grade_var.get()
        subject = self.subject_var.get()
        main_topic = self.main_topic_var.get()
        subtopics = self.subtopics_var.get()
        num_questions = self.num_questions_var.get()

        # Get selected exercise types from checkboxes
        selected_exercise_types = []
        for exercise_type, var in self.exercise_type_vars.items():
            if var.get():
                selected_exercise_types.append(exercise_type)

        # Convert list to string for validation (backwards compatibility)
        exercise_types_str = ", ".join(selected_exercise_types) if selected_exercise_types else ""

        # Validate inputs using the prompt generator
        is_valid, error_message = self.prompt_generator.validate_inputs(
            grade, subject, main_topic, subtopics, exercise_types_str, num_questions
        )

        # Additional validation for exercise types
        if is_valid and not selected_exercise_types:
            is_valid = False
            error_message = "Bitte wählen Sie mindestens einen Aufgabentyp aus."

        if not is_valid:
            messagebox.showerror("Eingabefehler", error_message)
            return

        # Generate the prompt using the prompt generator
        prompt = self.prompt_generator.create_prompt_template(
            num_questions, grade, subject, main_topic, subtopics, selected_exercise_types
        )

        # Display the prompt in the output area
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, prompt)

        # Automatically copy to clipboard
        try:
            pyperclip.copy(prompt)
        except Exception:
            pass  # Silent fail for auto-copy

        # Show visual feedback: green flash for text area
        self.show_text_area_success()

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
            # Show visual feedback: green button flash and checkmark
            self.show_copy_button_success()
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Kopieren in die Zwischenablage: {str(e)}")

    def show_text_area_success(self):
        """Show green flash feedback for successful prompt generation"""
        # Store original background color
        original_bg = self.output_text.cget("bg")

        # Set green background
        self.output_text.configure(bg="lightgreen")

        # Reset to original color after 1.5 seconds
        self.root.after(1500, lambda: self.output_text.configure(bg=original_bg))

    def show_copy_button_success(self):
        """Show green flash feedback for successful clipboard copy"""
        # Store original button properties
        original_text = self.copy_button.cget("text")
        original_relief = self.copy_button.cget("relief")
        original_bg = self.copy_button.cget("background")

        # Set success styling
        self.copy_button.configure(text="✓ Copy to Clipboard", relief="solid", background="lightgreen")

        # Reset to original styling after 2 seconds
        def reset_button():
            self.copy_button.configure(text=original_text, relief=original_relief, background=original_bg)

        self.root.after(2000, reset_button)
