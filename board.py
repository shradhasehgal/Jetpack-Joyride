
import config
import random
from colorama import init, Fore, Back, Style
import numpy as np
import global_var

class Map(object):

    height = int(config.rows) 
    width = int(config.columns*8)

    def __init__(self):
        self.start_index = 0
        self.matrix = np.array([[" " for i in range(self.width)] for j in range(self.height)])
        self.create_sky()
        self.create_ground()
        self._speed = 0.007
        self._speedup_flag = 0
        self._speedup_time = 0
        self._bullet_speed = 0.04
        self._magnet_flag = 0
        self._magnet_right = 0
        self._step = 1

    def set_speed(self, x):
        self._speed = x

    def get_speed(self):
        return self._speed

    def set_step(self, x):
        self._step = x

    def get_step(self):
        return self._step

    def get_bullet_speed(self):
        return self._bullet_speed

    def set_bullet_speed(self, x):
        self._bullet_speed = x

    def set_speedup_flag(self, x):
        self._speedup_flag = x

    def get_speedup_flag(self):
        return self._speedup_flag

    def get_speedup_time(self):
        return self._speedup_time
    
    def set_speedup_time(self, x):
        self._speedup_time = x

    def render(self):
        for y in range(3, self.height):
            pr = []
            for x in range(self.start_index, self.start_index + config.columns):
                if y == 3:
                    pr.append(Fore.LIGHTCYAN_EX + Style.BRIGHT+(self.matrix[y][x] + Style.RESET_ALL))

                elif y == self.height - 1:
                    pr.append(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+(self.matrix[y][x] + Style.RESET_ALL))
                
                elif global_var.mp.start_index <= 980 and global_var.mando.get_shield() == 1 and x >= global_var.mando.xget() and x <= global_var.mando.xget() + 2 and y >= global_var.mando.yget() and y <= global_var.mando.yget() + 2:
                    pr.append(Fore.LIGHTGREEN_EX + Style.BRIGHT +(self.matrix[y][x] + Style.RESET_ALL))
                
                # elif self.matrix[y][x] == "#":
                #     pr.append(Fore.LIGHTRED_EX + Style.BRIGHT +(self.matrix[y][x] + Style.RESET_ALL))

                # elif self.matrix[y][x] == "$":
                #     pr.append(Fore.LIGHTYELLOW_EX + Style.BRIGHT +(self.matrix[y][x] + Style.RESET_ALL))
                
                # elif self.matrix[y][x] == "B":
                #     pr.append(Fore.BLUE + Style.BRIGHT +(self.matrix[y][x] + Style.RESET_ALL))
                
                # elif self.matrix[y][x] == "M":
                #     pr.append(Fore.LIGHTCYAN_EX + Style.BRIGHT +(self.matrix[y][x] + Style.RESET_ALL))
                
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
        
    def magnet_check(self, magnets):
        self._magnet_flag = 0
        for mag in magnets:
            if mag.xget() >= global_var.mp.start_index and mag.xget() <= global_var.mp.start_index + config.columns:
                self._magnet_flag = 1
                if mag.xget() > global_var.mando.xget():
                    self._magnet_right = 1
                else:
                    self._magnet_right = 0

    
    def get_magnet_flag(self):
        return self._magnet_flag
    
    def get_magnet_right(self):
        return self._magnet_right