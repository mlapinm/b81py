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

class EventSet():
  def __init__(self, value):
    self.kind = None
    self.value = value
    if type(value) == int:
      self.kind = 'set int'
    elif type(value) == float:
      self.kind = 'set float'  
    elif type(value) == str:
      self.kind = 'set str'  

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
    elif event.kind == 'set int':
      print('...get int')
      obj.integer_field = event.value
    else:
      print('int later...')
      return super().handle(obj, event)

class FloatHandler(NullHandler):

  def handle(self, obj, event):
    if event.kind == 'float':
      print('...float')
      return obj.float_field
    elif event.kind == 'set float':
      print('...float')
      obj.float_field = event.value
    else:
      print('float later...')
      return super().handle(obj, event)

class StrHandler(NullHandler):

  def handle(self, obj, event):
    if event.kind == 'str':
      print('....str')
      return obj.string_field
    elif event.kind == 'set str':
      print('...str')
      obj.string_field = event.value
    else:
      print('str later...')
      return super().handle(obj, event)

if __name__ == "__main__":
  # from b08main import *
  # cd b81py/b21042op/
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
  res = chain.handle(obj, EventSet(10))
  print(res)
  res = chain.handle(obj, EventSet(0.5))
  print(res)
  res = chain.handle(obj, EventSet("other text"))
  print(res)

