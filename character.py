import random


class Character:
    def __init__(self, name, hp, attack_power, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        base_damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        damage = max(1, base_damage - target.defense)
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        return damage

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)


class Player(Character):
    def special_attack(self, target):
        damage = max(2, (self.attack_power * 2) - target.defense)
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        return damage


class Enemy(Character):
    pass