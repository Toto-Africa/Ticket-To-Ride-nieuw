class Route:
    __color = ""
    __pathCost = 0
    __cities = []
    __occupiedBy = 0

    def __init__(self, id, color, pathCost, cities, occupiedBy):
        self.__id = id
        self.__color = color
        self.__pathCost = pathCost
        self.__cities = cities
        self.__occupiedBy = occupiedBy # Is 0 indien niet ingenomen door iemand. Een ander getal geeft de ID van een speler

    #
    # getters and setters
    #

    def get_id(self):
        return self.__id

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
    def set_cities(self, city1, city2):
        self.__cities = [city1, city2]

    def get_occupiedBy(self):
        return self.__occupiedBy
    def set_occupiedBy(self, occupiedBy):
        self.__occupiedBy = occupiedBy

# aanmaken
# for i in range():
# #     self.board.add_edge(routes[i].get_cities()[0], routes[i].get_cities()[1], weight=routes[i].get_pathCost(), edgeColors=routes[i].get_color())
# subset van kaart
# listOfCities = [
#   "Berlijn", "Wenen", "Warschau", "Kiev", "Boekarest" # 0, 1, 2, 3, 4
# ]
# routes = []
# # Berlijn to
# # Wenen to
# routes.append(Route('yellow', 1, [listOfCities[1], listOfCities[0]], 0)) # Berlijn (yellow)
# routes.append(Route('red',    1, [listOfCities[1], listOfCities[0]], 0)) # Berlijn (red)
# # Warschau to
# routes.append(Route('blue',   2, [listOfCities[2], listOfCities[0]], 0)) # Berlijn (blue)
# routes.append(Route('green',  2, [listOfCities[2], listOfCities[0]], 0)) # Berlijn (green)
# routes.append(Route('black',  1, [listOfCities[2], listOfCities[1]], 0)) # Wenen (black)
# # Kiev to
# routes.append(Route('white',  3, [listOfCities[3], listOfCities[1]], 0)) # Wenen (white)
# routes.append(Route('yellow', 1, [listOfCities[3], listOfCities[2]], 0)) # Warschau (yellow)
# # Boekarest to
# routes.append(Route('yellow', 2, [listOfCities[4], listOfCities[1]], 0)) # Wenen (yellow)
# routes.append(Route('blue',   2, [listOfCities[4], listOfCities[1]], 0)) # Wenen (blue)
# routes.append(Route('red',    2, [listOfCities[4], listOfCities[3]], 0)) # Kiev (red)

