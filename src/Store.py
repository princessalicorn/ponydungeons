from time import sleep
from clear import clear

class timesbought():
    def __init__(self, armor, weapon, speed):
        self.armor = armor
        self.weapon = weapon
        self.speed = speed

shopvalues = timesbought(1, 1, 1)

def checkbal(wallet, price):
    if wallet >= price:
        return True
    else:
        return False


def generate_price(type):
    if type <= 1:
        return 25
    elif (type > 1, type <= 5):
        return int(0.7 * (25 * type))
    else:
        return 25 * type


def shop(player, bought):
    i = 0
    while i < 1:
        armorprice = generate_price(bought.armor)
        weaponprice = generate_price(bought.weapon)
        speedprice = generate_price(bought.speed)
        clear()
        print("Your balance is ${}".format(player.wallet))
        print("""
        What do you want to buy?
        1. HP (+15) $5       2. Attack +5 ${}
        3. Defense +5 ${}    4. Agility (+5) $35
        5. View Stats        6. Quit
        """.format(weaponprice, armorprice))
        opt = int(input())
        if opt == 1:
            if checkbal(player.wallet, 15):
                player.health += 15
                player.wallet -= 5
            else:
                clear()
                print("Insufficient Balance")
                sleep(2)
        elif opt == 2:
            if checkbal(player.wallet, weaponprice):
                bought.weapon += 1
                player.strength += 5
                player.wallet -= weaponprice
            else:
                clear()
                print("Insufficient Balance")
                sleep(2)
        elif opt == 3:
            if checkbal(player.wallet, armorprice):
                bought.armor += 1
                player.defense += 5
                player.wallet -= armorprice
            else:
                clear()
                print("Insufficient Balance")
                sleep(2)
        elif opt == 4:
            if checkbal(player.wallet, bought.speed):
                player.speed += 5
                player.wallet -= bought.speed
            else:
                clear()
                print("Insufficient Balance")
                sleep(2)
        elif opt == 5:
            clear()
            print("Stats: {}HP {}ATK {}DEF {}SPD".format(player.health, player.strength, player.defense, player.speed))
            sleep(2)
        elif opt == 6:
            i = 1
        else:
            clear()
            print("Enter a Valid Number.")
            sleep(2)
