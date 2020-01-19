import global_var 
import global_funct
import random
import config
import objects
from time import time, sleep
import signal
from getch import KBHit
from global_var import mando, dragon
from global_funct import remove_shield, allow_shield, move_board_back, gravity

kb = KBHit()

global_funct.create_board()
mando.render()
dragon.render()
global_funct.print_board()

global_var.LAST_TIME = time()
global_var.TIME_BEGUN = round(global_var.LAST_TIME)

bullets = []
dragon_bullets = []

magnet_flag = 0
magnet_up = 0
po = 0
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

    if char == 'w' and magnet_flag == 0:
        if mando.yget() >= 5:
            mando.yset(-1)
            mando.set_air_pos(mando.yget())
            mando.set_air_time(time())

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

def drag_bullets_move():
    i = 0
    no_bullets = len(dragon_bullets)

    while i < no_bullets:
        dragon_bullets[i].clear()
        if dragon_bullets[i].xget() >= global_var.mp.start_index:
            dragon_bullets[i].xset(-1)
            i += 1

        else:
            del(dragon_bullets[i])
            no_bullets -=1
    
    i = 0
    while i < no_bullets:
        dragon_bullets[i].render()
        i += 1

def bullet_dragon_col():
    i = 0
    no_bullets = len(bullets)

    while i < no_bullets:
        if bullets[i].check_drag_collision() == 1:
            bullets[i].clear()
            del(bullets[i])
            no_bullets -= 1
        else:
            i += 1


def bullet_mando_col():
    i = 0
    no_bullets = len(dragon_bullets)

    while i < no_bullets:
        if dragon_bullets[i].check_mando_collision() == 1:
            dragon_bullets[i].clear()
            del(dragon_bullets[i])
            no_bullets -= 1
        else:
            i += 1




    
bullet_time = time()
mag_time = time()
config.create_dragon() 
f = 1

while True:

    global_var.TIME_REM = global_var.TIME_TOTAL - round(time()) + global_var.TIME_BEGUN
    if global_var.TIME_REM == 0:
        print("Time over!")
        break

    # print(global_var.mp.start_index)
    remove_shield()
    allow_shield()
    check_speedup_time()
    mando.clear()


    magnet_flag = 0
    for mag in global_funct.magnets:
        if mando.xget() >= mag.xget()-5 and mando.xget() <= mag.xget() + 5:
            magnet_flag = 1
            if mag.yget() < mando.yget():
                magnet_up = 1
            else:
                magnet_up = 0
             

    if magnet_flag == 1 and time() - mag_time > global_var.MAGNET_SPEED:
        mag_time = time()
        if magnet_up == 1:
            if mando.yget() >= 5:
                mando.yset(-1)

        else:
            mando.yset(1)

    mando.check_collision()

    movedin()
    mando.check_collision()
    # mando.check_magnet()


    if magnet_flag == 0 and mando.yget() < global_var.mando_ground:
        t = time() - mando.get_air_time()
        posn = int(mando.get_air_pos() + 5*t*t)
        if posn > global_var.mando_ground:
            posn = global_var.mando_ground

        mando.ydset(posn)
        mando.check_collision()

    if time() - bullet_time > global_var.mp.get_bullet_speed():
        # print(global_var.mp.get_bullet_speed())
        bullets_move()
        bullet_time = time()


    if time() - global_var.LAST_TIME > global_var.mp.get_speed():
        # print(global_var.mp.get_speed())
        move_board_back()
        global_var.LAST_TIME = time()
        drag_bullets_move()
        mando.check_collision()

    # dragon.check_collision()
    dragon.clear()
    if global_var.mp.start_index >= 970:
        if mando.yget() <= 36:
            dragon.ydset(mando.yget())
        else:
            dragon.ydset(36)        
        bullet_dragon_col()

        if time() - dragon.get_bullet_time() > dragon.get_bullet_speed():

            drag_bullet = objects.Dragon_Bullet(["o"],dragon.xget() -1, dragon.yget()+3)
            drag_bullet.render()
            dragon_bullets.append(drag_bullet)
            dragon.set_bullet_time(time())
            # drag_bullets_move()
        
    if global_var.mp.start_index == 1000:
        bullet_mando_col()

    mando.render()
    dragon.render()
    global_funct.print_board()
        
    if dragon.get_lives() == 0:
        print("You won!")
        quit()
