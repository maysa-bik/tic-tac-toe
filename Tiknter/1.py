from tkinter import *
from tkinter import messagebox
import tkinter

gamewindow = Tk()
gamewindow.title("tic tac toe")
gamewindow.geometry("800x800+400+400")
gamewindow.configure(background='orange')

topframe = Frame(gamewindow, width=798, height=390, bd=5, relief=RIDGE, bg="blue", padx=2, pady=4)
topframe.grid(row=0, column=0)

downframe = Frame(gamewindow, width=798, height=290, bd=5, relief=RIDGE, bg="yellow", padx=2, pady=4)
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

def scorekeeper():
    if(button1["text"] == "x" and button2 == "x" and button3["text"] == "x"):
        button1.configure(background="pink", fg="green")  
        button2.configure(background="pink", fg="green") 
        button3.configure(background="pink", fg="green")  
        s = float(playerx.get())
        score = (s + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("winer est x", "la game est terminer")    

button1 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button1))
button1.grid(row=1, column=0) 

button2 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button2))
button2.grid(row=1, column=1) 

button3 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button3))
button3.grid(row=1, column=2) 

button4 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button4))
button4.grid(row=2, column=0) 

button5 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button5))
button5.grid(row=2, column=1) 

button6 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button6))
button6.grid(row=2, column=2) 

button7 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button7))
button7.grid(row=3, column=0) 

button8 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button8))
button8.grid(row=3, column=1) 

button9 = Button(topframe, text=" ", font=("Times 22 bold"), height=2, width=6, bg="silver", command=lambda :checker(button9))
button9.grid(row=3, column=2) 


labelplayerx = Label(downframe, font=("arial", 26,"bold"), text="Résultat la joueur x :", padx=2, pady=2, bg="gold")
labelplayerx.grid(row=0, column=0)

labelplayero = Label(downframe, font=("arial", 26,"bold"), text="Résultat la joueur o :", padx=2, pady=2, bg="gold")
labelplayero.grid(row=1, column=0)

resultx = Entry(downframe, font=("arial", 26,"bold"), bd=2, fg="black")
resultx.grid(row=1, column=1)




gamewindow.mainloop()