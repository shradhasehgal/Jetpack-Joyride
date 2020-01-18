import global_var 
import global_funct
import config
from time import time,sleep

class Object():
    
    def __init__(self, character, x, y):
        self._posx = x
        self._posy = y
        self._width = len(character[0])
        self._height = len(character)
        self._shape = character

    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]

    def xget(self):
        return self._posx

    def yget(self):
        return self._posy
    
    def xdset(self, x):
        self._posx = x
    
    def ydset(self, x):
        self._posy = x

    def xset(self, x):
        self._posx += x
    
    def yset(self, x):
        self._posy += x

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self._posy][i+self._posx] = " "




class Mando(Object):

    def __init__(self, character ,x, y, lives):
        super().__init__(character, x, y)
        self._lives = 5
        self._coins = 0
        self._score = 0
        self._shield = 0
        self._shield_allow = 1
        self._shield_time = 0
        self._fall_speed = 0
        self ._air_time = 0
        self._air_pos = 0

    # def xset(self, x):
    #     self._posx += x

    # def yset(self, x):
    #     self._posy += x

    def lives(self):
        return self._lives

    def coins(self):
        return self._coins
    
    def score(self):
        return self._score

    def red_lives(self):
        self._lives -= 1
    
    def inc_coins(self):
        self._coins += 1
    
    def inc_score(self):
        self._score += 1
    
    def set_shield(self, x):
        self._shield = x

    def get_shield(self):
        return self._shield
    
    def set_shield_allow(self, x):
        self._shield_allow = x

    def get_shield_allow(self):
        return self._shield_allow

    def get_shield_time(self):
        return self._shield_time

    def set_shield_time(self, x):    
        self._shield_time = x
    
    def get_fall_speed(self):
        return self._fall_speed 

    def inc_fall_speed(self):
        self._fall_speed += 1

    def set_fall_speed(self, x):
        self._fall_speed = x
    
    def get_air_time(self):
        return self._air_time

    def set_air_time(self, x):
        self._air_time = x

    def get_air_pos(self):
        return self._air_pos

    def set_air_pos(self, x):
        self._air_pos = x

    def render(self):
        if self._shield == 1:
            for i in range(self._width):
                for j in range(self._height):
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]
        
        else:
            for i in range(self._width):
                for j in range(self._height):
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]

    
    def check_collision(self):
        
        for i in range(self._width):
                for j in range(self._height):
                    
                    if global_var.mp.matrix[j+self._posy][i+self._posx] == "$":
                        self._coins += 1
                        global_var.mp.matrix[j+self._posy][i+self._posx] = " "

                    elif global_var.mp.matrix[j+self._posy][i+self._posx] == "#" or global_var.mp.matrix[j+self._posy][i+self._posx] == "M":
                        
                        if self._lives > 1:
                            self._lives -= 1
                            global_var.mp.start_index = 0
                            self._posx = 5
                            self._posy = global_var.mp.height - len(config.mando) - 1

                        else:
                            print("Oops, you lost!")
                            quit()                

                    elif global_var.mp.matrix[j+self._posy][i+self._posx] == "B":
                        global_funct.clear_boost(self._posx, self._posy)
                        global_var.mp.set_speedup_time(time())
                        global_var.mp.set_speedup_flag(1)
                        global_var.mp.set_speed(global_var.BOARD_SPEED_FAST)
                        global_var.mp.set_bullet_speed(global_var.BULLET_SPEED_FAST)


                    

class Bullet(Object):

    def __init__(self, character ,x, y):
        super().__init__(character, x, y)

    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                if global_var.mp.matrix[j+self._posy][i+self._posx] == " ":
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                if global_var.mp.matrix[j+self._posy][i+self._posx] == "-" or global_var.mp.matrix[j+self._posy][i+self._posx] == ">":
                    global_var.mp.matrix[j+self._posy][i+self._posx] = " "
    
    def check_collision(self):
        for i in range(self._width):
                for j in range(self._height):    
                    if global_var.mp.matrix[j+self._posy][i+self._posx] == "#":
                        global_funct.clear_beam(self._posx, self._posy)