from src.udemy.fastapi.oop.pets.animal import Animal


class Dog(Animal):
    #All animal attributes
    can_sched: bool
    domestic_name: str

    # override the talk of animal
    def talk(self):
        print("bark!")





