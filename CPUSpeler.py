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

    def is_cpu(self):
        return True

    def getpawn(self):
        self.get_pawns()

    def set_mis_in_prog(self, mis_in_prog):
        self.__mis_in_prog = mis_in_prog

    def get_mis_in_prog(self):
        return self.__mis_in_prog

    def get_attempts(self):
        return self.__attempts

    def increase_attempts(self):
        self.__attempts = self.__attempts + 1


    # logica blijft hetzelfde in CPUSpeler en Speler
    #def remove_cards_from_hand(self, color, amount):
    #    aantalMetWilds = self.hand[color]+self.hand["wild"]
    #    aantalPionnen = self.get_pawns()
    #    bewerkingCode = 0 # 0 = geldig, 1 = ongeldig. Te weinig resources, 2 = spel afgelopen
    #    if(aantalMetWilds < amount or aantalPionnen < amount):
    #        bewerkingCode = 1
    #    else:
    #        if(self.hand[color]<amount):
    #            rest = amount - self.hand[color]
    #            self.hand[color] = 0
    #            self.hand["wild"] = self.hand["wild"] - rest
    #            self.remove_pawns(amount)
    #            if self.get_pawns() == 0:
    #                bewerkingCode = 2
    #                #messagebox.showwarning("Spel afgelopen", "Speler: " + self.__name + " heeft geen pionnen meer over!")
    #        else:
    #            self.hand[color] = self.hand[color] - amount
    #            self.remove_pawns(amount)
    #            if self.get_pawns() == 0:
    #                bewerkingCode = 2
    #                #messagebox.showwarning("Spel afgelopen", "Speler: " + self.__name + " heeft geen pionnen meer over!")
    #    return bewerkingCode
