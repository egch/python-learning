class Enemy:


    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    # instance method
    def talk(self):
        print(f"I am a {self.type_of_enemy} enemy")

    def walk_forward(self):
        print(f"{self.type_of_enemy} walk forward")

    def attack(self):
        print(f"{self.type_of_enemy} attack")

    # constructors
    def __init__(self):
        pass

    # def __init__(self):
    #     print("something")

