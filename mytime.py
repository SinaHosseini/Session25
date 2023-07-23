

class MyTime:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.condition()

    def add_second(self):
        self.second += 1
        self.condition()

    def sub_second(self):
        self.second -= 1
        self.condition()

    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)

    def sum(self, other):
        new_second = self.second + other.second
        new_minute = self.minute + other.minute
        new_hour = self.hour + other.hour
        result = MyTime(new_hour, new_minute, new_second)
        return result

    def equal(self, other):
        new_second = self.second - other.second
        new_minute = self.minute - other.minute
        new_hour = self.hour - other.hour
        if new_second == 0 and new_minute == 0 and new_hour == 0:
            return True
        else:
            return False

    def to_string(self):
        return f"{self.hour}:{self.minute}:{self.second}"

    def sub(self, other):
        new_second = self.second + other.second
        new_minute = self.minute + other.minute
        new_hour = self.hour + other.hour
        result = MyTime(new_hour, new_minute, new_second)
        return result

    @staticmethod
    def convert_second_to_time(second):
        x = MyTime(0, 0, second)
        return x

    def convert_time_to_second(self):
        second = (self.hour * 60 + self.minute) * 60 + self.second
        return second

    def convert_GMT_to_Tehran(self):
        Tehran = Time(3, 30, 0)
        x = Time.sum(self, Tehran)

    def condition(self):
        while self.second >= 60:
            self.second -= 60
            self.minute += 1

        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        while self.hour >= 24:
            self.hour -= 24

        while self.second < 0:
            self.second += 60
            self.minute -= 1

        while self.minute < 0:
            self.minute += 60
            self.hour -= 1

        while self.hour < 0:
            self.hour += 24
