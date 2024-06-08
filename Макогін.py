from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('конкурс від макара')
question = QLabel('скільки раз макар бомбив белгород?')
btn_answer1 = QRadioButton('12')
btn_answer2 = QRadioButton('37')
btn_answer3 = QRadioButton('987898')
btn_answer4 = QRadioButton('9999999999 в секунду')
layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment=Qt.AlignCenter)
layout_main.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layout_main.addWidget(btn_answer2, alignment=Qt.AlignCenter)
layout_main.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layout_main.addWidget(btn_answer4, alignment=Qt.AlignCenter)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('правильно! ви виграли  і ви получаєте барабанний дріт двері які видуть до макара')
    victory_win.exec_()

def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('не правильно! ви виграли  і ви не получаєте барабанний дріт двері які видуть до макара')
    victory_win.exec_()

btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_win)

main_win.setLayout(layout_main)
main_win.show()

app.exec_()
