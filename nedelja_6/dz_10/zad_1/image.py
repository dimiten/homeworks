from file import File


class Image(File):

    def __init__(self, name, extension, size, description, modified, data, dimension):
        super().__init__(name, extension, size, description, modified, data)
        self.dimension = dimension
