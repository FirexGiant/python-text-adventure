from os import name
from os import system 
def clearScreen():
    if name == "nt":
        system("cls")
    else:
        system("clear") 

from time import sleep
from keyboard import is_pressed
from keyboard import wait
def typeout(string, delay = 0.035, newline = True, pauseOnPeriod = False):
    for char in string:
        print(char, end='', flush=True)
        if is_pressed('space'):
            # Quickly write out the rest of the string 
            delay = 0
            pauseOnPeriod = False 
        elif char == '.' and pauseOnPeriod:
            wait('space')
        sleep(delay)
    print()

from World import World
world = World()

