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
    milesToGasStationLow = round(random.uniform(1,25),2)
    milesToGasStationQuarterTank = round(random.uniform(26,50),1)
    if gaslevelindicater == "empty":
        print("WARNING no gas")
        sleep(1)
        print("Calling Emergency Contact")
    elif gaslevelindicater == "low":
        print("Warning")
        sleep(1)
        print("Your gas tank is extremely low, checking google Maps for the closest gas station. ")
        sleep(1)
        print("The closest gas station is ",listOfGasStations(),"which is",milesToGasStationLow,"miles away.")
    elif gaslevelindicater == "quarter Tank":
        print("WARNING")
        sleep(1)
        print("your tank is a quarter tank full cheking google for the closet gas station")
        sleep(1)
        print("the closest gas station is", listOfGasStations(), "which is", milesToGasStationQuarterTank)
    elif gaslevelindicater =="Half Tank":
        print("Your gas tank is Half Full")
        print("you still have plenty of gas")
    elif gaslevelindicater == "Three Quarter Tank":
        print("Your tank is Three Quarter Full")
        print("you still have plenty gas ")
    else:
        print("\nYour gas tank is full. Have a safe drive")



gaslevelAlert()
