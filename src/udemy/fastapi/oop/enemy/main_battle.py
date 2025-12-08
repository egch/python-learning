from src.udemy.fastapi.oop.enemy.enemy import Enemy
from src.udemy.fastapi.oop.enemy.ogre import Ogre
from src.udemy.fastapi.oop.enemy.zombie import Zombie


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()
    while e1.health_points > 0 and e2.health_points > 0:
        print('____')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.health_points} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.health_points} HP left')
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage
    print('____')
    if e1.health_points > e2.health_points:
        print(f'{e1.get_type_of_enemy()} wins')
    elif e1.health_points < e2.health_points:
        print(f'{e2.get_type_of_enemy()} wins')
    else:
        print("draw")




zombie = Zombie(10,1)
ogre = Ogre(1,3)

battle(zombie, ogre)