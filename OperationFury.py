
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


vrs()