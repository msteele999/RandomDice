import random

def roll_dice(die_type, number_of_dice):
    results = [random.randint(1, die_type) for _ in range(number_of_dice)]
    total = sum(results)
    return total, results

def print_with_border(message):
    top_left = '╔'
    top_right = '╗'
    bottom_left = '╚'
    bottom_right = '╝'
    horizontal = '═'
    vertical = '║'
    padding = 2
    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    width = max_length + padding * 2
    
    print('\033[44m\033[37m')  # Set background to blue and text to white
    print(' ' * (padding + 1) + top_left + horizontal * width + top_right)
    for line in lines:
        print(' ' * (padding + 1) + f"{vertical}{' ' * padding}{line.ljust(max_length)}{' ' * padding}{vertical}")
    print(' ' * (padding + 1) + bottom_left + horizontal * width + bottom_right)
    print('\033[0m')  # Reset color

def main():
    print("Welcome to the Random Dice Generator!")
    while True:
        user_input = input("\nEnter the type of die to roll (4, 6, 8, 10, 12, 20, 100) or 'q' to quit: ").strip().lower()
        
        if user_input == 'q':
            print("\nGoodbye!")
            break
        
        if user_input.isdigit():
            die_type = int(user_input)
            if die_type not in [4, 6, 8, 10, 12, 20, 100]:
                print("Invalid die type. Please enter one of the following: 4, 6, 8, 10, 12, 20, 100.")
                continue
            
            number_of_dice = input(f"\nHow many {die_type}-sided dice would you like to roll? ").strip()
            if not number_of_dice.isdigit():
                print("Invalid number of dice. Please enter a positive integer.")
                continue
            
            number_of_dice = int(number_of_dice)
            total, results = roll_dice(die_type, number_of_dice)
            result_message = (
                f"Rolled {number_of_dice}d{die_type}:\n"
                f"Individual die results: {results}\n"
                f"Total of {number_of_dice} dice: {total}"
            )
            print_with_border(result_message)
        else:
            print("Invalid input. Please enter a number for the type of die or 'q' to quit.")

if __name__ == "__main__":
    main()
