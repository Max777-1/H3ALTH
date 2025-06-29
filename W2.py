from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QLineEdit
from Variables import *
from w3 import *
#Classes
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(W1_window_name)
        self.resize(win_height, win_width)
        self.move(win_move_x, win_move_y)
    def initUI(self):
        #Layouts
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.insert_name = QLabel(W2_name)
        self.name_edit = QLineEdit(W2_namebox)
        self.age = QLabel(W2_age)
        self.insert_age = QLineEdit(W2_default)
        self.instruction1 = QLabel(W2_instruction1)
        self.test1_btn = QPushButton(W2_button1_text)
        self.insert_test1 = QLineEdit(W2_default)
        self.instruction2 = QLabel(W2_instruction2)
        self.test2_btn = QPushButton(W2_button2_text)
        self.instruction3 = QLabel(W2_instruction3)
        self.test3_btn = QPushButton(W2_button3_text)
        self.insert_test3 = QLineEdit(W2_default)
        self.button_next = QPushButton("Finish test")
        #Widgets
        self.l_line.addWidget(self.insert_name)
        #self.r_line.addWidget(self.timer)
        self.l_line.addWidget(self.name_edit)
        self.l_line.addWidget(self.age)
        self.l_line.addWidget(self.insert_age)
        self.l_line.addWidget(self.instruction1)
        self.l_line.addWidget(self.test1_btn)
        self.l_line.addWidget(self.insert_test1)
        self.l_line.addWidget(self.instruction2)
        self.l_line.addWidget(self.test2_btn)
        self.l_line.addWidget(self.instruction3)
        self.l_line.addWidget(self.test3_btn)
        self.l_line.addWidget(self.insert_test3)
        self.l_line.addWidget(self.button_next)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.time = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def connects(self):
        self.test1_btn.clicked.connect(self.timer_test)
        self.test2_btn.clicked.connect(self.timer_test)
        self.test3_btn.clicked.connect(self.timer_test)
        self.button_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = FinalWin()

#app = QApplication([])
#mw = W2()
##app.exec_()