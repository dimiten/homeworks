from file import File


class Text(File):

    def __init__(self, name, extension, size, description, modified, data: str):
        super().__init__(name, extension, size, description, modified, data)
        self.num_of_chars = 0
        for i in range(len(data)):
            self.num_of_chars += i

