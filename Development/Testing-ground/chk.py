from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label1 = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()

        self.label_set = [self.label1, self.label2, self.label3]
        self.label_pointer = 0

        self.input = QLineEdit()
        self.button_pointer_changer = QPushButton("Shift edit section")
        self.button_pointer_changer.clicked.connect(self._on_button_clicked)
        layout = QVBoxLayout()

        self.input.textChanged.connect(self.label_set[self.label_pointer].setText)
        
        layout.addWidget(self.input)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.button_pointer_changer)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)
    
    def _on_button_clicked(self):
        self.input.textChanged.disconnect(self.label_set[self.label_pointer].setText)
        if self.label_pointer < len(self.label_set):
            self.label_pointer += 1
        else:
            self.label_pointer = 0
        self.input.textChanged.connect(self.label_set[self.label_pointer].setText)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
