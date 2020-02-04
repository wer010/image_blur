import sys
import cv2
import MyWindow
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)

    window = MyWindow.mywindow()
    window.show()

    sys.exit(app.exec())



if __name__ == '__main__':
    main()




