class Enemy:
    __slots__ = ['_type_of_enemy', '_health_points', '_attack_damage']

    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self._type_of_enemy = type_of_enemy
        self._health_points = health_points
        self._attack_damage = attack_damage

    @property
    def type_of_enemy(self):
        return self._type_of_enemy

# Now you CANNOT add new attributes:
# zombie = Enemy("zombie", 10, 5)
# zombie.new_attribute = "test"  # AttributeError!
