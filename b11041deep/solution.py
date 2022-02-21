import encodings
import os
import tempfile

class Singleton:
  instance = None
  num = 0

  def __new__(cls):
    if cls.instance is None:
      cls.instance = super().__new__(cls)
    return cls.instance

  def get(cls):
    cls.num += 1
    return cls.num

  def get_path(cls):
    str_num = 'tmp' + cls.__str__()
    tmp_path = tempfile.gettempdir()
    path = os.path.join(tmp_path, str_num)
    return path

  def __str__(cls):
    cls.num += 1
    return "{:05}".format(cls.num)


class File:

  def __init__(self, name):
    self.name = name
    is_file = os.path.exists(self.name)
    self.strs = []
    if not is_file:
      with open(self.name, 'w') as f:
        pass
    self.text = self.read()
    with open(self.name, 'r') as f:
      self.strs = f.readlines()
    self.current = 0
    self.end = len(self.strs)


  def __str__(self):
    return self.name

  def read(self):
    with open(self.name, 'r') as f:
      self.text = f.read()
      self.strs = f.readlines()
      self.current = 0
      self.end = len(self.strs)
    return self.text

  def write(self, text):
    with open(self.name, "w") as f:
      f.write(text)
    self.__init__(self.name)
    # self.text = self.read()
    return len(text)

  def __iter__(self):
    return self

  def __next__(self):
    if self.current >= self.end:
      self.current = 0
      raise StopIteration
    result = self.strs[self.current]
    self.current += 1
    return result

  def __add__(self, obj):
    text = self.text + obj.text
    name = Singleton().get_path()

    obj3 = self.__class__(name)
    obj3.write(text)
    obj3.__init__(name)

    return obj3



if __name__ == "__main__":
  cwd = "./b81py/b11041deep/"
  path_to_file = 'some_filename1'
  is_file = os.path.exists(cwd + path_to_file)   # False
  file_obj = File(cwd + path_to_file)
  # print(file_obj.read())
  file_obj.write('454545\nerwrwwrwr\n')
  # print(file_obj)

  n2 = File(cwd + 'some_filename2')
  n3 = file_obj + n2
  for i, e in enumerate(n3):
    print(i, ascii(e) )
    pass

  print(n3)
          
