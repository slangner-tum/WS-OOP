class Person:
    # declaration - not necessary
    __name = None
    __surname = None
    __age = None
    __licence = None

    # constructor
    def __init__(self, name="Max", surname="Mustermann", age=18, licence=False):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__licence = licence

    # destructor
    def __del__(self):
        pass

    # other methods
    def passed_driving_test(self):
        self.__licence = True

    def driving_licence(self):
        return self.__licence
