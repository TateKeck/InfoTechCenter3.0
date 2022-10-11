# Gass
# Programer: Tate keck
# Version 1.0

"""
Define a function to check our gas gauge and determine how far
 we have until we need gasoline based on an if, elif, else
 condition
"""

# import library here
import random
from time import sleep
# gas level funcion

def gaslevelgauge():
    gasslevellist=["empty","Low","quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentgaslevel = random.choice(gasslevellist)
    return currentgaslevel

# variable calling the gaslevelgague funcuion to store value once
gaslevelindicater = gaslevelgauge()

def gaslevelAlert():
    if gaslevelindicater == "empty":
        print("WARNIG no gas")
        sleep(1)
        print("Calling Emergency Contact")



gaslevelAlert()
