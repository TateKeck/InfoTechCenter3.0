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
    gasslevellist=["empty","low","quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentgaslevel = random.choice(gasslevellist)
    return currentgaslevel

# variable calling the gaslevelgague funcuion to store value once
gaslevelindicater = gaslevelgauge()
def listOfGasStations():
    gasStation = ["Shell","Circle K","Marathon","Speedway","Meijer"]
    gasStationNearby = random.choice(gasStation)
    return gasStationNearby
def gaslevelAlert():
    milesToGasStation = round(random.uniform(1,24),2)
    if gaslevelindicater == "empty":
        print("WARNING no gas")
        sleep(1)
        print("Calling Emergency Contact")
    elif gaslevelindicater == "low":
        print("Warning")
        sleep(1)
        print("Your gas tank is extremely low, checking google Maps for the closest gas station. ")
        sleep(1)
        print("The closest gas station is ",listOfGasStations(),"which is",milesToGasStation,"miles away.")





gaslevelAlert()
