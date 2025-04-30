from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget,
    QTableWidgetItem, QHBoxLayout
)
import sys

class TableEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add/Delete Rows Example")

        # Layouts
        self.layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Example: 2 columns
        self.table.setHorizontalHeaderLabels(["Name", "Age", "val1", "val2"])

        # Buttons
        self.add_button = QPushButton("Add Row")
        self.delete_button = QPushButton("Delete Row")

        # Connect buttons
        self.add_button.clicked.connect(self.add_row)
        self.delete_button.clicked.connect(self.delete_row)

        # Assemble layouts
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.delete_button)

        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

    def add_row(self):
        row_position = self.table.rowCount()
        col_posi = self.table.columnCount()
        self.table.insertRow(row_position)
        for i in range(col_posi):
            self.table.setItem(row_position, i, QTableWidgetItem(""))

    def delete_row(self):
        selected_rows = set()
        for item in self.table.selectedItems():
            selected_rows.add(item.row())
        
        for row in sorted(selected_rows, reverse=True):
            self.table.removeRow(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableEditor()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())
