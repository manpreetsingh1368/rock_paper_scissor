import random

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \\ / _` | '_ \\ / _ \\ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \\__,_| .__/ \\___|_|   
| |         | |              
|_|         |_|        
'''

rock = '''    
        ______
     .-'      `-.
   .'            `.
  /                \\
 |                  |
 |  ~    ROCK     ~ |
 |                  |
  \\                /
   `.            .'
     `-.______.-'
'''

scissors = ''' 
    \\    /
     \\  /
      ||
     (  )
      ||
     /  \\
    /    \\
---      ---
'''

choice = [paper, rock, scissors]
names = ["Paper", "Rock", "Scissors"]

user_score = 0
computer_score = 0
draws = 0

print("Welcome to Rock, Paper, Scissors!")

while True:
    # Get user input with validation
    while True:
        try:
            user_choice = int(input("Enter your choice: 0 - Paper, 1 - Rock, 2 - Scissors: "))
            if user_choice in [0, 1, 2]:
                break
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    computer_choice = random.randint(0, 2)

    print("\nYou chose:")
    print(choice[user_choice])

    print("Computer chose:")
    print(choice[computer_choice])

    # Determine winner
    if user_choice == computer_choice:
        print("It's a draw!")
        draws += 1
    elif (user_choice == 0 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 0):
        print("You won this round!")
        user_score += 1
    else:
        print("You lost this round.")
        computer_score += 1

    print(f"\nScores: You: {user_score} | Computer: {computer_score} | Draws: {draws}")

    # Play again?
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye.")
        break
