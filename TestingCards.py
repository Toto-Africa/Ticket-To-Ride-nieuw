import TrainCards
import MissionCards
import Speler
import time


class Test(object):
        player = Speler.Speler(1, "Elmer", "21", "Rood")
        deck = TrainCards.TrainCards()
        #missions = MissionCards.MissionCards()
        for j in range(10):
            getrokkenKaart = deck.dealCard()
            player.add_card_to_hand(getrokkenKaart)

        print(player.hand)
        player.remove_cards_from_hand("red", 9)
        print(player.hand)
        #for i in range(80):
        #        time.sleep(0.1)
        #        ticket = deck.dealCard()
        #        if ticket == 'gedaan':
        #                print("Einde Spel")
        #                break
        #        else:
        #                print(ticket)
        #print(ticket[0])
        #ticket = missions.dealMission()
        #print(ticket[0])    #--> GEEFT EERSTE MOGELIJKE ROUTE VAN TICKET
        #print(ticket)
        #print(len(ticket[1]))
        #print(ticket[1][1])
        #lijst = list(ticket)
        # print(lijst)
        #ticket = deck.dealCard()
