
# Rock, paper Scissors Game
import random
# need to figure out how to incorporate the score keeper and display the score and round number
user_score = 0 
computer_score = 0
round_no = 0

name = input("Welcome to the game of 'ROCK, PAPER, SCISSORS!' What is your name?: ")
print(f"Okay {name} lets play!")

while True:
    player_choice = input("Pick your wepon! 'r' for ROCK, 'p' for PAPER, 's' for SCISSORS or 'q' to QUIT: ")

    if player_choice == 'q':
        print(f"Thanks for playing {name}, Hopefully we can play again soon!")
        break

    computer_choice = random.choice(['r', 'p', 's'])

    if player_choice == computer_choice:
        print("Its a draw!")
    
    elif player_choice == 'r' and computer_choice == 's' \
        or player_choice == 'p' and computer_choice == 'r' \
        or player_choice == 's' and computer_choice == 'p': \
        print(f"Computer chose: {computer_choice}, 'YOU WIN!'")
    
    else:
        print(f"Computer chose: {computer_choice} ")
        print("COMPUTER WINS!")


