from random import randrange
Mistery = randrange(1, 101)

def Jeu():
    print ("\t\tLe jeu du Plus ou moins\t\t")
    print ("\t\tLes regles mettre un chiffre entre 1 et 100\t\t")
    print ("\t\tVous n'avez le droit qu'a 5 essai\t\t")

choix = 0
compteur = 0

def sortie(why):
    print why



while choix != Mistery:

    # noinspection PyBroadException,PyBroadException
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
    except ValueError as Exception:
        raise ValueError


    compteur += 1

    if compteur == 6:
        print ("vous avez perdu")
        print ("voulez vous recommencer ?")
        print ("tapez 'oui' pour recommencer ou tapez 'non' pour quitter")

        ch = raw_input()


        if ch == "oui":
            def bidule():
                return Jeu()



        if ch == "non":
            raise NameError

        for x in xrange(1, 101):
            if ch == x:
                raise ValueError




def machin():
    print Jeu()

Truc = Jeu()
Truc.machin()
