
if __name__ == "__main__":

    class Engine:
        pass

from b04observer import *

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

