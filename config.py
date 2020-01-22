import os
import sys
import termios, tty, time
from colorama import init, Fore, Back, Style
# import objects
from math import pi
import numpy as np 

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

magnet = [ ["M", "M", "M", "M"], ["M", "M", "M", "M"] ]

dg_pow_up = [ ["D", "D"], ["D", "D"] ]
# magnet = [ ["M"], ["M"], ["M"]]


coins = [["$","$", "$", "$","$", "$"]]

bullet = [["-", ">"]]

# g = """             
# /     \\
#                    ((     ))
#                ===  \\\_v_//  ===
#                  ====)_^_(====
#                  ===/ O O \===
#                  = | /_ _\ | =
#                 =   \/_ _\/   =
#                      \_ _/
#                      (o_o) """

g = """      [||||||||||]        
                           
         /\_/\\            
     /\  |6 6|  /\\          
    /  \ \<">/ /  \\          
   / ,__`~)-(~___, \\           
  /.',-'`/_/`'-,  '.\\           
   ,'    \_\    ',              
  :       \|\     ;             
   ',     /|/    ,'             
    '-,__ \W\_,-))                
               ((                 
                )                  
                """
dragon = []

def create_dragon():
  arr = []
  for i in g:
    if i != '\n':
      arr.append(i)
    else:
      dragon.append(arr)
      arr = []


def create_mydragon(phase):
  my_dragon = []
  height = 8
  base = -pi
  for i in range(30):
      my_dragon.append(base + phase*pi/8)
      base += 2*pi/30

  my_dragon = np.sin(my_dragon)
  my = [0 for i in range(30)]

  for i in range(30):
    my[i] = int(my_dragon[i]* (height/2))

  mando_dragon = []
  for i in range(height+2):
    p = []
    for j in range(30):
      p.append(' ')

    mando_dragon.append(p)

  for i in range(27):
    mando_dragon[my[i]+4][i] = "~"
  
  mando_dragon[my[26]+4][26] = "@"
  mando_dragon[my[27]+4][27] = ">"
  mando_dragon[my[28]+4][28] = ">"
  mando_dragon[my[29]+4][29] = ">"

  return mando_dragon