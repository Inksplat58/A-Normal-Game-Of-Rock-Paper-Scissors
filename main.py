import os
import time
def loading():
    print(".")
    time.sleep(0.2)
    os.system("clear")
    time.sleep(0.2)
    print("..")
    time.sleep(0.2)
    os.system("clear")
    print("...")
    time.sleep(0.2)
    os.system("clear")
    time.sleep(0.2)
def game():
    playerChoice = int(input())
    time.sleep(1)
    print("Pick one: Rock(1), Paper(2), Scissors(3).")
    time.sleep(0.5)
    os.system("clear")
    if playerChoice == (1):
        print("You chose rock")
        for i in range(5):
            loading()
            os.system("clear")
        print("I pick paper, you lose!")
        time.sleep(0.5)
        print("Want to try again?")
        time.sleep(2)
        print("Too bad, you can't.")
    elif playerChoice == (2):
        print("You chose paper")
        for i in range(5):
            loading()
            os.system("clear")
        print("I pick scissors, you lose!")
        time.sleep(0.5)
        print("Want to try again?")
        time.sleep(2)
        print("Too bad, you can't")
    elif playerChoice == (3):
        print("You chose scissors")
        for i in range(5):
            loading()
            os.system("clear")
        print("I pick rock, you lose!")
        time.sleep(0.5)
        print("Want to try again?")
        time.sleep(2)
        print("Too bad, you can't")
    else:
        print("You lost, that's not a valid answer.")
game()
