from tkinter import *
import random

from ia import ia 


def next_turn(row, col):
    global player   
    # من اجل ان اعرف اي لاهب ضغط الاول
    if game_btns[row][col]['text'] == "" and check_Gagner() is False:
        game_btns[row][col]['text'] = player

        if check_Gagner() == False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " Rôle "))

        elif check_Gagner() == True:
            label.config(text=(players[0] + " Gagner"))

        elif check_Gagner() == "Égalité":
            label.config(text=("Égalité, Non gagner ! "))
    """  
    # Vérifiez si la cellule est vide
    if game_btns[row][col]['text'] == "":

        # Appelez la fonction ia() pour obtenir l'emplacement sur lequel l'IA souhaite jouer
        pos = ia.ia(game_btns, player)

        # Placez le marqueur de l'IA à l'emplacement
        game_btns[row][col]['text'] = player

        # Changez le joueur
        player = "O" if player == "X" else "X"
    """  
    
    if game_btns[row][col]['text'] == "" and not check_Gagner():

        if player == players[0]: # هل هو اللاعب الاول او لا الذي ضغط
            # Mettre le symbole du joueur actuel
            game_btns[row][col]['text'] = player

            if check_Gagner() == False: # من اجل ان نختبر هل في حالة فوز حصلت او لا
                # Changer de joueur  # هنا من اجل اللاعب التاني يكوت عليه الدور ان يلعب
                player = players[1] 
                label.config(text=(players[1] + " Rôle "))

            elif check_Gagner() == True:  # اذا تحقق شرط من شروط الفوز
                label.config(text=(players[0] + " Gagner"))  #   ده معناه انه فاز سوف تذهر له هذه الرساله

            elif check_Gagner() == "Égalité":
                label.config(text=("Égalité, Non gagner ! "))            


            """
             elif player == players[1]:  # elif عشان يختبرها اذا الشرط الاول لم يتحقق
             # Mettre le symbole du joueur actuel # 2
             game_btns[row][col]['text'] = player


             """
            

        elif player == players[1]:
            # Appel de la fonction ia pour l'emplacement de l'IA
            ia_position = ia(game_btns, player)

            # Vérifiez si l'emplacement retourné par l'IA est valide
            if ia_position and game_btns[ia_position[0]][ia_position[1]]['text'] == "":
                game_btns[ia_position[0]][ia_position[1]]['text'] = player

            """
            if ia_position:
                # Placer le marqueur de l'IA à l'emplacement
                game_btns[ia_position[0]][ia_position[1]]['text'] = player        
            """
            if check_Gagner() == False:
                # Changer de joueur
                player = players[0]
                label.config(text=(players[0] + " Rôle"))

            elif check_Gagner() == True:
                label.config(text=(players[1] + " Gagner"))

            elif check_Gagner() == "Égalité":
                label.config(text=("Égalité, Non gagner ! "))

def check_Gagner():  # من اجل ان تختبر حالات الفوز في اللعبة
    # Vérifier toutes les conditions horizontales
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            game_btns[row][0].config(text="", bg="cyan")
            game_btns[row][1].config(text="", bg="cyan")
            game_btns[row][2].config(text="", bg="cyan")
            return True
    # Vérifier toutes les conditions verticales  # هنا من اجل حالة الفوز العامودية
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            game_btns[0][col].config(text="", bg="cyan")
            game_btns[1][col].config(text="", bg="cyan")
            game_btns[2][col].config(text="", bg="cyan")
            return True

    # Vérifier les conditions diagonales #  هنا من اجل حاله الفوز بشكل مائل
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(text="", bg="cyan")
        game_btns[1][1].config(text="", bg="cyan")
        game_btns[2][2].config(text="", bg="cyan")
        return True

    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(text="", bg="cyan")
        game_btns[1][1].config(text="", bg="cyan")
        game_btns[2][0].config(text="", bg="cyan")
        return True     

    # S'il ne reste plus d'espaces vides  # هنا في حاله عدم الفوز
    if not check_empty_spaces():
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='red')

        return 'Égalité'

    else:
        return False

def check_empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

    """
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces == 1

    if spaces == 0:
        return False
    else:
        return True
    """
def start_new_game():
    global player
    player = random.choice(players)
    label.config(text=(player + " Rôle"))

    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="#F0F0F0")

window = Tk()

window.title("Tic_Tac_Toe")

players = ["x", "o"]
player = random.choice(players)

game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]     

label = Label(text=(player + " Rôle "), font=('consolas', 40)) # من اجل اسم الاعب او الشخث الذي عليه دور اللعب 
label.pack(side="top") # لكي يضع النص فوق 

restart_btn = Button(text="restart", font=('consolas', 20), command=start_new_game) #  زر من اجل نستطيع من حلاله اعادة تشغيل اللعبة 
restart_btn.pack(side="top")

btns_frame = Frame(window) # من اجل ان ننشئ 9 ازرار الذي سوف نضغط عليهم 
btns_frame.pack()

for row in range(3):  
    for col in range(3):# من اجل ان تعيد لي المؤبعات التسعة الذي طلبناهن فوق 
        game_btns[row][col] = Button(btns_frame, text="", font=('consolas', 50), width=5, height=2, command=lambda row=row, col=col: next_turn(row,col))
        
        game_btns[row][col].grid(row=row, column=col)
window.mainloop()


