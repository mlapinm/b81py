from solution import FileReader

file_path = "d:/programs/b81py/b1103deep/"

reader = FileReader(file_path + "some_file.txt")
text = reader.read()

print(text)
print(type(reader))
