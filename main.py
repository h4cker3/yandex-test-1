import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QInputDialog

SCREEN_SIZE = [900, 900]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.toponym = ''

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')
        # Получаем карту из метода show_map в файл 'file.png' используя self.toponym

        ## Изображение
        self.pixmap = QPixmap('file.png')
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(250, 250)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

    def run(self):
        toponym, ok_pressed = QInputDialog.getText(self, "Введите топоним",
                                                "Введите название места, которые вы хотите найти")
        if ok_pressed:
            self.toponym = toponym
        else:
            sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
