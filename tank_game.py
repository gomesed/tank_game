import random

class Tank:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    def __str__(self):
        if self.alive:
            return f"{self.name} ({self.armor} armor, {self.ammo} shells)"
        else:
            return f"{self.name} (DEAD)"

    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(f"{self.name} fires on {enemy.name}")
            enemy.hit()
        else:
            print(f"{self.name} has no shells!")

    def hit(self):
        self.armor -= 20
        print(f"{self.name} is hit")
        if self.armor <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print(f"{self.name} explodes!")

def create_tanks(num_tanks):
    tanks = {}
    for i in range(num_tanks):
        name = input(f"Enter the name of the tank {i+1}: ")
        tanks[chr(ord('a')+i)] = Tank(name)
    return tanks

num_tanks = int(input("How many tanks do you want to create? (between 2 and 10): "))
if num_tanks < 2 or num_tanks > 10:
    print("Invalid number of tanks. The game will be terminated.")
else:
    tanks = create_tanks(num_tanks)
    players = list(tanks.keys())
    print("Players:", players)

    while len(players) > 1:
        current_player = random.choice(players)
        print(f"Player's turn {current_player}:")
        enemy_players = players.copy()
        enemy_players.remove(current_player)
        print("Enemies:", enemy_players)

        target_player = input("Choose a player to shoot (player letter): ")
        while target_player not in enemy_players:
            target_player = input("Invalid player. Choose a player to shoot (player letter): ")

        attacker = tanks[current_player]
        defender = tanks[target_player]
        attacker.fire_at(defender)
        if not defender.alive:
            players.remove(target_player)

        for tank in tanks.values():
            print(tank)
        print()

    winner = players[0]
    print(f"The winning tank is: {tanks[winner].name}")
