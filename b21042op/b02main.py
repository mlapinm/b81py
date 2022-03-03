
PUT, GET, OPEN = "PUT", "GET", "OPEN"

class Event:

  def __init__(self, kind):
    self.kind = kind

class NullHandler:

  def __init__(self, successor=None):
    self.__successor = successor

  def handle(self, event):
    self.__successor.handle(event)

class OpenBookshelf(NullHandler):
  def handle(self, event):
    if event.kind == OPEN:
      print('open bookshelf')
      print()
    else:
      print('(open bookshelf) later...')
      super().handle(event)

class PutDuma(NullHandler):
  def handle(self, event):
    if event.kind == PUT:
      print('put Duma')
      print()
    else:
      print('(put Duma) later...')
      super().handle(event)

class GetCupper(NullHandler):
  def handle(self, event):
    if event.kind == GET:
      print('get Cupper')
      print()
    else:
      print('(get Cupper) later...')
      super().handle(event)

class Giver:

  def __init__(self):
    # self.handlers = OpenBookshelf(GetCupper(PutDuma(NullHandler())))
    self.handlers = PutDuma(GetCupper(OpenBookshelf(NullHandler())))
    self.events = []

  def add_event(self, event):
    self.events.append(event)

  def handle_events(self):
    for event in self.events:
      self.handlers.handle(event)


if __name__ == "__main__":
  events = [Event(OPEN), Event(GET), Event(PUT)]
  # events = [Event(PUT), Event(GET), Event(OPEN)]
  # events = [Event(OPEN), Event(GET)]
  giver = Giver()
  for event in events:
    giver.add_event(event)

  print([e.kind for e in giver.events])

  giver.handle_events()



  print('aaaa')
