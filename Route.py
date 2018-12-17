class Route:
    def __init__(self, color, pathCost, cities, occupiedBy):
        self.__color = color
        self.__pathCost = pathCost
        self.__cities = cities
        self.__occupiedBy = occupiedBy # Is 0 indien niet ingenomen door iemand. Een ander getal geeft de ID van een speler

    #
    # getters and setters
    #

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_pathCost(self):
        return self.__pathCost

    def set_pathCost(self, pathCost):
        self.__pathCost = pathCost

    def get_cities(self):
        return self.__cities

    def get_cities_nr(self, nr):
        return self.__cities[nr]

    def set_cities(self, city1, city2):
        self.__cities = [city1, city2]

    def get_occupiedBy(self):
        return self.__occupiedBy

    def set_occupiedBy(self, occupiedBy):
        self.__occupiedBy = occupiedBy
