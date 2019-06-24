from time import sleep
from keyboard import is_pressed
from keyboard import wait

marks = (".", "!", "?")

def typeout(string, delay = 0.035, newline = True, pauseDelay = 1.35):
    for char in string:
        print(char, end='', flush=True)
        if is_pressed('space'):
            delay = 0
            pauseDelay = 0
        elif char in marks:
            sleep(pauseDelay)
        sleep(delay)
    if newline:
        print()
