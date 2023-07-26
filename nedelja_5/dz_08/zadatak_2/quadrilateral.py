from line import Line


class Quadrilateral:

    def __init__(self, line_a: Line, line_b: Line):
        self.line_a = line_a
        self.line_b = line_b

    def calculate_circumference(self):
        return 2 * self.line_a.length + 2 * self.line_b.length

    def calculate_area_of_surface(self):
        return self.line_a.length * self.line_b.length
