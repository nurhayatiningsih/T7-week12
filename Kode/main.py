# Nama  : Nurhayati Ningsih
# NIM   : F1D02410085
# Kelas : C

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor
from dashboard import DashboardWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    p = QPalette()
    p.setColor(QPalette.Window, QColor(245, 246, 250))
    p.setColor(QPalette.WindowText, QColor(51, 51, 51))
    p.setColor(QPalette.Base, QColor(255, 255, 255))
    p.setColor(QPalette.AlternateBase, QColor(245, 247, 250))
    p.setColor(QPalette.Highlight, QColor(46, 134, 171))
    p.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
    app.setPalette(p)

    window = DashboardWindow()
    window.show()
    sys.exit(app.exec())