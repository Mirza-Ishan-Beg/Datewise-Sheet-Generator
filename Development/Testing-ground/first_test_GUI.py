from PyQt6.QtWidgets import QApplication
from GUI_Base._GUI_COMPONENT_with_themes_ver4 import MainWindow
from GUI_Base._CSS_APPLIER_VER1 import CssManager
from GUI_Base.themes_section.themes import THEMES

import sys

class DatewiseSheetGenerator:
    def __init__(self):
        self.window = MainWindow(200, 200, 400, 300, "Testing PYQT6")
        self.css_mgr = CssManager(THEMES["dark"])
        self.test_screen()

    def test_screen(self):
        self.window.clear_widgets()

        # Define a simple vertical layout with one label and one button
        ribbon = {
            "qvboxlayout_main": {
                "greeting_label": {"widget_type": "label", "text": "Welcome!"},
                "action_button": {"widget_type": "button", "text": "Click Me",
                                "callback": lambda: print("Hello world")}
            }
        }
        self.window.add_flexible_ribbon(ribbon, self.window.main_layout, self.window.widgets_container)

        # Apply dark theme CSS
        self.css_mgr.apply_css_to_all_widgets(self.window.widgets_container)
        self.window.apply_stylesheet_to_all_layout(THEMES["dark"])

        self.window.show()
    

def main():
    app = QApplication(sys.argv)
    instance = DatewiseSheetGenerator()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()