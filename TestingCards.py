import TrainCards
import MissionCards
import time


class Test(object):



        deck = TrainCards.TrainCards()
        missions = MissionCards.MissionCards()

        for i in range(80):
                time.sleep(0.1)
                ticket = deck.dealCard()
                if ticket == 'gedaan':
                        print("Einde Spel")
                        break
                else:
                        print(ticket)
        #print(ticket[0])
        #print(ticket[1][0])    --> GEEFT EERSTE MOGELIJKE ROUTE VAN TICKET
        #lijst = list(ticket)
        # print(lijst)
        #ticket = deck.dealCard()
