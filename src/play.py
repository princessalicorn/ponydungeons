import random as rng
from time import sleep
##Classes and Definitions##
from clear import clear
from Level import *
from Player import *
from Artifact import *
from store import shop, shopvalues

def rngattkfactor(name):
    toprngbound = 2 * name.strength
    lowrngbound = int(-0.5 * name.strength)
    rngfactor = rng.randrange(lowrngbound, toprngbound)
    return rngfactor


def monster_attacks(monster, health, defense):
    rngfactor = rngattkfactor(monster)
    newhealth = health - monster.strength - rngfactor + defense
    if newhealth > health:
        newhealth = health
    return newhealth


def player_attacks(monster, player, oldhealth):
    rngfactor = rngattkfactor(player)
    health = oldhealth - player.strength - rngfactor + monster.defense
    if oldhealth < health:
        health = oldhealth
    return health


def fight_monster(monster, player):
    battlehealth = player.health
    playerstrength = player.strength
    playerdefense = player.defense
    playerspeed = player.speed

    inithealth = monster.health
    print("You are fighting a(n) {}".format(monster.name))
    while inithealth > 0:
        if battlehealth <= 0:
            clear()
            print("")
            print("")
            print("")
            print("You died.")
            sleep(2)
            quit()
        clear()
        print("Stats: {}HP {}ATK {}DEF {}SPD".format(battlehealth, playerstrength, playerdefense, playerspeed))
        print("{} Stats: {}HP {}ATK {}DEF".format(monster.name, inithealth, monster.strength, monster.defense))
        print("""What will you do?
                 1. Attack
                 2. Run
              """)
        opt = int(input())
        if opt == 1:
            battlehealth = monster_attacks(monster, battlehealth, playerdefense)
            inithealth = player_attacks(monster, player, inithealth)
        elif opt == 2:
            esc = playerspeed * rng.randrange(1,7) - 2
            if esc > 50:
                clear()
                print("You escaped!")
                sleep(2)
                player.wallet = player.wallet - monster.reward
                inithealth = 0
                return battlehealth
            else:
                battlehealth = monster_attacks(monster, battlehealth, playerdefense)
        else:
            print("Enter a valid number.")
            sleep(2)

    print("You defeated {}!".format(monster.name))
    sleep(2)
    clear()
    return battlehealth

def update_stats(artifact, player):
    player.health = player.health + artifact.healthbuf
    player.strength = player.strength + artifact.strengthbuf
    player.defense = player.defense + artifact.defensebuf
    player.speed = player.speed + artifact.speedbuf


def play_level(lname, player):
    i = 0
    while i < lname.monstercount:
        if lname.artluck * rng.randrange(1, 5) > 50:
            artifact = rng.choice((artifactlist))
            print("You got {}".format(artifact.name))
            print(artifact.description)
            update_stats(artifact, player)
            sleep(2)
            clear()
        else:
            monster = rng.choice(lname.monstertypes)
            newplayerhealth = fight_monster(monster, player)
            player.health = newplayerhealth
            player.wallet = player.wallet + monster.reward
            i+=1

def main():
    play_level(level1, player1)
    shop(player1, shopvalues)
    play_level(level2, player1)
    shop(player1, shopvalues)
    play_level(level3, player1)
    shop(player1, shopvalues)
    play_level(level4, player1)
    shop(player1, shopvalues)
    play_level(level5, player1)
    shop(player1, shopvalues)
    play_level(level6, player1)
    shop(player1, shopvalues)
    play_level(level7, player1)
    shop(player1, shopvalues)
    play_level(level8, player1)
    shop(player1, shopvalues)
    play_level(level9, player1)
    shop(player1, shopvalues)
    play_level(level10, player1)
    shop(player1, shopvalues)
