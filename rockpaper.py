import random

def get_user_choice():
    while True:
        try:
            user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
            if user_choice in [0, 1, 2]:
                return user_choice
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.randint(0, 2)

def print_choice(name, choice):
    choices = ["Rock", "Paper", "Scissors"]
    print(f"{name} choice: {choices[choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win"
    else:
        return "You lose"

def play_again():
    while True:
        again = input("Do you want to play again? (y/n): ").lower()
        if again in ['y', 'n']:
            return again == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print_choice("Your", user_choice)
        print_choice("Computer's", computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if not play_again():
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
