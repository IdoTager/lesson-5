import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSpinBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Toggle")

        container = QWidget(self)
        layout = QVBoxLayout(container)

        self.number = QSpinBox(container)
        self.number.setObjectName("number")
        self.number.setRange(0, 10000)
        layout.addWidget(self.number)

        self.Start_button = QPushButton("start", container)
        self.Start_button.setObjectName("Start_button")
        self.Start_button.setCheckable(True)
        self.Start_button.toggled.connect(self.Start_button_method)
        layout.addWidget(self.Start_button)

        self.setCentralWidget(container)

    def Start_button_method(self, is_started):
        self.Start_button.setText("stop" if is_started else "start")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())