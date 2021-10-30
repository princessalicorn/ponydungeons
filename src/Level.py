from Monster import *

class Level:
    def __init__(self, value, monsters, artluck):
        self.value = value
        self.monstercount = monsters
        self.artluck = artluck
        self.monstertypes = []

level1 = Level(0, 5, 11)
level2 = Level(1, 6, 12)
level3 = Level(2, 7, 13)
level4 = Level(3, 8, 15)
level5 = Level(4, 9, 15)
level6 = Level(5, 10, 14)
level7 = Level(5, 10, 15)
level8 = Level(5, 8, 15)
level9 = Level(5, 5, 15)
level10 = Level(5, 1, 15)



level1.monstertypes.append(zombie)

level2.monstertypes.append(zombie)
level2.monstertypes.append(zpony)
level2.monstertypes.append(zpony)

level3.monstertypes.append(zpony)
level3.monstertypes.append(changeling1)
level3.monstertypes.append(changeling1)
level3.monstertypes.append(timberwolf)
level3.monstertypes.append(timberwolf)

level4.monstertypes.append(timberwolf)
level4.monstertypes.append(changeling1)
level4.monstertypes.append(changeling1)
level4.monstertypes.append(changeling2)
level4.monstertypes.append(changeling2)

level5.monstertypes.append(timberwolf)
level5.monstertypes.append(changeling2)
level5.monstertypes.append(changeling2)
level5.monstertypes.append(griffon)
level5.monstertypes.append(griffon)

level6.monstertypes.append(changeling2)
level6.monstertypes.append(griffon)
level6.monstertypes.append(griffon)
level6.monstertypes.append(smooze)
level6.monstertypes.append(smooze)

level7.monstertypes.append(griffon)
level7.monstertypes.append(smooze)
level7.monstertypes.append(smooze)
level7.monstertypes.append(parasprite)
level7.monstertypes.append(parasprite)

level8.monstertypes.append(smooze)
level8.monstertypes.append(parasprite)
level8.monstertypes.append(parasprite)
level8.monstertypes.append(changeling3)

level9.monstertypes.append(changeling3)

level10.monstertypes.append(chrysalis)
