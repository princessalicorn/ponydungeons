class Monster:
    def __init__(self, name, health, strength, defense, reward=0):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.reward = reward


zombie = Monster("Decrepit Zombie", 20, 5, 5, 20)
zpony = Monster("Zombified Pony", 50, 10, 5, 30)
timberwolf = Monster("Timberwolf", 30, 15, 10, 25)
changeling1 = Monster("Changeling Scout", 60, 15, 10, 40)
changeling2 = Monster("Changeling Worker", 60, 25, 15, 45)
griffon = Monster("Griffon", 70, 26, 25, 55)
smooze = Monster("The Smooze", 90, 35, 35, 70)
parasprite = Monster("Cloud of Parasprites", 110, 35, 50, 80)
changeling3 = Monster("Changeling Guard", 120, 40, 40, 100)

chrysalis = Monster("Queen Chrysalis", 250, 50, 50, 500)
#Good Job if you are reading this
TheUnstoppingForceOfCommunism = Monster("The Unstoppable Wave of Communism", 9999, 9999, 9999, 9999)
