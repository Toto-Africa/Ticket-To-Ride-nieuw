from tkinter import messagebox

import networkx as nx #soort van graph waar we het spelbord van kunnen maken
import Beurt
import Route
import Speler
#import os

from tkinter import *


#from PIL import Image, ImageTk

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GUI:


    def start(self):

        def close_start():
            master.destroy()

        def buttonstart():
            # hier dan overgaan naar beurt?
            # hoe doe ik da praktisch? :D

            if len(e1.get()) != 0:
                if agevar.get() != 0:
                    # controleren dat belangrijkste textvakken niet leeg zijn
                    username = e1.get()
                    age = agevar.get()
                    messagebox.showinfo("Hello Python", "Hello " + username + " : " + age)
                    if len(e2.get()) == 0:
                        cpu1 = "Patrick"
                    else:
                        cpu1 = e2.get()

                    if len(e4.get()) == 0:
                        cpu2 = "Staf"
                    else:
                        cpu2 = e3.get()

                    if len(e3.get()) == 0:
                        cpu3 = "Marc"
                    else:
                        cpu3 = e4.get()

                    cpunamen = []
                    cpunamen.append(cpu1)
                    cpunamen.append(cpu2)
                    cpunamen.append(cpu3)
                    beurt = Beurt.Beurt(username, age, 'pink', cpunamen);

                    print(beurt.return_player(1).get_name())

                    master.destroy()
                    my_gui.spelerstats()

                else:
                    messagebox.showwarning("Fout", "Gelieve al de nodige gegevens in te vullen ")
            else:
                messagebox.showwarning("Fout", "Gelieve al de nodige gegevens in te vullen  ")

                    # doorgeven en ga naar beurt dan? hoe doe ik da juist? :D variables zijn dan: (username, age, cpu1-3)
                    # kleuren moeten hier ook nog bij
                    # --> effe hardcoden denk ik

        # eerst namen ingeven: spelers aanmaken dus

        master = Tk()
        master.wm_title("Start")

        bg_image = PhotoImage(file="maxresdefault.png", )
        bg_image = bg_image.zoom(1)
        bg_image = bg_image.subsample(1)
        bg_label = Label(master, image=bg_image)
        bg_label.place(x=0, y=0, width=480, height=160)

        Label(master, text="Speler naam * - leeftijd * ").grid(row=0, column=4)
        Label(master, text="CPU1 naam").grid(row=1, column=4)
        Label(master, text="CPU2 naam").grid(row=2, column=4)
        Label(master, text="CPU3 naam").grid(row=3, column=4)

        e1 = Entry(master)
        e2 = Entry(master)
        e3 = Entry(master)
        e4 = Entry(master)

        ages = []

        for i in range(1, 100):
            ages.append(i)

        agevar = StringVar(master)
        drop = OptionMenu(master, agevar, *ages)

        b1 = Button(master, text="Start Spel", command=buttonstart) #als er op button gedrukt wordt dan voeren we 'buttonstart' uit
        b2 = Button(master, text="Afsluiten", command=close_start)

        e1.grid(row=0, column=5)
        drop.grid(row=0, column=6)
        e2.grid(row=1, column=5)
        e3.grid(row=2, column=5)
        e4.grid(row=3, column=5)
        b1.grid(row=4, column=5)
        b2.grid(row=4, column=6)

        mainloop(0)

    def initbord(self):

        # subset van kaart
        listOfCities = [
            "Berlijn", "Wenen", "Warschau", "Kiev", "Boekarest"  # 0, 1, 2, 3, 4
        ]

        routes = []
        # Berlijn to
        # Wenen to
        #rou = Route.Route('', 0, ["", ""], 0)
        routes.append(Route.Route('r', 1, [listOfCities[1], listOfCities[0]], 0))  # Berlijn (yellow)
        routes.append(Route.Route('r', 1, [listOfCities[1], listOfCities[0]], 0))  # Berlijn (red)
        # Warschau to
        routes.append(Route.Route('b', 2, [listOfCities[2], listOfCities[0]], 0))  # Berlijn (blue)
        routes.append(Route.Route('g', 2, [listOfCities[2], listOfCities[0]], 0))  # Berlijn (green)
        routes.append(Route.Route('b', 1, [listOfCities[2], listOfCities[1]], 0))  # Wenen (black)
        # Kiev to
        routes.append(Route.Route('r', 3, [listOfCities[3], listOfCities[1]], 0))  # Wenen (white)
        routes.append(Route.Route('g', 1, [listOfCities[3], listOfCities[2]], 0))  # Warschau (yellow)
        # Boekarest to
        routes.append(Route.Route('r', 2, [listOfCities[4], listOfCities[1]], 0))  # Wenen (yellow)
        routes.append(Route.Route('b', 2, [listOfCities[4], listOfCities[1]], 0))  # Wenen (blue)
        routes.append(Route.Route('r', 2, [listOfCities[4], listOfCities[3]], 0))  # Kiev (red)

        board = nx.Graph()

        board.add_node("Berlijn", pos=(1, 1))
        board.add_node("Wenen", pos=(2, 0))
        board.add_node("Warschau", pos=(3, 1))
        board.add_node("Kiev", pos=(5, 0))
        board.add_node("Boekarest", pos=(5, -2))
        #for city in listOfCities:
         #   board.add_node(city)
          #  print(city)

        for route in routes:
          #                 # from city                # to city                  # path cost                      # color of path
          board.add_edge(route.get_cities()[0], route.get_cities()[1], color=route.get_color(), weight=route.get_pathCost())
          print(route.get_cities()[0] + " naar " + route.get_cities()[1] +  " kleur " + route.get_color())

        edges = board.edges()
        colors = [board[u][v]['color'] for u, v in edges]
        weights = [board[u][v]['weight'] for u, v in edges]

        pos = nx.get_node_attributes(board, 'pos')

        copyBoard = board.copy()

        nx.draw(board, pos, edges=edges, edge_color=colors, width=weights, with_labels=True)
        #nx.draw_networkx_nodes(board, pos, node_size=700)
        #nx.draw_networkx_edge_labels(board, pos)

        plt.axis('off')
        plt.show()

        return routes

    def win(self):

        master = Tk()
        master.wm_title("Winner")

        bg_image = PhotoImage(file="win.png", )

        bg_label = Label(master, image=bg_image)

        bg_label.pack()
        Label(master, text="... WINT! Feestje! Amai, tof seg! Hoho, leuk spelletje!", bg="black", fg="white", font=("Helvetica", 30)).pack()

        mainloop(0)

    def spelerstats(self): #hier gaan we het attribuut speler (en beurt????) zeker moeten megeven, eventueel ook de graph of list met spelers

        root = Tk()

        bg_image = PhotoImage(file="maxresdefault.png", )
        bg_image = bg_image.zoom(1)
        bg_image = bg_image.subsample(1)
        bg_label = Label(root, image=bg_image)
        bg_label.place(x=0, y=0, width=980, height=720)


        root.wm_title("Spelersbord")
        # Quit when the window is done !!!!WERKT NOG ALTIJD NIET GOED!!!
        root.wm_protocol('WM_DELETE_WINDOW', root.quit)

        f = plt.figure(figsize=(5, 4))
        a = f.add_subplot(111)
        plt.axis('off')

        # INSERT HIER ONZE GRAPH (dit is voorbeeldgraph)
        #OP termijn zou route moeten doorgegeven worden, en dan kan er veel van dieje zever hieronder wweg
        listOfCities = [
            "Berlijn", "Wenen", "Warschau", "Kiev", "Boekarest"  # 0, 1, 2, 3, 4
        ]

        routes = []
        #
        #rou = Route.Route('', 0, ["", ""], 0)
        routes.append(Route.Route('r', 1, [listOfCities[1], listOfCities[0]], 0))  # Berlijn (yellow)
        routes.append(Route.Route('r', 1, [listOfCities[1], listOfCities[0]], 0))  # Berlijn (red)
        # Warschau to
        routes.append(Route.Route('b', 2, [listOfCities[2], listOfCities[0]], 0))  # Berlijn (blue)
        routes.append(Route.Route('g', 2, [listOfCities[2], listOfCities[0]], 0))  # Berlijn (green)
        routes.append(Route.Route('b', 1, [listOfCities[2], listOfCities[1]], 0))  # Wenen (black)
        # Kiev to
        routes.append(Route.Route('r', 3, [listOfCities[3], listOfCities[1]], 0))  # Wenen (white)
        routes.append(Route.Route('g', 1, [listOfCities[3], listOfCities[2]], 0))  # Warschau (yellow)
        # Boekarest to
        routes.append(Route.Route('r', 2, [listOfCities[4], listOfCities[1]], 0))  # Wenen (yellow)
        routes.append(Route.Route('b', 2, [listOfCities[4], listOfCities[1]], 0))  # Wenen (blue)
        routes.append(Route.Route('r', 2, [listOfCities[4], listOfCities[3]], 0))  # Kiev (red)

        board = nx.Graph()

        board.add_node("Berlijn", pos=(1, 1))
        board.add_node("Wenen", pos=(2, 0))
        board.add_node("Warschau", pos=(3, 1))
        board.add_node("Kiev", pos=(5, 0))
        board.add_node("Boekarest", pos=(5, -2))
        #for city in listOfCities:
         #   board.add_node(city)
          #  print(city)

        for route in routes:
          #                 # from city                # to city                  # path cost                      # color of path
          board.add_edge(route.get_cities()[0], route.get_cities()[1], color=route.get_color(), weight=route.get_pathCost())
          print(route.get_cities()[0] + " naar " + route.get_cities()[1] +  " kleur " + route.get_color())

        edges = board.edges()
        colors = [board[u][v]['color'] for u, v in edges]
        weights = [board[u][v]['weight'] for u, v in edges]

        pos = nx.get_node_attributes(board, 'pos')

        copyBoard = board.copy()

        nx.draw(board, pos, edges=edges, edge_color=colors, width=weights, with_labels=True, ax=a)

        # Canvas maken en hier graph in tekenen
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1)

        def next_graph():
            messagebox.showinfo("test")



        def route_innemen():
            popup = Tk()

            listOfCities = [
                "Berlijn", "Wenen", "Warschau", "Kiev", "Boekarest"  # 0, 1, 2, 3, 4
            ]

            vanvar = StringVar(popup)
            naarvar = StringVar(popup)

            dropvan = OptionMenu(popup, vanvar, *listOfCities)
            dropnaar = OptionMenu(popup, naarvar, *listOfCities)

            def cancel_route():
                popup.destroy()

            Label(popup, text="Van").grid(row=0, column=0)
            #evan = Entry(popup)
            dropvan.grid(row=0, column=1)
            Label(popup, text="Naar").grid(row=1, column=0)
            #enaar = Entry(popup)
            dropnaar.grid(row=1, column=1)
            b = Button(popup, text="INNEMEN", command=next_graph)
            b2 = Button(popup, text="Annuleer", command=cancel_route)
            b.grid(row=2, column =0)
            b2.grid(row=2, column=1)


            mainloop(1)

        #Control Buttons
        #Methodes uit beurt vasthangen aan deze routes
        b = Button(root, text="Extra treinkaart", command=next_graph)
        b1 = Button(root, text="Route innemen", command=route_innemen)
        b2 = Button(root, text="Missie wisselen", command=next_graph)

        b.grid(row=4)
        b1.grid(row=5)
        b2.grid(row=6)

        #Spelerstats displayen
        Label(root, text="Treinkaarten (R;G;Z;W;B;G)", bg="grey", fg="white").grid(row=9, column=0)
        Label(root, text="alle kaarten van de speler").grid(row=9, column=1, sticky="W")
        Label(root, text="Pionnen", bg="grey", fg="white").grid(row=10, column=0)
        Label(root, text="speler.pawns").grid(row=10, column = 1, sticky="W")
        Label(root, text="Missie1", bg="grey", fg="white").grid(row=11, column=0)
        Label(root, text="speler.missions1").grid(row=11, column=1, sticky="W")
        Label(root, text="Missie2", bg="grey", fg="white").grid(row=12, column=0)
        Label(root, text="speler.missions2").grid(row=12, column= 1, sticky="W")

        #SCOREBORD
        #tabel aanmaken

        Label(root, text="Spelersnamen", bg="black", fg="white").grid(row=4, column=4)
        Label(root, text="Voltooide missies", bg="black", fg="white").grid(row=4, column=5)
        Label(root, text="Pionnen", bg="black", fg="white").grid(row=4, column=6)
        Label(root, text="Toto africa").grid(row=5, column=4)
        Label(root, text="Elmer").grid(row=6, column=4)
        Label(root, text="Jan").grid(row=7, column=4)
        Label(root, text="Dries").grid(row=8, column=4)

        #als rest klaar is dan scorebord van goed naar slecht laten tonen (voorlopig: this will do)

        mainloop(1)
        #Hierin speler statistieken (pionnen, kaarten, etc) laten zien + besturingsknoppen
        #Ook scorebord


my_gui = GUI()
while True:
    my_gui.start()
    #my_gui.spelerstats()

