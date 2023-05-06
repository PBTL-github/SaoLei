from PyQt5 import QtGui
from PyQt5.QtWidgets import QPushButton
from PyQt5.Qt import pyqtSignal, Qt


class SaoLeiBtn(QPushButton):
    firstClick = False
    rightClicked = pyqtSignal()

    def __init__(self, parent=None):
        super(SaoLeiBtn, self).__init__(parent)
        self.sid = 0
        self.X = 0
        self.Y = 0
        self.indexX = 0
        self.indexY = 0
        self.isOpen = False
        self.isBoom = False
        self.aroundBoomNum = 0

    def add_around_boom_num(self):
        self.aroundBoomNum += 1

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        super().mousePressEvent(e)
        if e.button() == Qt.RightButton:
            self.rightClicked.emit()

