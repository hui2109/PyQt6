from PySide6.QtWidgets import *
import sys
app = QApplication(sys.argv)
window=QWidget()
window.setWindowTitle(' Hello World! ')
window.resize(600,600)
window.move(200,200)
label=QLabel(window)
label.setText('Hello World')
label.move(300,300)
window.show()
sys.exit(app.exec())


