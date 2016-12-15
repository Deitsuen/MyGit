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
    raise ValueError



while choix != Mistery:
    # noinspection PyExceptClausesOrder
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
            # noinspection PyUnboundLocalVariable
            sortie("entre 1 et 100 !!!")
    except NameError,e:
        print "ce n'est pas un nom"
        print e



        if choix < 1:
            sortie("entre 1 et 100 !!!")
    except NameError,e:
        print "ce n'est pas un nom"
        print e


    compteur = compteur +1

    if compteur == 6:
        print ("vous avez perdu")
        print ("voulez vous recommencer ?")
        print ("tapez 'oui' pour recommencer ou tapez 'non' pour quitter")
        ch = raw_input()
        if ch == "oui":
            def bidule():
                return Jeu()









Truc = Jeu()
Truc.bidule()
