from PyQt5.QtCore import Qt,QRect,pyqtSignal,QCoreApplication
from PyQt5.QtWidgets import QLineEdit,QSlider,QGroupBox,QPushButton, QFileDialog, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QLabel
from PyQt5.QtGui import QDoubleValidator,QImage, QPixmap, QPainter, QPen

class MyLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False
    pressed = pyqtSignal(int,int)
    released = pyqtSignal(int,int)
    #鼠标点击事件
    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()
        self.pressed.emit(event.x(),event.y())

    #鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False
        self.released.emit(event.x(),event.y())

    #鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()
    #绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
        painter.drawRect(rect)




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

        self.bb_area = MyLabel()
        self.bb_area.setText('Picture')
        self.bb_area.setStyleSheet("border: 2px solid gray")
        self.bb_area.setAlignment(Qt.AlignTop)
        self.bb_area.pressed.connect(self.mousedown)
        self.bb_area.released.connect(self.mouseup)

        a1 = QPushButton()
        a1.setText("打开")
        a1.clicked.connect(self.loadFile)
        a2 = QPushButton()
        a2.setText("保存")
        a3 = QPushButton()
        a3.setText("退出")
        a3.clicked.connect(QCoreApplication.quit)
        b1 = QLabel()
        b1.setText("模糊系数")
        b2 = QSlider(Qt.Horizontal)
        b2.setMinimum(0)
        b2.setMaximum(100)
        b2.setValue(50)

        b3 = QLineEdit()
        b3.setValidator(QDoubleValidator())
        b3.setText("25")

        b4 = QPushButton()
        b4.setText("确定")

        self.b5 = QLabel()



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
        bt_arealayout.setStretchFactor(b4,1)
        bt_arealayout.addWidget(self.b5)
        bt_arealayout.setStretchFactor(self.b5, 4)


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
        s = self.bb_area.size()
        self.image = QPixmap(file_name)
        os = self.image.size()
        ri = self.image.scaled(s, Qt.KeepAspectRatio, Qt.FastTransformation)
        rs = ri.size()
        self.r = max(rs.width()/os.width(), rs.height()/os.height())
        self.bb_area.setPixmap(ri)

    def mousedown(self,x,y):
        self.x0 = round(x/self.r)
        self.y0 = round(y/self.r)

    def mouseup(self,x,y):
        self.x1 = round(x/self.r)
        self.y1 = round(y/self.r)
        # self.b4.setText('x0:{},y0:{},x1:{},y1:{}'.format(self.x0, self.y0, self.x1, self.y1))
        self.roi = self.image.copy(self.x0,self.y0,self.x1-self.x0,self.y1-self.y0)
        self.b5.setPixmap(self.roi.scaled(self.b5.size(),Qt.KeepAspectRatio, Qt.FastTransformation))
