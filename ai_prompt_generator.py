"""
Main module for AI Prompt Generator

This module contains the main application logic and coordinates between
the UI and prompt creation components.

Author: AI Assistant
Date: October 2025
"""

import tkinter as tk
from ui import AIPromptGeneratorUI
from create_prompt import PromptGenerator


class AIPromptGeneratorApp:
    """Main application class that coordinates UI and prompt generation"""

    def __init__(self):
        """Initialize the application"""
        self.root = tk.Tk()
        self.prompt_generator = PromptGenerator()
        self.ui = AIPromptGeneratorUI(self.root, self.prompt_generator)

    def run(self):
        """Start the application"""
        self.root.mainloop()


def main():
    """Main function to run the application"""
    app = AIPromptGeneratorApp()
    app.run()


if __name__ == "__main__":
    main()
