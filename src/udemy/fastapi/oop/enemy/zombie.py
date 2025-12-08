from src.udemy.fastapi.oop.enemy.enemy import Enemy
import random


class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Zombie',
                         health_points=health_points,
                         attack_damage=attack_damage)

    # instance method - we override method from the Enemy class
    def talk(self):
        print("*Grumbling ...")

    # this method only belongs to the Zombie class, not to its parent class
    def spread_disease(self ):
        print('The zombie is trying to spread infection')

    def special_attack(self):
        dis_special_attack_work = random.random() < 0.5
        if dis_special_attack_work:
            self.health_points +=2
            print('Zombie regenerated 2HP!')


