"""
programme fait par matis marcil berube
groupe 402
description: tp2 - jeu devinette
"""

import random

start_jeu = True
nb_min = 0
nb_max = 1000

while start_jeu:
    print("Le but du jeu es de trouver le nombfre que jai en tete!")
    nb_ale = random.randint(nb_min, nb_max)
    print("parfait jai chooisi un nombre entre 0 et 1000!")
    print("bonne chance!")
    nb_try = 1
    boucle_jeu = True
    while boucle_jeu == True:

        essai = int(input(f"essaie numero {nb_try}, entrer un nombre:"))

        if essai < nb_ale:
            print("penser plus grand!")
        elif essai > nb_ale:
            print("penser plus petit!")
        elif essai == nb_ale:
            print("bravo vous avez gagner!!!")
            rejouer = input("voulez vous rejouer")
            if rejouer == "oui":
                boucle_jeu = False
            else:
                print("merci davoir jouer!")
                boucle_jeu = False
                start_jeu = False


