from enemy import *

zombie = Enemy()
zombie.type_of_enemy = 'Zombie'
print(f'{zombie.type_of_enemy} has {zombie.health_points}'
      f' health points And can do attack of {zombie.attack_damage}')

zombie.talk()
zombie.walk_forward()
zombie.attack()