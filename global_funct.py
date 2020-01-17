import config
import random
import os
import global_var
from colorama import Fore, Back, Style

def create_header():
    print("\033[2;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT + ("SCORE: " + str(global_var.mando.score()) + "   |  COINS: " + str(global_var.mando.coins()) + "   |  LIVES: " + str(global_var.mando.lives()) + "   |  TIME: " +str(global_var.TIME_REM))  .center(config.columns), end='')
    print(Style.RESET_ALL)

def print_board():
    create_header()
    global_var.mp.render()