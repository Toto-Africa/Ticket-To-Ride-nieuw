class Route:
    # het route object houd de routes bij
    def __init__(self, color, pathCost, cities, occupiedBy):
        self.__color = color
        self.__pathCost = pathCost
        self.__cities = cities
        self.__occupiedBy = occupiedBy # Is 0 indien niet ingenomen door iemand. Een ander getal geeft de ID van een speler

    #
    # getters and setters
    #

    # kleur van de route teruggeven
    def get_color(self):
        return self.__color

    # kleur van de route instellen
    def set_color(self, color):
        self.__color = color

    # de kost van de route teruggeven
    def get_pathCost(self):
        return self.__pathCost

    # de kost van de route instellen
    def set_pathCost(self, pathCost):
        self.__pathCost = pathCost

    # de steden teruggeven
    def get_cities(self):
        return self.__cities

    # een van de steden teruggeven
    def get_cities_nr(self, nr):
        return self.__cities[nr]

    # de steden instellen
    def set_cities(self, city1, city2):
        self.__cities = [city1, city2]

    # teruggeven wie de route heeft ingenomen (0 = nog niet ingenomen)
    def get_occupiedBy(self):
        return self.__occupiedBy

    # instellen wie de route heeft ingenomen
    def set_occupiedBy(self, occupiedBy):
        self.__occupiedBy = occupiedBy
