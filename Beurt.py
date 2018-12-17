import Speler
import CPUSpeler
#from klasses import GUI
import TrainCards
import MissionCards
import Route
from random import randint
from collections import defaultdict
from tkinter import messagebox

from Speler import Speler

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
        global player
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
        player.set_missions(missioncard1, missioncard2)

        cpu_colors = ['blue', 'green', 'yellow']
        # CPU-spelers aanmaken: 3 CPU-spelers (2, 3, 4) # #Willekeurige leeftijd tussen 10 en 99

        global cpu_x
        cpu_x = CPUSpeler.CPUSpeler(2, cpu_names[0], 'blue')
        global cpu_y
        cpu_y = CPUSpeler.CPUSpeler(3, cpu_names[1], 'green')
        global cpu_z
        cpu_z = CPUSpeler.CPUSpeler(4, cpu_names[2], 'yellow')


        # 4 treinkaarten nemen om te starten (CPU)
        for j in range(0, 3):
            # Treinkaarten toekennen aan CPU's
            traincard = self.deck.dealCard() #traincards_array.append(traincard)  # # Indien methode "TrainCards.dealcard" kaartenteller van Speler verhoogt, dan is dit niet nodig
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
        cpu_x.set_missions(missioncard1, missioncard2)

        missioncard1 = self.missioncards.dealMission()
        missioncard2 = self.missioncards.dealMission()
        cpu_y.set_missions(missioncard1, missioncard2)

        missioncard1 = self.missioncards.dealMission()
        missioncard2 = self.missioncards.dealMission()
        cpu_z.set_missions(missioncard1, missioncard2)


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

    def swap_mission(self, pl, table = list):
        # Route: tussen 2 aanliggende steden
        # Weg: tussen 2 niet-aanliggende steden (missie dus)


        # TODO Check bij wisselen van missiekaarten
        # Iedere mogelijke weg afgaan en kijken of daar al 1 van ingenomen is
        # Als van alle mogelijke wegen (tussen de 2 missiesteden) minstens 1 route is ingenomen, dan is het onmogelijk

        bool1 = False  # Zegt of er nog een hele weg tussen de steden van missiekaart 1 beschikbaar is.
                       # Zegt dus of voltooien van missie nog mogelijk is.

        # Controle of aan voorwaarden voldaan is
        # 1) Waar staan missies van missiekaart 1 in tabel? Itereren door lange tabel
        for i in range(len(table)):
            # Naar juiste rij gaan (missiekaart 1)
            if pl.get_mission(1) == table[i]:
                # LOGICA: controleer of iedere mogelijke weg/route onmogelijk is
                # 2) Itereren over iedere mogelijke route/weg tussen de twee steden
                for j in range(len(table[i][1])):

                    # TODO Meer if-structuren in soort case-structure met grootte van route = aantal 'and'
                    # Aantal routes in weg?
                    if len(table[i][1][j]) == 1:
                        if table[i][1][j][0] == 0:  # Correct?
                            bool1 = True
                            break

                    if len(table[i][1][j]) == 2:
                        if table[i][1][j][0] == 0 and table[i][1][j][1] == 0:  # Correct?
                            bool1 = True
                            break

                    if len(table[i][1][j]) == 3:
                        if table[i][1][j][0] == 0 and table[i][1][j][1] == 0 and table[i][1][j][2] == 0:  # Correct?
                            bool1 = True
                            break

                    #for k in range(len(table[i][1][j])):
                        #route = table[i][1][j][k] # Werkt dit??????????
                        # 3) Controleren of route al ingenomen is
                        #if route.get_occupied() == 0:
                            #bool1 = True
                            #break # Er is nog minstens 1 route vrij, dus rest controleren hoeft niet


            # Idem voor missiekaart 2
        for i in range(len(table)):
            # Naar juiste rij gaan (missiekaart 1)
            if pl.get_mission(2) == table[i]:
                # LOGICA: controleer of iedere mogelijke weg/route onmogelijk is
                # 2) Itereren over iedere mogelijke route/weg tussen de twee steden
                for j in range(len(table[i][1])):

                    # TODO Meer if-structuren in soort case-structure met grootte van route = aantal 'and'
                     # Aantal routes in weg?
                    if len(table[i][1][j]) == 1:
                        if table[i][1][j][0] == 0:  # Correct?
                            bool2 = True
                            break

                    if len(table[i][1][j]) == 2:
                        if table[i][1][j][0] == 0 and table[i][1][j][1] == 0:  # Correct?
                            bool2 = True
                            break

                    if len(table[i][1][j]) == 3:
                        if table[i][1][j][0] == 0 and table[i][1][j][1] == 0 and table[i][1][j][2] == 0:  # Correct?
                            bool2 = True
                            break

        if not bool1 and not bool2:
            # Beide missies niet uit te voeren? -> bool = True
            new_mission1 = self.missioncards.dealMission()
            new_mission2 = self.missioncards.dealMission()
            pl.set_missions(new_mission1, new_mission2)








    #def extra_traincard(self, pl = Speler.Speler):
    def extra_traincard(self, pl):
        color = self.deck.dealCard()                # dealCard: returnt 1 kaart? Correcte methode? Instantie maken eerst?
        pl.add_card_to_hand(color)                                        #NOTA VAN ELMER: Best object bv "Deck" aanmaken --> self.deck = TrainCards.TrainCards()
                                                #Dit initialiseert Traincards met een stapel, daarna doe je self.deck.dealCard()" natuurlijk in de speler zijn hand


    #def conquer_route(self, route = Route.Route(), player = Speler.Speler()):
    def conquer_route(self, route, player):
        statuscode = 0
        # nota jan:
        # statuscode => 0 = alles ok, 1 = route reeds ingenomen, 2 = niet genoeg treinkaarten of pionnen, 3 = pionnen op
        # de menselijke speler kan communiceren via messageboxes, CPU niet. => daarom code
        # Is route al ingenomen?
        if route.get_occupiedBy() == 0:
            # Heeft speler genoeg treinkaarten?
            aantalMetWilds = player.get_traincards(route.get_color()) + player.get_traincards("wild")
            if(aantalMetWilds < route.get_pathCost() or player.get_pawns() < route.get_pathCost()):
                #messagebox.showwarning("Waarschuwing","Onvoldoende treinkaarten \n\n of \n\npionnen")
                statuscode = 2
            else:
                route.set_occupiedBy(player.get_id())
                player.remove_cards_from_hand(route.get_color(),route.get_pathCost())
                player.remove_pawns(route.get_pathCost())
                if(player.get_pawns() == 0):
                    #messagebox.showwarning("Waarschuwing",
                    #                       "Speler " + player.get_name() + " heeft geen pionnen meer over!")
                    statuscode = 3
                    #EINDIGEN SPEL
                else:
                    self.end_of_beurt(player) # deze droppen voor statuscode (standaard 0)
        else:
            #print("Deze route is reeds ingenomen")
            statuscode = 1
            # Moet nog naar messagebox?
        return statuscode


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

