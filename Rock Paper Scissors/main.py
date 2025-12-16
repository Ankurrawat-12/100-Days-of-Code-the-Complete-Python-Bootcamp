import random

def game():
    choice = int(input("What do you choose? (0: Rock, 1: Paper, 2: Scissors): "))
    computer = random.randint(0,2)
    if choice == 0:
        if computer == 0:
            print("Rock\nIt's a draw")
        elif computer == 1:
            print("Paper\nYou lose")
        else:
            print("Scissors\nYou win")

    elif choice == 1:
        if computer == 0:
            print("Rock\nYou Win")
        elif computer == 1:
            print("Paper\nIt's a draw")
        else:
            print("Scissors\nYou lose")

    else:
        if computer == 0:
            print("Rock\nYou lose")
        elif computer == 1:
            print("Paper\nYou Win")
        else:
            print("Scissors\nIt's a draw")


