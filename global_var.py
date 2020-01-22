import board
import objects
import config 

mp = board.Map()

TIME_REM = 0
TIME_BEGUN = 0
TIME_TOTAL = 150
LAST_TIME = 0
FLY_TIME = 0

mando_ground = mp.height - len(config.mando) - 1
mando = objects.Mando(config.mando, 5, mando_ground, config.lives)
config.create_dragon()
dragon = objects.Dragon(config.dragon, mp.width - 80, mando_ground - 20)


BULLET_SPEED = 0.04
BULLET_SPEED_FAST = 0.01

BOARD_SPEED = 0.1
BOARD_SPEED_FAST = 0.05

MAGNET_SPEED = 0.02

message = ""
magnet_flag = 0

bullets = []
beams = []
magnets = []
coins = []
boosts = []
dragon_bullets = []
dg_power_up = []

BULLET_TIME = 0