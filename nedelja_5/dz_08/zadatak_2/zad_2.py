from dot import Dot
from line import Line
from quadrilateral import Quadrilateral

dot_1 = Dot(0, 0)
dot_2 = Dot(0, 3)
dot_3 = Dot(4, 0)
dot_4 = Dot(4, 3)

line_1 = Line(dot_1, dot_2, 3)
line_2 = Line(dot_3, dot_4, 4)

quadrilateral1 = Quadrilateral(line_1, line_2)

print(quadrilateral1.calculate_circumference())
print(quadrilateral1.calculate_area_of_surface())
