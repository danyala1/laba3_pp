import first_script
import second_script
import third_script
import iterator

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import sys


def click_button_first_star():
    iterator(1)


def click_button_second_star():
    iterator(2)


def click_button_third_star():
    iterator(3)


def click_button_fourth_star():
    iterator(4)


def click_button_fifth_star():
    iterator(5)


def application():
    dirs = [[iterator(1)], [], [], [], []]
    print(dirs)
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Простая программа")
    window.setGeometry(800, 600, 800, 600)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Это надпись directory")
    main_text.move(0, 0)
    main_text.adjustSize()

    title_opinion = QtWidgets.QLabel(window)
    title_opinion.setText("Заголовок:")
    title_opinion.move(0, 200)
    title_opinion.adjustSize()

    plus_opinion = QtWidgets.QLabel(window)
    plus_opinion.setText("Достоинства:")
    plus_opinion.move(0, 300)
    plus_opinion.adjustSize()

    minus_opinion = QtWidgets.QLabel(window)
    minus_opinion.setText("Недостатки:")
    minus_opinion.move(0, 400)
    minus_opinion.adjustSize()

    text_opinion = QtWidgets.QLabel(window)
    text_opinion.setText("Отзыв:")
    text_opinion.move(0, 500)
    text_opinion.adjustSize()

    button_create_dataset = QtWidgets.QPushButton(window)
    button_create_dataset.move(0, 30)
    button_create_dataset.setText("Создать dataset")
    button_create_dataset.setFixedWidth(200)
    button_create_dataset.clicked.connect(first_script.first_script)

    button_recreate_dataset = QtWidgets.QPushButton(window)
    button_recreate_dataset.move(0, 90)
    button_recreate_dataset.setText("Перекопировать dataset")
    button_recreate_dataset.setFixedWidth(200)
    button_recreate_dataset.clicked.connect(second_script.second_script)

    button_copy_random_dataset = QtWidgets.QPushButton(window)
    button_copy_random_dataset.move(0, 150)
    button_copy_random_dataset.setText("Рандомный элемент dataset")
    button_copy_random_dataset.setFixedWidth(200)
    button_copy_random_dataset.clicked.connect(third_script.third_script)

    button_first_star = QtWidgets.QPushButton(window)
    button_second_star = QtWidgets.QPushButton(window)
    button_third_star = QtWidgets.QPushButton(window)
    button_fourth_star = QtWidgets.QPushButton(window)
    button_fifth_star = QtWidgets.QPushButton(window)

    button_first_star.move(700, 30)
    button_second_star.move(700, 60)
    button_third_star.move(700, 90)
    button_fourth_star.move(700, 120)
    button_fifth_star.move(700, 150)

    button_first_star.setText("1>>")
    button_second_star.setText("2>>")
    button_third_star.setText("3>>")
    button_fourth_star.setText("4>>")
    button_fifth_star.setText("5>>")

    button_first_star.clicked.connect(click_button_first_star)
    button_second_star.clicked.connect(click_button_second_star)
    button_third_star.clicked.connect(click_button_third_star)
    button_fourth_star.clicked.connect(click_button_fourth_star)
    button_fifth_star.clicked.connect(click_button_fifth_star)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()