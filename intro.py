from colorama import Fore
import time
def intro(text, delay=0.003):
    print(Fore.RED, end='')
    for char in text:
        print(char, end='')
        time.sleep(delay)
    print(Fore.RESET, end="")