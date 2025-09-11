# # import pym
# # print(pym.add(1,43))


# import pym as p
# print(p.add(1,43))


# import random

# list=["12",2,4,2,2,23]
# print(random.choice(list))
# print(random.randint(1,33))


# import math

# print(math.sqrt(16))


# from dog import *

# dog=Dog()
# print(dog.legs);
# print(dog.type);
# print(dog.ears);


from enemy import *

zombie=Enemy("zoobie",18,5)
zombie.talk()
zombie.walk_farword()
zombie.attack()

zombie=Enemy("ogre",12,3)
zombie.talk()
zombie.walk_farword()
zombie.attack()
print(zombie.get_type_of_enemy())  # ✓ Works
zombie.__type_of_enemy = "ogre"  # ✗ Error - cannot access private
print(zombie.get_type_of_enemy())  # ✓ Works

# --------> Output <---------------
# i am zoobie. Be prepared to fight
# zoobie moves closer to you
# zoobie attacks for 5 damage
# i am ogre. Be prepared to fight
# ogre moves closer to you
# ogre attacks for 3 damage
# ogre
# ogre