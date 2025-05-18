# themes.py

"""
THEMES MADE SO FAR:
    1.  THEMES
        1.1.  LIGHT
            1.1.1.  MAIN WINDOW
            1.1.2.  BUTTON
            1.1.3.  TABLE
            1.1.4.  LABEL
        1.2.  DARK
            1.2.1.  MAIN WINDOW
            1.2.2.  BUTTON
            1.2.3.  TABLE
            1.2.4.  LABEL
"""

# themes.py

THEMES = {
    "light": {
        "QMainWindow": {
            "": "background-color: #ffffff;"
        },
        "QPushButton": {
            "": """
                background-color: #f0f0f0;
                color: #000000;
                border: 1px solid #cccccc;
                padding: 8px;
                border-radius: 4px;
            """,
            ":hover": "background-color: #e0e0e0;"
        },
        "QTableWidget": {
            "": """
                background-color: white;
                gridline-color: #ddd;
            """,
            "::item:hover": "background-color: #e0e0e0;",
            "QHeaderView::section": "background-color: #f0f0f0;"
        },
        "QLabel": {
            "": """
                color: #000000;
                font-size: 14px;
            """
        }
    },
    "dark": {
        "QMainWindow": {
            "": "background-color: #2d2d2d;"
        },
        "QWidget#qvboxlayout_central_widget": {
            "": "background-color: #232323;"
        },
        "QPushButton": {
            "": """
                background-color: #444444;
                color: #ffffff;
                border: 1px solid #666666;
                padding: 8px;
                border-radius: 4px;
            """,
            ":hover": "background-color: #555555;"
        },
        "QTableWidget": {
            "": """
                background-color: #2b2b2b;
                gridline-color: #444;
                alternate-background-color: #323232;
                border: 1px solid #555;
                font-family: "Segoe UI", "Arial", sans-serif;
                font-size: 13px;
                color: #ddd;
                selection-background-color: #555;
                selection-color: white;
            """,
            "::item": """
                padding: 6px;
                border: 1px solid #444;
            """,
            "::item:hover": "background-color: #404040;",
            "::item:selected": """
                background-color: #666;
                color: white;
                border: 1px solid #777;
            """,
            "::viewport": "background-color: #222;"
        },
        "QHeaderView": {
            "": """
                background-color: #1e1e1e;
                color: #ddd;
                border: none;
            """
        },
        "QHeaderView::section": {
            "": """
                background-color: #333;
                color: #ddd;
                padding: 5px;
                border: 1px solid #444;
                font-weight: bold;
            """,
            ":hover": "background-color: #444;",
            ":pressed": "background-color: #555;"
        },
        "QTableCornerButton::section": {
            "": """
                background-color: #333;
                border: 1px solid #444;
            """
        },
        "QScrollBar:vertical": {
            "": """
                background: #222;
                width: 10px;
                border-radius: 5px;
            """,
            "::handle": """
                background: #444;
                border-radius: 5px;
            """,
            "::handle:hover": "background: #555;",
            "::sub-line, ::add-line": "background: none; border: none;",
            "::sub-page, ::add-page": "background: none;"
        },
        "QScrollBar:horizontal": {
            "": """
                background: #222;
                height: 10px;
                border-radius: 5px;
            """,
            "::handle": """
                background: #444;
                border-radius: 5px;
            """,
            "::handle:hover": "background: #555;",
            "::sub-line, ::add-line": "background: none; border: none;",
            "::sub-page, ::add-page": "background: none;"
        },
        "QLabel": {
            "": """
                color: #ffffff;
                font-size: 14px;
            """
        },
        "QMessageBox": {
            "": """
                background-color: #2E2E2E;
                color: #FFFFFF;
                border: 1px solid #555;
            """,
            },
            "QMessageBox QLabel": {
                "": "color: #FFFFFF;",
            },
            "QMessageBox QPushButton": {
                "": """
                    background-color: #444;
                    color: #FFFFFF;
                    border: 1px solid #555;
                    padding: 5px;
                    border-radius: 4px;
                """,
                ":hover": "background-color: #555;",
            },

    }
}