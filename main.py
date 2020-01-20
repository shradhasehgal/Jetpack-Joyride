import global_var 
import global_funct
import random
import config
import objects
from time import time, sleep
import signal
from getch import KBHit
from global_var import mando, dragon
from global_funct import remove_shield, allow_shield, move_board_back, check_speedup_time, dragon_bullets, bullets
import inputs 


global_funct.initialize_board()
global_var.LAST_TIME = time()
global_var.TIME_BEGUN = round(global_var.LAST_TIME)



    
bullet_time = time()
mag_time = time()
config.create_dragon() 
f = 1

while True:

    global_var.TIME_REM = global_var.TIME_TOTAL - round(time()) + global_var.TIME_BEGUN
    if global_var.TIME_REM == 0:
        print("Time over!")
        break

    remove_shield()
    allow_shield()
    check_speedup_time()
    mando.clear()

    inputs.movedin()
    mando.check_collision()

    global_var.magnet_flag = 0
    magnet_right = 0
    for mag in global_funct.magnets:
        if mag.xget() >= global_var.mp.start_index and mag.xget() <= global_var.mp.start_index + config.columns:
            global_var.magnet_flag = 1
            if mag.xget() > mando.xget():
                magnet_right = 1
            else:
                magnet_right = 0


    if mando.yget() < global_var.mando_ground:
        t = time() - mando.get_air_time()
        posn = int(mando.get_air_pos() + 5*t*t)
        if posn > global_var.mando_ground:
            posn = global_var.mando_ground

        mando.ydset(posn)
        mando.check_collision()

    if time() - bullet_time > global_var.mp.get_bullet_speed():
        global_funct.bullets_move(bullets)
        bullet_time = time()


    if time() - global_var.LAST_TIME > global_var.mp.get_speed():
        if global_var.magnet_flag == 1:
            print("wheee")
            if magnet_right == 1:
                if mando.xget() < global_var.mp.start_index + config.columns - 5:
                    mando.xset(2)

            global_var.mp.start_index += 1
        else:
            move_board_back(global_var.magnet_flag)
        global_var.LAST_TIME = time()
        dragon.drag_bullets_move(dragon_bullets)
        mando.check_collision()

    dragon.clear()
    if global_var.mp.start_index >= 970:
        if mando.yget() <= 36:
            dragon.ydset(mando.yget())
        else:
            dragon.ydset(36)        
        dragon.bullet_col(bullets)

        if time() - dragon.get_bullet_time() > dragon.get_bullet_speed():

            drag_bullet = objects.Dragon_Bullet(["o"],dragon.xget() -1, dragon.yget()+3)
            drag_bullet.render()
            dragon_bullets.append(drag_bullet)
            dragon.set_bullet_time(time())
        
    if global_var.mp.start_index == 1000:
        mando.bullet_col(dragon_bullets)

    mando.render()
    dragon.render()
    global_funct.print_board()
        
    if dragon.get_lives() == 0:
        message = "You won!"
        global_funct.display_ending(message)
        quit()
