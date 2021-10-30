class Artifact:
    def __init__(self, name, description, healthbuf, strengthbuf, defensebuf, speedbuf, slot):
        self.name = name
        self.description = description
        self.healthbuf = healthbuf
        self.strengthbuf = strengthbuf
        self.defensebuf = defensebuf
        self.speedbuf = speedbuf
        self.slot = slot

### Various Goodies you can get!
attackcharm = Artifact("an Amulet of Strength", "Increases your strength by 5 points.", 0, 5, 0, 0, "amulet")
defensecharm = Artifact("an Amulet of Defense", "Increases your defense by 5 points.", 0, 0, 5, 0, "amulet")
speedcharm = Artifact("an Amulet of Agility", "Increases your agility by 5 points.", 0, 0, 0, 5, "amulet")
healfood = Artifact("a Meal.", "Just a small meal.", 5, 0, 0, 0, "amulet")
smallpot = Artifact("a Lesser Healing Potion", "Increases health by 15", 15, 0, 0, 0, "amulet")
medpot = Artifact("a Moderate Healing Potion", "Increases health by 30", 30, 0, 0, 0, "amulet")
largepot = Artifact("a Large Healing Potion", "Increases health by 50", 50, 0, 0, 0, "amulet")
artifactlist = [attackcharm, defensecharm, healfood, speedcharm, smallpot, medpot, largepot]
