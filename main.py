import global_var 
import global_funct
import random
import config
import objects
from time import time 
from getch import _getChUnix as getChar
from alarmexception import AlarmException
import signal

global_funct.create_board()
global_var.mando.render()
global_funct.print_board()

global_var.LAST_TIME = time()
global_var.TIME_BEGUN = round(global_var.LAST_TIME)


def movedin():
    # moves the player

    def alarmhandler(signum, frame):
        # ''' input method '''
        raise AlarmException

    def user_input(timeout=0.15):
        # ''' input method '''
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    char = user_input()

    if char == 'd':
        print("d")

    if char == 'a':
        print("a")

    if char == 'w':
        print("w")

    if char == ' ' and global_var.shield_allow == 1:
        print("whee")
    
    if char == 'e':
        print("bulle")
        
    if char == 'q':
    	quit()

while True:

    global_var.TIME_REM = global_var.TIME_TOTAL - round(time()) + global_var.TIME_BEGUN

    if global_var.TIME_REM == 0:
        print("Time over!")
        break
    
    # if time() - global_var.LAST_TIME > 0.04:
    # global_var.mp.start_index += 1
    # global_funct.print_board()
    # global_var.LAST_TIME = time()
