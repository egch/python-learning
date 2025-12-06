from src.udemy.fastapi.oop.enemy.enemy import Enemy


class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Zombie', health_points=health_points, attack_damage=attack_damage)
