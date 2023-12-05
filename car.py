import random
import time
from enum import Enum


class _CarStatus(Enum):
    STOPPED = 0
    STARTED = 1
    DRIVING = 2


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
    fuel_level = None

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
        self.fuel_level = 100
        print(f"\n"
              f"Congratulations to your new car. It's a {self.color.lower()} {self.brand} {self.model} from {self.year}.\n"
              f"Enjoy your next trip with {self.performance} HP and {self.fuel_level}% fuel ({self.fuel_type})\n")

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
        return self.fuel_level

    # Setter methods
    def __set_status(self, status):
        if _CarStatus.__contains__(status):
            self.status = status
            print(f"{self.brand} {self.model}: changed status to {self.status.name}")
        else:
            print("invalid status")

    def __set_fuel_level(self, level):
        if 0 <= level <= 100:
            self.fuel_level = level
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
        if (level in range(0, 101) and level > self.fuel_level):
            print(f"{self.brand} {self.model} is refueling from {self.fuel_level} to {level}")
            self.fuel_level = level
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

            print(f"{self.brand} {self.model}: Driving Home For Chrismas ...")

            for i in range(1, 10):
                print(f"{self.brand} {self.model}: {int(distance - i * (distance / 10))} km left")
                self.__set_fuel_level(self.fuel_level - random.randint(2, 5))
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


if __name__ == '__main__':
    car1 = Car("BMW", "X5", "Blue", 2023, 300, "Gasoline")
    car1.drive(100)
