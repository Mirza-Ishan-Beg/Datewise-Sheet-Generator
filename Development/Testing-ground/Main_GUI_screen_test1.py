from PyQt6.QtWidgets import QApplication
from GUI_Base._GUI_COMPONENT_with_themes_ver4 import MainWindow
from GUI_Base._CSS_APPLIER_VER1 import CssManager
from GUI_Base.themes_section.themes import THEMES

import sys

class DatewiseSheetGenerator:
    def __init__(self):
        self.window = MainWindow(200, 200, 400, 300, "Testing PYQT6")
        self.css_mgr = CssManager(THEMES["dark"])
        self.home_screen()
    
    def home_screen(self):
        # I will keep this clear widgets function call here because we may not always need to clear 
        # all of the widgets.
        self.window.clear_widgets()

        # Define a simple vertical layout with one label and one button
        ribbon = self.screen_selection_region("HomeScreen")

        # Apply dark theme CSS
        self.css_mgr.apply_css_to_all_widgets(self.window.widgets_container)
        self.window.apply_stylesheet_to_all_layout(THEMES["dark"])

        self.window.show()

    def settings_screen(self):
        pass

    def creation_screen(self):
        """
        Both the Update and Creation will be handled here, I will save the stuff in .JSON format and therefore
        there will be no issues.

        I will fetch the saved templates contents and put them right back here.

        Prompt a alert if the current file is:
            No exact match of the content in the already saved JSONs.
            (I do not know if this is efficient... but we will see about efficiency once this is completed.)
        
        Therefore, a button for going back, load button, save button and a table.
        Below the table we will have options to add and remove new rows and columns, hence four buttons there.
        """
        self.window.clear_widgets()
        self.screen_selection_region("CreationScreen")

        # Apply dark theme CSS
        self.css_mgr.apply_css_to_all_widgets(self.window.widgets_container)
        self.window.apply_stylesheet_to_all_layout(THEMES["dark"])

        self.window.show()

    def instructions_screen(self):
        pass
    
    # --------------------------------------------------------------------- #
    # -------------------       UTILITY SECTION         ------------------- #
    # --------------------------------------------------------------------- #

    def screen_selection_region(self, screen_name: dict):
        """
        Will consist of collection of ribbons and regex selections of each ribbon to initiate any screen
        The screens will be still the same, and widget will still be given back, yet to keep
        everything together this function will make sure the widget creation is taken care of.

        It takes only one param, that is a key for the nested dictionary which contains all all those
        ribbons as their value.

        Returns the choosen ribbon to smooth out the operations to be contains at a specific region.
        """
        ribbon_collection = {
            "HomeScreen": {
                "qvboxlayout_main": {
                    "greeting_label": {"widget_type": "label", "text": "Welcome!"},
                    "action_button": {"widget_type": "button", "text": "Click Me",
                                    "callback": lambda: print("Hello world")},
                    "template_create_button": {"widget_type": "button", "text": "Template Creation",
                                    "callback": self.creation_screen}
                }
            },
            "CreationScreen": {
                "qvboxlayout_main": {
                    "qhboxlayout_buttons_set_top": {
                        "back_button": {"widget_type": "button", "text": "Home",
                                         "callback": lambda: print("will connect to home!")},
                        "load_button": {"widget_type": "button", "text": "Home",
                                         "callback": lambda: print("will connect to load a template!")},
                        "save_button": {"widget_type": "button", "text": "Home",
                                         "callback": lambda: print("will connect to save a template!")}
                    },
                    "table": {"widget_type": "table", "rows": 2, "columns": 2,
                               "header": ["A", "B"], "data": [[], []]},
                    "qhboxlayout_buttons_set_bottom": {
                        "add_row_button": {"widget_type": "button", "text": "Add Row",
                                         "callback": lambda: print("will Add a row!")},
                        "rem_row_button": {"widget_type": "button", "text": "Remove Row",
                                         "callback": lambda: print("will Remove a row!")},
                        "add_col_button": {"widget_type": "button", "text": "Add Column",
                                         "callback": lambda: print("will Add a Column!")},
                        "rem_col_button": {"widget_type": "button", "text": "Remove Column",
                                         "callback": lambda: print("will Remove a Column!")}
                    }
                }
            }
        }
        ribbon = ribbon_collection[screen_name]
        self.window.add_flexible_ribbon(ribbon, self.window.main_layout, self.window.widgets_container)
        return ribbon
    

def main():
    app = QApplication(sys.argv)
    instance = DatewiseSheetGenerator()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()