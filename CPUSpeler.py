import Speler
from random import randint

__metaclass__ = type


class CPUSpeler(Speler.Speler):
    # def __init__(self, id, name, age, color, pawnnr, missionscomp, currmissions, isCPU, hand):
    # Speler.__init__(self, id, name, age, color, pawnnr, missionscomp, currmissions, hand)
    # self.__isCPU = isCPU

    # Michiel: constructor van Speler met "super(CPUSpeler, self).__init__()"

    # Of def __init__(self):
    #       Speler.__init__(self, isCPU=True) # Mss wel de volgorde van argumenten omdraaien?

    # Pawn op 20 zetten, random leeftijd, namen van CPU-spelers, willekeurige missioncards en traincards trekken

    # Michiel constructor
    # Age niet meegeven als argument in constructor CPU-Speler
    def __init__(self, id, name, color):  # Niet zeker van inheritance
        age = randint(10, 99)
        super(CPUSpeler, self).__init__(self, id, name, age, color)  # Correcte manier van inheritance in Python 2.7?
        self.hand = Counter(red=0, blue=0, green=0, black=0, white=0, yellow=0)  # Opvragen met hand['red']

    # Heeft deze ook methodes add_card_to_hand en remove_card_from_hand van Speler???

    # def add_card_to_hand(self, color): # Mogen weg?
    # self.hand[color] = self.hand[color] + 1

    # def remove_card_from_hand(self, color): # Mogen weg?
    # self.hand[color] = self.hand[color] - 1

    def is_cpu(self):
        return True

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_color(self, color):
        self.__color = color

    def set_pawnnr(self, pawnnr):
        self.__pawnnr = pawnnr

    def set_missionscomp(self, missionscomp):
        self.__missionscomp = missionscomp

    def set_currmissions(self, currmissions):
        self.__currmissions = currmissions