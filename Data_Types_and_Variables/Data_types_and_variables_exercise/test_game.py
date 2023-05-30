import random

# Create variables for moves
rock = "rock"
paper = "paper"
scissors = "scissors"

# Read player's move
player_move = input("Enter your move (r for rock, p for paper, s for scissors): ")

# Match player's move with possible options
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    print("Invalid input. Exiting the game.")
    raise SystemExit

# Choose computer's move
computer_move = random.choice([rock, paper, scissors])

# Print computer's move
print(f"The computer chose {computer_move}.")

# Compare player's move with computer's move
if player_move == computer_move:
    print("It's a tie!")
elif (player_move == rock and computer_move == scissors) or \
     (player_move == paper and computer_move == rock) or \
     (player_move == scissors and computer_move == paper):
    print("You win!")
else:
    print("Computer wins!")
