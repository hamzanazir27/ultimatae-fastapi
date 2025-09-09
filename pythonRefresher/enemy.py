class Enemy:
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy  # Private (double underscore)
        self.health_points = health_points     # Public
        self.attack_damage = attack_damage     # Public

    # Getter method
    def get_type_of_enemy(self):
        return self.__type_of_enemy

    # No setter = cannot change type after creation
    def talk(self):
        print(f"i am {self.__type_of_enemy}. Be prepared to fight")

    def walk_farword(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")