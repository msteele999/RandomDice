import random
from d4 import get_d4_faces
from d6 import get_d6_faces
from d8 import get_d8_faces
from d10 import get_d10_faces
from d12 import get_d12_faces
from d20 import get_d20_faces

def roll_dice(die_type, number_of_dice):
    results = [random.randint(0 if die_type == 10 else 1, die_type) for _ in range(number_of_dice)]
    total = sum(results)
    return total, results

def dice_face(die_type, number):
    if die_type == 4:
        faces = get_d4_faces()
        return faces[number]
    elif die_type == 6:
        faces = get_d6_faces()
        return faces[number]
    elif die_type == 8:
        faces = get_d8_faces()
        return faces[number]
    elif die_type == 10:
        faces = get_d10_faces()
        return faces[number]
    elif die_type == 12:
        faces = get_d12_faces()
        return faces[number]
    elif die_type == 20:
        faces = get_d20_faces()
        return faces[number]
    else:
        return [f"Rolled a {number}"]

def print_dice_faces(die_type, results):
    if die_type in [4, 6, 8, 10, 12, 20]:
        faces = [dice_face(die_type, result) for result in results]
        for line in range(len(faces[0])):
            print("   ".join(face[line] for face in faces))
    elif die_type == 100:
        tens = results[0] // 10
        units = results[0] % 10
        faces = [dice_face(10, tens), dice_face(10, units)]
        for line in range(len(faces[0])):
            print("      ".join(face[line] for face in faces))
    else:
        print("Non-graphical representation for non-4, non-6, non-8, non-10, non-12, non-20, or non-100-sided dice.")
        print("Results: ", results)

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
            
            if die_type == 100:
                number_of_dice = 1
            else:
                number_of_dice = input(f"\nHow many {die_type}-sided dice would you like to roll? ").strip()
                if not number_of_dice.isdigit():
                    print("Invalid number of dice. Please enter a positive integer.")
                    continue
                number_of_dice = int(number_of_dice)
            
            total, results = roll_dice(die_type, number_of_dice)
            
            result_message = (
                f"Rolled {number_of_dice}d{die_type}:\n"
                f"Individual die results: {results}\n"
                f"Total of {number_of_dice} dice: {total}\n"
            )
            
            print_with_border(result_message)
            
            print_dice_faces(die_type, results)
        else:
            print("Invalid input. Please enter a number for the type of die or 'q' to quit.")

if __name__ == "__main__":
    main()
