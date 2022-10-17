
#Import Libraries Here
from time import sleep #We imported the sleep function from the time library

import random


print("\n\nwelcome to Operation Furry InfoTechCenter ")
sleep(2)
print("\nOperation Furry's Operation System Is Booting Up")

for i in range(2):
    print("Os Booting Up")
    sleep(2)


# Weather
# developer:Tate Keck
# version 1.0




"""
create a function for our current weather using the
 random. choice function to determine what the weather
is picking from a list _ using lf, elif and else statements
to check the condition and print a specific
"""




# Weather condition using the random.choice library
# to randomly choose a condition and storing it in its brain
def weather():
    WeatherForcast = ["Rain", "Snow", "Sunny", "Windy", "Foggy", "Storming", "Icy"]
    WeatherCondition = random.choice(WeatherForcast)
    return WeatherCondition
weatherAlert = weather()
print(weatherAlert)

def vrs():
    if weatherAlert == "Icy":
        print("\nVRS has changed your Alarm 30 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 30 MPH")
    elif weatherAlert == "snow":
        print("\nVRS has changed your Alarm 20 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 40 MPH")
    elif weatherAlert == "windy":
        print("\nVRS has changed your Alarm 10 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 45 MPH")
    elif weatherAlert == "foggy":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 30 MPH")
    elif weatherAlert == "storming":
        print("\nVRS has changed your Alarm 20 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 20 MPH")
    elif weatherAlert == "rain":
        print("\nVRS has changed your Alarm 10 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 30 MPH")
    else:
        print("\nVRS has changed your Alarm 1 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 100 MPH")



"""
Define a function to check our gas gauge and determine how far
 we have until we need gasoline based on an if, elif, else
 condition
"""


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

# call funcions here
vrs()
gaslevelAlert()
