import random


def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors):")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "it's a tie"
    
    elif player == "rock":
        if computer == "scissors":
            return "rock beats scissors, you win!"
        else: 
            return "paper beats rock, you lose."
    
    elif player == "paper":
        if computer == "rock":
            return "paper beats rock, you win!"
        else: 
            return "scissor beats paper, you lose."        
    elif player == "scissors":
        if computer == "paper":
            return "scissors beats paper, you win!"
        else: 
            return "rock beats scissors, you lose."
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
