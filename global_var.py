import board
import objects
import config 

mp = board.Map()

TIME_REM = 0
TIME_BEGUN = 0
TIME_TOTAL = 100
LAST_TIME = 0

mando = objects.Mando(config.mando, 0, mp.height - len(config.mando) - 1, config.lives)
