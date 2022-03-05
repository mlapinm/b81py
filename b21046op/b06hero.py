import yaml

class HeroFactory:
    @classmethod
    def create_hero(Class, name):
        return Class.Hero(name)
    
    @classmethod
    def create_weapon(Class):
        return Class.Weapon()
    
    @classmethod
    def create_spell(Class):
        return Class.Spell()

class WarriorFactory(HeroFactory):
    class Hero:
        def __init__(self, name):
            self.name = name
            self.weapon = None
            self.armor = None
            self.spell = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Warior hits with {self.weapon.hit()}")
            self.weapon.hit()

        def cast(self):
            print(f"Warior casts {self.spell.cast()}")
            self.spell.cast()
              
    class Weapon:
        def hit(self):
            return "Claymore"
        
    class Spell:
        def cast(self):
            return "Power"
        
    
class MageFactory(HeroFactory):
    class Hero:
        def __init__(self, name):
            self.name = name
            self.weapon = None
            self.armor = None
            self.spell = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Mage hits with {self.weapon.hit()}")
            self.weapon.hit()

        def cast(self):
            print(f"Mage casts {self.spell.cast()}")
            self.spell.cast()
            
    class Weapon:
        def hit(self):
            return "Staff"
        
    class Spell:
        def cast(self):
            return "Fireball"
    
        
class AssassinFactory(HeroFactory):
    class Hero:
        def __init__(self, name):
            self.name = name
            self.weapon = None
            self.armor = None
            self.spell = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Assassin hits with {self.weapon.hit()}")
            self.weapon.hit()

        def cast(self):
            print(f"Assassin casts {self.spell.cast()}")
     
    class Weapon:
        def hit(self):
            return "Dagger"
        
    class Spell:
        def cast(self):
            return "Invisibility"

def create_hero(factory):
    hero = factory.create_hero("Nagibator")
    
    weapon = factory.create_weapon()
    spell = factory.create_spell()
    
    hero.add_weapon(weapon)
    hero.add_spell(spell)
    
    return hero

# -------------------------------------------------------------------

def factory_constructor (loader , node):
  data = loader. construct_scalar (node)
  if data == "mage":
    return MageFactory
  elif data == "warrior":
    return WarriorFactory
  else:
    return AssassinFactory    


class Character (yaml.YAMLObject):
  yaml_tag = "!Character" # тэг, на который надо смотреть
  # теперь стала методом класса.
  # а factory стал атрибутом класса
  def create_hero(self):
    hero = self.factory.create_hero(self.name)
    weapon = self.factory.create_weapon ()
    spell = self.factory.create_spell ()
    hero.add_weapon (weapon)
    hero.add_spell (spell)
    return hero

hero_yaml = '''
--- !Character
factory:
  !factory assassin
name:
  7NaGiBaToR7
'''

if __name__ == "__main__":

  loader = yaml.Loader
  loader.add_constructor("!factory", factory_constructor )
  hero = yaml.load(hero_yaml).create_hero ()
  hero.hit () # пробуем ударить
  hero.cast () # пробуем ударить
  
  print('bbb')

