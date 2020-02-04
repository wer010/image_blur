from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider,QGroupBox,QPushButton, QFileDialog, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QLabel
from PyQt5.QtGui import QPixmap


class mywindow(QWidget):
    def __init__(self):
        super().__init__()
    #     self.setupui()
    #
    # def setupui(self):
        total_area = QHBoxLayout()
        self.setLayout(total_area)
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('图像处理')

        a_area = QGroupBox()
        # a_area.setStyleSheet("border: 2px solid red")
        a_arealayout = QVBoxLayout()
        a_area.setLayout(a_arealayout)

        b_area = QGroupBox()
        b_arealayout = QVBoxLayout()
        b_area.setLayout(b_arealayout)
        bt_arealayout = QHBoxLayout()

        self.bb_area = QLabel()
        self.bb_area.setText('Picture')
        self.bb_area.setStyleSheet("border: 2px solid gray")



        a1 = QPushButton()
        a1.setText("打开")
        a1.clicked.connect(self.loadFile)
        a2 = QPushButton()
        a2.setText("保存")
        a3 = QPushButton()
        a3.setText("退出")
        b1 = QLabel()
        b1.setText("模糊系数")
        b2 = QSlider(Qt.Horizontal)


        a_arealayout.addWidget(a1)
        a_arealayout.addWidget(a2)
        a_arealayout.addWidget(a3)
        bt_arealayout.addWidget(b1)
        bt_arealayout.addWidget(b2)

        b_arealayout.addLayout(bt_arealayout)
        b_arealayout.addWidget(self.bb_area)

        total_area.addWidget(a_area)
        total_area.addWidget(b_area)
        total_area.setStretchFactor(a_area, 3)
        total_area.setStretchFactor(b_area, 7)



    def loadFile(self):
        file_name,_ = QFileDialog.getOpenFileName(self,'打开文件',"D:\\","Image files(*.jpg *.gif)")
        size = self.bb_area.size()
        self.bb_area.setPixmap(QPixmap(file_name).scaled(size, Qt.KeepAspectRatio, Qt.FastTransformation))
        # self.bb_area.setText('Picture Opened')