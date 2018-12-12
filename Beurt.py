import Speler
import CPUSpeler
#from klasses import GUI
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
        global player = Speler.Speler(1, name, age, color) # Menselijke speler altijd ID = 0 geven # Of Speler.Speler.__init__(...)

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

        cpu_colors = ['blue', 'green', 'yellow']
        # CPU-spelers aanmaken: 3 CPU-spelers (2, 3, 4)                                                                                             # #Willekeurige leeftijd tussen 10 en 99

        global cpu_x = CPUSpeler.CPUSpeler(2, cpu_names[0], 'blue')
        global cpu_y = CPUSpeler.CPUSpeler(3, cpu_names[1], 'green')
        global cpu_z = CPUSpeler.CPUSpeler(4, cpu_names[2], 'yellow')

        # 4 treinkaarten nemen om te starten (CPU)
        for j in range(0, 3):
            # Treinkaarten toekennen aan CPU's
            traincard = self.deck.dealCard()                #traincards_array.append(traincard)  # # Indien methode "TrainCards.dealcard" kaartenteller van Speler verhoogt, dan is dit niet nodig
            cpu_x.add_card_to_hand(traincard) # Werkt hopelijk

        for j in range(0, 3):
            # Treinkaarten toekennen aan CPU's
            traincard = self.deck.dealCard()
            cpu_y.add_card_to_hand(traincard)

        for j in range(0, 3):
                # Treinkaarten toekennen aan CPU's
                traincard = self.deck.dealCard()  # traincards_array.append(traincard)  # # Indien methode "TrainCards.dealcard" kaartenteller van Speler verhoogt, dan is dit niet nodig
                cpu_z.add_card_to_hand(traincard)  # Werkt hopelijk


        # Missiekaarten toekennen aan CPU's (terug buitenste for-loop om over CPU's te stappen)
        missioncard1 = self.missioncards.dealMission()
        missioncard2 = self.missioncards.dealMission()
        cpu_x.set_currmissions = tuple([missioncard1, missioncard2])

        missioncard1 = self.missioncards.dealMission()
        missioncard2 = self.missioncards.dealMission()
        cpu_y.set_currmissions = tuple([missioncard1, missioncard2])

        missioncard1 = self.missioncards.dealMission()
        missioncard2 = self.missioncards.dealMission()
        cpu_z.set_currmissions = tuple([missioncard1, missioncard2])


    # Normale methodes
    def return_player(self, id):
        if id == 1:
            return player
        if id == 2:
            return cpu_x
        if id == 3:
            return cpu_y
        if id==4:
            return cpu_z



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
            if player.get_traincards(route.get_color()) >= route.get_pathCost() or player.get_traincards(route.get_color() + player.get_traincards(route.get_color('wild')) >= route.get_pathCost()):
                route.set_occupiedBy(player.get_id)
                player.remove_card_from_hand(route.get_color(), route.get_pathCost())
                player.remove_pawns(route.get_pathCost())
                self.end_of_beurt(player)
            else:
                print("Niet genoeg treinkaarten")                # Moet nog naar messagebox?

        else:
            print("Deze route is reeds ingenomen")
            # Moet nog naar messagebox?



    # Mee in conquer_route geimplementeerd
    # def check_completed_route(self, routeid):
       # print("Test")
        # Code controleer of er een route voltooid is
        # If (kaarten van Speler kloppen om route in te nemen en nrOfBoxes klopt)
            # Route.isTaken == true



    # Controleer of missie voltooid werd
    # Ja, missie werd voltooid: aantal voltooide missies + 1
    # Zes verschillende missies voltooid? -> ja: Speler wint
    # Neen: zijn pionnen van speler op? -> Ja: Speler met meeste voltooide missies wint
    # Neen: nieuwe missiekaart

    # Neen, missie werd niet voltooid:
    # Zijn pionnen op? --> Ja: speler met meeste voltooide missies wint
    # Neen: volgende beurt
    #def end_of_beurt(self, pl = Speler.Speler, tabel = list):
        #if  Missie voltooid (Hoe implementeren???)
        # Eerst itereren door eerste kolom ("Waar staat missie?")
        # Dan itereren door elementen in tweede kolom ("Staat route erin?")

     #   mission_accomp = False # boolean mission_accomp zegt of Speler missie voltooid heeft
      #  pl_mission1 = pl.get_missions()[0]
        #pl_mission2 = pl.get_missions()[1]
       # for i in self.missioncards:
            # Juiste rij zoeken in tabel met routes
          #  tabel_missions = tabel[i][0]
           # tabel_missions.split(",")
        #    if tabel[i][0] == pl_mission1
            # Daarna waardes in tweede kolom voor die rij itereren en controleren of juiste route erbij zit

        #if mission_accomp:
            #pl.set_missionscomp()

         #   if  pl.get_missionscomp() == 6:
                # Spel is uit, pl wint -> naar overwinningsscherm
          #  else:
           #     if pl.get_pawns == 0:
                    # Speler met meeste aantal voltooide missies wint
             #   else:
                    # Nieuwe missiekaart

        # Missie werd niet voltooid
        # else:
          #  if pl.get_pawns == 0:
                # Speler met meeste aantal voltooide missies wint
           # else:
                # Volgende beurt -> Wel "else" statement nodig?



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