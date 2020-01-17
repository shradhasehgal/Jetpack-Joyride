import global_var 
import global_funct
import random
import config
import objects
from time import time 

global_funct.create_board()
global_funct.print_board()

global_var.LAST_TIME = time()
global_var.TIME_BEGUN = round(global_var.LAST_TIME)

while True:

    global_var.TIME_REM = global_var.TIME_TOTAL - round(time()) + global_var.TIME_BEGUN

    if global_var.TIME_REM == 0:
        print("Time over!")
        break
    
    # if time() - global_var.LAST_TIME > 0.04:
    global_var.mp.start_index += 1
    global_funct.print_board()
    global_var.LAST_TIME = time()