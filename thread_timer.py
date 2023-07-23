import time
from PySide6.QtCore import *
from mytime import MyTime


class TimerThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 15, 0)

    def run(self):
        while True:
            self.time.add_second()
            self.signal_show.emit(self.time)
            time.sleep(1)

    def set_time(self, second, minute, hour):
        self.time.second = second
        self.time.minute = minute
        self.time.hour = hour
