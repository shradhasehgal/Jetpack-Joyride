import board
import objects
import config 

mp = board.Map()

TIME_REM = 0
TIME_BEGUN = 0
TIME_TOTAL = 120
LAST_TIME = 0
FLY_TIME = 0

mando_ground = mp.height - len(config.mando) - 1
mando = objects.Mando(config.mando, 5, mando_ground, config.lives)
config.create_dragon()
dragon = objects.Dragon(config.dragon, mp.width - 80, mando_ground - 20)


BULLET_SPEED = 0.04
BULLET_SPEED_FAST = 0.02

BOARD_SPEED = 0.1
BOARD_SPEED_FAST = 0.06

MAGNET_SPEED = 0.02

message = ""