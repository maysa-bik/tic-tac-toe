# Fichier "ia.py"
import random

def ia(board, signe):
    # Implémentation simple : l'IA choisit un emplacement aléatoire non occupé
    empty_spots = [i for i, val in enumerate(board) if val == 0]
    
    if empty_spots:
        return random.choice(empty_spots)
    else:
        return False