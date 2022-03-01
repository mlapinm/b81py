from abc import ABC, abstractclassmethod

if __name__ == "__main__":

    class Engine:
        pass

class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)

class AbstractObserver(ABC):

    @abstractclassmethod
    def update(self, message):
        pass

class ShortNotificationPrinter(AbstractObserver):

    def __init__(self):
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message['title'])
        # print(self.achievements)

class FullNotificationPrinter(AbstractObserver):

    def __init__(self):
        self.achievements = []

    def update(self, message):
        fltr = [e for e in self.achievements if message['title'] in e['title']]
        if len(fltr) == 0:
            self.achievements += [message]
        # print(self.achievements)


if __name__ == "__main__":
    class Engine:
      pass

    engine = Engine()
    observable_engine = ObservableEngine()

    short_printer = ShortNotificationPrinter()
    full_printer = FullNotificationPrinter()
    observable_engine.subscribe(short_printer)
    observable_engine.subscribe(full_printer)

    observable_engine.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
    observable_engine.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})

