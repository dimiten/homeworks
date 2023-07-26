from enum import Enum
from athletes_classes import Jumper, Runner


class TypeDiscipline(Enum):
    JUMPING = 1
    RUNNING = 2


class Discipline:
    def __init__(self, name, type: TypeDiscipline, num_of_contestants):
        self.__name = name
        self.__type = type
        self.__num_of_contestants = num_of_contestants
        self.contestants = []

    def get_type(self):
        return self.__type

    def get_num_of_contestants(self):
        return self.__num_of_contestants

    def input_contestants(self):
        if self.get_type() == TypeDiscipline.JUMPING:
            for i in range(self.get_num_of_contestants()):
                jumper = Jumper()
                jumper.input_athlete()
                self.contestants.append(jumper)

        if self.get_type() == TypeDiscipline.RUNNING:
            for i in range(self.get_num_of_contestants()):
                runner = Runner()
                runner.input_athlete()
                self.contestants.append(runner)

    def show_victor(self):
        if self.get_type() == TypeDiscipline.JUMPING:
            results = []
            for contestant in self.contestants:
                results.append(int(contestant.get_result()))
            best_result = max(results)

            for contestant in self.contestants:
                if int(contestant.get_result()) == best_result:
                    print(f"The victor of jumping is: {contestant.show_athlete()}")

        if self.get_type() == TypeDiscipline.RUNNING:
            results = []
            for contestant in self.contestants:
                results.append(int(contestant.get_result()))
            best_result = min(results)

            for contestant in self.contestants:
                if int(contestant.get_result()) == best_result:
                    print(f"The victor of running is: {contestant.show_athlete()}")
