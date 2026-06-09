import random

options = ("rock", "paper", "scissors")


running = True

right_answer = 0
wrong_answer = 0


while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Choose an option (rock, paper, scissors): ").lower()
        if player not in options:
            print("That's not a valid option!")

    if player == computer:
        print(f"The computer chose {computer}, you chose {player}")
        print("That's a tie!")
    elif player == "rock" and computer == "scissors":
        print(f"The computer chose {computer}, you chose {player}")
        print("That's a win!")
        right_answer += 1
    elif player == "paper" and computer == "rock":
        print(f"The computer chose {computer}, you chose {player}")
        print("That's a win!")
        right_answer += 1
    elif player == "scissors" and computer == "paper":
        print(f"The computer chose {computer}, you chose {player}")
        print("That's a win!")
        right_answer += 1
    else:
        print(f"The computer chose {computer}, you chose {player}")
        print("That's a lose")
        wrong_answer += 1

    while True:

        play_again = input("Do you want to play again? (Yes/No) ").lower()

        if play_again == "no":
            running = False
            break
        elif play_again == "yes":
            break
        else:
            print("that's not a valid option!")


print(f"You have {right_answer} right answers and {wrong_answer} wrong answers")