# volledige kaart (Nu niet gebruiken)
# listOfCities = [
#     "Dublin", "Brest", "Madrid", "Londen", "Parijs",          #  0  1  2  3  4
#     "Barcelona", "Amsterdam", "Zurich", "Rome", "Copenhagen", #  5  6  7  8  9
#     "Berlijn", "Wenen", "Sarajevo", "Athene", "Stockholm",    # 10 11 12 13 14
#     "Warschau", "Kiev", "Boekarest", "Ankara", "Riga",        # 15 16 17 18 19
#     "Moscou", "Rostov"                                        # 20 21
# ]
# routes = []
# # Dublin to
# # Brest to
# routes.append(Route('blue',   2, [listOfCities[1], listOfCities[0]], 0)) # Dublin (blue)
# # Madrid to
# routes.append(Route('green',  3, [listOfCities[2], listOfCities[1]], 0)) # Brest (green)
# # Londen to
# routes.append(Route('green',  1, [listOfCities[3], listOfCities[0]], 0)) # Dublin (green)
# routes.append(Route('yellow', 1, [listOfCities[3], listOfCities[0]], 0)) # Dublin (yellow)
# routes.append(Route('red',    2, [listOfCities[3], listOfCities[1]], 0)) # Brest (red)
# # Parijs to
# routes.append(Route('blue',   3, [listOfCities[4], listOfCities[2]], 0)) # Madrid (blue)
# routes.append(Route('red',    3, [listOfCities[4], listOfCities[2]], 0)) # Madrid (red)
# routes.append(Route('yellow', 2, [listOfCities[4], listOfCities[1]], 0)) # Brest (yellow)
# routes.append(Route('green',  1, [listOfCities[4], listOfCities[3]], 0)) # Londen (green)
# routes.append(Route('black',  1, [listOfCities[4], listOfCities[3]], 0)) # Londen (black)
# # Barcelona to
# routes.append(Route('white',  2, [listOfCities[5], listOfCities[4]], 0)) # Parijs (white)
# routes.append(Route('white',  1, [listOfCities[5], listOfCities[2]], 0)) # Madrid (white)
# routes.append(Route('red',    1, [listOfCities[5], listOfCities[2]], 0)) # Madrid (red)
# # Amsterdam to
# routes.append(Route('white',  1, [listOfCities[6], listOfCities[3]], 0)) # Londen (white)
# routes.append(Route('black',  1, [listOfCities[6], listOfCities[3]], 0)) # Londen (black)
# routes.append(Route('blue',   1, [listOfCities[6], listOfCities[4]], 0)) # Parijs (blue)
# # Zurich to
# routes.append(Route('blue',   1, [listOfCities[7], listOfCities[4]], 0)) # Parijs (blue)
# routes.append(Route('white',  1, [listOfCities[7], listOfCities[4]], 0)) # Parijs (white)
# # Rome to
# routes.append(Route('white',  1, [listOfCities[8], listOfCities[7]], 0)) # Zurich (white)
# routes.append(Route('green',  1, [listOfCities[8], listOfCities[7]], 0)) # Zurich (green)
# routes.append(Route('black',  2, [listOfCities[8], listOfCities[5]], 0)) # Barcelona (black)
# routes.append(Route('yellow', 2, [listOfCities[8], listOfCities[5]], 0)) # Barcelona (yellow)
# # Copenhagen to
# routes.append(Route('red',    2, [listOfCities[9], listOfCities[6]], 0)) # Amsterdam (red)
# # Berlijn to
# routes.append(Route('white',  1, [listOfCities[10], listOfCities[9]], 0)) # Copenhagen (white)
# routes.append(Route('green',  1, [listOfCities[10], listOfCities[9]], 0)) # Copenhagen (green)
# routes.append(Route('black',  1, [listOfCities[10], listOfCities[6]], 0)) # Amsterdam (black)
# routes.append(Route('green',  1, [listOfCities[10], listOfCities[6]], 0)) # Amsterdam (green)
# routes.append(Route('yellow', 3, [listOfCities[10], listOfCities[4]], 0)) # Parijs (yellow)
# routes.append(Route('white',  3, [listOfCities[10], listOfCities[4]], 0)) # Parijs (white)
# # Wenen to
# routes.append(Route('yellow', 1, [listOfCities[11], listOfCities[10]], 0)) # Berlijn (yellow)
# routes.append(Route('red',    1, [listOfCities[11], listOfCities[10]], 0)) # Berlijn (red)
# routes.append(Route('black',  2, [listOfCities[11], listOfCities[7]], 0)) # Zurich (black)
# routes.append(Route('red',    2, [listOfCities[11], listOfCities[7]], 0)) # Zurich (red)
# routes.append(Route('blue',   2, [listOfCities[11], listOfCities[8]], 0)) # Rome (blue)
# # Sarajevo to
# routes.append(Route('green',  2, [listOfCities[12], listOfCities[11]], 0)) # Wenen (green)
# routes.append(Route('black',  2, [listOfCities[12], listOfCities[8]], 0)) # Rome (black)
# # Athene to
# routes.append(Route('blue',   3, [listOfCities[13], listOfCities[8]], 0)) # Rome (blue)
# routes.append(Route('white',  3, [listOfCities[13], listOfCities[8]], 0)) # Rome (white)
# routes.append(Route('red',    1, [listOfCities[13], listOfCities[12]], 0)) # Sarajevo (red)
# # Stockholm to
# routes.append(Route('blue',   1, [listOfCities[14], listOfCities[9]], 0)) # Copenhagen (blue)
# routes.append(Route('black',  1, [listOfCities[14], listOfCities[9]], 0)) # Copenhagen (black)
# # Warschau to
# routes.append(Route('blue',   2, [listOfCities[15], listOfCities[10]], 0)) # Berlijn (blue)
# routes.append(Route('green',  2, [listOfCities[15], listOfCities[10]], 0)) # Berlijn (green)
# routes.append(Route('black',  1, [listOfCities[15], listOfCities[11]], 0)) # Wenen (black)
# # Kiev to
# routes.append(Route('white',  3, [listOfCities[16], listOfCities[11]], 0)) # Wenen (white)
# routes.append(Route('yellow', 1, [listOfCities[16], listOfCities[15]], 0)) # Warschau (yellow)
# # Boekarest to
# routes.append(Route('yellow', 2, [listOfCities[17], listOfCities[13]], 0)) # Athene (yellow)
# routes.append(Route('green',  1, [listOfCities[17], listOfCities[12]], 0)) # Sarajevo (green)
# routes.append(Route('yellow', 2, [listOfCities[17], listOfCities[11]], 0)) # Wenen (yellow)
# routes.append(Route('blue',   2, [listOfCities[17], listOfCities[11]], 0)) # Wenen (blue)
# routes.append(Route('red',    2, [listOfCities[17], listOfCities[16]], 0)) # Kiev (red)
# # Ankara to
# routes.append(Route('blue',   2, [listOfCities[18], listOfCities[17]], 0)) # Boekarest (blue)
# routes.append(Route('black',  2, [listOfCities[18], listOfCities[17]], 0)) # Boekarest (black)
# routes.append(Route('green',  2, [listOfCities[18], listOfCities[13]], 0)) # Athene (green)
# routes.append(Route('red',    2, [listOfCities[18], listOfCities[13]], 0)) # Athene (red)
# # Riga to
# routes.append(Route('yellow', 1, [listOfCities[19], listOfCities[14]], 0)) # Stockholm (yellow)
# routes.append(Route('red',    1, [listOfCities[19], listOfCities[14]], 0)) # Stockholm (red)
# routes.append(Route('white',  1, [listOfCities[19], listOfCities[15]], 0)) # Warschau (white)
# # Moskou to
# routes.append(Route('yellow', 3, [listOfCities[20], listOfCities[19]], 0)) # Riga (yellow)
# routes.append(Route('green',  3, [listOfCities[20], listOfCities[19]], 0)) # Riga (green)
# routes.append(Route('red',    3, [listOfCities[20], listOfCities[15]], 0)) # Warschau (red)
# routes.append(Route('black',  3, [listOfCities[20], listOfCities[15]], 0)) # Warschau (black)
# routes.append(Route('green',  2, [listOfCities[20], listOfCities[16]], 0)) # Kiev (green)
# # Rostov to
# routes.append(Route('white',  3, [listOfCities[21], listOfCities[18]], 0)) # Ankara (white)
# routes.append(Route('black',  3, [listOfCities[21], listOfCities[18]], 0)) # Ankara (black)
# routes.append(Route('green',  2, [listOfCities[21], listOfCities[17]], 0)) # Boekarest (green)
# routes.append(Route('red',    2, [listOfCities[21], listOfCities[17]], 0)) # Boekarest (red)
# routes.append(Route('black',  2, [listOfCities[21], listOfCities[16]], 0)) # Kiev (black)
# routes.append(Route('yellow', 2, [listOfCities[21], listOfCities[20]], 0)) # Moscow (yellow)
# routes.append(Route('blue',   2, [listOfCities[21], listOfCities[20]], 0)) # Moscow (blue)
