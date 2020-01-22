import global_var 
import global_funct
import random
import config
import objects
from time import time, sleep
import signal
from getch import KBHit
from global_var import mando, dragon, bullets, dragon_bullets
from global_funct import remove_shield, allow_shield, move_board_back, check_speedup_time, move_with_magnet
import inputs 


global_funct.initialize_board()
# mo = objects.My_Dragon(config.create_mydragon(0), 10, 10)
# mo.render()

while True:

    global_var.TIME_REM = global_var.TIME_TOTAL - round(time()) + global_var.TIME_BEGUN
    if global_var.TIME_REM == 0:
        message = "Time over!"
        global_funct.display_ending(message)
        break


    remove_shield()
    allow_shield()
    check_speedup_time()
    mando.clear()

    inputs.movedin()
    mando.check_collision()

    global_funct.gravity(mando)
    global_funct.move_bullets(bullets)

    global_var.mp.magnet_check(global_var.magnets)

    if time() - global_var.LAST_TIME > global_var.mp.get_speed():
        global_funct.mag_reset()
        if global_var.mp.get_magnet_flag() == 1:
            move_with_magnet(mando)
        else:
            move_board_back()

        mando.check_collision()
        global_var.LAST_TIME = time()
        dragon.drag_bullets_move(dragon_bullets)
        mando.check_collision()

    dragon.clear()

    if global_var.mp.start_index >= 970:
        dragon.set_pos_to_mando(mando)      
        dragon.bullet_col(bullets)

        if time() - dragon.get_bullet_time() > dragon.get_bullet_speed():
            dragon.throw_bullet(dragon_bullets)
        
    if global_var.mp.start_index == 1000:
        mando.bullet_col(dragon_bullets)

    mando.render()
    dragon.render()
    global_funct.print_board()
        

