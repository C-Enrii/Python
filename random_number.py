import random

random_number = random.randint(0,100)

answer = int(input("Choose a number between 0 a 100: "))

if answer == random_number:
    print("Great, you did it on the first try.")

else:

    while answer != random_number:
        if answer > random_number:
            print("Too High")
        else:
            print("Too Low")

        answer = int(input("Try Again: "))
    print("You did it! Congratulations.")

