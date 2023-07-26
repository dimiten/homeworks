class Dot:

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def change_x_coordinate(self, new_x_coordinate: int):
        self.x_coordinate = new_x_coordinate

    def change_y_coordinate(self, new_y_coordinate: int):
        self.y_coordinate = new_y_coordinate
