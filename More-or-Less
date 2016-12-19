from random import randrange

mistery = randrange(1, 101)


def game():
    """

game() : Regroup all variable and functions

choice : Allows write your reponse

randrange: Randange chosen a random in range defined

mistery : It's a variable of randrange

counter: Count the number of tries

choice2 : Allows write your reponse after to have fail

rewind : Allows of rewind a game()
"""


choice = 0

counter = 0

print ("\t\tGame of More or Less\t\t")
print ("\t\tThe Rules: Chosen numbers between 1 and 100\t\t")
print ("\t\tYou only have 5 chances \t\t")

while choice != mistery:

    try:
        choice = input()
        choice = int(choice)

        if choice < mistery:
            print("it's bigger")

        if choice > mistery:
            print("it's smaller")

        if choice == mistery:
            print ("Congratulation you have find a secret number !!!!")
            raise SystemExit

        if choice < 1 or choice > 100:
            raise ValueError
    except ValueError as e:
        print e
        print "incorrect Value"
        raise SystemExit

    counter += 1

    if counter == 5:
        print ("Game Over")
        print ("want to start over?")
        print ("write '-1' for restart or write '2' for exit")

        choice2 = int(raw_input())

        if choice2 == "-1":
            def rewind():
                return game()

        for x in xrange(1, 101):
            if choice2 == x:
                raise SystemExit
