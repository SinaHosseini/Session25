

class MyTime:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.seconde = s

    def plus(self):
        self.seconde += 1
        if self.seconde >= 60:
            self.minute += 1
            self.seconde -= 60
        if self.minute >= 60:
            self.hour += 1
            self.minute -= 60
