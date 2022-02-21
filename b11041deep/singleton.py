import tempfile
import os

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

if __name__ == "__main__":

  a = Singleton()
  print(a.get_path())
  print(a.get_path())
  print(a.get_path())




