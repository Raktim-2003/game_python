import random
import math
lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")

count = 0
flag = False

while count < total_chances:
    count += 1

    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congratulations you did it in ",
              count, " try")

        flag = True
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

if not flag:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
    print("\tI things you will  come soon !")

#number gussing game.
#game complete by_26_07_2024 15:20
#helped by chatgpt,python_librearies_etc......... 


