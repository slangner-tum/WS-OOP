class Engine:
    # declaration - not necessary
    __performance = None
    __capacity = None
    __number_of_cylinders = None
    __rpm = None

    # constructor
    def __init__(self, performance, capacity=1.9, num_cyl=5, rpm=0):
        self.__performance = performance
        self.__capacity = capacity
        self.__number_of_cylinders = num_cyl
        self.__rpm = rpm

    # destructor
    def __del__(self):
        self.__rpm = 0

    # getter methods
    def get_performance(self):
        return self.__performance

    def get_capacity(self):
        return self.__capacity

    def get_rpm(self):
        return self.__rpm

    # setter methods
    def set_rpm(self, rpm):
        self.__rpm = rpm

    # other methods
    def start(self):
        self.__rpm = 1200

    def stop(self):
        self.__rpm = 0
