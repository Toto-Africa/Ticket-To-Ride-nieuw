import Speler
import CPUSpeler
import GUI
import TrainCards
import MissionCards
import Route
from random import randint
from collections import defaultdict
d = defaultdict(int)

# Iedere keer nieuwe instantie van Beurt? Of altijd de gegevens verversen?
# TODO GUI triggert Beurt. Eerste keer Beurt (init): aanmaken spelers, verdelen van kaarten en aanmaken routes

# Aantal kaarten bijhouden live bijhouden in Speler?

class Beurt:

    # Constructor
    def __init__(self, name, age, color, cpu_names): # Welke argumenten zijn het beste? List of array van spelers?
        # TODO aanmaken spelers, verdelen van kaarten en aanmaken routes
        # Iedere speler krijgt 2 missiekaarten en 4 treinkaarten

        # Planning: eerst gewone speler aanmaken. Dan CPU-spelers: eerst kaarten genereren, dan toekennen bij aanmaken CPU-speler

        # Menselijke speler aanmaken: heeft id = 1
        # Treinkaarten en missiekaarten op begin van spel: constructor Speler
        player = Speler.Speler(1, name, age, color) # Menselijke speler altijd ID = 0 geven # Of Speler.Speler.__init__(...)

        self.deck = TrainCards.TrainCards() # Deck treinkaarten
        self.missioncards = MissionCards.MissionCards()  # Deck missiekaarten

        #for i in range(aantalSpelers): # Niet nodig omdat je enkel aan player toekent
        for j in range(4):
            getrokkenKaart = self.deck.dealCard()
            player.add_card_to_hand(getrokkenKaart)

        # Missiekaarten menselijke speler
        missioncard1 = self.missioncards.dealMission()
        missioncard2 = self.missioncards.dealMission()
        player.set_currmissions(tuple([missioncard1, missioncard2]))

        d = {} # Dictionary

        # CPU-spelers aanmaken: 3 CPU-spelers (2, 3, 4)
        for i in range(0, 3):
            # cpu2, cpu3 en cpu4: werkt dit? (Getal achter "cpu" is ID)
            # namen cpu's zitten in array: itereren over array?
            d["cpu" + str(i+2)] = CPUSpeler.CPUSpeler(i+2, cpu_names[i], randint(10, 99), OVERIGE_KLEUREN) # Eerste deel werkt                                                                                               # #Willekeurige leeftijd tussen 10 en 99

        # 4 treinkaarten nemen om te starten (CPU)
        for k in range(len(d)):
            for j in range(0, 3):
                # Treinkaarten toekennen aan CPU's
                traincard = self.deck.dealCard()
                #traincards_array.append(traincard)  # # Indien methode "TrainCards.dealcard" kaartenteller van Speler verhoogt, dan is dit niet nodig
                k.add_card_to_hand(traincard) # Werkt hopelijk

            # Missiekaarten toekennen aan CPU's (terug buitenste for-loop om over CPU's te stappen)
            missioncard1 = self.missioncards.dealMission()
            missioncard2 = self.missioncards.dealMission()
            k.set_currmissions = tuple([missioncard1, missioncard2])


    # Normale methodes
    def swap_mission(self, pl = Speler.Speler, mission_to_change = str()): # Correct????
        new_mission = self.missioncards.dealMission()
        for i in range(0, 2):
            if pl.get_missions()[i] == mission_to_change:
                pl.get_missions[i] = new_mission


    def extra_traincard(self, pl = Speler.Speler):
        color = self.deck.dealCard()                # dealCard: returnt 1 kaart? Correcte methode? Instantie maken eerst?
        pl.add_card_to_hand(color)                                        #NOTA VAN ELMER: Best object bv "Deck" aanmaken --> self.deck = TrainCards.TrainCards()
                                                #Dit initialiseert Traincards met een stapel, daarna doe je self.deck.dealCard()" natuurlijk in de speler zijn hand


    def conquer_route(self, route = Route.Route, player = Speler.Speler):
        # Is route al ingenomen?
        if route.get_occupiedBy() == 0:
            # Heeft speler genoeg treinkaarten?
            if player.get_traincards(route.get_color()) >= route.get_pathCost():
                route.set_occupiedBy(player.get_id)
                player.remove_card_from_hand(route.get_color(), route.get_pathCost())
                player.set_missioncomp() # Verhoog aantal voltooide missies met 1

                check_six_completed_routes(player)
            else:
                print("Niet genoeg treinkaarten")
                # Moet nog naar messagebox?

        else:
            print("Deze route is reeds ingenomen")
            # Moet nog naar messagebox?



    # Mee in conquer_route geimplementeerd
    # def check_completed_route(self, routeid):
       # print("Test")
        # Code controleer of er een route voltooid is
        # If (kaarten van Speler kloppen om route in te nemen en nrOfBoxes klopt)
            # Route.isTaken == true

    def check_six_completed_routes(self, player = Speler.Speler):
        if player.get_missionscomp == 6:
            print("Spel voltooid")
            # Toon eindscherm



    # ================================================================================================


# OUDE COMMENTS
# TODO constructor van Speler: gegevens startscherm (naam, leeftijd) + kaarten genereren

# TODO eerste beurt -> init, dit gebeurt in klasse Speler
# TODO eerste beurt -> spelbord in GUI initialiseren
# TODO eerste beurt -> vanuit GUI, initBoard alle routes definieren (hardcoded) + scorebord

# TODO spel bezig:
# TODO Hoe missiekaarten controleren qua uitvoerbaarheid? Eerst knop onklikbaar zetten en op begin van beurt berekenen wat kan en wat niet kan
# TODO route innemen -> eerst op GUI route aanklikken -> naar klasse Route om info over die route op te halen -> naar Beurt -> naar Speler: controle of speler genoeg kaarten heeft -> speler geeft go of no go aan Beurt (true/false)
# TODO -> LET OP: meerdere routes tussen steden mogelijk!

# NOTE: CPU-speler -> focussen op missiekaarten (wel 2 trekken) en altijd kortste route laten nemen
# NOTE: voor routes 0 als ingenomen en 1-4 de spelers