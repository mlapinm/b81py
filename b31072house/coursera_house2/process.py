#process.py
# from .coursera_house.core.tasks import *
from coursera_house.core.tasks import *
import time


def process_start():

  while True:
    smart_home_manager()
    time.sleep(5)


if __name__ == "__main__":
  process_start()

  