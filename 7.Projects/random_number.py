import random

Target = random.randint(1,100)

while True:
    UserChoice = input("guess the choice or quit:")
    if (UserChoice == "quit"):
        break
    UserChoice = int(UserChoice)
    if ( UserChoice == Target):
        print("your guess is correct!!")
        break
    elif (UserChoice < Target):
        print("your guess is too small,guess again.. ")
    else:
        print("your guess is too big,guess again...")

print("......GAME OVER....")

                       
