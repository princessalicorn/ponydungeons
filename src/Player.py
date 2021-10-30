from Monster import Monster

class Player(Monster):
    def __init__(self, name, health, strength, defense, reward, speed, wallet):
        super().__init__(name, health, strength, defense, reward)
        self.speed = speed
        self.wallet = wallet


player1 = Player("Player", 100, 10, 5, 0, 10, 0)
