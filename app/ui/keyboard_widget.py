from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QTabWidget
)


class MathKeyboard(QWidget):

    def __init__(self, input_field):

        super().__init__()

        self.input_field = input_field

        main_layout = QVBoxLayout()

        tabs = QTabWidget()

        tabs.setStyleSheet("""
            QTabBar::tab {
                background: #2b2b2b;
                color: white;
                padding: 12px;
                border-radius: 8px;
                margin: 4px;
                font-size: 14px;
            }

            QTabBar::tab:selected {
                background: #5c5470;
            }
        """)

        # TAB 1
        basic_tab = QWidget()

        basic_layout = QGridLayout()

        basic_buttons = [
            ["x", "y", "π", "e", "√"],
            ["7", "8", "9", "+", "-"],
            ["4", "5", "6", "×", "÷"],
            ["1", "2", "3", "^", "("],
            ["0", ".", ",", ")", "←"],
            ["C"]
        ]

        self.create_buttons(
            basic_buttons,
            basic_layout
        )

        basic_tab.setLayout(basic_layout)

        # TAB 2
        function_tab = QWidget()

        function_layout = QGridLayout()

        function_buttons = [
            ["sin", "cos", "tan", "ln", "log"],
            ["abs", "sinh", "cosh", "tanh", "%"],
            ["<", ">", "<=", ">=", "="],
            ["[", "]", "{", "}", "!"]
        ]

        self.create_buttons(
            function_buttons,
            function_layout
        )

        function_tab.setLayout(function_layout)

        tabs.addTab(basic_tab, "Básico")
        tabs.addTab(function_tab, "Funciones")

        main_layout.addWidget(tabs)

        self.setLayout(main_layout)

    def create_buttons(self, buttons, layout):

        row = 0

        for button_row in buttons:

            col = 0

            for text in button_row:

                button = QPushButton(text)

                button.setMinimumHeight(60)

                # CLEAR
                if text == "C":

                    button.setStyleSheet("""
                        QPushButton {
                            background-color: #5a3d46;
                            color: white;
                            border-radius: 12px;
                            font-size: 18px;
                            font-weight: bold;
                        }
                    """)

                # DELETE
                elif text == "←":

                    button.setStyleSheet("""
                        QPushButton {
                            background-color: #4e445c;
                            color: white;
                            border-radius: 12px;
                            font-size: 18px;
                            font-weight: bold;
                        }
                    """)

                # NORMAL
                else:

                    button.setStyleSheet("""
                        QPushButton {
                            background-color: #2d2d2d;
                            color: white;
                            border-radius: 12px;
                            font-size: 18px;
                        }

                        QPushButton:hover {
                            background-color: #3a3a3a;
                        }
                    """)

                button.clicked.connect(
                    lambda checked, t=text:
                    self.insert_text(t)
                )

                if text == "C":

                    layout.addWidget(
                        button,
                        row,
                        0,
                        1,
                        5
                    )

                else:

                    layout.addWidget(
                        button,
                        row,
                        col
                    )

                col += 1

            row += 1

    def insert_text(self, text):

        if text == "←":

            current = self.input_field.text()

            self.input_field.setText(current[:-1])

        elif text == "C":

            self.input_field.clear()

        elif text == "π":

            self.input_field.insert("pi")

        elif text == "e":

            self.input_field.insert("E")

        elif text == "√":

            self.input_field.insert("sqrt(")

        elif text == "sin":

            self.input_field.insert("sin(")

        elif text == "cos":

            self.input_field.insert("cos(")

        elif text == "tan":

            self.input_field.insert("tan(")

        elif text == "ln":

            self.input_field.insert("log(")

        elif text == "log":

            self.input_field.insert("log10(")

        elif text == "abs":

            self.input_field.insert("Abs(")

        elif text == "sinh":

            self.input_field.insert("sinh(")

        elif text == "cosh":

            self.input_field.insert("cosh(")

        elif text == "tanh":

            self.input_field.insert("tanh(")

        elif text == "×":

            self.input_field.insert("*")

        elif text == "÷":

            self.input_field.insert("/")

        elif text == "!":

            self.input_field.insert("factorial(")

        else:

            self.input_field.insert(text)