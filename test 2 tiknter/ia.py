"""
def ia(board, signe):

    # Vérifiez si l'IA peut gagner au prochain tour
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = signe
                if (board) == signe:
                    return row * 3 + col
                board[row][col] = 0

    # Vérifiez si l'IA peut empêcher le joueur de gagner au prochain tour
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = joueur
                if check_winner(board) == joueur:
                    return row * 3 + col
                board[row][col] = 0

    # Choisissez un emplacement aléatoire vide
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return row * 3 + col

    return False
"""

# Dans le fichier ia.py

import random

def ia(board, signe):
    # Liste des emplacements vides
    empty_positions = []

    # Parcourir le tableau pour trouver les emplacements vides
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                empty_positions.append((i, j))

    # Choisir un emplacement vide au hasard
    # Si des emplacements vides sont disponibles, choisissez-en un au hasard
    if empty_positions:
        return random.choice(empty_positions)
    else:
        return False  # Aucun emplacement vide disponible, renvoie False

