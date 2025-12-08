import random

from src.udemy.fastapi.oop.enemy.enemy import Enemy
from src.udemy.fastapi.oop.enemy.zombie import Zombie


class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Ogre', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print('Ogre is slamming hands all around')

    def special_attack(self):
        dis_special_attack_work = random.random() < 0.20
        if dis_special_attack_work:
            self.health_points +=4
            print('Ogre get angry and increases attack by 4')


