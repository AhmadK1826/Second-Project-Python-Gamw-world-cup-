import time
import random


def print_pause(msg):
    print(msg)
    time.sleep(1.5)


def intro():
    print("********************************************")
    print("*    Welcome to the World Cup Shootout!    *")
    print_pause("********************************************\n")
    print_pause("The crowd is roaring... All eyes are on you...")
    print_pause("You're the star striker, standing at the penalty spot.")
    print_pause("One shot... One chance... Will you bring the trophy home?")
    print_pause("Get ready to take the final penalty kick!")


def choose_direction():
    print_pause("\nChoose your shot direction:")
    print_pause("1. Top Left")
    print_pause("2. Top Right")
    print_pause("3. Bottom Left")
    print_pause("4. Bottom Right")
    print_pause("5. Center")

    directions = ["1", "2", "3", "4", "5"]
    choice = input("Enter the number of your choice (1-5):\n ")

    if choice in directions:
        return int(choice)
    else:
        print_pause("Invalid choice. Try again.")
        return choose_direction()


def goalkeeper_reaction(player_choice):
    if random.randint(1, 5) == int(player_choice):
        print_pause("Oh no! The goalkeeper SAVED it!")
        print_pause("The crowd gasps... You were so close!")
        return play_again()
    else:
        print_pause("GOOAAAL!!! You smashed it in!")
        print_pause("The crowd erupts! You're the hero of the match!")


def play_again():
    response = input("Want to play again? (yes or no)\n").lower()
    if response == 'yes':
        return True
    elif response == 'no':
        return False
    else:
        print_pause("I didn't understand.")
        return play_again()


def play(answer):
    if answer:
        player_choice = choose_direction()
        goalkeeper_reaction(player_choice)
        play_again()
    elif not answer:
        print("Have a nice day, goodbye!")


intro()
player_choice = choose_direction()
goalkeeper_reaction(player_choice)
answer = play_again()
play(answer)
