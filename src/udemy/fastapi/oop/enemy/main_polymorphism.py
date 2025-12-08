from src.udemy.fastapi.oop.enemy.enemy import Enemy
from src.udemy.fastapi.oop.enemy.ogre import Ogre
from src.udemy.fastapi.oop.enemy.zombie import Zombie


def battle(en: Enemy):
    en.talk()
    en.attack()

zombie = Zombie(10,1)
ogre = Ogre(20, 3)

battle(zombie)
battle(ogre)

# *Grumbling ...
# Zombie attack
# Ogre is slamming hands all around
# Ogre attack
