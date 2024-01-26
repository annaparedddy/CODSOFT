import random
def get_user_choice():
    user_choice = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()
    while user_choice not in ['r', 'p', 's']:
        print("Invalid choice. Please enter 'r', 'p', or 's'.")
        user_choice = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()
    return user_choice
def get_computer_choice():
    return random.choice(['r', 'p', 's'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        return "You win!"
    else:
        return "Computer wins!"
def play_game():
    print("Let's play Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
play_game()
