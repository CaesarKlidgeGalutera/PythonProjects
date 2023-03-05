import random

# this is a simple rock paper scissors program
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Enter your choice (rock, paper, scissors): ")
result = {"player": player, "computer": computer}


def match(player_choice, computer_choice):
    output = ""
    if player == computer:
        output = "It's a tie!"
    elif player == "rock" and computer == "scissors":
        output = "You win!"
    elif player == "rock" and computer == "paper":
        output = "You lose!"
    elif player == "paper" and computer == "scissors":
        output = "You lose!"
    elif player == "paper" and computer == "rock":
        output = "You win!"
    elif player == "scissors" and computer == "rock":
        output = "You lose!"
    elif player == "scissors" and computer == "paper":
        output = "You win!"
    return output


print(result)
print(match(player, computer))
