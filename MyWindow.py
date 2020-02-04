from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit,QSlider,QGroupBox,QPushButton, QFileDialog, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QLabel
from PyQt5.QtGui import QPixmap,QIntValidator


class mywindow(QWidget):
    def __init__(self):
        super().__init__()
    #     self.setupui()
    #
    # def setupui(self):
        total_arealayout = QHBoxLayout()
        self.setLayout(total_arealayout)
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle('图像处理')

        a_area = QGroupBox()
        # a_area.setStyleSheet("border: 2px solid red")
        a_arealayout = QVBoxLayout()
        a_area.setLayout(a_arealayout)

        b_area = QGroupBox()
        b_arealayout = QVBoxLayout()
        b_area.setLayout(b_arealayout)
        bt_area = QWidget()
        bt_arealayout = QHBoxLayout()
        bt_area.setLayout(bt_arealayout)

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
        b2.setMinimum(0)
        b2.setMaximum(100)
        b2.setValue(50)

        b3 = QLineEdit()
        b3.setValidator(QIntValidator())
        b3.setText("25")

        b4 = QLabel()



        a_arealayout.addWidget(a1)
        a_arealayout.addWidget(a2)
        a_arealayout.addWidget(a3)
        bt_arealayout.addWidget(b1)
        bt_arealayout.setStretchFactor(b1,1)
        bt_arealayout.addWidget(b2)
        bt_arealayout.setStretchFactor(b2,1)
        bt_arealayout.addWidget(b3)
        bt_arealayout.setStretchFactor(b3,1)
        bt_arealayout.addWidget(b4)
        bt_arealayout.setStretchFactor(b4,4)


        b_arealayout.addWidget(bt_area)
        b_arealayout.addWidget(self.bb_area)
        b_arealayout.setStretchFactor(bt_area,3)
        b_arealayout.setStretchFactor(self.bb_area, 7)

        total_arealayout.addWidget(a_area)
        total_arealayout.addWidget(b_area)
        total_arealayout.setStretchFactor(a_area, 2)
        total_arealayout.setStretchFactor(b_area, 8)



    def loadFile(self):
        file_name,_ = QFileDialog.getOpenFileName(self,'打开文件',"D:\\","Image files(*.jpg *.gif)")
        size = self.bb_area.size()
        self.bb_area.setPixmap(QPixmap(file_name).scaled(size, Qt.KeepAspectRatio, Qt.FastTransformation))
        # self.bb_area.setText('Picture Opened')