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

def display_ending(message):
    os.system('tput reset')
    print(Fore.CYAN + Style.BRIGHT + "FINAL STANDINGS:".center(config.columns))
    print(Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + ("SCORE: " + str(global_var.mando.score())).center(config.columns))
    print(Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + ("LIVES: " + str(global_var.mando.lives())).center(config.columns))
    print(Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + (message).center(config.columns))
    print(Style.RESET_ALL)
    return

def create_board():

    i = 1
    x = 10

    
    while x < global_var.mp.width - 250:

        no = random.randint(0, 3)
        y = random.randint(10, global_var.mp.height-15)
        
        #beams
        enemy = objects.Object(config.enemy[no], x, y)
        global_var.beams.append(enemy)
        enemy.render()
        
        #magnets
        if i % 3 == 0:
            magnet = objects.Object(config.magnet, x + 10 , y)
            global_var.magnets.append(magnet)
            magnet.render()
        
        i += 1
        x += random.randint(20, 30)
        if x > global_var.mp.width - 250:
            break
            
        y = random.randint(10, global_var.mp.height-15)

        #coins
        coin = objects.Object(config.coins, x, y)
        global_var.coins.append(coin)
        coin.render()


        x += random.randint(20, 30)
        y = random.randint(10, global_var.mp.height-15)
        
        #boost
        boost = objects.Object(config.boost, x, y)
        global_var.boosts.append(boost)
        boost.render()

        x += random.randint(20, 50)

def initialize_board():

    create_board()
    global_var.mando.render()
    global_var.mando.render()
    print_board()
    global_var.LAST_TIME = time()
    global_var.TIME_BEGUN = round(global_var.LAST_TIME)
    global_var.BULLET_TIME = global_var.LAST_TIME
    config.create_dragon() 


        
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

    for i in range(5):
        for j in range(5):
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
    if global_var.mp.start_index < global_var.mp.width - 200:
        global_var.mp.start_index += 1  
        global_var.mando.xset(1)

def check_speedup_time():
    if global_var.mp.get_speedup_flag() == 1 and time() - global_var.mp.get_speedup_time() > 10:
        global_var.mp.set_speedup_flag(0)
        global_var.mp.set_speed(global_var.BOARD_SPEED)
        global_var.mp.set_bullet_speed(global_var.BULLET_SPEED)



def bullets_move(bullets):
    i = 0
    no_bullets = len(bullets)

    while i < no_bullets:
        bullets[i].clear()
        if bullets[i].xget() < global_var.mp.start_index + config.columns:
            bullets[i].xset(2)
            bullets[i].check_collision()
            i += 1

        else:
            del(bullets[i])
            no_bullets -=1
    
    i = 0
    while i < no_bullets:
        bullets[i].render()
        i += 1

def gravity(mando):
    
    if mando.yget() < global_var.mando_ground:
        t = time() - mando.get_air_time()
        posn = int(mando.get_air_pos() + 5*t*t)
        if posn > global_var.mando_ground:
            posn = global_var.mando_ground

        mando.ydset(posn)
        mando.check_collision()

def move_bullets(bullets):
    if time() - global_var.BULLET_TIME > global_var.mp.get_bullet_speed():
        bullets_move(bullets)
        global_var.BULLET_TIME = time()

def move_with_magnet(mando):

    if global_var.mp.get_magnet_right() == 1:
        if mando.xget() < global_var.mp.start_index + config.columns - 5:
            mando.xset(2)
        
    elif mando.xget() < global_var.mp.start_index + 5:
        mando.xset(1)
        
    global_var.mp.start_index += 1