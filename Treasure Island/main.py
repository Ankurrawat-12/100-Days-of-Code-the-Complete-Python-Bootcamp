import random

def play_once():
    print("====================================")
    print("      WELCOME TO TREASURE ISLAND    ")
    print("====================================")
    print("Your mission is to find the Treasure.\n")

    # FLAGS
    skip_lake = False
    skip_maze = False

    # STEP 1: CROSSROAD
    while True:
        choice1 = input(
            "You are at a crossroad.\n"
            "Do you go LEFT, RIGHT, or STRAIGHT (shortcut)? → "
        ).strip().lower()

        if choice1 == "right":
            print("\nYou walked right into a hunter's trap pit.")
            print("You broke your neck.\nGAME OVER ❌")
            return

        elif choice1 == "left":
            print("\nYou follow the forest path safely...")
            break

        elif choice1 == "straight":
            print("\nYou discovered a narrow, dangerous shortcut path along a cliff...")
            # Shortcut: 50% chance instant death, 50% skip lake + maze and go near doors
            if random.random() < 0.5:
                print("A rockslide knocks you off the cliff.")
                print("You fall endlessly into the abyss.\nGAME OVER ❌")
                return
            else:
                print("You somehow survive and reach near an ancient temple directly!")
                skip_lake = True
                skip_maze = True
                break
        else:
            print("Invalid choice! Type LEFT, RIGHT or STRAIGHT.")

    # STEP 2: FOREST / CAVE (only if not full shortcut)
    if not (skip_lake and skip_maze):
        while True:
            print("\nYou enter a dark forest.")
            choice2 = input(
                "Do you: \n"
                " - follow the PATH\n"
                " - CLIMB the big hill (shortcut)\n"
                " - enter a CAVE (risky shortcut)\n"
                "→ "
            ).strip().lower()

            if choice2 == "path":
                print("\nYou carefully walk the path and reach a misty lake.")
                break

            elif choice2 == "climb":
                print("\nYou climb the hill and see a faster route that bypasses the maze.")
                skip_maze = True
                print("You slide down the other side and reach a misty lake.")
                break

            elif choice2 == "cave":
                print("\nYou go inside the cave…")
                # Risky shortcut: might skip lake, OR die
                if random.random() < 0.5:
                    print("A monster wakes up and eats you alive.")
                    print("You died screaming.\nGAME OVER ❌")
                    return
                else:
                    print("You find an underground tunnel that leads near the temple.")
                    skip_lake = True
                    print("You skipped the lake entirely!")
                    break
            else:
                print("Choose PATH, CLIMB or CAVE only!")

    # STEP 3: LAKE (only if not skipped)
    if not skip_lake:
        while True:
            print("\nYou reach a wide, silent lake.")
            choice3 = input(
                "Do you: \n"
                " - SWIM across\n"
                " - WAIT for a boat\n"
                " - build a RAFT (shortcut)\n"
                "→ "
            ).strip().lower()

            if choice3 == "swim":
                print("\nYou start swimming...")
                print("Suddenly, water snakes wrap around your legs.")
                print("You drown.\nGAME OVER ❌")
                return

            elif choice3 == "wait":
                print("\nYou wait patiently...")
                print("A mysterious old man appears with a boat and takes you safely across.")
                break

            elif choice3 == "raft":
                print("\nYou quickly build a raft using logs...")
                # Shortcut: success but you skip part of the maze
                if random.random() < 0.3:
                    print("Your raft breaks in the middle. You sink.")
                    print("GAME OVER ❌")
                    return
                else:
                    print("You cross fast and find a hidden side entrance near the maze exit.")
                    skip_maze = True
                    break

            else:
                print("Choose SWIM, WAIT, or RAFT only!")

    # STEP 4: MAZE (only if not skipped)
    if not skip_maze:
        print("\nYou now stand before an ancient stone maze.")
        print("The walls are high and covered in moss.")
        while True:
            choice4 = input(
                "Inside the maze, you see three paths.\n"
                "Do you go LEFT, RIGHT, or FORWARD? → "
            ).strip().lower()

            if choice4 == "left":
                print("\nYou walk into a dead end filled with spikes from the ceiling.")
                print("You couldn't escape in time.\nGAME OVER ❌")
                return
            elif choice4 == "right":
                print("\nYou find a secret door that leads straight to the temple entrance!")
                break
            elif choice4 == "forward":
                print("\nYou wander for hours but finally find the exit.")
                print("Exhausted, you reach the temple entrance.")
                break
            else:
                print("Choose LEFT, RIGHT, or FORWARD only!")

    # STEP 5: TEMPLE DOORS
    print("\nAt last, you stand before three massive doors in the temple:")
    print("🟥 RED door  | 🟨 YELLOW door | 🟩 GREEN door")
    print("There is also a small BROKEN door at the side (hidden shortcut).")

    while True:
        door = input(
            "Which door do you choose? RED, YELLOW, GREEN, or BROKEN → "
        ).strip().lower()

        if door == "red":
            print("\nThe room explodes in flames.")
            print("You are burned to ashes.\nGAME OVER ❌")
            return

        elif door == "green":
            print("\nYou enter a room full of hungry beasts.")
            print("They jump at you.\nGAME OVER ❌")
            return

        elif door == "yellow":
            print("\nThe door slowly opens...")
            print("Inside is a huge chest filled with GOLD and JEWELS!")
            print("💰💰 YOU FOUND THE TREASURE! 💰💰")
            print("YOU WON! 🏆")
            break

        elif door == "broken":
            # Fun shortcut: 50% super win, 50% dumb death
            print("\nYou squeeze through the broken side door...")
            if random.random() < 0.5:
                print("You fall directly into a treasure vault full of gold.")
                print("A true speedrunner's ending! 🏆")
                print("YOU WON VIA SHORTCUT! 🎉")
                break
            else:
                print("You fall straight into a pit hidden behind the broken door.")
                print("That was a bad idea.\nGAME OVER ❌")
                return
        else:
            print("Choose RED, YELLOW, GREEN or BROKEN only!")

    print("\nThank you for playing Treasure Island!")

def game():
    while True:
        play_once()
        again = input("\nDo you want to play again? (yes/no) → ").strip().lower()
        if again != "yes":
            print("\nGoodbye, adventurer! 👋")
            break

game()
