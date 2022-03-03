class SomeObject():
  def __init__(self):
    self.integer_field = 0
    self.float_field = 0.0

class Event:
  def __init__(self):
    self.kind = None

class EventGet(Event):
  def __init__(self, type_):
    super().__init__()
    if(type_ == float):
      self.kind = 'float'
    elif(type_ == int):
      self.kind = 'int'

class NullHandler():
  def __init__(self, successor):
    self.successor = successor

  def handle(self, obj, event):
    return self.successor.handle(obj, event)

class IntHandler(NullHandler):
  def handle(self, obj, event):
    if event.kind == 'int':
      print('... int')
      return obj.integer_field
    else:
      print('later ...')
      return super().handle(obj, event)

class FloatHandler(NullHandler):
  def handle(self, obj, event):
    if event.kind == 'float':
      print('... float')
      print(obj.float_field)
      return obj.float_field
    else:
      print('later ...')
      return super().handle(obj, event)

if __name__ == '__main__':
  obj = SomeObject()
  obj.integer_field = 42
  obj.float_field = 3.14

  chain = IntHandler(FloatHandler(NullHandler))

  event = EventGet(float)
  print(event.kind)
  res1 = chain.handle(obj, event)
  print(res1)

  