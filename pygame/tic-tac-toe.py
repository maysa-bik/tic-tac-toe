import sys  # sys: Module fournissant un accès à certaines variables utilisées ou maintenues par l'interpréteur et à des fonctions qui interagissent fortement avec l'interpréteur.
import pygame # pygame: Bibliothèque pour la création de jeux.
import numpy as np # numpy: Bibliothèque pour le support de tableaux multidimensionnels et de matrices.

from constants import *

# pygame setup 
pygame.init() # pygame.init(): Initialisation de Pygame.
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # screen: Création de la fenêtre du jeu.
pygame.display.set_caption('TIC TAC TOE AI') # pygame.display.set_caption('TIC TAC TOE AI'): Définition du titre de la fenêtre.
screen.fill(BG_color) # Remplissage de l'écran avec la couleur d'arrière-plan.

class Board:
    # La classe Board représente le plateau de jeu. Elle a des méthodes pour marquer une case, vérifier si une case est vide, obtenir les cases vides, vérifier si le plateau est plein ou vide.
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS))
        self.empty_sqrs = self.squares # {squares}
        self.marked_sqrs = 0
        

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1


    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0
    
    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append(row, col)

        return empty_sqrs            
    
    def isfull(self):
        return self.marked_sqrs == 9
    
    def isempty(self):
        return self.marked_sqrs == 0

class Game:
    #La classe Game gère l'état du jeu. Elle a une instance de la classe Board et des méthodes pour afficher les lignes sur l'écran, dessiner les figures (croix ou cercle), et passer au tour suivant.

    def __init__(self):
        self.board = Board()
        self.player = 1  # 1-cross  # 2-circles
        self.show_lines()
    

    def show_lines(self): # Cette fonction dessine les lignes du plateau de jeu.
        # vertical
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0),(SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0),(WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE),(WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE),(WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    def draw_fig(self, row, col): # Cette fonction dessine une croix ou un cercle en fonction du joueur actuel.
        if self.player == 1:
            # draw cross
            # desc line 
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            # asc line 
            start_asc = (col * SQSIZE + OFFSET, row *SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

        elif self.player == 2:
            # draw circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADUIS, CIRC_WIDTH)




    def next_turn(self): # Cette fonction passe au tour suivant en changeant le joueur actuel.
        self.player = self.player %  2 + 1 

def main():
    # La fonction principale du jeu. Elle initialise le jeu, crée un objet Game, puis entre dans une boucle principale où elle gère les événements de la fenêtre et met à jour l'affichage.

    # object
    game = Game()
    board = game.board

    while True:  # La boucle principale du jeu où les événements sont traités en permanence.

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            if event.type == pygame.MOUSEBUTTONDOWN: 
                # Lorsqu'un clic de souris est détecté, les coordonnées du clic sont utilisées pour déterminer la case sur laquelle le joueur a cliqué.
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE


                if board.empty_sqr(row, col):
                    board.mark_sqr(row, col, game.player)
                    game.draw_fig(row, col)
                    game.next_turn()
                    
                    
                    
                


        pygame.display.update()
        # Cette ligne met à jour l'affichage à chaque itération de la boucle principale.
main()                