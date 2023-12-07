"""

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur, hauteur = 800, 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Ma Fenêtre Pygame")

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Autres opérations de la boucle principale ici
    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)  

    pygame.display.flip()


    #    global Current_player  # Assurez-vous que current_player est une variable globale 

    # Vérifiez si la case est déjà occupée
    #if plateau[row][col] == " ":
        #plateau[row][col] = current_player 
    #else:
        #print("La case est déjà occupée. Choisissez une autre position. ")
        #return False 
"""





  

    


       

