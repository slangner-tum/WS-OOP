import random
import time
from enum import Enum


class _CarStatus(Enum):
    STOPPED = 0
    STARTED = 1
    DRIVING = 2


class _Weather(Enum):
    CLEAR = 0
    RAIN = 1
    SNOW = 2


def example_function(param1, param2, param3=0):
    # code section
    result = param1 * param2 + param3  # calculating

    # return section
    return result


class Car:
    # Declaration - not necessary
    brand = None
    model = None
    color = None
    year = None
    performance = None
    fuel_type = None
    mileage = None
    status = None
    __fuel_level = None

    # Constructor
    def __init__(self, brand, model, color, year, performance, fuel_type):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.performance = performance
        self.fuel_type = fuel_type
        self.mileage = 0
        self.status = _CarStatus.STOPPED
        self.__fuel_level = 100
        print(f"\n"
              f"Congratulations to your new car. "
              f"It's a {self.color.lower()} {self.brand} {self.model} from {self.year}."
              f"\n"
              f"Enjoy your next trip with {self.performance} HP and {self.__fuel_level}% fuel ({self.fuel_type})"
              f"\n")

    # Destructor
    def __del__(self):
        print(f"{self.brand} {self.model}: this car is destroyed")

    # Getter methods
    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_year(self):
        return self.year

    def get_performance(self):
        return self.performance

    def get_fuel_type(self):
        return self.fuel_type

    def get_mileage(self):
        return self.mileage

    def get_status(self):
        return self.status

    def get_fuel_level(self):
        return self.__fuel_level

    # Setter methods
    def __set_status(self, status):
        if _CarStatus.__contains__(status):
            self.status = status
            print(f"{self.brand} {self.model}: changed status to {self.status.name}")
        else:
            print("invalid status")

    def __set_fuel_level(self, level):
        if 0 <= level <= 100:
            self.__fuel_level = level
            print(f"{self.brand} {self.model}: current fuel level {level}")
        else:
            print(f"{self.brand} {self.model}: invalid input")

    # other methods
    def accelerate(self, speed):
        if self.status == _CarStatus.STOPPED or self.status == _CarStatus.STARTED:
            print(f"{self.brand} {self.model}: you're not driving so you can't accelerate")
        elif self.status == _CarStatus.DRIVING:
            print(f"{self.brand} {self.model}: accelerating to {speed} km/h")

    def brake(self, speed=0):
        if self.status == _CarStatus.STOPPED or self.status == _CarStatus.STARTED:
            print(f"{self.brand} {self.model}: you're not driving so you can't brake")
        elif self.status == _CarStatus.DRIVING:
            print(f"{self.brand} {self.model}: braking to {speed} km/h")

    def refuel(self, level=100):
        if level in range(0, 101) and level > self.__fuel_level:
            print(f"{self.brand} {self.model} is refueling from {self.__fuel_level} to {level}")
            self.__fuel_level = level
        else:
            print(f"{self.brand} {self.model}: something went wrong during the refuelling")

    def drive(self, distance):
        if self.status == _CarStatus.DRIVING:
            print(f"{self.brand} {self.model}: you're already driving")
        elif distance < 0:
            print(f"{self.brand} {self.model}: invalid distance")
        else:
            if self.status == _CarStatus.STOPPED:
                self.start_engine()
            self.__set_status(_CarStatus.DRIVING)
            self.accelerate(100)

            print(f"{self.brand} {self.model}: Driving Home For Christmas ...")

            for i in range(1, 10):
                print(f"{self.brand} {self.model}: {int(distance - i * (distance / 10))} km left")
                self.__set_fuel_level(self.__fuel_level - random.randint(2, 5))
                time.sleep(0.75)
            print(f"{self.brand} {self.model}: 0 km left")

            self.brake(0)
            self.__set_status(_CarStatus.STARTED)
            self.stop_engine()

    def start_engine(self):
        if self.status == _CarStatus.STARTED:
            print(f"{self.brand} {self.model}: engine already started")
        elif self.status == _CarStatus.DRIVING:
            print(f"{self.brand} {self.model}: You're driving so I hope your engine is already started")
        elif self.status == _CarStatus.STOPPED:
            print(f"{self.brand} {self.model}: engine is started")
            self.status = _CarStatus.STARTED
        else:
            print(f"{self.brand} {self.model}: there's something wrong with the engine, good luck")

    def stop_engine(self):
        if self.status == _CarStatus.STARTED:
            print(f"{self.brand} {self.model}: engine is stopped")
            self.status = _CarStatus.STOPPED
        elif self.status == _CarStatus.DRIVING:
            print(f"{self.brand} {self.model}: while driving you can't stop your engine")
        elif self.status == _CarStatus.STOPPED:
            print(f"{self.brand} {self.model}: engine is already stopped")
            self.status = _CarStatus.STARTED
        else:
            print(f"{self.brand} {self.model}: there's something wrong with the engine, good luck")

    # example function
    @staticmethod
    def __get_verbrauch(distance, runtime, weather=_Weather.CLEAR):
        # code section
        base_consumption = distance * 0.1

        if weather == _Weather.RAIN:
            base_consumption *= 1.2
        elif weather == _Weather.SNOW:
            base_consumption *= 1.5

        if runtime > 2:
            base_consumption *= 1.1

        # return section
        return base_consumption


def func_no_return(param1):
    print(f"parameter = {param1}")
    return


def func_one_return(param1, param2):
    return param1 + param2


def func_multiple_return(param1, param2):
    return param1 * 2, param2 * 3


if __name__ == '__main__':
    print(f"return value of {func_no_return.__name__}: {func_no_return(5)}")
    print(f"return value of {func_one_return.__name__}: {func_one_return(5, 6)}")
    print(f"return value of {func_multiple_return.__name__}: {func_multiple_return(2, 3)}")

    # car1 = Car("BMW", "X5", "Blue", 2023, 300, "Gasoline")
    # car1.drive(100)
