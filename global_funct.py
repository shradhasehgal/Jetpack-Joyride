import config
import random
import os
import global_var
from colorama import Fore, Back, Style
import objects

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
    for i in range(7):
        for j in range(7):
            if global_var.mp.matrix[y+i][x+j] == "#":
                global_var.mp.matrix[y+i][x+j] = " "


def clear_boost(x, y):
    x -= 1
    y -= 1

    for i in range(7):
        for j in range(7):
            if global_var.mp.matrix[y+i][x+j] == "B":
                global_var.mp.matrix[y+i][x+j] = " "

def gravity():

    i = 1
    global_var.mando.yset(i)

    if global_var.mando.yget() >= global_var.mando_ground:
        global_var.mando.ydset(global_var.mando_ground)