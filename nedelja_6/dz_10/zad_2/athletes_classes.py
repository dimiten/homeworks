from abc import ABC
from athlete import Athlete


class Runner(Athlete, ABC):
    def __init__(self, name="", surname="", result=0):
        super().__init__(name, surname, result)

    def better_result(self, other: "Runner"):
        if self.get_result() < other.get_result():
            return self.get_result()
        return other.get_result()


class Jumper(Athlete, ABC):
    def __init__(self, name="", surname="", result=0):
        super().__init__(name, surname, result)

    def better_result(self, other: "Jumper"):
        if self.get_result() > other.get_result():
            return self.get_result()
        return other.get_result()
