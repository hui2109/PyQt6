from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.pressed_keys = set()
        self.setWindowTitle('多个普通键+1个修饰键')

    def keyPressEvent(self, event):
        # print(Qt.KeyboardModifier.ControlModifier.value)
        if event.key() == Qt.Key.Key_A or event.key() == Qt.Key.Key_B or \
                event.key()==Qt.Key.Key_Control:
            self.pressed_keys.add(event.key())
            # self.pressed_keys.add(event.modifiers())

            print(self.pressed_keys)
        if Qt.Key.Key_A in self.pressed_keys and \
                Qt.Key.Key_B in self.pressed_keys and \
                Qt.Key.Key_Control in self.pressed_keys:
            print('用户按下了Ctrl+A+B')
            self.pressed_keys.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())