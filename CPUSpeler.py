import Speler
import collections
from Speler import Speler as Parent
from random import randint


class CPUSpeler(Parent):
    __mis_in_prog = 0
    __attempts = 0

    # Age niet meegeven als argument in constructor CPU-Speler (wordt random bepaald)
    def __init__(self, id, name, color):  # Niet zeker van inheritance
        age = randint(10, 99)
        super(CPUSpeler, self).__init__(id, name, age, color)
        self.hand = collections.Counter(red=0, blue=0, green=0)  # Opvragen met hand['red']

    # geeft terug of de speler door de CPU wordt gespeeld
    def is_cpu(self):
        return True

    # geeft het aantal resterende pionnen terug
    def getpawn(self):
        self.get_pawns()

    # dit stelt de te proberen missie in (missiekaart 1 of missiekaart 2)
    def set_mis_in_prog(self, mis_in_prog):
        self.__mis_in_prog = mis_in_prog

    # hiermee kan de te proberen missiekaart opgevraagd worden
    def get_mis_in_prog(self):
        return self.__mis_in_prog

    # dit geeft terug hoeveel keer de CPU speler geprobeerd heeft om een missie te voltooien (aantal keren kaart bijgevraagd)
    def get_attempts(self):
        return self.__attempts

    # indien een missie niet kan voltooid worden moet de pogingen teller verhoogd worden
    def increase_attempts(self):
        self.__attempts = self.__attempts + 1

    # indien een missie voltooid is moet de poginen teller gereset worden
    def reset_attempts(self):
        self.__attempts = 0
