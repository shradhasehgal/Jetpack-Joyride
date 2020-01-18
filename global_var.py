import board
import objects
import config 

mp = board.Map()

TIME_REM = 0
TIME_BEGUN = 0
TIME_TOTAL = 100
LAST_TIME = 0
FLY_TIME = 0

mando = objects.Mando(config.mando, 5, mp.height - len(config.mando) - 1, config.lives)
mando_ground = mp.height - len(config.mando) - 1


BULLET_SPEED = 0.04
BULLET_SPEED_FAST = 0.02

BOARD_SPEED = 0.4
BOARD_SPEED_FAST = 0.1

MAGNET_SPEED = 0.05