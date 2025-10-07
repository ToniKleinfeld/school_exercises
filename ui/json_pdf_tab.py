"""
JSON to PDF Generator Tab

Tab component for importing JSON and generating PDF files.

Author: Toni Kleinfeld
Date: October 2025
"""

from json_import_ui import JSONImportUI


class JsonPdfTab:
    """JSON import and PDF generation tab"""

    def __init__(self, parent_frame):
        """
        Initialize the JSON to PDF tab

        Args:
            parent_frame: Parent tkinter frame
        """
        self.parent = parent_frame
        self.json_import_ui = None
        self.create_ui()

    def create_ui(self):
        """Create the tab UI"""
        self.json_import_ui = JSONImportUI(self.parent)
