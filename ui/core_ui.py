"""
Core UI Module

Main UI class that manages the window and tab structure.

Author: Toni Kleinfeld
Date: October 2025
"""

import tkinter as tk
from tkinter import ttk
from .prompt_tab import PromptGeneratorTab
from .json_pdf_tab import JsonPdfTab
from config import WINDOW_TITLE, WINDOW_SIZE


class AIPromptGeneratorUI:
    """Core UI class for the AI Prompt Generator application"""

    def __init__(self, root, prompt_generator):
        """
        Initialize the UI with the main window and prompt generator

        Args:
            root: Tkinter root window
            prompt_generator: Instance of PromptGenerator class
        """
        self.root = root
        self.prompt_generator = prompt_generator
        self.notebook = None
        self.prompt_tab_instance = None
        self.json_pdf_tab_instance = None

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

        # Tab 1: JSON Prompt Generator
        prompt_tab_frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(prompt_tab_frame, text="JSON Prompt Generator")
        self.prompt_tab_instance = PromptGeneratorTab(prompt_tab_frame, self.root, self.prompt_generator)

        # Tab 2: JSON Import & PDF Generator
        json_pdf_tab_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(json_pdf_tab_frame, text="JSON → PDF Generator")
        self.json_pdf_tab_instance = JsonPdfTab(json_pdf_tab_frame)
