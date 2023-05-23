"""Ce fichier comporte un script python permettant de jouer au jeu du pendu avec une base de mots
aléatoirs déjà définie dans le fichier texte "mots_pendu.txt". Le joueur possède 6 chances par défaut pour trouver
le mot.Ce nombre peut-être modifier. """

import random

# Constantes
FICHIER_MOTS = "mots_pendu.txt" # Constante permettant de changer facilement le fichier contenant les mots à deviner
CHANCES = 6  # Constante permettant de modifier le nombre de chances facilement (vakeur par défaut : 6 chances)

# Fonction pour choisir un mot au hasard dans le fichier texte
def choisir_mot(mots):
    return random.choice(mots)

# Fonction permettant d'afficher l'état du mot cherché par l'utilisateur
def affichage_mot(lettres, mot_choisi):
    #print(mot_choisi)  # A SUPPRIMER !!!!
    affichage_liste =['_' for i in range(len(mot_choisi))]
    for caractere in lettres:
        for j in range(len(mot_choisi)):
            if caractere == mot_choisi[j]:
                affichage_liste[j] = caractere
    affichage_chaine = ''.join(affichage_liste)
    return affichage_chaine

# Fonction permettant de savoir si le mot a été trouvé (TRUE) ou non (FALSE)
def mot_trouve(lettres, mot_choisi):
    if affichage_mot(lettres, mot_choisi) == mot_choisi:
        return True
    else:
        return False

# Fonction permettant de vérifier si la lettre choisi par l'utilisateur a déjà été utilisée (TRUE) ou non (FALSE)
def verif_lettre_deja_utilisee(lettre, chaine_car):
    if lettre in chaine_car:
        return True
    else:
        return False

# Fonction permettant de vérifier si l'élément entré par l'utilisateur est bien une lettre ET en minuscule
def verif_caractere(lettre : str):
    if lettre.isupper():  # Si lettre majuscule, on la convertie en lettre minuscule
        return lettre.lower()
    elif lettre.islower():
        return lettre
    else:  # Si autre qu'une lettre, on demande à l'utilisateur de réessayer et on vérifie jusqu'à ce qu'il entre une lettre
        new_lettre = input('Veuillez entrer une lettre : ')
        return verif_caractere(new_lettre)


# Fonction permettant de lancer le jeu du pendu, avec en entrer un entier 'chance' afin de régler le nombre de chances
def jeu_pendu(chance : int):
    with open(FICHIER_MOTS, 'r') as f: # Ouverture du fichier texte
        liste_mots = f.read().splitlines()
    mot_hasard = choisir_mot(liste_mots)  # Choix au hasard d'un mot par l'ordinateur
    print(mot_hasard)
    print("Bonjour ! L'ordinateur a choisi un mot.\n "
          f"Voici le nombre de lettres à trouver : {len(mot_hasard)}\n", affichage_mot('', mot_hasard),
          '\nBonne chance !' )
    nombre_chances = chance
    lettres_trouvees = ''  # Initialisation des chaines de caractères pour stocker les lettres
    lettres_deja_utilisées = ''
    tentative = verif_caractere(input('Choisir une lettre : '))  # Première tentative pour l'utilisateur
    while nombre_chances > 1 : # Tant qu'il reste des chances
        if tentative in mot_hasard: # Si la lettre choisie est dans le mot à deviner
            lettres_trouvees += tentative
            if verif_lettre_deja_utilisee(tentative, lettres_deja_utilisées) == True: # Si la lettre est déjà utilisée, on prévient l'utilisateur qui change de lettre
                print(f'Attention ! Tu as déjà essayé la lettre {tentative}. \n'
                      f'RAPPEL --> voici les lettres déjà utilisées : {lettres_deja_utilisées}')
                tentative = verif_caractere(input('Choisir une lettre : '))
            else :
                lettres_deja_utilisées += tentative
                print(f'Tu as trouvé la lettre {tentative} !\n', affichage_mot(lettres_trouvees, mot_hasard))
                if mot_trouve(lettres_trouvees, mot_hasard) == False: # Si le mot n'a pas été trouvé
                    tentative = verif_caractere(input('Choisir une lettre : '))  # on demande une nouvelle lettre à l'utilisateur
                else : # Si le mot a été trouvé, on lfélicite l'utlisateur
                    print(f'Bravo! Tu as trouvé le mot entier {affichage_mot(lettres_trouvees, mot_hasard)} en {6 - nombre_chances} essais !')
                    nombre_chances = 0
                    again = verif_caractere(input('Veux-tu recommencer ? (oui/non) :')) # On demande si l'utilisateur veut rejouer
                    if again == 'oui':
                        jeu_pendu(chance)
                    else:
                        return (affichage_mot(lettres_trouvees, mot_hasard))
        elif tentative not in mot_hasard: # Si la lettre n'est pas dans le mot à deviner
            if verif_lettre_deja_utilisee(tentative,lettres_deja_utilisées) == False: # On vérifie si la lettre a été utilisée
                nombre_chances -= 1
                lettres_deja_utilisées += tentative
                print(f'Mauvaise lettre ! Il ne te reste plus que {nombre_chances} chance(s).')
            elif verif_lettre_deja_utilisee(tentative, lettres_deja_utilisées)==True: # Si elle a déjà été utilisée, l'utilisateur ne perd pas de chance
                print(f'Attention ! Tu as déjà essayé la lettre {tentative}. \n'
                      f'RAPPEL --> voici les lettres déjà utilisées : {lettres_deja_utilisées}')
            tentative = verif_caractere(input('Choisir une lettre : '))

    print('Dommage, tu as perdu(e) !') # Si le mot n'a pas été trouvé après les 6 chances, on lui propose de rejouer
    again = verif_caractere(input('Veux-tu recommencer ? (oui/non) :'))
    if again =='oui':
        jeu_pendu(chance)

# Lancement du jeu
jeu_pendu(CHANCES)
