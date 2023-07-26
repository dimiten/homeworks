from dot import Dot


class Line:

    def __init__(self, start_dot: Dot, end_dot: Dot, length: int):
        self.start_dot = start_dot
        self.end_dot = end_dot
        self.length = length

    def change_start_dot(self, new_start_dot: Dot):
        self.start_dot = new_start_dot

    def change_end_dot(self, new_end_dot: Dot):
        self.start_dot = new_end_dot

    def change_length(self, new_length: int):
        self.length = new_length
