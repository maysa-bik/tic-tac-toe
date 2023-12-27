# Fichier "ia.py"
import random

def ia(board, signe):
    # Recherche d'une case pour gagner
    for i in range(9):
        if board[i] == " ":
            board[i] = signe
            if gagne(board, signe):
                board[i] = " "  # Annuler le mouvement
                return i
            board[i] = " "  # Annuler le mouvement

    # Recherche d'une case pour bloquer l'adversaire
    adversaire_signe = "o" if signe == "x" else "x"
    for i in range(9):
        if board[i] == " ":
            board[i] = adversaire_signe
            if gagne(board, adversaire_signe):
                board[i] = " "  # Annuler le mouvement
                return i
            board[i] = " "  # Annuler le mouvement

    # Si aucune opportunité de gagner ou de bloquer, choisir une case vide au hasard
    cases_vides = [i for i in range(9) if board[i] == " "]
    if cases_vides:
        return random.choice(cases_vides)
    else:
        return False

def gagne(board, signe):
    # Vérifier les lignes, colonnes et diagonales pour une victoire
    for i in range(3):
        if all(board[i*3 + j] == signe for j in range(3)) or \
           all(board[j*3 + i] == signe for j in range(3)):
            return True

    if all(board[i] == signe for i in [0, 4, 8]) or \
       all(board[i] == signe for i in [2, 4, 6]):
        return True

    return False
