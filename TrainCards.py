import random


class TrainCards(object):

    def __init__(self):
        self.colors = ["g", "b", "r"]
        self.cards = ["wild" for i in range(6)] + [i for i in self.colors for j in range(22)]
        self.shuffle(self.cards)



    def shuffle(self, cards):
        random.shuffle(cards)


    def dealCard(self):

        try:
            return self.cards.pop()  # Pop() removes the last item from the list and returns it

        except IndexError:
            #SPEL STOPPEN
            return("leeg")


    def cardsLeftover(self):
        return len(self.cards)  # Geeft weer hoeveel treinkaarten er nog zijn, kan bv tellertje geven op bord?
                                # Indien dit niet gewenst is, deze methode verwijderen


    # print(dealCard())