import collections

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

        self.hand = collections.Counter(red=0, blue=0, green=0)  # Opvragen met hand['red']


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
        if(self.hand[color]>=amount):
            self.hand[color] = self.hand[color] - amount
        else:
            rest = amount - self.hand[color]
            self.hand[color] = self.hand[color] - self.hand[color]
            self.hand["wild"] = self.hand["wild"] - rest