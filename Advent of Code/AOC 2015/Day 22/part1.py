import copy

with open("input.txt") as file:
    data = file.read().splitlines()
    boss_hp = int(data[0].split()[2])
    boss_damage = int(data[1].split()[1])

# cost, damage, heal, armor, mana, duration
spells = {
    "Magic Missile": (53, 4, 0, 0, 0, 0),
    "Drain": (73, 2, 2, 0, 0, 0),
    "Shield": (113, 0, 0, 7, 0, 6),
    "Poison": (173, 3, 0, 0, 0, 6),
    "Recharge": (229, 0, 0, 0, 101, 5),
}

class Player:
    def __init__(self, hp, mana):
        self.hp = hp
        self.mana = mana
        self.armor = 0
        self.shield = 0
        self.poison = 0
        self.recharge = 0

    def can_cast(self, spell):
        cost = spells[spell][0]

        if (self.mana < cost):
            return False
        if (spell == "Shield" and self.shield > 0):
            return False
        if (spell == "Poison" and self.poison > 0):
            return False
        if (spell == "Recharge" and self.recharge > 0):
            return False
        
        return True


class Enemy:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    def attack(self, player):
        dmg = max(1, self.damage - player.armor)
        player.hp -= dmg


class Game:
    def __init__(self):
        self.player = Player(50, 500)
        self.enemy = Enemy(boss_hp, boss_damage)
        self.cost = 0

    def apply_effects(self):
        if (self.player.shield > 0):
            self.player.armor = spells["Shield"][3]
            self.player.shield -= 1
        else:
            self.player.armor = 0

        if (self.player.poison > 0):
            self.enemy.hp -= spells["Poison"][1]
            self.player.poison -= 1

        if (self.player.recharge > 0):
            self.player.mana += spells["Recharge"][4]
            self.player.recharge -= 1

    def play(self, player_turn):
        global res

        if (self.cost >= res):
            return

        self.apply_effects()

        if (self.enemy.hp <= 0):
            res = min(res, self.cost)
            return

        if (player_turn):
            for spell in spells:
                if (not self.player.can_cast(spell)):
                    continue

                new_game = copy.deepcopy(self)
                cost, dmg, heal, armor, mana, duration = spells[spell]

                new_game.player.mana -= cost
                new_game.cost += cost

                if (spell == "Magic Missile"):
                    new_game.enemy.hp -= dmg
                elif (spell == "Drain"):
                    new_game.enemy.hp -= dmg
                    new_game.player.hp += heal
                elif (spell == "Shield"):
                    new_game.player.shield = duration
                elif (spell == "Poison"):
                    new_game.player.poison = duration
                elif (spell == "Recharge"):
                    new_game.player.recharge = duration

                new_game.play(False)
        else:
            self.enemy.attack(self.player)

            if (self.player.hp > 0):
                self.play(True)


res = float("inf")
game = Game()
game.play(True)

print(res)
