from tkinter import *
from tkinter import messagebox
import tkinter
from ia_1 import ia

# Crée la fenêtre principale
gamewindow = Tk()
gamewindow.title("Tic Tac Toe")
gamewindow.geometry("800x800+400+400")
gamewindow.configure(background="#87CEEB")
# Définit les cadres pour la disposition des éléments
topframe = Frame(gamewindow, width=798, height=390, bd=5, relief=RIDGE, bg="#FFB6C1" , padx=2, pady=4)
topframe.grid(row=0, column=0)

downframe = Frame(gamewindow, width=798, height=290, bd=5, relief=RIDGE, bg="#FFFF99", padx=2, pady=4)
downframe.grid(row=1, column=0)

bottomframe = Frame(gamewindow, width=798, height=290, bd=5, relief=RIDGE, bg="silver", padx=2, pady=4)
bottomframe.grid(row=2, column=0)
# Initialise les variables pour le score des joueurs
playerx = IntVar()
playero = IntVar()

playerx.set(0)
playero.set(0)
# Variables pour les boutons et le suivi du tour
button = StringVar()
click = True

# Fonction pour gérer le clic sur un bouton
def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "x"
        click = False
        scorekeeper()

    elif buttons["text"] == " " and click == False:
        buttons["text"] = "o"
        click = True
        scorekeeper()
# Fonction pour réinitialiser la couleur des boutons
def colorreturn():
    button1.configure(fg="black")  
    button2.configure(fg="black") 
    button3.configure(fg="black") 
    button4.configure(fg="black") 
    button5.configure(fg="black") 
    button6.configure(fg="black") 
    button7.configure(fg="black") 
    button8.configure(fg="black") 
    button9.configure(fg="black")       

