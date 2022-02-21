
class TextIterator:
  def __init__(self, text):
    self.text = text
    self.strs = text.split('\n')
    self.current = 0
    self.end = len(self.strs)

  def __iter__(self):
    return self

  def __next__(self):
    if self.current >= self.end:
      raise StopIteration

    result = self.strs[self.current]
    self.current += 1
    return result

if __name__ == "__main__":
  ti = TextIterator("""12
34
56""")

  print(ti.strs)

  for i, e in enumerate(ti):
    print(i, ascii(e))

  print(444)
