from tkinter import messagebox

import networkx as nx #soort van graph waar we het spelbord van kunnen maken
import Beurt
import Route
import Speler
import CPUSpeler
#import os

from tkinter import *


#from PIL import Image, ImageTk

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GUI:


    def start(self):
        # Startscherm, hierin zal de speler terrechtkomen bij het opstarten van het spel vanuit hier zal hij zijn geg. moeten invullen en doorgaan
        def close_start():
            master.destroy()

        def buttonstart():

            if len(e1.get()) != 0:
                if agevar.get() != 0:
                    # controleren dat belangrijkste textvakken niet leeg zijn, andere tekstvakken (CPU spelers)
                    username = e1.get()
                    age = agevar.get()
                    messagebox.showinfo("Hello Python", "Hello " + username + " : " + age)
                    if len(e2.get()) == 0:
                        cpu1 = "Patrick"
                    else:
                        cpu1 = e2.get()

                    if len(e3.get()) == 0:
                        cpu2 = "Staf"
                    else:
                        cpu2 = e3.get()

                    if len(e4.get()) == 0:
                        cpu3 = "Marc"
                    else:
                        cpu3 = e4.get()

                    cpunamen = []
                    cpunamen.append(cpu1)
                    cpunamen.append(cpu2)
                    cpunamen.append(cpu3)
                    #CPU  spelers genereren adhv gegevens
                    beurt = Beurt.Beurt(username, age, 'pink', cpunamen);
                    #controle print (wordt niet getoond aan gebruiker)
                    print(beurt.return_player(2).get_name())

                    listOfCities = [
                        "Berlijn", "Wenen", "Warschau", "Kiev", "Boekarest"  # 0, 1, 2, 3, 4
                    ]

                    routes = []
                    #Hier voegen we onze routes toe, dit zal ten alle tijden gehardcoded moeten worden...
                    # rou = Route.Route('', 0, ["", ""], 0)
                    routes.append(Route.Route('r', 1, [listOfCities[1], listOfCities[0]], 0))  # Berlijn (yellow)
                    #routes.append(Route.Route('g', 1, [listOfCities[1], listOfCities[0]], 0))  # Berlijn (red)
                    # Warschau to
                    routes.append(Route.Route('b', 2, [listOfCities[2], listOfCities[0]], 0))  # Berlijn (blue)
                    #routes.append(Route.Route('g', 2, [listOfCities[2], listOfCities[0]], 0))  # Berlijn (green)
                    routes.append(Route.Route('b', 1, [listOfCities[2], listOfCities[1]], 0))  # Wenen (black)
                    # Kiev to
                    routes.append(Route.Route('r', 3, [listOfCities[3], listOfCities[1]], 0))  # Wenen (white)
                    routes.append(Route.Route('g', 1, [listOfCities[3], listOfCities[2]], 0))  # Warschau (yellow)
                    # Boekarest to
                    routes.append(Route.Route('g', 2, [listOfCities[4], listOfCities[1]], 0))  # Wenen (yellow)
                    #routes.append(Route.Route('b', 2, [listOfCities[4], listOfCities[1]], 0))  # Wenen (blue)
                    routes.append(Route.Route('r', 2, [listOfCities[4], listOfCities[3]], 0))  # Kiev (red)

                    master.destroy()
                    my_gui.spelerstats(beurt, routes)

                else:
                    #foutcontrole
                    messagebox.showwarning("Fout", "Gelieve al de nodige gegevens in te vullen ")
            else:
                #foutcontrole
                messagebox.showwarning("Fout", "Gelieve al de nodige gegevens in te vullen  ")

       #window aanmaken
        master = Tk()
        master.wm_title("Start")

        #achtergrond afbeelding
        b_image = PhotoImage(file="maxresdefault.png")
        b_image = b_image.zoom(1)
        b_image = b_image.subsample(1)
        bg_label = Label(master, image=b_image)
        bg_label.place(x=0, y=0, width=480, height=160)

        #opmaak
        Label(master, text="Speler naam * - leeftijd * ").grid(row=0, column=4)
        Label(master, text="CPU1 naam").grid(row=1, column=4)
        Label(master, text="CPU2 naam").grid(row=2, column=4)
        Label(master, text="CPU3 naam").grid(row=3, column=4)

        #opmaak
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
        #Methode om het spelbord te testen... om nieuwigheden eerst hier in te implementeren alvorens ze toe te voegen aan het actuele spel.
        listOfCities = [
            "Berlijn", "Wenen", "Warschau", "Kiev", "Boekarest"  # 0, 1, 2, 3, 4
        ]

        routes = []
        # Berlijn to
        # Wenen to
        #rou = Route.Route('', 0, ["", ""], 0)
        routes.append(Route.Route('b', 1, [listOfCities[1], listOfCities[0]], 0))  # Berlijn (yellow)
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

        #graph tekenen
        board = nx.MultiDiGraph()

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
          board.add_edge(route.get_cities()[0], route.get_cities()[1], color=route.get_color(), weight=route.get_pathCost(), title=str(route.get_pathCost()) + " " + str(route.get_occupiedBy()))
          # controle print (wordt niet getoond aan gebruiker)
          print(route.get_cities()[0] + " naar " + route.get_cities()[1] +  " kleur " + route.get_color())

        #edges selecteren, kleuren filteren, gewichten filteren
        edges = board.edges()
        colors = [board[u][v]['color'] for u, v in edges]
        weights = [board[u][v]['weight'] for u, v in edges]

        pos = nx.get_node_attributes(board, 'pos')

        #kopie van het bord bewaren
        copyBoard = board.copy()

        edge_labels = nx.get_edge_attributes(board, 'title')
        nx.draw(board, pos, edges=edges, edge_color=colors, width=weights, with_labels=True)
        #nx.draw_networkx_edge_labels(board,pos, edge_labels=weights)
        #nx.draw_networkx_nodes(board, pos, node_size=700)
        nx.draw_networkx_edge_labels(board, pos, edge_labels=edge_labels)

        plt.axis('off')
        plt.show()

        return routes

    def win(self, beurt):
        #speler komt op dit scherm uit als er aan de eindvoorwaarden voldaan is...
        master = Tk()
        master.wm_title("Winner")

        bg_image = PhotoImage(file="win.png", )

        bg_label = Label(master, image=bg_image)

        bg_label.pack()
        Label(master, text= "'" + beurt.return_player(1).get_name() + "' WINT! Feestje! Amai, tof seg! Hoho, leuk spelletje (wel moeilijk om te programeren denk ik)!", bg="black", fg="white", font=("Helvetica", 30)).pack()

        mainloop(0)

    def spelerstats(self, beurt, routes): #uiteraard moeten beurt en routes steeds worden doorgegeven tussen de verschillende beurten
        #Dit is het toegangscherm dat de speler te zien krijgt bij het spelen van het spel

        root = Tk()

        #achtergrondafbeelding
        bg_image = PhotoImage(file="maxresdefault.png", )
        bg_image = bg_image.zoom(1)
        bg_image = bg_image.subsample(1)
        bg_label = Label(root, image=bg_image)
        bg_label.place(x=0, y=0, width=980, height=720)


        root.wm_title("Spelersbord")
        # Quit when the window is done !!
        root.wm_protocol('WM_DELETE_WINDOW', root.quit)

        def updatescore():
            #Methode binnen spelerstat om het scorebord up te daten
            Label(root, text=beurt.return_player(1).get_pawns()).grid(row=5, column=6)
            Label(root, text=beurt.return_player(2).get_pawns()).grid(row=6, column=6)
            Label(root, text=beurt.return_player(3).get_pawns()).grid(row=7, column=6)
            Label(root, text=beurt.return_player(4).get_pawns()).grid(row=8, column=6)

            Label(root, text=beurt.return_player(1).get_missionscomp()).grid(row=5, column=5)
            Label(root, text=beurt.return_player(2).get_missionscomp()).grid(row=6, column=5)
            Label(root, text=beurt.return_player(3).get_missionscomp()).grid(row=7, column=5)
            Label(root, text=beurt.return_player(4).get_missionscomp()).grid(row=8, column=5)

            Label(root, text=beurt.return_player(1).get_name()).grid(row=5, column=4)
            Label(root, text=beurt.return_player(2).get_name()).grid(row=6, column=4)
            Label(root, text=beurt.return_player(3).get_name()).grid(row=7, column=4)
            Label(root, text=beurt.return_player(4).get_name()).grid(row=8, column=4)

        def updatedash():
            #Methode binnen spelerstat om de het dashboard van de speler up te daten
            Label(root, text=beurt.return_player(1).get_traincards('r')).grid(row=9, column=1, sticky="W")
            Label(root, text=beurt.return_player(1).get_traincards('g')).grid(row=10, column=1, sticky="W")
            Label(root, text=beurt.return_player(1).get_traincards('b')).grid(row=11, column=1, sticky="W")
            Label(root, text=beurt.return_player(1).get_traincards('wild')).grid(row=12, column=1, sticky="W")

            Label(root, text=beurt.return_player(1).get_pawns()).grid(row=13, column=1, sticky="W")

            Label(root, text=beurt.return_player(1).get_mission(1)[0]).grid(row=14, column=1, sticky="W")
            Label(root, text=beurt.return_player(1).get_mission(2)[0]).grid(row=15, column=1, sticky="W")

        #figuur in canvas plotten
        f = plt.figure(figsize=(5, 4))
        a = f.add_subplot(111)
        plt.axis('off')

        board = nx.Graph()

        def refreshgraph():
            #methode om de graph up te daten na een beurt

            board.clear()

            board.add_node("Berlijn", pos=(1, 1))
            board.add_node("Wenen", pos=(2, 0))
            board.add_node("Warschau", pos=(3, 1))
            board.add_node("Kiev", pos=(5, 0))
            board.add_node("Boekarest", pos=(5, -2))

            for route in routes:

              #                 # from city                # to city                  # path cost           # color of path       #label die meegegeven wordt
              if (route.get_occupiedBy() == 0):
                  ingenomen = ' v '
              else:
                  ingenomen = beurt.return_player(route.get_occupiedBy()).get_name()
              board.add_edge(route.get_cities()[0], route.get_cities()[1], color=route.get_color(), weight=route.get_pathCost(), title= str(route.get_pathCost()) + " ; " + ingenomen)
              # controle print (wordt niet getoond aan gebruiker)
              print(route.get_cities()[0] + " naar " + route.get_cities()[1] +  " kleur " + route.get_color())

            edges = board.edges()
            colors = [board[u][v]['color'] for u, v in edges]
            weights = [board[u][v]['weight'] for u, v in edges]

            pos = nx.get_node_attributes(board, 'pos')

            #
            edge_labels = nx.get_edge_attributes(board, 'title')
            nx.draw(board, pos, edges=edges, edge_color=colors, width=weights, with_labels=True, ax=a)
            nx.draw_networkx_edge_labels(board, pos, edge_labels=edge_labels)

            canvas = FigureCanvasTkAgg(f, master=root)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=1)

        # Canvas maken en hier graph in tekenen
        refreshgraph()



        def extra_tc():
            try:
                for i in range(2):
                    beurt.extra_traincard(beurt.return_player(1))
                    updatedash()
                    updatescore()
            except ValueError:
                winner()

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

            def next_graph():
                print(vanvar.get() + " naar " + naarvar.get() )

                routeX = beurt.search_route([vanvar.get(),naarvar.get()], routes)
                print(routeX)
                beep = beurt.conquer_route(routeX, beurt.return_player(1))
                print(str(beep) + " statuscode ")

                updatedash()
                updatescore()
                refreshgraph()
                popup.destroy()
                if (beep==0):
                    messagebox.showerror("Goed gedaan man!", "Deze route is succesvol ingenomen")
                if (beep==1):
                    messagebox.showerror("Oops foutje gemaakt", "Deze route is reeds ingenomen")
                if (beep==2):
                    messagebox.showerror("Oops foutje gemaakt", "Je hebt niet voldoende treinkaarten om deze route in te nemen")
                if (beep==3):
                    messagebox.showerror("Oops foutje gemaakt", "Je hebt niet voldoende pionnen om deze route in te nemen ")

            Label(popup, text="Van").grid(row=0, column=0)
            #evan = Entry(popup)
            dropvan.grid(row=0, column=1)
            Label(popup, text="Naar").grid(row=1, column=0)
            #enaar = Entry(popup)
            dropnaar.grid(row=1, column=1)
            bIn = Button(popup, text="INNEMEN", command=next_graph)
            bAn = Button(popup, text="Annuleer", command=cancel_route)
            bIn.grid(row=2, column =0)
            bAn.grid(row=2, column=1)

            mainloop(1)

        def winner():

            root.destroy()
            my_gui.win(beurt)

        def missiewissel():
            try:
                beurt.swap_mission(beurt.return_player(1))
                updatedash()
            except ValueError:
                winner()

        #Control Buttons
        #Methodes uit beurt vasthangen aan deze routes
        b = Button(root, text="Extra treinkaart", command=extra_tc)
        b1 = Button(root, text="Route innemen", command=route_innemen)
        b2 = Button(root, text="Missie wisselen", command=missiewissel)
        b3 = Button(root, text="Valsspelen is ook spelen", command=winner)

        b.grid(row=4)
        b1.grid(row=5)
        b2.grid(row=6)
        b3.grid(row=7)


        #Spelerstats displayen
        Label(root, text="Treinkaarten Rood", bg="grey", fg="white").grid(row=9, column=0)
        Label(root, text="Treinkaarten Groen", bg="grey", fg="white").grid(row=10, column=0)
        Label(root, text="Treinkaarten Blauw", bg="grey", fg="white").grid(row=11, column=0)
        Label(root, text="Treinkaarten Wild", bg="grey", fg="white").grid(row=12, column=0)
        Label(root, text="Pionnen", bg="grey", fg="white").grid(row=13, column=0)

        Label(root, text="Missie1", bg="grey", fg="white").grid(row=14, column=0)

        Label(root, text="Missie2", bg="grey", fg="white").grid(row=15, column=0)

        #SCOREBORD
        #tabel aanmaken

        Label(root, text="Spelersnamen", bg="black", fg="white").grid(row=4, column=4)
        Label(root, text="Voltooide missies", bg="black", fg="white").grid(row=4, column=5)
        Label(root, text="Pionnen", bg="black", fg="white").grid(row=4, column=6)

        #als rest klaar is dan scorebord van goed naar slecht laten tonen (voorlopig: this will do)

        updatedash()
        updatescore()

        mainloop(1)
        #Hierin speler statistieken (pionnen, kaarten, etc) laten zien + besturingsknoppen
        #Ook scorebord


my_gui = GUI()
while True:
    my_gui.start()
    #my_gui.spelerstats()