# Fonction pour vérifier le résultat de la partie
def scorekeeper():
    # Liste des combinaisons gagnantes possibles
    winning_combinations = [
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9],
        [button1, button4, button7],
        [button2, button5, button8],
        [button3, button6, button9],
        [button1, button5, button9],
        [button3, button5, button7]
    ]
    # Compte le nombre total de mouvements effectués
    total_moves = sum(button["text"] != " " for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9])
    
    # Vérifie s'il y a un match nul
    if total_moves == 9:
        messagebox.showinfo("Match Nul", "La partie est un match nul")
        colorreturn()
        return  # Ajoutez cette ligne pour sortir de la fonction après avoir trouvé un match nul
   
    # Vérifie les combinaisons gagnantes
    for combo in winning_combinations:
        if combo[0]["text"] == "x" and combo[1]["text"] == "x" and combo[2]["text"] == "x":
            for button in combo:
                button.configure(fg="green")
            playerx.set(playerx.get() + 1)
            messagebox.showinfo("Le gagnant est X", "La partie est terminée")
            colorreturn()
            return  # Ajoutez cette ligne pour sortir de la fonction après avoir trouvé une combinaison gagnante
        elif combo[0]["text"] == "o" and combo[1]["text"] == "o" and combo[2]["text"] == "o":
            for button in combo:
                button.configure(fg="green")
            playero.set(playero.get() + 1)
            messagebox.showinfo("Le gagnant est O", "La partie est terminée")
            colorreturn()
            return  # Ajoutez cette ligne pour sortir de la fonction après avoir trouvé une combinaison gagnante
            # Vérifiez s'il y a un match nul
            #if all(button["text"] != " " for row in buttons for button in row) and not any(combo[0]["text"] == "x" or combo[0]["text"] == "o" for combo in winning_combinations):
            messagebox.showinfo("Match Nul", "La partie est un match nul")
            colorreturn()
            return  # Ajoutez cette ligne pour sortir de la fonction après avoir trouvé un match nul
            

    # Vérifie les combinaisons gagnantes dans les colonnes individuelles
    # Vérifie les combinaisons gagnantes dans les lignes individuelles
    # Vérifie les combinaisons gagnantes dans les diagonales    
    if(button1["text"] == "x" and button2["text"] == "x" and button3["text"] == "x"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playerx.get())
        score = (s + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("winer est x", "la game est terminer")  
        colorreturn()

    elif(button1["text"] == "o" and button2["text"] == "o" and button3["text"] == "o"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playero.get())
        score = (s + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("winer est o", "la game est terminer") 
        colorreturn()

    elif(button4["text"] == "x" and button5["text"] == "x" and button6["text"] == "x"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playerx.get())
        score = (s + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("winer est x", "la game est terminer")   
        colorreturn()  

    elif(button4["text"] == "o" and button5["text"] == "o" and button6["text"] == "o"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playero.get())
        score = (s + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("winer est o", "la game est terminer")  
        colorreturn()

    elif(button7["text"] == "x" and button8["text"] == "x" and button9["text"] == "x"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playerx.get())
        score = (s + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("winer est x", "la game est terminer") 
        colorreturn()

    elif(button7["text"] == "o" and button8["text"] == "o" and button9["text"] == "o"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playero.get())
        score = (s + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("winer est o", "la game est terminer")
        colorreturn()  

    elif(button1["text"] == "x" and button4["text"] == "x" and button7["text"] == "x"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playerx.get())
        score = (s + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("winer est x", "la game est terminer") 
        colorreturn()

    elif(button1["text"] == "o" and button4["text"] == "o" and button7["text"] == "o"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playero.get())
        score = (s + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("winer est o", "la game est terminer") 
        colorreturn()  

    elif(button2["text"] == "x" and button5["text"] == "x" and button8["text"] == "x"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playerx.get())
        score = (s + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("winer est x", "la game est terminer") 
        colorreturn()

    elif(button2["text"] == "o" and button5["text"] == "o" and button8["text"] == "o"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playero.get())
        score = (s + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("winer est o", "la game est terminer")  
        colorreturn()

    elif(button3["text"] == "x" and button6["text"] == "x" and button9["text"] == "x"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playerx.get())
        score = (s + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("winer est x", "la game est terminer")
        colorreturn() 

    elif(button3["text"] == "o" and button6["text"] == "o" and button9["text"] == "o"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playero.get())
        score = (s + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("winer est o", "la game est terminer") 
        colorreturn()

    elif(button1["text"] == "x" and button5["text"] == "x" and button9["text"] == "x"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playerx.get())
        score = (s + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("winer est x", "la game est terminer")
        colorreturn()  

    elif(button1["text"] == "o" and button5["text"] == "o" and button9["text"] == "o"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playero.get())
        score = (s + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("winer est o", "la game est terminer") 
        colorreturn()

    elif(button3["text"] == "x" and button5["text"] == "x" and button7["text"] == "x"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playerx.get())
        score = (s + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("winer est x", "la game est terminer")
        colorreturn()  

    elif(button3["text"] == "o" and button5["text"] == "o" and button7["text"] == "o"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green") 
        s = float(playero.get())
        score = (s + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("winer est o", "la game est terminer")
        colorreturn()


def restart():
    # Réinitialise le texte des boutons à un espace vide
    button1["text"] = " "  
    button2["text"] = " "  
    button3["text"] = " "  
    button4["text"] = " "  
    button5["text"] = " "  
    button6["text"] = " "  
    button7["text"] = " "  
    button8["text"] = " "  
    button9["text"] = " "  

    # Rétablit la couleur d'origine des boutons
    button1.configure(background="silver")
    button2.configure(background="silver")
    button3.configure(background="silver")
    button4.configure(background="silver")
    button5.configure(background="silver")
    button6.configure(background="silver")
    button7.configure(background="silver")
    button8.configure(background="silver")
    button9.configure(background="silver")


# Fonction appelée pour commencer une nouvelle partie
def newgame():
    # Réinitialise le plateau de jeu et les scores des joueurs
    restart()
    playerx.set(0)
    playero.set(0)
# Création des boutons de jeu avec les commandes associées
button1 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button1))
button1.grid(row=1, column=0, sticky= S+N+E+W) 

button2 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button2))
button2.grid(row=1, column=1, sticky= S+N+E+W) 

button3 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button3))
button3.grid(row=1, column=2, sticky= S+N+E+W) 

button4 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button4))
button4.grid(row=2, column=0, sticky= S+N+E+W) 

button5 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button5))
button5.grid(row=2, column=1, sticky= S+N+E+W) 

button6 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button6))
button6.grid(row=2, column=2, sticky= S+N+E+W) 

button7 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button7))
button7.grid(row=3, column=0, sticky= S+N+E+W) 

button8 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button8))
button8.grid(row=3, column=1, sticky= S+N+E+W) 

button9 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button9))
button9.grid(row=3, column=2, sticky= S+N+E+W) 

