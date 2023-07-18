import sys
import time
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from mytime import MyTime


class MyThread(QThread):
    signal_time = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)

    def run(self):
        while True:
            self.time.plus()
            self.signal_time.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.hour = 0
        self.time.minute = 0
        self.time.seconde = 0


def reset_stopwatch():
    thread_stopwatch.reset()
    window.lbl_stopwatch.setText("0:0:0")


def stop_stopwatch():
    thread_stopwatch.terminate()


def start_stopwatch():
    thread_stopwatch.start()


def show_number(time):
    window.lbl_stopwatch.setText(f"{time.hour}:{time.minute}:{time.seconde}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    loader = QUiLoader()
    window = loader.load("mainwindow.ui")
    window.show()

    thread_stopwatch = MyThread()
    window.lbl_stopwatch.setText("0:0:0")
    window.btn_start_stopwatch.clicked.connect(start_stopwatch)
    window.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
    window.btn_reset_stopwatch.clicked.connect(reset_stopwatch)
    thread_stopwatch.signal_time.connect(show_number)

    app.exec()
