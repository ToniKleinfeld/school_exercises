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
        """Create and arrange all GUI widgets with tab system"""
        # Configure grid weights for responsive design
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Create notebook (tab container)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        # Tab 1: Standard Prompt Generator
        self.prompt_tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(self.prompt_tab, text="Prompt Generator (PDF)")

        # Tab 2: JSON Prompt Generator
        self.json_prompt_tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(self.json_prompt_tab, text="Prompt Generator (JSON)")

        # Tab 3: JSON Import & PDF Generator
        self.json_import_tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.json_import_tab, text="JSON → PDF Generator")

        # Create content for each tab
        self.create_prompt_generator_tab(self.prompt_tab, use_json=False)
        self.create_prompt_generator_tab(self.json_prompt_tab, use_json=True)
        self.create_json_import_tab(self.json_import_tab)

    def create_prompt_generator_tab(self, parent_frame, use_json=False):
        """Create prompt generator interface"""
        # Configure grid
        parent_frame.columnconfigure(1, weight=1)

        # Title
        tab_title = "JSON-Prompt Generator" if use_json else "Standard Prompt Generator"
        title_label = ttk.Label(parent_frame, text=tab_title, font=MAIN_FONT)
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Input fields
        self.create_input_fields(parent_frame)

        # Generate button
        button_text = "Generate JSON Prompt" if use_json else GENERATE_BUTTON_TEXT
        generate_button = tk.Button(
            parent_frame,
            text=button_text,
            command=lambda: self.generate_prompt(use_json=use_json),
            font=LABEL_FONT,
            relief="raised",
            bd=2,
        )
        generate_button.grid(row=8, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))

        # Store button reference
        if use_json:
            self.json_generate_button = generate_button
        else:
            self.generate_button = generate_button

        # Output section
        self.create_output_section(parent_frame, use_json=use_json)

        # Copy button
        copy_button = tk.Button(
            parent_frame,
            text=COPY_BUTTON_TEXT,
            command=lambda: self.copy_to_clipboard(use_json=use_json),
            font=LABEL_FONT,
            relief="raised",
            bd=2,
        )
        copy_button.grid(row=11, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        # Store button reference
        if use_json:
            self.json_copy_button = copy_button
        else:
            self.copy_button = copy_button

    def create_json_import_tab(self, parent_frame):
        """Create JSON import and PDF generation interface"""
        from json_import_ui import JSONImportUI

        self.json_import_ui = JSONImportUI(parent_frame)

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

    def create_output_section(self, parent, use_json=False):
        """Create the output section with generated prompt display"""
        # Output label
        label_text = "Generierter JSON-Prompt:" if use_json else "Generierter Prompt:"
        output_label = ttk.Label(parent, text=label_text, font=LABEL_FONT)
        output_label.grid(row=9, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))

        # Output text area with scrollbar
        output_text = scrolledtext.ScrolledText(parent, height=8, width=70, wrap=tk.WORD, font=OUTPUT_FONT)
        output_text.grid(row=10, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Store reference
        if use_json:
            self.json_output_text = output_text
        else:
            self.output_text = output_text

        # Configure text area to expand
        parent.rowconfigure(10, weight=1)

    def generate_prompt(self, use_json=False):
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
        if use_json:
            prompt = self.prompt_generator.create_json_prompt_template(
                num_questions, grade, subject, main_topic, subtopics, selected_exercise_types
            )
            output_text = self.json_output_text
            button = self.json_generate_button
        else:
            prompt = self.prompt_generator.create_prompt_template(
                num_questions, grade, subject, main_topic, subtopics, selected_exercise_types
            )
            output_text = self.output_text
            button = self.generate_button

        # Display the prompt in the output area
        output_text.delete(1.0, tk.END)
        output_text.insert(1.0, prompt)

        # Automatically copy to clipboard
        try:
            pyperclip.copy(prompt)
        except Exception:
            pass  # Silent fail for auto-copy

        # Show visual feedback: green flash for text area AND button success
        self.show_text_area_success(output_text)
        self.show_generate_button_success(button)

    def copy_to_clipboard(self, use_json=False):
        """Copy the generated prompt to clipboard"""
        output_text = self.json_output_text if use_json else self.output_text
        copy_button = self.json_copy_button if use_json else self.copy_button

        prompt_text = output_text.get(1.0, tk.END).strip()

        if not prompt_text:
            messagebox.showwarning(
                "Warnung", "Kein Prompt zum Kopieren vorhanden. Bitte generieren Sie zuerst einen Prompt."
            )
            return

        try:
            pyperclip.copy(prompt_text)
            # Show visual feedback: green button flash and checkmark
            self.show_copy_button_success(copy_button)
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Kopieren in die Zwischenablage: {str(e)}")

    def show_text_area_success(self, output_text):
        """Show green flash feedback for successful prompt generation"""
        # Store original background color
        original_bg = output_text.cget("bg")

        # Set green background
        output_text.configure(bg="lightgreen")

        # Reset to original color after 1.5 seconds
        self.root.after(1500, lambda: output_text.configure(bg=original_bg))

    def show_copy_button_success(self, copy_button):
        """Show green flash feedback for successful clipboard copy"""
        # Store original button properties
        original_text = copy_button.cget("text")
        original_relief = copy_button.cget("relief")
        original_bg = copy_button.cget("bg")

        # Set success styling (now works with tk.Button)
        copy_button.configure(text="✓ Copy to Clipboard", relief="solid", bg="lightgreen")

        # Reset to original styling after 2 seconds
        def reset_button():
            copy_button.configure(text=original_text, relief=original_relief, bg=original_bg)

        self.root.after(2000, reset_button)

    def show_generate_button_success(self, generate_button):
        """Show green flash feedback for successful prompt generation"""
        # Store original button properties
        original_text = generate_button.cget("text")
        original_relief = generate_button.cget("relief")
        original_bg = generate_button.cget("bg")

        # Set success styling
        success_text = "✓ " + original_text
        generate_button.configure(text=success_text, relief="solid", bg="lightgreen")

        # Reset to original styling after 2 seconds
        def reset_button():
            generate_button.configure(text=original_text, relief=original_relief, bg=original_bg)

        self.root.after(2000, reset_button)
