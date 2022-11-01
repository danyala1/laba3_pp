from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import sys


def application():
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
    button_create_dataset.move(350, 0)
    button_create_dataset.setText("Создать dataset")
    button_create_dataset.setFixedWidth(200)

    button_recreate_dataset = QtWidgets.QPushButton(window)
    button_recreate_dataset.move(350, 50)
    button_recreate_dataset.setText("Перекопировать dataset")
    button_recreate_dataset.setFixedWidth(200)

    button_copy_random_dataset = QtWidgets.QPushButton(window)
    button_copy_random_dataset.move(350, 100)
    button_copy_random_dataset.setText("Рандомный элемент dataset")
    button_copy_random_dataset.setFixedWidth(200)

    button_last_opinion = QtWidgets.QPushButton(window)
    button_last_opinion.move(350, 200)
    button_last_opinion.setText("Предыдущий отзыв")
    button_last_opinion.setFixedWidth(200)

    button_next_opinion = QtWidgets.QPushButton(window)
    button_next_opinion.move(350, 200)
    button_next_opinion.setText("Следующий отзыв")
    button_next_opinion.setFixedWidth(200)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()