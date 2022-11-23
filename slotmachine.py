
import random


ROWS = 3
COLS = 3


MAXIMAL_LINES = 3
MAXIMAL_BET = 100
MINIMAL_BET = 1



emoji_count = {                 #dic with symbols(emojisense extention) and value for how rare each symbol is(1 most rare 4 most common)
    "🐨" : 1, 
    "🐱" : 2,
    "🐶" : 3,
    "🦁" : 4
}                   



def slot_machine_spin(rows, cols, symbols):             #for loop creates the slot machine spin
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns =[]                             # empty list columns takes in random selected ite from dictionary, removing value for propability every time it loops thru
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns


        


def print_slot_machine(columns):                #printing slot machine in terminal when calling function in main(), using "-" as separator between items
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " - ")
            else:
                print(column[row], end = "")
        
        print()

def deposit():                                  #taking user innput for initial deposit
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def number_of_lines():              #taking user input for the amount of lines user would like to bet on
    while True:
        lines = input(f"On how many lines would you like to bet on? 1 - {MAXIMAL_LINES}. ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAXIMAL_LINES:
                break
            else:
                print(f"Enter a valid number between 1 and {MAXIMAL_LINES}.")
        else:
            print("Please enter a number.")
    
    return lines







def get_bet():              #taking user input on how much user would like to bet on each line
    while True:
        bet = input("What would you like to bet on each line?: $")
        if bet.isdigit():
            bet = int(bet)
            if MINIMAL_BET <= bet <= MAXIMAL_BET:
                break
            else:
                print(f"Amount must be in between {MINIMAL_BET} and {MAXIMAL_BET}")
        else:
            print("Please enter a number.")
    return bet


def main():                 #main function where all functions get called
    print("Welcome to the animal slot machine")
    balance = deposit()
    lines = number_of_lines()
    while True:             #while loop to calculate total bet of user
        bet = get_bet()
        total_bet =  lines * bet

        if total_bet > balance:
            print(f"You dont have enough money in your balance to make this bet. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = slot_machine_spin(ROWS, COLS, emoji_count)
    print_slot_machine(slots)

    # explaination for the user how to calculate winnings ifuser won on spin
    print("you are a winner if you see three of a kind in the lines you bet \n - 🦁: multiply bet on line times 1 \n - 🐶: multiply bet on line times 2 \n - 🐱: multiply bet on line times 3\n - 🐨: multiply bet on line times 4")
   
main()



