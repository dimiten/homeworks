from discipline import Discipline, TypeDiscipline


if __name__ == "__main__":
    long_jump = Discipline(name="Long jump", type=TypeDiscipline(1), num_of_contestants=3)
    sprint = Discipline(name="100m sprint", type=TypeDiscipline(2), num_of_contestants=3)

    long_jump.input_contestants()
    long_jump.show_victor()

    sprint.input_contestants()
    sprint.show_victor()
