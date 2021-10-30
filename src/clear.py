from os import system
from os import name as osname

def clear():
    if osname == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
