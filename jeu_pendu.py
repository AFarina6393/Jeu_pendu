"""Ce fichier comporte un script python permettant de jouer au jeu du pendu avec une base de mots
aléatoirs déjà défini dans un fichier texte. Le joueur possède 6 chance pour trouver le mot."""

import random

# On ouvre le fichier en mode lecture
with open("mots_pendu.txt", 'r') as f:
    liste_mots = f.read().splitlines()
    print(liste_mots)

# Fonction pour choisir un mot au hasard dans le fichier texte
def choisir_mot(mots):
    return random.choice(mots)

mot_choisi = choisir_mot(liste_mots)

def affichage_mot(lettres):
    print(mot_choisi)  # A SUPPRIMER !!!!
    affichage_liste =['_' for i in range(len(mot_choisi))]
    for caractere in lettres:
        for j in range(len(mot_choisi)):
            if caractere == mot_choisi[j]:
                affichage_liste[j] = caractere
    affichage_chaine = ''.join(affichage_liste)
    return affichage_chaine


#print('Voici le mot à trouver :', affichage_mot(''))


def jeu_pendu():
    affichage = affichage_mot('')
    chance = 6
    lettres_trouvees = ''
    while chance > 0 :
        tentative = input('Choisi une lettre : ')
        print(affichage_mot(lettres_trouvees))
        for lettre in mot_choisi :
                if tentative in mot_choisi :
                    lettres_trouvees += tentative
                    print(f'Tu as trouvé la lettre {tentative} !\n', affichage_mot(lettres_trouvees))
                    tentative = input('Choisi une lettre : ')
                elif '_' not in affichage_mot(lettres_trouvees):
                    print('Bravo! Tu as trouvé le mot entier :', affichage_mot(lettres_trouvees))
                    chance = 0
                elif tentative not in mot_choisi :
                    print(f'Mauvaise lettre ! Il ne te reste plus que {chance-1} chance(s). ')
                    tentative = input('Choisi une lettre : ')
                    chance -= 1
    else :
        print('Tu as perdu !')
    return(affichage_mot(lettres_trouvees))

def jeu_pendu1():
    affichage = affichage_mot('')
    chance = 6
    lettres_trouvees = ''
    tentative = input('Choisi une lettre : ')
    while chance > 2 :
        for lettre in mot_choisi :
            if tentative in mot_choisi and affichage_mot(lettres_trouvees)!=mot_choisi:
                    lettres_trouvees += tentative
                    print(f'Tu as trouvé la lettre {tentative} !\n', affichage_mot(lettres_trouvees))
                    tentative = input('Choisi une lettre : ')
            elif tentative not in mot_choisi :
                    chance -= 1
                    print(f'Mauvaise lettre ! Il ne te reste plus que {chance} chance(s). ')
                    tentative = input('Choisi une lettre : ')
            else:
                    print('Bravo! Tu as trouvé le mot entier :', affichage_mot(lettres_trouvees))
                    chance = 0
                    return (affichage_mot(lettres_trouvees))
    else :
        print('Tu as perdu !')

jeu_pendu1()
