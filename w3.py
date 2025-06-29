#Connecting modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton
from Variables import *


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        '''
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
        self.exp = exp
        '''
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(W3_window_name)
        self.resize(win_width, win_height)
        self.move(win_move_x, win_move_y)

    def initUI(self):
        self.v_line = QHBoxLayout()
        self.index = QLabel(W3_Rindex_text)
        self.performance = QLabel(W3_CPerf_text)
        self.v_line.addWidget(self.index)
        self.v_line.addWidget(self.performance)
        self.setLayout(self.v_line)

'''
    def results():
        self.index = (4*(int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200)/10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >=11:
                return txt_res2
'''