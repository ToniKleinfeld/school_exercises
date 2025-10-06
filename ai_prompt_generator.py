"""
AI Prompt Generator for Educational Exercises

A simple GUI application that generates AI prompts for creating educational exercises
based on user input parameters like grade, subject, topic, exercise type, and number of questions.

Author: AI Assistant
Date: October 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyperclip


class AIPromptGenerator:
    """Main application class for the AI Prompt Generator"""

    def __init__(self, root):
        """Initialize the application with the main window and widgets"""
        self.root = root
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        """Configure the main window properties"""
        self.root.title("AI Prompt Generator for Educational Exercises")
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
        title_label = ttk.Label(main_frame, text="AI Prompt Generator", font=("Arial", 16, "bold"))
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
        # Grade/Class
        ttk.Label(parent, text="Grade/Class:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.grade_var = tk.StringVar()
        grade_combo = ttk.Combobox(parent, textvariable=self.grade_var, width=40)
        grade_combo["values"] = (
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
            "7th",
            "8th",
            "9th",
            "10th",
            "11th",
            "12th",
            "University",
        )
        grade_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Subject
        ttk.Label(parent, text="Subject:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.subject_var = tk.StringVar()
        subject_combo = ttk.Combobox(parent, textvariable=self.subject_var, width=40)
        subject_combo["values"] = (
            "Mathematics",
            "English",
            "Science",
            "History",
            "Geography",
            "Physics",
            "Chemistry",
            "Biology",
            "Computer Science",
            "Literature",
            "Economics",
            "Philosophy",
            "Art",
            "Music",
        )
        subject_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Topic
        ttk.Label(parent, text="Topic:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.topic_var = tk.StringVar()
        topic_entry = ttk.Entry(parent, textvariable=self.topic_var, width=40)
        topic_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Exercise Type
        ttk.Label(parent, text="Exercise Type:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.exercise_type_var = tk.StringVar()
        exercise_combo = ttk.Combobox(parent, textvariable=self.exercise_type_var, width=40)
        exercise_combo["values"] = (
            "Multiple Choice",
            "Open Questions",
            "True/False",
            "Fill in the Blanks",
            "Short Answer",
            "Essay Questions",
            "Problem Solving",
            "Calculation Tasks",
            "Analysis Tasks",
        )
        exercise_combo.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Number of Questions
        ttk.Label(parent, text="Number of Questions:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.num_questions_var = tk.StringVar(value="5")
        num_spinbox = ttk.Spinbox(parent, from_=1, to=50, textvariable=self.num_questions_var, width=38)
        num_spinbox.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

    def create_output_section(self, parent):
        """Create the output section with generated prompt display"""
        # Output label
        output_label = ttk.Label(parent, text="Generated Prompt:", font=("Arial", 12, "bold"))
        output_label.grid(row=7, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))

        # Output text area with scrollbar
        self.output_text = scrolledtext.ScrolledText(parent, height=8, width=70, wrap=tk.WORD, font=("Consolas", 10))
        self.output_text.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Configure text area to expand
        parent.rowconfigure(8, weight=1)

    def validate_inputs(self):
        """Validate all required input fields"""
        required_fields = [
            (self.grade_var.get().strip(), "Grade/Class"),
            (self.subject_var.get().strip(), "Subject"),
            (self.topic_var.get().strip(), "Topic"),
            (self.exercise_type_var.get().strip(), "Exercise Type"),
            (self.num_questions_var.get().strip(), "Number of Questions"),
        ]

        for value, field_name in required_fields:
            if not value:
                messagebox.showerror("Validation Error", f"Please fill in the {field_name} field.")
                return False

        # Validate number of questions is a positive integer
        try:
            num = int(self.num_questions_var.get())
            if num <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Validation Error", "Number of Questions must be a positive integer.")
            return False

        return True

    def generate_prompt(self):
        """Generate the AI prompt based on user inputs"""
        if not self.validate_inputs():
            return

        # Get values from input fields
        grade = self.grade_var.get().strip()
        subject = self.subject_var.get().strip()
        topic = self.topic_var.get().strip()
        exercise_type = self.exercise_type_var.get().strip()
        num_questions = self.num_questions_var.get().strip()

        # Generate the prompt using the specified format
        prompt = self.create_prompt_template(num_questions, grade, subject, topic, exercise_type)

        # Display the prompt in the output area
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, prompt)

        # Show success message
        messagebox.showinfo("Success", "Prompt generated successfully!")

    def create_prompt_template(self, num_questions, grade, subject, topic, exercise_type):
        """Create the formatted prompt template"""
        prompt = f"""Generate {num_questions} exercises for {grade} grade students in {subject} on the topic "{topic}".
The exercises should be of type {exercise_type}.
Include answers and short explanations.
Format the output in JSON."""

        return prompt

    def copy_to_clipboard(self):
        """Copy the generated prompt to clipboard"""
        prompt_text = self.output_text.get(1.0, tk.END).strip()

        if not prompt_text:
            messagebox.showwarning("Warning", "No prompt to copy. Please generate a prompt first.")
            return

        try:
            pyperclip.copy(prompt_text)
            messagebox.showinfo("Success", "Prompt copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy to clipboard: {str(e)}")


def main():
    """Main function to run the application"""
    # Create main window
    root = tk.Tk()

    # Initialize application
    app = AIPromptGenerator(root)

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
