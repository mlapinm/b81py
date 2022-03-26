

def load():
  with open('b12curr.txt', 'rb') as f:
    return f.read()

class Requests:
    def get(self):
        return load()
        
requests = Requests()
