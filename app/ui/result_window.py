import numpy as np
import sympy as sp

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem
)

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas
)

from matplotlib.figure import Figure


class ResultWindow(QWidget):

    def __init__(self, result, parent=None):

        super().__init__()

        self.parent_window = parent

        self.setWindowTitle("Resultados")

        self.resize(1000, 700)

        self.setStyleSheet("""
            background-color: #1e1e1e;
            color: white;
        """)

        layout = QVBoxLayout()

        # RAÍZ
        root_label = QLabel(
            f"Raíz aproximada: {result['root']}"
        )

        root_label.setStyleSheet("""
            font-size: 20px;
            margin: 10px;
        """)

        layout.addWidget(root_label)

        # FUNCIÓN
        function_canvas = self.create_math_figure(
            result["expression"],
            "Función"
        )

        layout.addWidget(function_canvas)

        # DERIVADA
        derivative_canvas = self.create_math_figure(
            result["derivative"],
            "Derivada"
        )

        layout.addWidget(derivative_canvas)

        # TABLA
        table = QTableWidget()

        iterations = result["iterations"]

        table.setRowCount(len(iterations))

        table.setColumnCount(4)

        table.setHorizontalHeaderLabels([
            "Iteración",
            "x",
            "f(x)",
            "Error"
        ])

        for row, data in enumerate(iterations):

            for col, value in enumerate(data):

                table.setItem(
                    row,
                    col,
                    QTableWidgetItem(str(value))
                )

        layout.addWidget(table)

        # GRÁFICA
        figure = Figure()

        figure.patch.set_facecolor("#1e1e1e")

        canvas = FigureCanvas(figure)

        ax = figure.add_subplot(111)

        ax.set_facecolor("#1e1e1e")

        x = np.linspace(-10, 10, 400)

        y = result["function_numeric"](x)

        ax.plot(x, y)

        ax.axhline(0)

        ax.grid(True)

        layout.addWidget(canvas)

        self.setLayout(layout)

    # ==========================
    # FUNCIÓN MATEMÁTICA LATEX
    # ==========================

    def create_math_figure(self, expression, title):

        figure = Figure(figsize=(6, 1.5))

        figure.patch.set_facecolor("#1e1e1e")

        canvas = FigureCanvas(figure)

        ax = figure.add_subplot(111)

        ax.set_facecolor("#1e1e1e")

        ax.axis('off')

        latex_expr = sp.latex(expression)

        math_text = f"${latex_expr}$"

        ax.text(
            0.5,
            0.5,
            math_text,
            fontsize=22,
            ha='center',
            va='center',
            color='white'
        )

        return canvas

    # ==========================
    # CERRAR
    # ==========================

    def closeEvent(self, event):

        if self.parent_window:

            self.parent_window.show()

        event.accept()