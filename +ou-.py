from random import randrange
Mistery = randrange(1, 101)

def Jeu():
   """Le jeu du Plus ou moins
    >les Regles: vous devez rentrez un chiffre entre 1 et 100
    >Attention vous n'avez le droit qu'a 5 essai
    >Bon jeu !!!"""

choix = 0
compteur = 0

def sortie(why):
    print why
    raise ValueError



print ("\t\tLe jeu du Plus ou moins\t\t")
print ("\t\tLes regles mettre un chiffre entre 1 et 100\t\t")
print ("\t\tVous n'avez le droit qu'a 5 essai\t\t")

while choix != Mistery:


    try:
        choix = input()
        choix = int(choix)

        if choix < Mistery:
            print("C'est plus grand")

        if choix > Mistery:
            print("C'est plus petit")

        if choix == Mistery:
            # noinspection PyArgumentList
            print ("Bravo vous avez trouvez le chiffre cacher")

        if choix > 100:
            sortie("entre 1 et 100 !!!")

        if choix < 1:
            sortie("entre 1 et 100 !!!")
    finally:"Nothing"



    compteur += 1

    if compteur == 6:
        print ("vous avez perdu")
        print ("voulez vous recommencer ?")
        print ("tapez '-1' pour recommencer ou tapez '2' pour quitter")

        ch = int(raw_input())


        if ch == "-1":
            def bidule():
                return Jeu()


        for x in xrange(1, 101):
            if ch == x:
                raise ValueError




def machin():
    print Jeu()

Truc = Jeu()
Truc.machin()
