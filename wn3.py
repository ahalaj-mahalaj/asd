from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

from instr import win_x, win_y, win_width, win_height, txt_index, txt_workheart


class Wnd3(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_ui()
        self.connect()
        self.show()

    def init_ui(self):
        v_layout = QVBoxLayout()
        self.setLayout(v_layout)
        index_text = QLabel(txt_index)
        v_layout.addWidget(index_text)
        workheart = QLabel(txt_workheart)
        v_layout.addWidget(workheart)


    def connect(self):
        pass

    def set_appear(self):
        self.setWindowTitle('химия 11 класс арбузов')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)