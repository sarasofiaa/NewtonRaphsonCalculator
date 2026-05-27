from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from ui.keyboard_widget import MathKeyboard

from core.parser import FunctionParser
from core.validator import FunctionValidator
from core.newton_method import NewtonRaphsonMethod

from ui.result_window import ResultWindow


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Newton Raphson"
        )

        self.resize(700, 850)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
            }
        """)

        layout = QVBoxLayout()

        # TÍTULO
        title = QLabel(
            "NEWTON RAPHSON"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setFont(
            QFont(
                "Arial",
                24,
                QFont.Weight.Bold
            )
        )

        layout.addWidget(title)

        # INPUT FUNCIÓN
        self.input_field = QLineEdit()

        self.input_field.setPlaceholderText(
            "Ingrese la función..."
        )

        self.input_field.setMinimumHeight(70)

        self.input_field.setStyleSheet("""
            QLineEdit {
                background-color: #2b2b2b;
                border-radius: 15px;
                padding: 15px;
                font-size: 22px;
            }
        """)

        layout.addWidget(self.input_field)

        # X0
        self.x0_input = QLineEdit()

        self.x0_input.setPlaceholderText(
            "Valor inicial x0"
        )

        self.x0_input.setText("1")

        self.x0_input.setMinimumHeight(70)

        self.x0_input.setStyleSheet("""
            QLineEdit {
                background-color: #2b2b2b;
                border-radius: 15px;
                padding: 15px;
                font-size: 22px;
                color: white;
            }
        """)

        layout.addWidget(self.x0_input)

        # TOLERANCIA
        self.tolerance_input = QLineEdit()

        self.tolerance_input.setPlaceholderText(
            "Tolerancia"
        )

        self.tolerance_input.setText("0.0001")

        self.tolerance_input.setMinimumHeight(70)

        self.tolerance_input.setStyleSheet("""
            QLineEdit {
                background-color: #2b2b2b;
                border-radius: 15px;
                padding: 15px;
                font-size: 22px;
                color: white;
            }
        """)

        layout.addWidget(self.tolerance_input)

        # TECLADO
        keyboard = MathKeyboard(
            self.input_field
        )

        layout.addWidget(keyboard)

        # BOTÓN
        start_button = QPushButton(
            "INICIAR MÉTODO"
        )

        start_button.setMinimumHeight(70)

        start_button.setStyleSheet("""
            QPushButton {
                background-color: #5c5470;
                border-radius: 15px;
                font-size: 20px;
                font-weight: bold;
            }
        """)

        start_button.clicked.connect(
            self.start_process
        )

        layout.addWidget(start_button)

        self.setLayout(layout)

    def start_process(self):

        try:

            expression_text = (
                self.input_field.text()
            )

            x0 = float(
                self.x0_input.text()
            )

            tolerance = float(
                self.tolerance_input.text()
            )

            parsed_expression = (
                FunctionParser.parse_expression(
                    expression_text
                )
            )

            FunctionValidator.validate(
                parsed_expression
            )

            result = (
                NewtonRaphsonMethod.solve(
                    parsed_expression,
                    x0,
                    tolerance
                )
            )

            self.result_window = (
                ResultWindow(
                    result,
                    self
                )
            )

            self.hide()
            self.result_window.show()

        except Exception as error:

            QMessageBox.critical(
                self,
                "Error",
                str(error)
            )