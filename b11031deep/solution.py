


class FileReader():

    def __init__(self, file_name):
      self.file_name = file_name

    def read(self):
        text = ""
        try:
            with open(self.file_name, "r") as f:
                text = f.read()
        except Exception as ex:
            pass
        return text


def set_file(name):
    text = """qwe
asd
zxc"""
    with open(name, "w") as f:
        f.write(text)


if __name__ == "__main__":
    file_path = "d:/programs/b81py/b1103deep/"
    # set_file(file_path + "some_file.txt")



    reader = FileReader('not_exist_file.txt')
    text = reader.read()
    print(text)
    reader = FileReader(file_path + "some_file.txt")
    text = reader.read()
    print(text)
