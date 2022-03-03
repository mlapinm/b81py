class SomeObject():
  def __init__(self):
    self.integer_field = 0
    self.float_field = 0.0
    self.string_field = ""

class EventGet():
  def __init__(self, type_):
    self.kind = None
    if type_ == int:
      self.kind = 'int'
    elif type_ == float:
      self.kind = 'float'
    elif type_ == str:
      self.kind = 'str'

class NullHandler():
  def __init__(self, successor):
    self.successor = successor

  def handle(self, obj, event):
    return self.successor.handle(obj, event)

class IntHandler(NullHandler):

  def handle(self, obj, event):
    if event.kind == 'int':
      print('...int')
      return obj.integer_field
    else:
      print('int later...')
      return super().handle(obj, event)

class FloatHandler(NullHandler):

  def handle(self, obj, event):
    if event.kind == 'float':
      print('...float')
      return obj.float_field
    else:
      print('float later...')
      return super().handle(obj, event)

class StrHandler(NullHandler):

  def handle(self, obj, event):
    if event.kind == 'str':
      print('...str')
      return obj.string_field
    else:
      print('str later...')
      return super().handle(obj, event)

if __name__ == "__main__":

obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some string"

chain = IntHandler(FloatHandler(StrHandler(NullHandler)))

  res = chain.handle(obj, EventGet(int))
  print(res)
  res = chain.handle(obj, EventGet(float))
  print(res)
  res = chain.handle(obj, EventGet(str))
  print(res)

