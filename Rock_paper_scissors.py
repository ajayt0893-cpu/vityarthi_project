import random

'''give instructions  when you input something'''

print("Welcome to Rock-Paper-Scissors!")

print("Choose one: rock, paper, scissors")

# taking input from the user

user = input("Your choice: ").lower()
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

# use of random module to genrate a random choice from the list of choices.
print("Computer chose:", computer)

# use of conditional expressions

if user == computer:
    print("It's a tie!")

elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")

elif user in choices:
    print("Computer wins!")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")