import global_var 
import global_funct
import random
import config
import objects
from time import time 
import signal
from getch import KBHit

kb = KBHit()

global_funct.create_board()
global_var.mando.render()
global_funct.print_board()

global_var.LAST_TIME = time()
global_var.TIME_BEGUN = round(global_var.LAST_TIME)

bullets = []

def remove_shield():
    if global_var.mando.get_shield() == 1 and time() - global_var.mando.get_shield_time() > 10:
        global_var.mando.set_shield(0)

def allow_shield():
    if global_var.mando.get_shield_allow() == 0 and time() - global_var.mando.get_shield_time() > 70:
        global_var.mando.set_shield_allow(1)

def move_board_back():
    global_var.mp.start_index += 1
    global_var.mando.xset(1)

def check_speedup_time():

    if global_var.mp.get_speedup_flag() == 1 and time() - global_var.mp.get_speedup_time() > 10:
        # print("happy")
        # print(global_var.mp.get_speedup_time())
        # print(time())
        global_var.mp.set_speedup_flag(0)
        global_var.mp.set_speed(0.06)

def movedin():
    # moves the player

    char = kb.getinput()

    if char == 'd':
        if global_var.mando.xget() <= global_var.mp.start_index + config.columns - 6:
            global_var.mando.xset(1)

    if char == 'a':
        if global_var.mando.xget() >= global_var.mp.start_index + 4:
            global_var.mando.xset(-1)

    if char == 'w':
        if global_var.mando.yget() >= 5:
            global_var.mando.yset(-1)

    if char == ' ' and global_var.mando.get_shield_allow() == 1:
        global_var.mando.set_shield_allow(0)
        global_var.mando.set_shield_time(time())
        global_var.mando.set_shield(1)

    if char == 'e':
        bullet = objects.Object(config.bullet, global_var.mando.xget(), global_var.mando.yget())
        bullets.append(bullet)
        bullet.render()

    if char == 'q':
        print("Don't quit :(")
        quit()



while True:

    global_var.TIME_REM = global_var.TIME_TOTAL - round(time()) + global_var.TIME_BEGUN

    if global_var.TIME_REM == 0:
        print("Time over!")
        break

    remove_shield()
    allow_shield()
    check_speedup_time()
    global_var.mando.clear()
    movedin()
    global_var.mando.check_collision()

    if time() - global_var.LAST_TIME > global_var.mp.get_speed():
        move_board_back()
        global_var.LAST_TIME = time()
        global_var.mando.check_collision()
    
    global_var.mando.render()
    global_funct.print_board()
