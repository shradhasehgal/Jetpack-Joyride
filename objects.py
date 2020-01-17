import global_var 


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
    
    def shield_on(self):
        self._shield = 1

    def shield_off(self):
        self._shield = 0

    def get_shield(self):
        return self._shield

    def render(self):
        if self._shield == 1:
            for i in range(self._width):
                for j in range(self._height):
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]
        
        else:
            for i in range(self._width):
                for j in range(self._height):
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]

            





