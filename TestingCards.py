import TrainCards
import MissionCards
import time


class Test(object):



        deck = TrainCards.TrainCards()
        missions = MissionCards.MissionCards()

        #for i in range(80):
        #        time.sleep(0.1)
        #        ticket = deck.dealCard()
        #        if ticket == 'gedaan':
        #                print("Einde Spel")
        #                break
        #        else:
        #                print(ticket)
        #print(ticket[0])
        ticket = missions.dealMission()
        print(ticket[0])    #--> GEEFT EERSTE MOGELIJKE ROUTE VAN TICKET
        print(len(ticket[1]))
        print(ticket[1][1])
        #lijst = list(ticket)
        # print(lijst)
        #ticket = deck.dealCard()
