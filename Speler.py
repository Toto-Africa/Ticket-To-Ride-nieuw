import collections


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

    # naam teruggeven
    def get_name(self):
        return self.name

    # aantal resterende pionnen teruggeven
    def get_pawns(self):
        return self.pawnnr

    # pionnen verwijderen
    def remove_pawns(self, amount):
        self.pawnnr -= amount

    # missie teruggeven
    def get_mission(self, nr):
        if nr == 1:
            return self.__missioncard1
        if nr == 2:
            return self.__missioncard2

    # het aantal overige treinkaarten voor een bepaalde kleur teruggeven
    def get_traincards(self, color):
        return self.hand[color]

    # teruggeven of de speler een CPU is
    def is_cpu(self):
        return False

    # speler ID teruggeven
    def get_id(self):
        return self.id

    # teruggeven hoeveel missies een speler afgewerkt heeft
    def get_missionscomp(self):
        return self.missionscomp

    # de naam van de speler instellen
    def set_name(self, name):
        self.__name = name

    # leeftijd van de speler instellen
    def set_age(self, age):
        self.__age = age

    # kleur van de speler instellen
    def set_color(self, color):
        self.__color = color

    # verhoog de teller van de speler die aaangeeft hoeveel missies deze al voltooid heeft
    def set_missionscomp(self):
        self.__missionscomp += 1

    # stel de missiekaarten van de speler in
    def set_missions(self, missioncard1, missioncard2):
        self.__missioncard1 = missioncard1
        self.__missioncard2 = missioncard2

    # treinkaart van een bepaalde kleur toevoegen aan de speler
    def add_card_to_hand(self, color):
        self.hand[color] = self.hand[color] + 1

    # treinkaarten van een bepaalde kleur uit de hand van de speler verwijderen
    def remove_cards_from_hand(self, color, amount):
        if(self.hand[color]>=amount):
            self.hand[color] = self.hand[color] - amount
        else:
            rest = amount - self.hand[color]
            self.hand[color] = self.hand[color] - self.hand[color]
            self.hand["wild"] = self.hand["wild"] - rest