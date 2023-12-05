import Tire
from Tire import Tire


class Wheel:
    # declaration - not necessary
    __diameter = None
    __tire = None

    # constructor
    def __init__(self, diameter):
        self.__diameter = diameter
        self.__tire = Tire()

    # destructor - not necessary

    # getter methods
    def get_diameter(self):
        return self.__diameter

    def get_tire(self):
        return self.__tire
