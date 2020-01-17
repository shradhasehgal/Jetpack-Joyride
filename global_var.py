import board
import objects
import config 

mp = board.Map()

TIME_REM = 0
COINS = 0
SCORE = 0

mando = objects.Mando(config.mando, 0, mp.height - len(config.mando) - 1, config.lives)
