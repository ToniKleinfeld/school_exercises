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


class ToggleSwitch(tk.Canvas):
    """Custom toggle switch widget with animation"""

    def __init__(self, parent, width=60, height=30, command=None):
        super().__init__(parent, width=width, height=height, bg="#f0f0f0", highlightthickness=0, cursor="hand2")
        self.width = width
        self.height = height
        self.command = command
        self.is_on = False  # Start with PDF (False = PDF, True = JSON)

        # Colors
        self.bg_off = "#cccccc"  # Gray for PDF
        self.bg_on = "#4CAF50"  # Green for JSON
        self.toggle_color = "#ffffff"

        # Animation
        self.animation_steps = 10
        self.animation_delay = 20  # ms

        self.draw()
        self.bind("<Button-1>", self.toggle)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def draw(self, circle_x=None):
        """Draw the switch"""
        self.delete("all")

        # Background with rounded corners
        bg_color = self.bg_on if self.is_on else self.bg_off

        # Create rounded rectangle for background
        self.create_oval(0, 0, self.height, self.height, fill=bg_color, outline="")
        self.create_oval(self.width - self.height, 0, self.width, self.height, fill=bg_color, outline="")
        self.create_rectangle(
            self.height // 2, 0, self.width - self.height // 2, self.height, fill=bg_color, outline=""
        )

        # Circle position
        if circle_x is None:
            circle_x = self.width - self.height // 2 - 3 if self.is_on else self.height // 2

        # Toggle circle (simple design, no shadow)
        self.create_oval(
            circle_x - self.height // 2 + 3,
            3,
            circle_x + self.height // 2 - 3,
            self.height - 3,
            fill=self.toggle_color,
            outline="gray",
            width=1,
        )

    def toggle(self, event=None):
        """Toggle the switch state with animation"""
        self.is_on = not self.is_on
        self.animate()
        if self.command:
            self.command(self.is_on)

    def animate(self):
        """Animate the toggle transition"""
        start_x = self.height // 2 if not self.is_on else self.width - self.height // 2 - 3
        end_x = self.width - self.height // 2 - 3 if self.is_on else self.height // 2
        step = (end_x - start_x) / self.animation_steps

        def animate_step(current_step, current_x):
            if current_step <= self.animation_steps:
                self.draw(circle_x=current_x)
                self.after(self.animation_delay, lambda: animate_step(current_step + 1, current_x + step))

        animate_step(0, start_x)

    def on_enter(self, event=None):
        """Handle mouse enter (hover effect)"""
        self.config(bg="#e8e8e8")

    def on_leave(self, event=None):
        """Handle mouse leave"""
        self.config(bg="#f0f0f0")

    def get_state(self):
        """Get current state (False=PDF, True=JSON)"""
        return self.is_on

    def set_state(self, state):
        """Set the state programmatically"""
        if self.is_on != state:
            self.is_on = state
            self.draw()


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
        self.output_mode = "pdf"  # Default to PDF mode
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

        # Tab 1: Unified Prompt Generator (PDF/JSON)
        self.prompt_tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(self.prompt_tab, text="Prompt Generator")

        # Tab 2: JSON Import & PDF Generator
        self.json_import_tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.json_import_tab, text="JSON → PDF Generator")

        # Create content for each tab
        self.create_prompt_generator_tab(self.prompt_tab)
        self.create_json_import_tab(self.json_import_tab)

    def create_prompt_generator_tab(self, parent_frame):
        """Create unified prompt generator interface with PDF/JSON toggle"""
        # Configure grid
        parent_frame.columnconfigure(1, weight=1)

        # Title
        title_label = ttk.Label(parent_frame, text="Prompt Generator", font=MAIN_FONT)
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Output mode selector (PDF/JSON Toggle)
        mode_frame = ttk.Frame(parent_frame)
        mode_frame.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        pdf_label = ttk.Label(mode_frame, text="PDF", font=LABEL_FONT)
        pdf_label.pack(side=tk.LEFT, padx=5)

        self.toggle_switch = ToggleSwitch(mode_frame, command=self.on_mode_changed)
        self.toggle_switch.pack(side=tk.LEFT, padx=10)

        json_label = ttk.Label(mode_frame, text="JSON", font=LABEL_FONT)
        json_label.pack(side=tk.LEFT, padx=5)

        # Input fields
        self.create_input_fields(parent_frame, start_row=2)

        # Generate button
        self.generate_button = tk.Button(
            parent_frame,
            text=GENERATE_BUTTON_TEXT,
            command=self.generate_prompt,
            font=LABEL_FONT,
            relief="raised",
            bd=2,
        )
        self.generate_button.grid(row=9, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))

        # Output section
        self.create_output_section(parent_frame)

        # Copy button
        self.copy_button = tk.Button(
            parent_frame,
            text=COPY_BUTTON_TEXT,
            command=self.copy_to_clipboard,
            font=LABEL_FONT,
            relief="raised",
            bd=2,
        )
        self.copy_button.grid(row=12, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    def on_mode_changed(self, is_json):
        """Handle output mode toggle change"""
        self.output_mode = "json" if is_json else "pdf"
        # Update button text
        if is_json:
            self.generate_button.config(text="Generate JSON Prompt")
        else:
            self.generate_button.config(text=GENERATE_BUTTON_TEXT)

    def create_json_import_tab(self, parent_frame):
        """Create JSON import and PDF generation interface"""
        from json_import_ui import JSONImportUI

        self.json_import_ui = JSONImportUI(parent_frame)

    def create_input_fields(self, parent, start_row=1):
        """Create all input fields with labels"""
        row = start_row

        # Grade/Class - German school system
        ttk.Label(parent, text="Klasse/Jahrgangsstufe:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.grade_var = tk.StringVar()
        grade_combo = ttk.Combobox(parent, textvariable=self.grade_var, width=40)
        grade_combo["values"] = GRADES
        grade_combo.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1

        # Subject - German school subjects
        ttk.Label(parent, text="Fach:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.subject_var = tk.StringVar()
        subject_combo = ttk.Combobox(parent, textvariable=self.subject_var, width=40)
        subject_combo["values"] = SUBJECTS
        subject_combo.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        subject_combo.bind("<<ComboboxSelected>>", self.on_subject_changed)
        row += 1

        # Topic structure with main topic and subtopics
        ttk.Label(parent, text="Hauptthema:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.main_topic_var = tk.StringVar()
        main_topic_entry = ttk.Entry(parent, textvariable=self.main_topic_var, width=40)
        main_topic_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1

        # Subtopics
        ttk.Label(parent, text="Unterthemen:").grid(row=row, column=0, sticky=(tk.W, tk.N), pady=5)
        self.subtopics_var = tk.StringVar()
        subtopics_entry = ttk.Entry(parent, textvariable=self.subtopics_var, width=40)
        subtopics_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1

        # Help text for subtopics
        help_text = ttk.Label(
            parent,
            text="(Getrennt durch Kommas)",
            font=("Arial", 8),
            foreground="gray",
        )
        help_text.grid(row=row, column=1, sticky=tk.W, padx=(10, 0))
        row += 1

        # Exercise Types - Multiple selection with checkboxes
        self.create_exercise_type_section(parent, row=row)
        row += 1

        # Number of Questions per Type
        ttk.Label(parent, text="Anzahl der Aufgaben:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.num_questions_var = tk.StringVar(value=DEFAULT_NUM_QUESTIONS)
        num_spinbox = ttk.Spinbox(
            parent, from_=MIN_QUESTIONS, to=MAX_QUESTIONS, textvariable=self.num_questions_var, width=38
        )
        num_spinbox.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

    def create_exercise_type_section(self, parent, row=6):
        """Create exercise type selection with checkboxes"""
        ttk.Label(parent, text="Aufgabentypen:").grid(row=row, column=0, sticky=(tk.W, tk.N), pady=5)

        # Frame for checkboxes
        self.exercise_frame = ttk.Frame(parent)
        self.exercise_frame.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

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
        self.output_label = ttk.Label(parent, text="Generierter Prompt:", font=LABEL_FONT)
        self.output_label.grid(row=10, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))

        # Output text area with scrollbar
        self.output_text = scrolledtext.ScrolledText(parent, height=8, width=70, wrap=tk.WORD, font=OUTPUT_FONT)
        self.output_text.grid(row=11, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Configure text area to expand
        parent.rowconfigure(11, weight=1)

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

        # Generate the prompt based on output mode
        if self.output_mode == "json":
            prompt = self.prompt_generator.create_json_prompt_template(
                num_questions, grade, subject, main_topic, subtopics, selected_exercise_types
            )
            self.output_label.config(text="Generierter JSON-Prompt:")
        else:
            prompt = self.prompt_generator.create_prompt_template(
                num_questions, grade, subject, main_topic, subtopics, selected_exercise_types
            )
            self.output_label.config(text="Generierter Prompt:")

        # Display the prompt in the output area
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, prompt)

        # Automatically copy to clipboard
        try:
            pyperclip.copy(prompt)
        except Exception:
            pass  # Silent fail for auto-copy

        # Show visual feedback: green flash for text area AND button success
        self.show_text_area_success(self.output_text)
        self.show_generate_button_success(self.generate_button)

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
            self.show_copy_button_success(self.copy_button)
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
