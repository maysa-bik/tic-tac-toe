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

def colorreturn():
    button1.configure(fg="silver")  
    button2.configure(fg="silver") 
    button3.configure(fg="silver") 
    button4.configure(fg="silver") 
    button5.configure(fg="silver") 
    button6.configure(fg="silver") 
    button7.configure(fg="silver") 
    button8.configure(fg="silver") 
    button9.configure(fg="sliver")       

def scorekeeper():
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
    elif(button4["text"] == "o" and button5["text"] == "o" and button6["text"] == "o"):
        button1.configure(fg="green")  
        button2.configure(fg="green") 
        button3.configure(fg="green")  
        s = float(playerx.get())
        score = (s + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("winer est o", "la game est terminer")                                                           
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
    button6.configure(background="black")
    button7.configure(background="black")
    button8.configure(background="black")
    button9.configure(background="black")


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


labelplayero = Label(downframe, font=("arial", 26,"bold"), text="Résultat la joueur o :", padx=2, pady=2, bg="gold")
labelplayero.grid(row=0, column=0)

labelplayerx = Label(downframe, font=("arial", 26,"bold"), text="Résultat la joueur x :", padx=2, pady=2, bg="gold")
labelplayerx.grid(row=1, column=0)

resultx = Entry(downframe, font=("arial", 26,"bold"), bd=2, fg="black", textvariable=playerx)
resultx.grid(row=1, column=1)

resulto = Entry(downframe, font=("arial", 26,"bold"), bd=2, fg="black", textvariable=playero)
resulto.grid(row=0, column=1)

newgamebutton = Button(bottomframe, text="new game ", width=25, height=4, bd=2, bg="green", fg="black", font=("arial", 12,"bold"), command=newgame)
newgamebutton.grid(row=0, column=3)

newstartgamebutton = Button(bottomframe, text=" restart", width=25, height=4, bd=2, bg="green", fg="black", font=("arial", 12,"bold"), command=restart)
newstartgamebutton.grid(row=0, column=2)
"""
nothinkgamebutton = Button(bottomframe, text=" ", width=20, height=4, bd=2, bg="green", fg="black", font=("arial", 12,"bold"),)
nothinkgamebutton.grid(row=0, column=1)
"""
exitgamebutton = Button(bottomframe, text="sorti", width=25, height=4, bd=2, bg="green", fg="black", command=lambda :quit(gamewindow), font=("arial", 12,"bold"))
exitgamebutton.grid(row=0, column=0)


gamewindow.mainloop()