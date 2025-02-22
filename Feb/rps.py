import random

choices = ['rock', 'paper', 'scissors']

def get_winner(user, program):
    if user == program:
        return "It's a tie, try again"
    elif (user == "rock" and program == "scissors") or \
         (user == "paper" and program == "rock") or \
         (user == "scissors" and program == "paper"):
        return f"You win! I chose {program}, and {user} beats {program}"
    else:
        return f"You lose! I chose {program}, and {program} beats {user}"

def play_game():
    print("Hello User, today we'll be playing a game of Rock, Paper, Scissors!")
    
    while True:
        user = input("\nWould you like to play rock, paper, or scissors? (rock, paper, scissors) ").lower()
        if user not in choices:
            print("Please enter a correct choice of rock, paper, or scissors")
            continue
        
        program = random.choice(choices)
        result = get_winner(user, program)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no) ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()
