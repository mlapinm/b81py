import os

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
    text = ''
    with open(self.name, 'r') as f:
      text = f.read()
    return text

  def write(self, text):
    with open(self.name, "w") as f:
      f.write(text)

  def __iter__(self):
    return self

  def __next__(self):
    if self.current >= self.end:
      raise StopIteration
    result = self.strs[self.current]
    self.current += 1
    return result



if __name__ == "__main__":
  cwd = "./b81py/b11041deep/"
  path_to_file = 'some_filename1'
  is_file = os.path.exists(cwd + path_to_file)   # False
  file_obj = File(cwd + path_to_file)
  print(file_obj.read())
  file_obj.write('454545\nerwrwwrwr')
  print(file_obj)
  for e in file_obj:
    print(23, e)




  print(444)
