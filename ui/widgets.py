"""
Custom UI Widgets

Reusable custom widgets for the AI Prompt Generator application.

Author: Toni Kleinfeld
Date: October 2025
"""

import tkinter as tk


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
