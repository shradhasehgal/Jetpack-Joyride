import global_var 
import global_funct
import random
import config
import objects
from time import time, sleep
import signal
from getch import KBHit
from global_var import mando
from global_funct import remove_shield, allow_shield, move_board_back, gravity

kb = KBHit()

global_funct.create_board()
mando.render()
global_funct.print_board()

global_var.LAST_TIME = time()
global_var.TIME_BEGUN = round(global_var.LAST_TIME)

bullets = []

def check_speedup_time():

    if global_var.mp.get_speedup_flag() == 1 and time() - global_var.mp.get_speedup_time() > 10:
        global_var.mp.set_speedup_flag(0)
        global_var.mp.set_speed(global_var.BOARD_SPEED)
        global_var.mp.set_bullet_speed(global_var.BULLET_SPEED)

def movedin():
    # moves the player
    char = kb.getinput()

    if char == 'd':
        if mando.xget() <= global_var.mp.start_index + config.columns - 6:
            mando.xset(1)

    if char == 'a':
        if mando.xget() > global_var.mp.start_index + 4:
            mando.xset(-1)

    if char == 'w':
        if mando.yget() >= 5:
            mando.yset(-1)
            mando.set_air_pos(mando.yget())
            mando.set_air_time(time())
            # mando.set_fall_speed(0)
            # mando.yset(-1)
            # global_var.FLY_TIME = time()

    if char == ' ' and mando.get_shield_allow() == 1:
        mando.set_shield_allow(0)
        mando.set_shield_time(time())
        mando.set_shield(1)

    if char == 'e':
        bullet = objects.Bullet(config.bullet, mando.xget() + 4, mando.yget()+1)
        bullet.render()
        bullets.append(bullet)

    if char == 'q':
        print("Don't quit :(")
        quit()

def bullets_move():
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

bullet_time = time()
while True:

    global_var.TIME_REM = global_var.TIME_TOTAL - round(time()) + global_var.TIME_BEGUN

    if global_var.TIME_REM == 0:
        print("Time over!")
        break

    remove_shield()
    allow_shield()
    check_speedup_time()
    mando.clear()
    movedin()
    mando.check_collision()

    if mando.yget() < global_var.mando_ground:

        t = time() - mando.get_air_time()
        posn = int(mando.get_air_pos() + 5*t*t)
        if posn > global_var.mando_ground:
            posn = global_var.mando_ground

        mando.ydset(posn)

    if time() - bullet_time > global_var.mp.get_bullet_speed():
        print(global_var.mp.get_bullet_speed())
        bullets_move()
        bullet_time = time()

    if time() - global_var.LAST_TIME > global_var.mp.get_speed():
        print(global_var.mp.get_speed())
        move_board_back()
        global_var.LAST_TIME = time()
        mando.check_collision()
    
    mando.render()
    global_funct.print_board()
