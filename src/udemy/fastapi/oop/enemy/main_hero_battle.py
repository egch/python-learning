from src.udemy.fastapi.oop.enemy.enemy import Enemy
from src.udemy.fastapi.oop.enemy.hero import Hero
from src.udemy.fastapi.oop.enemy.ogre import Ogre
from src.udemy.fastapi.oop.enemy.weapon import Weapon
from src.udemy.fastapi.oop.enemy.zombie import Zombie




def hero_battle(h1: Hero, enemy: Enemy):

    while h1.health_points > 0 and enemy.health_points > 0:
        print('____')
        print(f'Hero: {h1.health_points} HP left')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_points} HP left')
        enemy.attack()
        h1.health_points -= enemy.attack_damage
        h1.attack()
        enemy.health_points -= h1.attack_damage
    print('____')
    if h1.health_points > enemy.health_points:
        print(f'Hero wins')
    elif h1.health_points < enemy.health_points:
        print(f'{enemy.get_type_of_enemy()} wins')
    else:
        print("draw")


zombie = Zombie(10,1)
ogre = Ogre(20,3)
hero = Hero(10,1)

weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()


hero_battle(hero, zombie)