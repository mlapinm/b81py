import os
import tempfile

class File:

  def __init__(self, name):
    self.name = name
    is_file = os.path.exists(self.name)
    if not is_file:
      with open(self.name, 'w') as f:
        pass
    self.text = self.read()
    self.strs = self.text.split('\n')
    self.current = 0
    self.end = len(self.strs)


  def __str__(self):
    return self.name

  def read(self):
    with open(self.name, 'r') as f:
      self.text = f.read()
      self.strs = self.text.split('\n')
      self.current = 0
      self.end = len(self.strs)
    return self.text

  def write(self, text):
    with open(self.name, "w") as f:
      f.write(text)
    self.__init__(self.name)
    return len(text)

  def __iter__(self):
    return self

  def __next__(self):
    if self.current >= self.end:
      raise StopIteration
    result = self.strs[self.current]
    self.current += 1
    return result

  def __add__(self, obj):
    text = self.text + obj.text
    # print(33, cwd, text)
    tf = tempfile.TemporaryFile()
    tf.close()
    obj3 = self.__class__(tf.name)
    obj3.write(text)
    return obj3



if __name__ == "__main__":
  cwd = "./b81py/b11041deep/"
  path_to_file = 'some_filename1'
  is_file = os.path.exists(cwd + path_to_file)   # False
  file_obj = File(cwd + path_to_file)
  # print(file_obj.read())
  file_obj.write('454545\nerwrwwrwr\n')
  # print(file_obj)
  for i, e in enumerate(file_obj):
    print(i, e)
    pass

  n2 = File(cwd + 'some_filename2')
  n3 = file_obj + n2

  print(n3)
          