# Crée une étiquette pour afficher le résultat du joueur O
labelplayero = Label(downframe, font=("arial", 26,"bold"), text="Résultat la joueur o :", padx=2, pady=2, bg="#FFA07A")
labelplayero.grid(row=0, column=0)
# Crée une étiquette pour afficher le résultat du joueur X
labelplayerx = Label(downframe, font=("arial", 26,"bold"), text="Résultat la joueur x :", padx=2, pady=2, bg="#FFA07A")
labelplayerx.grid(row=1, column=0)
# Crée une entrée pour afficher le résultat du joueur X
resultx = Entry(downframe, font=("arial", 26,"bold"), bd=2, fg="black", textvariable=playerx)
resultx.grid(row=1, column=1)
# Crée une entrée pour afficher le résultat du joueur O
resulto = Entry(downframe, font=("arial", 26,"bold"), bd=2, fg="black", textvariable=playero)
resulto.grid(row=0, column=1)
# Crée un bouton pour commencer une nouvelle partie
newgamebutton = Button(bottomframe, text="Nouvelle partie ", width=25, height=4, bd=2, bg="#98FF98", fg="black", font=("arial", 12,"bold"), command=newgame)
newgamebutton.grid(row=0, column=3)
# Crée un bouton pour redémarrer la partie actuelle
newstartgamebutton = Button(bottomframe, text="Redémarrer", width=25, height=4, bd=2, bg="#98FF98", fg="black", font=("arial", 12,"bold"), command=restart)
newstartgamebutton.grid(row=0, column=2)
# Crée un bouton pour quitter l'application
exitgamebutton = Button(bottomframe, text="Quitter", width=25, height=4, bd=2, bg="#98FF98", fg="black", command=lambda :quit(gamewindow), font=("arial", 12,"bold"))
exitgamebutton.grid(row=0, column=0)
# Le bouton "Quitter" utilise la commande lambda pour appeler la fonction quit(gamewindow)
# quit(gamewindow) ferme la fenêtre principale de jeu (gamewindow) et termine l'application
# Cela sert de bouton de sortie pour fermer proprement l'application lorsqu'il est cliqué

def get_board_state():
    return [
        [button1["text"], button2["text"], button3["text"]],
        [button4["text"], button5["text"], button6["text"]],
        [button7["text"], button8["text"], button9["text"]]
    ]
def play_ia():
    # Fonction pour le tour de l'IA
    board_state = get_board_state()
    move = ia(board_state, "o")  # "o" représente le signe de l'IA
    if move is not False:
        # Mettez à jour l'interface graphique ou le tableau de jeu avec le mouvement de l'IA
        # Par exemple, si move est 4, cela signifie que l'IA veut jouer à la position 4.
        if move == 0:
            checker(button1)
        elif move == 1:
            checker(button2)
        elif move == 2:
            checker(button3)
        elif move == 3:
            checker(button4)
        elif move == 4:
            checker(button5)
        elif move == 5:
            checker(button6)
        elif move == 6:
            checker(button7)
        elif move == 7:
            checker(button8)
        elif move == 8:
            checker(button9)


gamewindow.mainloop()