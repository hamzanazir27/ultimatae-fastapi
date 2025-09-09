class Enemy:
    # type_of_enemy=""
    # health_points=10
    # attack_damage=1
    ### 2. No-Argument Constructor

   
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
    def talk(self):
        print(f"i am {self.type_of_enemy}. Be prepared to fight")

    def walk_farword(self):
        print(f"{self.type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")