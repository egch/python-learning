from enemy import *
from src.udemy.fastapi.oop.enemy.ogre import Ogre
from src.udemy.fastapi.oop.enemy.zombie import Zombie

zombie = Enemy('Zombie')
# we cannot change it as it's private
#zombie.__type_of_enemy = 'Lion'

print(f'{zombie.get_type_of_enemy()} has {zombie.health_points}'
      f' health points And can do attack of {zombie.attack_damage}')

zombie.talk()
zombie.walk_forward()
zombie.attack()

zombie2 = Enemy('Dracula', 20, 30)
# Dracula has 20 health points And can do attack of 30
print(f'{zombie2.get_type_of_enemy()} has {zombie2.health_points}'
      f' health points And can do attack of {zombie2.attack_damage}')

ogre = Ogre(23, 30)

zombie2 = Zombie(20,1)
print(zombie2.get_type_of_enemy())
zombie2.talk() # *Grumbling ...
zombie2.spread_disease()


ogre = Ogre(20, 30)


