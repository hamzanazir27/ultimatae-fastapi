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
