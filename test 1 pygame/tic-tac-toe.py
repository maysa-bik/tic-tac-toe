import sys  # sys: Module fournissant un accès à certaines variables utilisées ou maintenues par l'interpréteur et à des fonctions qui interagissent fortement avec l'interpréteur.
import pygame # pygame: Bibliothèque pour la création de jeux.
import numpy as np # numpy: Bibliothèque pour le support de tableaux multidimensionnels et de matrices.

from constants import *

from ai import *

# pygame setup 
pygame.init() # pygame.init(): Initialisation de Pygame.
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # screen: Création de la fenêtre du jeu.
pygame.display.set_caption('TIC TAC TOE AI') # pygame.display.set_caption('TIC TAC TOE AI'): Définition du titre de la fenêtre.
screen.fill(BG_color) # Remplissage de l'écran avec la couleur d'arrière-plan.

class Button:
    def __init__(self, text, rect, color, action):
        self.text = text
        self.rect = pygame.Rect(rect)
        self.color = color
        self.action = action

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)  # Bordure
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()

class Board:
    # La classe Board représente le plateau de jeu. Elle a des méthodes pour marquer une case, vérifier si une case est vide, obtenir les cases vides, vérifier si le plateau est plein ou vide.
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS))
        self.empty_sqrs = self.squares # {squares}
        self.marked_sqrs = 0

    def final_state(self, show=False):
        '''
            @return 0 if there is no win yet 
            @return 1 if player 1 win 
            @return 2 if player 2 win
        '''
        # vertical wins 
        for col in range (COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]

        # horizontal wins 
        for row in range (ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    iPos = (20, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]
        
        # desc diagonal 
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 2)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # asc diagonal 
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]
        
        # no win yet 
        return 0
    
    def check_game_state(self):
        # Vérifiez s'il y a un gagnant
        winner = self.final_state(show=False)
        if winner == 1 or winner == 2:
            return f"Joueur {winner} a gagné !"

        # Vérifiez s'il y a un match nul
        if self.isfull():
            return "Match nul !"

        # Si le jeu n'est pas terminé
        return None

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
                    empty_sqrs.append((row, col))

        return empty_sqrs

    '''
    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append(row, col)

        return empty_sqrs            
    '''
    def isfull(self):
        return self.marked_sqrs == 9
    
    def isempty(self):
        return self.marked_sqrs == 0

class AI:
    def __init__(self, level=0, player=2):
        self.level = level
        self.player = player
    
    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_sqrs))

        return empty_sqrs[idx] # (row, col)
    
    def evel(self, main_board):
        if self.level == 0:
            # random choice
            move = self.rnd(main_board)  

        else:
            #minimax algo choice
            pass

        return move # row, col

class Game:
    #La classe Game gère l'état du jeu. Elle a une instance de la classe Board et des méthodes pour afficher les lignes sur l'écran, dessiner les figures (croix ou cercle), et passer au tour suivant.

    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1  # 1-cross  # 2-circles
        self.gamemode = 'ai' # pvp or ai
        self.running = True
        self.show_lines() 
    
    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        result = self.board.check_game_state()
        if result:
            print(result)
            self.running = False
        else:
            self.next_turn()
        
    def show_lines(self): # Cette fonction dessine les lignes du plateau de jeu.
        # vertical
        screen.fill(BG_color)
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

    def change_gamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'
    
    def isover(self):
        return self.board.final_state != 0 or self.board.isfull()

    def reset(self):
        self.__init__()
    '''

    
    def __init__(self):
        self.players = ["Joueur 1", "Joueur 2"]
        self.player = ""
        self.create_game_board()

    def create_game_board(self):
        # Initialisez votre plateau de jeu (grille, boutons, etc.)
        self.game_btns = [[None for _ in range(3)] for _ in range(3)]
        # ... (autres configurations)

    def start_new_game(self):
        self.player = random.choice(self.players)
        # ... (autres configurations pour le début d'une nouvelle partie)

    def le_jeu_est_terminé(self):
        # Vérifiez si un joueur a gagné en ligne
        for row in range(3):
            if self.game_btns[row][0]['text'] == self.game_btns[row][1]['text'] == self.game_btns[row][2]['text'] != "":
                return True
        # ... (autres conditions de victoire) 
    '''  
    
def main():
    # La fonction principale du jeu. Elle initialise le jeu, crée un objet Game, puis entre dans une boucle principale où elle gère les événements de la fenêtre et met à jour l'affichage.


    # object
    game = Game()
    board = game.board
    ai = game.ai

    while True:  # La boucle principale du jeu où les événements sont traités en permanence.

        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            '''
            # Gérez le début d'une nouvelle partie
            if besoin_de_commencer_une_nouvelle_partie:
                game.start_new_game()
                besoin_de_commencer_une_nouvelle_partie = False  # Remettez à False après avoir traité l'événement

            # Gérez la fin du jeu
            if game.le_jeu_est_terminé():
                print("Le jeu est terminé. Affichez le résultat ou effectuez d'autres actions nécessaires.")
                besoin_de_commencer_une_nouvelle_partie = True  # Mettez à True pour commencer une nouvelle partie   
            '''
            if  event.type == pygame.KEYDOWN:

                # g-gamemode
                if event.key == pygame.K_g:
                    game.change_gamemode()

                # r-restart
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai    

                # 0-random ai   
                if event.key == pygame.K_0:
                    ai.level = 0

                # 1-random ai 
                if event.key == pygame.K_1:
                    ai.level = 1   

            if event.type == pygame.MOUSEBUTTONDOWN: 
                # Lorsqu'un clic de souris est détecté, les coordonnées du clic sont utilisées pour déterminer la case sur laquelle le joueur a cliqué.
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                '''
                if game.board.empty_sqr(row, col):
                    game.make_move(row, col)
                '''
                
                if board.empty_sqr(row, col):
                    game.make_move(row, col)

                    if game.isover():
                        game.running = False
            
                    
 
        # .... (autres conditions)
        if game.gamemode == 'ai' and game.player == ai.player and  game.running:
            # update the screen 
            pygame.display.update()  

            # ai methods    
            row, col = ai.evel(board)
            game.make_move(row, col)
            if game.isover():
                game.running = False
        pygame.display.update()    
main()              