import sys 
import pygame
import numpy as np

from constants import *

# pygame setup 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill(BG_color)

class Board:
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS))
        self.mark_sqr(1,1,2)
        print(self.squares)

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player

class Game:

    def __init__(self):
        self.board = Board()
        self.show_lines()
    

    def show_lines(self):
        # vertical
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0),(SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0),(WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE),(WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE),(WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)
def main():

    # object
    game = Game()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
main()                