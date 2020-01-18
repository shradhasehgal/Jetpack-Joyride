import config
import random
import os
import global_var
from colorama import Fore, Back, Style
import objects
from time import time

def create_header():
    print("\033[2;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT + ("SCORE: " + str(global_var.mando.score()) + "   |  COINS: " + str(global_var.mando.coins()) + "   |  LIVES: " + str(global_var.mando.lives()) + "   |  TIME: " +str(global_var.TIME_REM))  .center(config.columns), end='')
    print(Style.RESET_ALL)

def print_board():
    create_header()
    global_var.mp.render()



bullets = []
beams = []
magnets = []
coins = []
boosts = []

def create_board():

    i = 1
    x = 10
    
    while x < global_var.mp.width - 200:

        no = random.randint(0, 3)
        y = random.randint(10, global_var.mp.height-15)
        
        #beams
        enemy = objects.Object(config.enemy[no], x, y)
        beams.append(enemy)
        enemy.render()
        
        #magnets
        if i % 10 == 0:
            magnet = objects.Object(config.magnet, x + 10 , y)
            magnets.append(magnet)
            magnet.render()
        
        i += 1
        x += random.randint(20, 30)
        y = random.randint(10, global_var.mp.height-15)

        #coins
        coin = objects.Object(config.coins, x, y)
        coins.append(coin)
        coin.render()


        x += random.randint(20, 30)
        y = random.randint(10, global_var.mp.height-15)
        
        #boost
        boost = objects.Object(config.boost, x, y)
        boosts.append(boost)
        boost.render()

        x += random.randint(20, 50)

        
def clear_beam(x, y):
    x -= 3 
    y -= 3
    for i in range(9):
        for j in range(9):
            if global_var.mp.matrix[y+i][x+j] == "#":
                global_var.mp.matrix[y+i][x+j] = " "


def clear_boost(x, y):
    x -= 1
    y -= 1

    for i in range(3):
        for j in range(3):
            if global_var.mp.matrix[y+i][x+j] == "B":
                global_var.mp.matrix[y+i][x+j] = " "


def clear_magnet(x, y):
    x -= 5
    y -= 2

    for i in range(6):
        for j in range(2):
            if global_var.mp.matrix[y+i][x+j] == "M":
                global_var.mp.matrix[y+i][x+j] = " "


def remove_shield():
    if global_var.mando.get_shield() == 1 and time() - global_var.mando.get_shield_time() > 10:
        global_var.mando.set_shield(0)

def allow_shield():
    if global_var.mando.get_shield_allow() == 0 and time() - global_var.mando.get_shield_time() > 70:
        global_var.mando.set_shield_allow(1)

def move_board_back():
    global_var.mp.start_index += 1
    global_var.mando.xset(1)

def gravity():

    global_var.mando.yset(global_var.mando.get_fall_speed())
    print(global_var.mando.get_fall_speed())
    if global_var.mando.yget() > global_var.mando_ground:
        global_var.mando.ydset(global_var.mando_ground)
    global_var.mando.inc_fall_speed()