from PyQt6.QtWidgets import QApplication, QVBoxLayout, QSizePolicy, QTableWidget, QTableWidgetItem, QHBoxLayout, QFileDialog
from PyQt6.QtCore import Qt
from GUI_Base._GUI_COMPONENT_with_themes_ver4 import MainWindow
from GUI_Base._CSS_APPLIER_VER1 import CssManager
from GUI_Base.themes_section.themes import THEMES
from excel_extractors import MiniBackend

import sys
import json

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

        path_load = ["qvboxlayout_main", "qhboxlayout_buttons_set_top", "load_button"]
        path_save = ["qvboxlayout_main", "qhboxlayout_buttons_set_top", "save_button"]

        obj_load = self.window.find_widget(ribbon, path_load)
        obj_save = self.window.find_widget(ribbon, path_save)

        obj_load.clicked.connect(lambda: self.load_template(self.table))
        obj_save.clicked.connect(lambda: self.save_template(self.table))

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
            },
            "GeneratorScreen": {
                "qvboxlayout_main": {
                    "qhboxlayout_buttons_set1": {
                        "year_label": {"widget_type": "label", "text": "Enter the Year: "},
                        "year_input": {"widget_type": "input_box", "text": "Enter Year to generate..."}
                    },
                    "qhboxlayout_buttons_set2": {
                        "name_label": {"widget_type": "label", "text": "Enter the file name: "},
                        "name_input": {"widget_type": "input_box", "text": "Enter name of file (with .xlsx)..."}
                    },
                    "Generator_button": {"widget_type": "button", "text": "Generate",
                                        "callback": lambda: print("Will Generate.")
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
        Fetches all the table's contents and saves them into a JSON file following
        a pandas-style structure: {"columns": [...], "data": [[...], [...], ...]}.
        The user is prompted to choose where to save the file using a file dialog.
        """

        row_count = table.rowCount()
        col_count = table.columnCount()

        # Extract column headers
        columns = [table.horizontalHeaderItem(col).text() if table.horizontalHeaderItem(col) else f"Column{col}"
                for col in range(col_count)]

        # Extract table data
        data = []
        for row in range(row_count):
            row_data = []
            for col in range(col_count):
                item = table.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)

        # Format into dictionary
        table_dict = {
            "columns": columns,
            "data": data
        }

        # Open save file dialog
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setNameFilter("JSON Files (*.json);;All Files (*)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                file_path = selected_files[0]
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(table_dict, f, indent=4, ensure_ascii=False)
    
    def load_template(self, table: QTableWidget):
        """
        Loads a JSON table template file and populates the QTableWidget with its contents.
        Assumes the JSON file follows the pandas-style structure:
        {"columns": [...], "data": [[...], [...], ...]}.
        """

        # Open file dialog to select the JSON file
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        file_dialog.setNameFilter("JSON Files (*.json);;All Files (*)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                file_path = selected_files[0]
                with open(file_path, "r", encoding="utf-8") as f:
                    table_dict = json.load(f)

                columns = table_dict.get("columns", [])
                data = table_dict.get("data", [])

                # Setup table dimensions
                table.setColumnCount(len(columns))
                table.setRowCount(len(data))

                # Set headers
                table.setHorizontalHeaderLabels(columns)

                # Fill table data
                for row_index, row_data in enumerate(data):
                    for col_index, cell_value in enumerate(row_data):
                        table.setItem(row_index, col_index, QTableWidgetItem(cell_value))
    
    def init_excel_construction(self):
        """
        Will take in JSON file, but first it opens the file from the file dialog box.

        Then it will check the formatting to make sure it does not fall into fatal error.

        Then it will generate the excel sheet out of the dataframe retrieved. Here the dataframe
        is just repeated over and over for every day sequencing, divided by month into 12 sheets.

        This button will be in the home screen itself.
        """
        value = 2025
        obj_saver = MiniBackend("Temp_sheet_gen.xlsx", value, "Temp_sheet_gen.xlsx")

    def close_window(self):
        if self.window is not None:
            self.window.close()
    

def main():
    app = QApplication(sys.argv)
    instance = DatewiseSheetGenerator()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()