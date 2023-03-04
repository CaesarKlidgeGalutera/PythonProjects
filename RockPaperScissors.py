import random
#this is a simple rock paper scissors program
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Enter your choice (rock, paper, scissors): ")
result = { "player" : player, "computer" : computer}

def match(player, computer):
    result=""
    if player == computer:
        result = "It's a tie!"
    elif player == "rock" and computer == "scissors":
        result = "You win!"
    elif player == "rock" and computer == "paper":
        result = "You lose!"
    elif player == "paper" and computer == "scissors":
        result = "You lose!"
    elif player == "paper" and computer == "rock":
        result = "You win!"
    elif player == "sciccors" and computer == "rock":
        result = "You lose!"
    elif player == "scissors" and computer == "paper":
        result = "You win!"
    return result

print(result)
print(match(player, computer))