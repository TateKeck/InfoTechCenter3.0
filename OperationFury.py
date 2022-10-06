# Weather
# developer:Tate Keck
# version 1.0

"""
create a function for our current weather using the
 random. choice function to determine what the weather
is picking from a list _ using lf, elif and else statements
to check the condition and print a specific
"""


# Import Libraries here
import random

# Weather condition using the random.choice library
# to randomly choose a condition and storing it in its brain
def weather():
    WeatherForcast = ["Rain", "Snow", "Sunny", "Cloudy", "Foggy", "Storming", "Icy"]
    WeatherCondition = random.choice(WeatherForcast)
    return WeatherCondition

