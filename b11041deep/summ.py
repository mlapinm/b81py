
class Number:
  def __init__(self, num):
    self.num = num

  def __add__(self, obj):
    sum = self.num + obj.num
    n3 = self.__class__(sum)
    return n3 

  def __str__(self):
    return str(self.num)

if __name__ == "__main__":

  n1 = Number(1)
  n2 = Number(2)

  n3 = n1 + n2

  print(444, n3)
