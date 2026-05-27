from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QProgressBar
)

from PyQt6.QtCore import Qt


class LoadingDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Procesando")

        self.setFixedSize(350, 180)

        self.setStyleSheet("""
            background-color: #1e1e1e;
            color: white;
        """)

        layout = QVBoxLayout()

        label = QLabel(
            "Analizando función..."
        )

        label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        label.setStyleSheet("""
            font-size: 18px;
        """)

        progress = QProgressBar()

        progress.setRange(0, 0)

        progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #444;
                border-radius: 10px;
                background-color: #2d2d2d;
                height: 25px;
            }

            QProgressBar::chunk {
                background-color: #5c5470;
                border-radius: 10px;
            }
        """)

        layout.addWidget(label)
        layout.addWidget(progress)

        self.setLayout(layout)