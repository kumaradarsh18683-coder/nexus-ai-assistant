import sys
from PySide6.QtWidgets import QApplication
from gui import NexusUI

app = QApplication(sys.argv)

window = NexusUI()
window.show()

sys.exit(app.exec())