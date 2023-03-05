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
        output = "You win! Rock beats scissors"
    elif player == "rock" and computer == "paper":
        output = "You lose! Paper beats rock"
    elif player == "paper" and computer == "scissors":
        output = "You lose! Scissors cuts paper"
    elif player == "paper" and computer == "rock":
        output = "You win! Paper beats rock"
    elif player == "scissors" and computer == "rock":
        output = "You lose! Rock beats scissors"
    elif player == "scissors" and computer == "paper":
        output = "You win! Scissors cuts paper"
    return output


print("You chose " + result["player"] + ", computer chose " + result["computer"])
print(match(result["player"], result["computer"]))
