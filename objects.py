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
                # print(j+self._posy, i+self._posx)
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
        self._under_magnet = 0

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
    
    def inc_score(self, x):
        self._score += x
    
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

    def get_under_magnet(self):
        return self._under_magnet 
    
    def set_under_magnet(self, x):
        self._under_magnet = x

    def render(self):
        if self._shield == 1:
            for i in range(self._width):
                for j in range(self._height):
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]
        
        else:
            for i in range(self._width):
                for j in range(self._height):
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]


    def bullet_col(self, dragon_bullets):
        i = 0
        no_bullets = len(dragon_bullets)

        while i < no_bullets:
            if dragon_bullets[i].check_mando_collision() == 1:
                dragon_bullets[i].clear()
                del(dragon_bullets[i])
                no_bullets -= 1
            else:
                i += 1


    
    def check_collision(self):

        for i in range(self._width):
            for j in range(self._height):
                
                if global_var.mp.matrix[j+self._posy][i+self._posx] == "$":
                    self._coins += 1
                    self._score += 1
                    global_var.mp.matrix[j+self._posy][i+self._posx] = " "

                elif global_var.mp.matrix[j+self._posy][i+self._posx] == "#" or global_var.mp.matrix[j+self._posy][i+self._posx] == "M" or global_var.mp.matrix[j+self._posy][i+self._posx] == "o": 
                    if self._shield == 1:
                        global_funct.clear_beam(self._posx, self._posy)
                        self._score += 5

                    elif self._lives > 1:
                        self._lives -= 1

                        if global_var.mp.start_index != 1000:
                            global_var.mp.start_index = 0
                            self._posx = 5
                            self._posy = global_var.mando_ground
                        else:
                            self._posx = global_var.mp.start_index + 5
                            self._posy = 5
                            return


                    else:
                        message = "Oops, you lost!"
                        global_funct.display_ending(message)
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
                if global_var.mp.start_index < 1000:
                    if global_var.mp.matrix[j+self._posy][i+self._posx] == " ":
                        global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]
                
                else:
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
                    global_var.mando.inc_score(5)

    
    def check_drag_collision(self):
        flag = 1
        for i in range(len(config.dragon[0])):
            for j in range(len(config.dragon)):
                if j + global_var.dragon.yget() == self._posy:
                    if i + global_var.dragon.xget() == self._posx or i + global_var.dragon.xget() == self._posx + 1:
                        global_var.dragon.collision()
                        flag = 0

        if flag == 0:
            return 1 



class Dragon(Object):

    def __init__(self, character ,x, y):
        super().__init__(character, x, y)
        self._bullet_speed = 3
        self._lives = 5
        self._bullet_time = 0

    def get_lives(self):
        return self._lives
    
    def get_bullet_speed(self):
        return self._bullet_speed
    
    def get_bullet_time(self):
        return self._bullet_time 
    
    def set_bullet_time(self, x):
        self._bullet_time = x
        
    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                if global_var.mp.matrix[j+self._posy][i+self._posx] == " ":
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self._posy][i+self._posx] = " "
    
    def print_lives(self):
        i = 10 - 2*self._lives        
        while i > 0:
            self._shape[0][17-i] = " "
            i -= 1


    def collision(self):
        self._lives -= 1
        self.print_lives()

    def drag_bullets_move(self, dragon_bullets):
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

        
    def bullet_col(self, bullets):
        i = 0
        no_bullets = len(bullets)

        while i < no_bullets:
            if bullets[i].check_drag_collision() == 1:
                bullets[i].clear()
                del(bullets[i])
                no_bullets -= 1
            else:
                i += 1

class Dragon_Bullet(Object):

    def __init__(self, character ,x, y):
        super().__init__(character, x, y)   
        self._foo = 0
    
    def check_mando_collision(self):
        for i in range(len(config.mando[0])):
            if self._foo == 1:
                break
            for j in range(len(config.mando)):  
                if global_var.mando.yget()+j == self._posy and global_var.mando.xget()+i == self._posx:
                    global_var.mando.red_lives()
                    if global_var.mando.lives() == 0:
                        message = "Ded"
                        global_funct.display_ending(message)
                        quit()
                    # global_var.mando.ydset(40)
                    global_var.mando.xdset(global_var.mp.start_index + 5)
                    self._foo = 1
                    break                

        return self ._foo