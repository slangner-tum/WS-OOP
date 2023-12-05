import random


class Tire:
    # declaration - not necessary
    __width = None
    __air_Pressure = None

    # constructor
    def __init__(self, width=22.5):
        self.__width = width
        self.__air_Pressure = 2.5

    # destructor
    def __del__(self):
        self.__air_Pressure = 0
        print(f"This is a flat tire")

    # getter methods
    def get_width(self):
        return self.__width

    def get_air_pressure(self):
        return self.__air_Pressure

    # other methods
    def check_air_pressure(self):
        if random.randint(0, 20) == 0:
            self.__air_Pressure = 0

        if self.__air_Pressure == 0:
            print("I'm flat, please inflate me.")
        return self.__air_Pressure

    def inflate_tire(self):
        self.__air_Pressure = 2.5
