
"""
Boolean & Operators
"""
class Enemy:
    #I can remove the list of fields as already defined in the constructor
    #attack_damage: str
    #health_points: int
    #type_of_enemy: int

# encapsulation
# getters
    # we need now this since __type_of_enemy is private
    def get_type_of_enemy(self):
        return self.__type_of_enemy

# instance method
    def talk(self):
        print(f"I am a {self.get_type_of_enemy()} enemy")


    def walk_forward(self):
        print(f"{self.get_type_of_enemy()} walk forward")


    def attack(self):
        print(f"{self.get_type_of_enemy()} attacks for {self.attack_damage} damage")

    def special_attack(self):
        print("Enemy has no special attack")


    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.attack_damage = attack_damage
        self.health_points = health_points
        self.__type_of_enemy = type_of_enemy  #now type_of_enemy is private and it can no longer be changed
