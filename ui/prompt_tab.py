"""
Prompt Generator Tab

Tab component for the unified prompt generator with PDF/JSON toggle.        self.copy_button.grid(row=11, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    def create_json_im        # Output text area with scrollbar
        self.output_text = scrolledtext.ScrolledText(self.parent, height=8, width=70, wrap=tk.WORD, font=OUTPUT_FONT)
        self.output_text.grid(row=10, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Configure text area to expand
        self.parent.rowconfigure(10, weight=1)ab(self, parent_frame):oni Kleinfeld
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


class PromptGeneratorTab:
    """Prompt generator tab with PDF/JSON toggle"""

    def __init__(self, parent_frame, root, prompt_generator):
        """
        Initialize the prompt generator tab

        Args:
            parent_frame: Parent tkinter frame
            root: Root window (for after() callbacks)
            prompt_generator: Instance of PromptGenerator class
        """
        self.parent = parent_frame
        self.root = root
        self.prompt_generator = prompt_generator

        # Variables for input fields
        self.grade_var = None
        self.subject_var = None
        self.main_topic_var = None
        self.subtopics_var = None
        self.num_questions_var = None
        self.exercise_type_vars = {}
        self.exercise_checkboxes = []
        self.exercise_frame = None

        # UI elements
        self.generate_button = None
        self.copy_button = None
        self.output_label = None
        self.output_text = None

        self.create_ui()

    def create_ui(self):
        """Create the complete tab UI"""
        # Configure grid
        self.parent.columnconfigure(1, weight=1)

        # Title
        title_label = ttk.Label(self.parent, text="JSON Prompt Generator", font=MAIN_FONT)
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Input fields
        self.create_input_fields(start_row=1)

        # Generate button
        self.generate_button = tk.Button(
            self.parent,
            text="Generate JSON Prompt",
            command=self.generate_prompt,
            font=LABEL_FONT,
            relief="raised",
            bd=2,
        )
        self.generate_button.grid(row=8, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))

        # Output section
        self.create_output_section()

        # Copy button
        self.copy_button = tk.Button(
            self.parent,
            text=COPY_BUTTON_TEXT,
            command=self.copy_to_clipboard,
            font=LABEL_FONT,
            relief="raised",
            bd=2,
        )
        self.copy_button.grid(row=12, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    def create_input_fields(self, start_row=1):
        """Create all input fields with labels"""
        row = start_row

        # Grade/Class
        ttk.Label(self.parent, text="Klasse/Jahrgangsstufe:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.grade_var = tk.StringVar()
        grade_combo = ttk.Combobox(self.parent, textvariable=self.grade_var, width=40)
        grade_combo["values"] = GRADES
        grade_combo.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1

        # Subject
        ttk.Label(self.parent, text="Fach:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.subject_var = tk.StringVar()
        subject_combo = ttk.Combobox(self.parent, textvariable=self.subject_var, width=40)
        subject_combo["values"] = SUBJECTS
        subject_combo.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        subject_combo.bind("<<ComboboxSelected>>", self.on_subject_changed)
        row += 1

        # Main topic
        ttk.Label(self.parent, text="Hauptthema:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.main_topic_var = tk.StringVar()
        main_topic_entry = ttk.Entry(self.parent, textvariable=self.main_topic_var, width=40)
        main_topic_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1

        # Subtopics
        ttk.Label(self.parent, text="Unterthemen:").grid(row=row, column=0, sticky=(tk.W, tk.N), pady=5)
        self.subtopics_var = tk.StringVar()
        subtopics_entry = ttk.Entry(self.parent, textvariable=self.subtopics_var, width=40)
        subtopics_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1

        # Help text for subtopics
        help_text = ttk.Label(self.parent, text="(Getrennt durch Kommas)", font=("Arial", 8), foreground="gray")
        help_text.grid(row=row, column=1, sticky=tk.W, padx=(10, 0))
        row += 1

        # Exercise Types
        self.create_exercise_type_section(row=row)
        row += 1

        # Number of Questions per Type
        ttk.Label(self.parent, text="Anzahl der Aufgaben:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.num_questions_var = tk.StringVar(value=DEFAULT_NUM_QUESTIONS)
        num_spinbox = ttk.Spinbox(
            self.parent, from_=MIN_QUESTIONS, to=MAX_QUESTIONS, textvariable=self.num_questions_var, width=38
        )
        num_spinbox.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

    def create_exercise_type_section(self, row=6):
        """Create exercise type selection with checkboxes"""
        ttk.Label(self.parent, text="Aufgabentypen:").grid(row=row, column=0, sticky=(tk.W, tk.N), pady=5)

        # Frame for checkboxes
        self.exercise_frame = ttk.Frame(self.parent)
        self.exercise_frame.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Help label
        help_label = ttk.Label(
            self.exercise_frame,
            text="Bitte wählen Sie zuerst ein Fach aus, um verfügbare Aufgabentypen zu sehen.",
            font=HELP_FONT,
            foreground="gray",
        )
        help_label.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=5)
        self.exercise_checkboxes.append(help_label)

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
        exercise_types = EXERCISE_MAPPINGS.get(selected_subject, DEFAULT_EXERCISE_TYPES)

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

    def create_output_section(self):
        """Create the output section with generated prompt display"""
        # Output label
        self.output_label = ttk.Label(self.parent, text="Generierter JSON-Prompt:", font=LABEL_FONT)
        self.output_label.grid(row=9, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))

        # Output text area with scrollbar
        self.output_text = scrolledtext.ScrolledText(self.parent, height=8, width=70, wrap=tk.WORD, font=OUTPUT_FONT)
        self.output_text.grid(row=10, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Configure text area to expand
        self.parent.rowconfigure(10, weight=1)

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

        # Convert list to string for validation
        exercise_types_str = ", ".join(selected_exercise_types) if selected_exercise_types else ""

        # Validate inputs
        is_valid, error_message = self.prompt_generator.validate_inputs(
            grade, subject, main_topic, subtopics, exercise_types_str, num_questions
        )

        if is_valid and not selected_exercise_types:
            is_valid = False
            error_message = "Bitte wählen Sie mindestens einen Aufgabentyp aus."

        if not is_valid:
            messagebox.showerror("Eingabefehler", error_message)
            return

        # Generate JSON prompt
        prompt = self.prompt_generator.create_json_prompt_template(
            num_questions, grade, subject, main_topic, subtopics, selected_exercise_types
        )

        # Display the prompt
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, prompt)

        # Auto-copy to clipboard
        try:
            pyperclip.copy(prompt)
        except Exception:
            pass

        # Visual feedback
        self.show_text_area_success()
        self.show_generate_button_success()

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
            self.show_copy_button_success()
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Kopieren in die Zwischenablage: {str(e)}")

    def show_text_area_success(self):
        """Show green flash feedback for successful prompt generation"""
        original_bg = self.output_text.cget("bg")
        self.output_text.configure(bg="lightgreen")
        self.root.after(1500, lambda: self.output_text.configure(bg=original_bg))

    def show_copy_button_success(self):
        """Show green flash feedback for successful clipboard copy"""
        original_text = self.copy_button.cget("text")
        original_relief = self.copy_button.cget("relief")
        original_bg = self.copy_button.cget("bg")

        self.copy_button.configure(text="✓ Copy to Clipboard", relief="solid", bg="lightgreen")

        def reset_button():
            self.copy_button.configure(text=original_text, relief=original_relief, bg=original_bg)

        self.root.after(2000, reset_button)

    def show_generate_button_success(self):
        """Show green flash feedback for successful prompt generation"""
        original_text = self.generate_button.cget("text")
        original_relief = self.generate_button.cget("relief")
        original_bg = self.generate_button.cget("bg")

        success_text = "✓ " + original_text
        self.generate_button.configure(text=success_text, relief="solid", bg="lightgreen")

        def reset_button():
            self.generate_button.configure(text=original_text, relief=original_relief, bg=original_bg)

        self.root.after(2000, reset_button)
