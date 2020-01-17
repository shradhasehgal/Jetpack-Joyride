import config
import random
from colorama import init, Fore, Back, Style
import numpy as np
import global_var

class Map(object):

    height = int(config.rows) 
    width = int(config.columns*10)

    def __init__(self):
        self.start_index = 0
        self.matrix = np.array([[" " for i in range(self.width)] for j in range(self.height)])
        self.create_sky()
        self.create_ground()

    def render(self):
        for y in range(3, self.height):
            pr = []
            for x in range(self.start_index, self.start_index + config.columns):
                if global_var.mando.get_shield() == 1 and x >= global_var.mando.xget() and x <= global_var.mando.xget() + 2 and y >= global_var.mando.yget() and y <= global_var.mando.yget() + 2:
                    pr.append("\033[1;32;40m"+(self.matrix[y][x] + Style.RESET_ALL))
                else:
                    pr.append(self.matrix[y][x] + Style.RESET_ALL)
            print(''.join(pr))

    def create_ground(self):
        y = self.height - 1
        for x in range(self.width):
            self.matrix[y][x] = "T"


    def create_sky(self): 
        for x in range(self.width):
            self.matrix[3][x] = "X"
        
