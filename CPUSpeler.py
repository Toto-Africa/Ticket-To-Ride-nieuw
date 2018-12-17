import Speler
import collections
from Speler import Speler as Parent
from random import randint


class CPUSpeler(Parent):

    # Age niet meegeven als argument in constructor CPU-Speler
    def __init__(self, id, name, color):  # Niet zeker van inheritance
        age = randint(10, 99)
        #self.name = name
        #self.pawnnr = 20
        #self.missionscomp = 0
        #Speler.Speler(id, self.name, age, color)

        super(CPUSpeler, self).__init__(id, name, age, color)  # Correcte manier van inheritance in Python 2.7?
        self.hand = collections.Counter(red=0, blue=0, green=0)  # Opvragen met hand['red']

    # Heeft deze ook methodes add_card_to_hand en remove_card_from_hand van Speler???

    # def add_card_to_hand(self, color): # Mogen weg?
    # self.hand[color] = self.hand[color] + 1

    # def remove_card_from_hand(self, color): # Mogen weg?
    # self.hand[color] = self.hand[color] - 1

    def is_cpu(self):
        return True

    def getpawn(self):
        #return super(CPUSpeler, self).get_pawns()
        self.get_pawns()

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
