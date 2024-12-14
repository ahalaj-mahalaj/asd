from pickle import GLOBAL

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit
from PyQt6.QtCore import Qt, QTimer, QTime
from instr import win_width, win_height, win_x, win_y, txt_hintname, txt_age, txt_test2, txt_test1, txt_test3
from wn3 import Wnd3

class Wnd2(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_ui()
        self.connect()
        self.show()

    def init_ui(self):
        h_layout = QHBoxLayout()
        self.setLayout(h_layout)
        v_layout1 = QVBoxLayout()
        v_layout2 = QVBoxLayout()
        h_layout.addLayout(v_layout1)
        h_layout.addLayout(v_layout2)

        fio = QLabel(txt_hintname)
        v_layout1.addWidget(fio)
        fio_box = QLineEdit()
        fio_box.setPlaceholderText('ну тут короче са')
        v_layout1.addWidget(fio_box, alignment=Qt.AlignmentFlag.AlignLeft)

        current_age = QLabel(txt_age)
        v_layout1.addWidget(current_age, alignment=Qt.AlignmentFlag.AlignLeft)

        self.age_box = QLineEdit()
        self.age_box.setPlaceholderText('если что, писать нуж')
        v_layout1.addWidget(self.age_box, alignment=Qt.AlignmentFlag.AlignLeft)
        spina1 = QLabel(txt_test1)
        v_layout1.addWidget(spina1, alignment=Qt.AlignmentFlag.AlignLeft)
        test1_button = QPushButton('начать первый тест')
        v_layout1.addWidget(test1_button, alignment=Qt.AlignmentFlag.AlignLeft)
        test1_button.clicked.connect(self.timer_test1)

        self.test1_res = QLineEdit()
        v_layout1.addWidget(self.test1_res, alignment=Qt.AlignmentFlag.AlignLeft)
        self.test1_res.setPlaceholderText('а тут результаты')

        squats_expl = QLabel(txt_test2)
        v_layout1.addWidget(squats_expl, alignment=Qt.AlignmentFlag.AlignLeft)
        squats_button = QPushButton('щас комп взорвётся')
        squats_button.clicked.connect(self.timer_test2)

        v_layout1.addWidget(squats_button, alignment=Qt.AlignmentFlag.AlignLeft)

        spina2 = QLabel(txt_test3)
        v_layout1.addWidget(spina2, alignment=Qt.AlignmentFlag.AlignLeft)

        final_tst_button = QPushButton('последний тест')
        v_layout1.addWidget(final_tst_button, alignment=Qt.AlignmentFlag.AlignLeft)
        final_tst_button.clicked.connect(self.timer_test3)

        self.fin_line1 = QLineEdit()
        self.fin_line1.setPlaceholderText('а тут тест2')
        v_layout1.addWidget(self.fin_line1, alignment=Qt.AlignmentFlag.AlignLeft)

        self.fin_line2 = QLineEdit()
        v_layout1.addWidget(self.fin_line2, alignment=Qt.AlignmentFlag.AlignLeft)
        self.fin_line2.setPlaceholderText('а тут тест 3')

        self.send_res = QPushButton('ну давай, отправь результаты')
        v_layout1.addWidget(self.send_res, alignment=Qt.AlignmentFlag.AlignCenter)

        self.universnal_timer = QLabel('а тут время покажет')
        v_layout2.addWidget(self.universnal_timer, alignment=Qt.AlignmentFlag.AlignCenter)
        self.universnal_timer.setStyleSheet('font-size:99px')

    def connect(self):
        self.send_res.clicked.connect(self.hide_show)

    def set_appear(self):
        self.setWindowTitle('химия 10 класс арбузов')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def hide_show(self):
        count = 0
        try:
            age = int(self.age_box.text())
            count +=1
        except ValueError:
            self.age_box.setText('дятел, тут цифры')
        try:
            res1 = int(self.test1_res.text())
            count += 1
        except ValueError:
            self.test1_res.setText('тут тоже цифры')
        try:
            fin1 = int(self.fin_line1.text())
            count +=1
        except ValueError:
            self.fin_line1.setText('тут тоже')
        try:
            fin2 = int(self.fin_line2.text())
            count +=1
        except ValueError:
            self.fin_line2.setText('и тут')
        if count == 4:
            self.win_3 = Wnd3()
            self.hide()

    def timer_test1(self):
        global time
        time = QTime(0,0,3)
        self.timer = QTimer()
        self.timer.timeout.connect(self.second_passed)
        self.timer.start(1000)

    def timer_test2(self):
        global time
        time = QTime(0,0,46)
        self.timer = QTimer()
        self.timer.timeout.connect(self.second_passed)
        self.timer.start(1000)

    def timer_test3(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.second_passed_test2)
        self.timer.start(1000)

    def second_passed_test2(self):
        global time
        time = time.addSecs(-1)
        self.universnal_timer.setText(time.toString('hh:mm:ss'))
        if int(time.toString('ss')) == 0:
            self.timer.stop()
            self.universnal_timer.setText('ну всё')
        if int(time.toString('ss')) > 45:
            self.universnal_timer.setStyleSheet('color:Olive;font-size:99px')
        elif int(time.toString('ss')) > 15:
            self.universnal_timer.setStyleSheet('color:Black;font-size:99px')
        elif int(time.toString('ss')) < 15:
            self.universnal_timer.setStyleSheet('color:Olive;font-size:99px')

    def second_passed(self):
        global time
        time = time.addSecs(-1)
        self.universnal_timer.setText(time.toString('hh:mm:ss'))
        if int(time.toString('ss')) == 0:
            self.timer.stop()
            self.universnal_timer.setText('ну всё')