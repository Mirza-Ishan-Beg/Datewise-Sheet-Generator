from PyQt6.QtWidgets import QApplication, QVBoxLayout, QSizePolicy, QTableWidget, QTableWidgetItem, QHBoxLayout
from PyQt6.QtCore import Qt
from GUI_Base._GUI_COMPONENT_with_themes_ver4 import MainWindow
from GUI_Base._CSS_APPLIER_VER1 import CssManager
from GUI_Base.themes_section.themes import THEMES

import sys

class DatewiseSheetGenerator:
    def __init__(self):
        self.window = MainWindow(200, 200, 400, 300, "Datewise Sheet Generator v1.2.0")
        self.css_mgr = CssManager(THEMES["dark"])
        self.table = None  # Needed for making the table accessable in any method...
        self.home_screen()
    
    def home_screen(self):
        # I will keep this clear widgets function call here because we may not always need to clear 
        # all of the widgets.
        self.window.clear_widgets()

        custom_title_css = {
            "title_main":
                {"": "color: #AAA; font-size: 26px; font-weight: bold"},  # Custom color and bold
        }

        # Define a simple vertical layout with one label and one button
        ribbon = self.screen_selection_region("HomeScreen")
        print(ribbon)
        title_label_path = ["qvboxlayout_main", "title_label"]
        obj_title_label = self.window.find_widget(ribbon, title_label_path)  # Object retrival succeeded.

        # Apply dark theme CSS
        self.css_mgr.apply_css_to_all_widgets(self.window.widgets_container)
        self.css_mgr.apply_css_to_widget(obj_title_label,
                                                "QLabel",
                                                custom_title_css["title_main"])  # CSS adjustments are good!
        obj_title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Alignments works...
        obj_title_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        obj_title_label.setMaximumHeight(100)  # Integer in pixels.

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
        ribbon = self.screen_selection_region("CreationScreen")

        path_table = ["qvboxlayout_main", "table"]
        self.table = self.window.find_widget(ribbon, path_table)

        # Connections are made here because self.table is still empty, which is required by util methods.

        path_add_row = ["qvboxlayout_main", "qhboxlayout_buttons_set_bottom", "add_row_button"]
        path_rem_row = ["qvboxlayout_main", "qhboxlayout_buttons_set_bottom", "rem_row_button"]
        path_add_col = ["qvboxlayout_main", "qhboxlayout_buttons_set_bottom", "add_col_button"]
        path_rem_col = ["qvboxlayout_main", "qhboxlayout_buttons_set_bottom", "rem_col_button"]

        obj_arow = self.window.find_widget(ribbon, path_add_row)
        obj_rrow = self.window.find_widget(ribbon, path_rem_row)
        obj_acol = self.window.find_widget(ribbon, path_add_col)
        obj_rcol = self.window.find_widget(ribbon, path_rem_col)

        obj_arow.clicked.connect(lambda: self.modify_table_add(self.table, is_row=True))
        obj_rrow.clicked.connect(lambda: self.modify_table_delete(self.table, is_row=True))
        obj_acol.clicked.connect(lambda: self.modify_table_add(self.table, is_row=False))
        obj_rcol.clicked.connect(lambda: self.modify_table_delete(self.table, is_row=False))

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
                    "title_label": {"widget_type": "label", "text": "Datewise Sheet Generator"},
                    "template_create_button": {"widget_type": "button", "text": "Template Creation",
                                    "callback": self.creation_screen},
                    "quit_button": {"widget_type": "button", "text": "Quit",
                                    "callback": self.close_window},
                }
            },
            "CreationScreen": {
                "qvboxlayout_main": {
                    "qhboxlayout_buttons_set_top": {
                        "back_button": {"widget_type": "button", "text": "Home",
                                         "callback": self.home_screen},
                        "load_button": {"widget_type": "button", "text": "Load",
                                         "callback": lambda: print("will connect to load a template!")},
                        "save_button": {"widget_type": "button", "text": "Save",
                                         "callback": lambda: print("will connect to save a template!")}
                    },
                    "table": {"widget_type": "table", "rows": 2, "columns": 2,
                               "header": ["A", "B"], "data": [[], []]},
                    "qhboxlayout_buttons_set_bottom": {
                        "add_row_button": {"widget_type": "button", "text": "Add Row",
                                         "callback": lambda: print("Will Add a row.")},
                        "rem_row_button": {"widget_type": "button", "text": "Remove Row",
                                         "callback": lambda: print("Will Delete a row.")},
                        "add_col_button": {"widget_type": "button", "text": "Add Column",
                                         "callback": lambda: print("Will Add a column.")},
                        "rem_col_button": {"widget_type": "button", "text": "Remove Column",
                                         "callback": lambda: print("Will Delete a column.")}
                    }
                }
            }
        }
        ribbon = ribbon_collection[screen_name]
        ribbon = self.window.add_flexible_ribbon(ribbon, self.window.main_layout, self.window.widgets_container)
        print(self.window.main_layout)
        return ribbon
    
    def modify_table_add(self, table: QTableWidget, is_row: bool):
        if is_row:
            row = table.rowCount()
            table.insertRow(row)
            # Optional: populate with default items
            for col in range(table.columnCount()):
                table.setItem(row, col, QTableWidgetItem(f"Row {row}"))
        else:
            col = table.columnCount()
            table.insertColumn(col)
            # Optional: populate existing rows with empty items
            for row in range(table.rowCount()):
                table.setItem(row, col, QTableWidgetItem(f"Col {col}"))

    def modify_table_delete(self, table: QTableWidget, is_row: bool):
        selected_items = table.selectedItems()
        if not selected_items:
            return  # Nothing selected

        target_indexes = set()
        for item in selected_items:
            index = item.row() if is_row else item.column()
            target_indexes.add(index)

        for index in sorted(target_indexes, reverse=True):
            if is_row:
                table.removeRow(index)
            else:
                table.removeColumn(index)
    
    def save_template(self, table: QTableWidget):
        """
        Will fetch all the table's contents and then put them inside the JSON file of a dictionary.
        The dictionary is such that it follows pandas convention of the dataframe structuring.

        This is done in order to make sure the sheet generation is handled with care.
        """
        pass

    def close_window(self):
        if self.window is not None:
            self.window.close()
    

def main():
    app = QApplication(sys.argv)
    instance = DatewiseSheetGenerator()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()