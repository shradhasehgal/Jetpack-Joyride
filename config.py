import os
import sys
import termios, tty, time
from colorama import init, Fore, Back, Style

columns = 150
rows = 50

lives = 5

mando = [[" ", " ", "O"], ["(", "*", "|"], [" ", "/", "\\"]]

boost = [ ["B","B"],["B","B"]]
enemy = [ 
            [ ["#", "#"], ["#","#"], ["#","#"], ["#", "#"] ], 

            [ ["#", "#","#","#"] ,["#", "#","#","#"]], 

            [
                [" ", " ", " ", "#","#"],
                [" ", " ", "#", "#", " "],
                [" ", "#", "#", " ", " "],
                ["#", "#", " ", " ", " "]
            ], 

            [
                ["#", "#", " ", " ", " "],
                [" ", "#", "#", " ", " "],
                [" ", " ", "#", "#", " "],
                [" ", " ", " ", "#", "#"]
            ],
            
        ]

magnet = [ ["M", "M", "M", "M", "M"], ["M", "M", "M", "M", "M"] ]

coins = [["$","$", "$", "$","$", "$"]]

bullet = [["-", ">"]]