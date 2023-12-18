from tkinter import *
from tkinter import messagebox
import tkinter
from ia_1 import ia

gamewindow = Tk()
gamewindow.title("tic tac toe")
gamewindow.geometry("800x800+400+400")
gamewindow.configure(background="#87CEEB")

topframe = Frame(gamewindow, width=798, height=390, bd=5, relief=RIDGE, bg="#FFB6C1" , padx=2, pady=4)
topframe.grid(row=0, column=0)

downframe = Frame(gamewindow, width=798, height=290, bd=5, relief=RIDGE, bg="#FFFF99", padx=2, pady=4)
downframe.grid(row=1, column=0)

bottomframe = Frame(gamewindow, width=798, height=290, bd=5, relief=RIDGE, bg="silver", padx=2, pady=4)
bottomframe.grid(row=2, column=0)

playerx = IntVar()
playero = IntVar()

playerx.set(0)
playero.set(0)

button = StringVar()
click = True

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

def scorekeeper():
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
    total_moves = sum(button["text"] != " " for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9])
    
    if total_moves == 9:
        messagebox.showinfo("Match Nul", "La partie est un match nul")
        colorreturn()
        return  # Ajoutez cette ligne pour sortir de la fonction après avoir trouvé un match nul
   
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



    '''     

    else:
        return
    tkinter.messagebox.showinfo("Match Nul")
    ''' 
def restart():
    button1["text"] = " "  
    button2["text"] = " "  
    button3["text"] = " "  
    button4["text"] = " "  
    button5["text"] = " "  
    button6["text"] = " "  
    button7["text"] = " "  
    button8["text"] = " "  
    button9["text"] = " "  

    button1.configure(background="silver")
    button2.configure(background="silver")
    button3.configure(background="silver")
    button4.configure(background="silver")
    button5.configure(background="silver")
    button6.configure(background="silver")
    button7.configure(background="silver")
    button8.configure(background="silver")
    button9.configure(background="silver")



def newgame():
    restart()
    playerx.set(0)
    playero.set(0)

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


labelplayero = Label(downframe, font=("arial", 26,"bold"), text="Résultat la joueur o :", padx=2, pady=2, bg="#FFA07A")
labelplayero.grid(row=0, column=0)

labelplayerx = Label(downframe, font=("arial", 26,"bold"), text="Résultat la joueur x :", padx=2, pady=2, bg="#FFA07A")
labelplayerx.grid(row=1, column=0)

resultx = Entry(downframe, font=("arial", 26,"bold"), bd=2, fg="black", textvariable=playerx)
resultx.grid(row=1, column=1)

resulto = Entry(downframe, font=("arial", 26,"bold"), bd=2, fg="black", textvariable=playero)
resulto.grid(row=0, column=1)

newgamebutton = Button(bottomframe, text="new game ", width=25, height=4, bd=2, bg="#98FF98", fg="black", font=("arial", 12,"bold"), command=newgame)
newgamebutton.grid(row=0, column=3)

newstartgamebutton = Button(bottomframe, text=" restart", width=25, height=4, bd=2, bg="#98FF98", fg="black", font=("arial", 12,"bold"), command=restart)
newstartgamebutton.grid(row=0, column=2)
"""
nothinkgamebutton = Button(bottomframe, text=" ", width=20, height=4, bd=2, bg="green", fg="black", font=("arial", 12,"bold"),)
nothinkgamebutton.grid(row=0, column=1)
"""
exitgamebutton = Button(bottomframe, text="sorti", width=25, height=4, bd=2, bg="#98FF98", fg="black", command=lambda :quit(gamewindow), font=("arial", 12,"bold"))
exitgamebutton.grid(row=0, column=0)

# Importez la fonction ia depuis le fichier ia.py

"""
# ... (votre code existant)
buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda i=i, j=j: checker(buttons[i][j]))
        buttons[i][j].grid(row=i + 1, column=j, sticky=S + N + E + W)

def play_ia():
    move = ia(get_board_state(), "o")
    if move is not False:
        i, j = move // 3, move % 3
        if buttons[i][j]["text"] == " ":
            buttons[i][j]["text"] = "o"
            scorekeeper()


def play_ia():
    # Fonction pour le tour de l'IA
    move = ia(get_board_state(), "o")  # "o" représente le signe de l'IA
    if move is not False:
        # Mettez à jour l'interface graphique ou le tableau de jeu avec le mouvement de l'IA
        # Par exemple, si move est 4, cela signifie que l'IA veut jouer à la position 4.
        button[move]["text"] = "o"
        scorekeeper()

def play_ia():
    # Fonction pour le tour de l'IA
    move = ia(get_board_state(), "o") # "o" représente le signe de l'IA
    print("IA move:", move)
    if move is not False:
        # Mettez à jour l'interface graphique ou le tableau de jeu avec le mouvement de l'IA
        # Par exemple, si move est 4, cela signifie que l'IA veut jouer à la position 4.
        buttons[move]["text"] = "o"
        scorekeeper()
"""

gamewindow.mainloop()