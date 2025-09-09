class Enemy:
    type_of_enemy=""
    health_points=10
    attack_damage=1

    def talk(self):
        print(f"i am {self.type_of_enemy}. Be prepared to fight")

    def walk_farword(self):
        print(f"{self.type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")