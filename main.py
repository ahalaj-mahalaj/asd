from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from instr import win_width, win_height, win_x, win_y, txt_hello, txt_instruction, txt_next
from wn2 import Wnd2

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_ui()
        self.connect()
        self.show()
    def init_ui(self):
        v_layout1 = QVBoxLayout()
        v_layout1.setSpacing(100)
        self.setLayout(v_layout1)
        haelo_text = QLabel(txt_hello)
        explain_txt = QLabel(txt_instruction)
        self.button_next1 = QPushButton(txt_next)
        v_layout1.addWidget(haelo_text)
        v_layout1.addWidget(explain_txt)
        v_layout1.addWidget(self.button_next1, alignment=Qt.AlignmentFlag.AlignHCenter)
    def connect(self):
        self.button_next1.clicked.connect(self.hide_show)

    def set_appear(self):
        self.setWindowTitle('химия 9 класс арбузов')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def hide_show(self):
        self.win_2 = Wnd2()
        self.hide()
app = QApplication([])
wnd = Window()





app.exec()