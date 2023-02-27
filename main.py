from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from random import randint


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(240, 570, 91, 23))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "Создать круг"))


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.update)
        self.r = 0
        self.color = QtGui.QColor(0, 0, 0)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setBrush(self.color)
        painter.drawEllipse(300 - (self.r // 2), 300 - (self.r // 2), self.r, self.r)

    def update(self):
        self.r = randint(1, 500)
        self.color = QtGui.QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
