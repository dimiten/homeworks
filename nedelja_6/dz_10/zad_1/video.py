from image import Image


class Video(Image):
    def __init__(self, name, extension, size, description, modified, data, dimension, length):
        super().__init__(name, extension, size, description, modified, data, dimension)
        self.length = length
