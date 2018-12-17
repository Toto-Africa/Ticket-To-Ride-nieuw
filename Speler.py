# import TrainCards
import collections
from tkinter import messagebox

# LOGICA PIONNEN!!!
class Speler:
    # constructor
    def __init__(self, id, name, age, color):
        self.id = id
        self.name = name  # deze opbjecten krijgt hij door van de GUI? ofwa?
        self.age = age  # deze opbjecten krijgt hij door van de GUI? ofwa?
        self.color = color  # deze opbjecten krijgt hij door van de GUI? ofwa?
        self.pawnnr = 20
        self.missionscomp = 0


        # Met collection.hand is beter denk ik: card=TrainCards.dealCard();self.hand[card] += 1; maar kdenk collection best nog initialiseren
        # Op die manier wordt elke kleur (dus "red" bv) als een aantal bijgehouden ipv een lijst

        self.hand = collections.Counter(red=0, blue=0, green=0)  # Opvragen met hand['red']

        # dit zou dan de constructor zijn om nieuwe spelers aan te maken? 'Jaa (Dries) :D'
        # Je geeft dan id, name, age, color mee in het startscherm (GUI)  'id genereer je automatisch bij het startscherm of hier?, de rest komt uit het startscherm'

        # pawnnr, missionscomplete, traincards en missioncards worden dan gegenereerd? (controleren of dit wel de juiste instanties zijn?)

    def get_name(self):
        return self.name

    def get_pawns(self):
        return self.pawnnr

    def remove_pawns(self, amount):
        self.pawnnr -= amount

    def get_mission(self, nr):
        if nr == 1:
            return self.__missioncard1
        if nr == 2:
            return self.__missioncard2

    def get_traincards(self, color):
        return self.hand[color]

    def is_cpu(self):
        return False

    def get_id(self):
        return self.id

    def get_missionscomp(self):
        return self.missionscomp

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_color(self, color):
        self.__color = color

    def set_missionscomp(self):
        self.__missionscomp += 1

    def set_missions(self, missioncard1, missioncard2):
        self.__missioncard1 = missioncard1
        self.__missioncard2 = missioncard2


    def add_card_to_hand(self, color):
        self.hand[color] = self.hand[color] + 1

    def remove_cards_from_hand(self, color, amount):
        if(self.hand[color]<amount):
            rest = amount - self.hand[color]
            self.hand[color] = 0
            self.hand["wild"] = self.hand["wild"] - rest
        else:
            self.hand[color] = self.hand[color] - amount

    """"
    DIT MOET IN BEURT DENK IK? in methode 'extra_train_card'

    Samenwerken met treinkaarten? iets met een kaarten dek waaruit je uit kan 'trekken'
    --> zou er ongeveer zo kunnen uitzien:

    NOTA VAN ELMER: Dit is hoe ik bovenstaande opmerking bedoel
    Deck is niet nodig, deze is enkel nodig als ge da deck aanvult, maar ge kunt mijne cardslist gewoon blijven poppen tot die leeg is
    Het poppen van de lijst gebeurt in GUI denk ik of in beurt met "Deck.dealCard()", deck is dan het object dat je van traincards aanmaakte

    #add traincard to hand
        def addCardToHand(self, traincard):

            if traincard != None:
                self.hand[traincard] += 1

        """