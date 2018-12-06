# import TrainCards
import collections

# LOGICA PIONNEN!!!
class Speler:
    # constructor
    def __init__(self, id, name, age, color):
        self.__id = id
        self.__name = name  # deze opbjecten krijgt hij door van de GUI? ofwa?
        self.__age = age  # deze opbjecten krijgt hij door van de GUI? ofwa?
        self.__color = color  # deze opbjecten krijgt hij door van de GUI? ofwa?
        self.__pawnnr = 20
        self.__missionscomp = 0
        self.__missions = tuple(["string1", "string2"])  # Zelfde als ("string1", "string2")

        # Met collection.hand is beter denk ik: card=TrainCards.dealCard();self.hand[card] += 1; maar kdenk collection best nog initialiseren
        # Op die manier wordt elke kleur (dus "red" bv) als een aantal bijgehouden ipv een lijst

        self.hand = collections.Counter(red=0, blue=0, green=0, black=0, white=0, yellow=0)  # Opvragen met hand['red']

        # dit zou dan de constructor zijn om nieuwe spelers aan te maken? 'Jaa (Dries) :D'
        # Je geeft dan id, name, age, color mee in het startscherm (GUI)  'id genereer je automatisch bij het startscherm of hier?, de rest komt uit het startscherm'

        # pawnnr, missionscomplete, traincards en missioncards worden dan gegenereerd? (controleren of dit wel de juiste instanties zijn?)

    # onderstaande is vrij overbodig denk ik

    def get_pawns(self):
        return self.__pawnnr

    def get_missions(self):
        return self.__missions

    def get_traincards(self, color):
        return self.hand[color]

    def is_cpu(self):
        return False

    def get_id(self):
        return self.__id

    def get_missionscomp(self):
        return self.__missionscomp

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_color(self, color):
        self.__color = color

    def set_pawnnr(self, pawnnr):
        self.__pawnnr = pawnnr

    def set_missionscomp(self, missionscomp):
        self.__missionscomp += 1

    def set_currmissions(self, currmissions):
        self.__currmissions = currmissions

    def add_card_to_hand(self, color):
        self.hand[color] = self.hand[color] + 1

    def remove_cards_from_hand(self, color, amount):
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