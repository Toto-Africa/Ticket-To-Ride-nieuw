import random

class MissionCards(object):
    def __init__(self):
        self.missions = [(("Berlijn, Kiev"), (("Warschau"),("Wenen"),("Warschau, Wenen"),("Wenen, Bucharest"))),
                     (("Berlijn, Bucharest"), (("Wenen"), ("Warschau, Kiev"), ("Warschau, Wenen"))),
                     (("Warschau, Bucharest"), (("Wenen"),("Kiev"),("Berlijn, Wenen"))),
                     (("Berlijn, Wenen"),(("Warschau"),("Warschau, Kiev"))),
                     (("Berlijn, Warschau"),(("Wenen"),("Wenen, Kiev"))),
                     (("Warschau, Wenen"),(("Berlijn"), ("Kiev"), ("Kiev, Bucharest"))),
                     (("Kiev, Bucharest"),(("Wenen"),("Warschau, Wenen"))),
                     (("Kiev, Wenen"),(("Bucharest"),("Warschau"),("Warschau, Berlijn"))),
                     (("Berlijn2, Kiev2"), (("Warschau"), ("Wenen"), ("Warschau, Wenen"), ("Wenen, Bucharest"))),
                     (("Berlijn2, Bucharest2"), (("Wenen"), ("Warschau, Kiev"), ("Warschau, Wenen"))),
                     (("Warschau2, Bucharest2"), (("Wenen"), ("Kiev"), ("Berlijn, Wenen"))),
                     (("Berlijn2, Wenen2"), (("Warschau"), ("Warschau, Kiev"))),
                     (("Berlijn2, Warschau2"), (("Wenen"), ("Wenen, Kiev"))),
                     (("Warschau2, Wenen2"), (("Berlijn"), ("Kiev"), ("Kiev, Bucharest"))),
                     (("Kiev2, Bucharest2"), (("Wenen"), ("Warschau, Wenen"))),
                     (("Kiev2, Wenen2"), (("Bucharest"), ("Warschau"), ("Warschau, Berlijn")))
                     #Enzovoort kunnen we deze hardcoden
               ]
        random.shuffle(self.missions)  # Schud de missies door mekaar
    #print(missions[0][1][2])  #Dit geeft "Tussen1, Tussen2, Tussen4" uit eerste missie, op deze manier kunnen we dus wel de tuples doorzoeken ;)
                                #TUPLES ZIJN IMMUTABLE --> Onwijzigbaar na initialisatie van values!




    def dealMission(self):
        try:
            return self.missions.pop() #Geeft de laatste item uit de list, dus dankzij shuffle een random mission
        except IndexError: #Als de stapel leeg is zullen we een IndexError krijgen en opvangen
            return("leeg")
