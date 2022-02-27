# =============================================================================
# Скрипт для тестирования решений студентов по заданию "Создание декоратора
# класса" (тесты содержат примеры, приведенные в описании задания)
# https://stepik.org/lesson/106937/step/4?unit=81460
# Скопируйте код вашего решения в секцию ВАШ КОД и запустите скрипт
# =============================================================================
from abc import ABC, abstractmethod

def print_hero(hero):
  stats = hero.get_stats()
  positive_effects = hero.get_positive_effects()
  negative_effects = hero.get_negative_effects()

  print(stats)
  print(positive_effects)
  print(negative_effects)

class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


# =============================================================================
# начало секции ВАШ КОД
# =============================================================================
# Поместите в этой секции реализацию классов AbstractEffect, AbstractPositive,
# AbstractNegative, Berserk, Blessing, Curse, EvilEye, Weakness из вашего
# решения

class AbstractEffect(Hero, ABC):

  def __init__(self, base):
    self.base = base

  @abstractmethod
  def get_positive_effects(self):
    pass

  @abstractmethod
  def get_negative_effects(self):
    pass

  @abstractmethod
  def get_stats(self):
    pass

class AbstractPositive(AbstractEffect):

  @abstractmethod
  def get_positive_effects(self):
    pass

  def get_negative_effects(self):
    return self.base.get_negative_effects()

  @abstractmethod
  def get_stats(self):
    pass

class AbstractNegative(AbstractEffect):

  def get_positive_effects(self):
    return self.base.get_positive_effects()

  @abstractmethod
  def get_negative_effects(self):
    pass

  @abstractmethod
  def get_stats(self):
    pass

class Berserk(AbstractPositive):

  def get_positive_effects(self):
    return self.base.get_positive_effects() + [self.__class__.__name__]

  def get_stats(self):
    stats = self.base.get_stats()
    stats['HP'] += 50
    stats['Strength'] += 7
    stats['Endurance'] += 7
    stats['Agility'] += 7
    stats['Luck'] += 7
    stats['Perception'] -= 3
    stats['Charisma'] -= 3
    stats['Intelligence'] -= 3
    return stats

class Blessing(AbstractPositive):

  def get_positive_effects(self):
      return self.base.get_positive_effects() + [self.__class__.__name__]

  def get_stats(self):
    stats = self.base.get_stats()
    stats['Strength'] += 2 
    stats['Perception'] += 2 
    stats['Endurance'] += 2 
    stats['Charisma'] += 2 
    stats['Intelligence'] += 2 
    stats['Agility'] += 2 
    stats['Luck'] += 2 
    return stats

class Weakness(AbstractNegative):

  def get_negative_effects(self):
      return self.base.get_negative_effects() + [self.__class__.__name__]

  def get_stats(self):
    stats = self.base.get_stats()
    stats['Strength'] -= 4 
    stats['Endurance'] -= 4 
    stats['Agility'] -= 4 
    return stats

class EvilEye(AbstractNegative):

  def get_negative_effects(self):
      return self.base.get_negative_effects() + [self.__class__.__name__]

  def get_stats(self):
    stats = self.base.get_stats()
    stats['Luck'] -= 10 
    return stats

class Curse(AbstractNegative):

  def get_negative_effects(self):
      return self.base.get_negative_effects() + [self.__class__.__name__]

  def get_stats(self):
    stats = self.base.get_stats()
    stats['Strength'] -= 2 
    stats['Perception'] -= 2 
    stats['Endurance'] -= 2 
    stats['Charisma'] -= 2 
    stats['Intelligence'] -= 2 
    stats['Agility'] -= 2 
    stats['Luck'] -= 2 
    return stats


# =============================================================================
# конец секции ВАШ КОД
# =============================================================================

if __name__ == '__main__':
    # создадим героя
    hero = Hero()

    brs1 = Berserk(hero)
    print_hero(brs1)
    brs2 = Berserk(brs1)
    print_hero(brs2)
    hero2 = Curse(brs2)

    # hero2.base = brs1
    print_hero(hero2)

    print(issubclass(Berserk, Hero))
