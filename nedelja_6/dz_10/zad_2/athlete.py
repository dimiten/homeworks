from abc import ABC, abstractmethod


class Athlete(ABC):
    def __init__(self, name, surname, result):
        self.name = name
        self.surname = surname
        self.__result = result

    def get_result(self):
        return self.__result

    def set_result(self, result):
        self.__result = result

    @abstractmethod
    def better_result(self, other: "Athlete"):
        pass

    def input_athlete(self):
        name = input("Name of athlete: ")
        self.name = name
        surname = input("Surname of athlete: ")
        self.surname = surname
        result = input("Result of athlete: ")
        self.set_result(result=result)

    def show_athlete(self):
        return f"Name: {self.name}, surname: {self.surname}, result: {self.get_result()}"
