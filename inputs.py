from getch import KBHit
from global_var import mando, dragon
from global_funct import remove_shield, allow_shield, move_board_back, check_speedup_time
import global_var
import global_funct
import config
from time import time
import objects

kb = KBHit()

def movedin():
    # moves the player
    char = kb.getinput()

    if char == 'd':
        if mando.xget() <= global_var.mp.start_index + config.columns - 6 and mando.xget() <= 1100:
            mando.xset(1)

    if char == 'a':
        if mando.xget() > global_var.mp.start_index + 4:
            mando.xset(-1)

    if char == 'w':
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
        global_var.bullets.append(bullet)

    if char == 'q':
        message = "Y U Quit :'("
        global_funct.display_ending(message)
        quit()