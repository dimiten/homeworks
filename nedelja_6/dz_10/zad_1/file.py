class File:

    def __init__(self, name, extension, size, description, modified, data):
        self.name = name
        self.extension = extension
        self.size = size
        self.description = description
        self.modified = modified
        self.data = data

    def read_from_file(self):
        with open(f"{self.name}.{self.extension}", "r") as f:
            return f.read()

    def write_in_file(self, data_to_write):
        with open(f"{self.name}.{self.extension}", "w") as f:
            f.write(data_to_write)
        self.modified += 1
