
import random



MAXIMAL_LINES = 3
MAXIMAL_BET = 100
MINIMAL_BET = 1

ROWS = 3
COLS = 3

emoji_count = {
    "🐨" : 1, 
    "🐱" : 2,
    "🐶" : 3,
    "🦁" : 4
}                   #needs impovements 

emoji_multiplier = {
    "🐨" : 4, 
    "🐱" : 3,
    "🐶" : 2,
    "🦁" : 1
}          

def slot_machine_spin(rows, cols, symbols):
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns =[]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns


        


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " - ")
            else:
                print(column[row], end = "")
        
        print()

def deposit():
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

def number_of_lines():
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



def total_earnings(columns, lines, bet, values):
    earnings = 0
    

    for line in range(lines):
        emoji = columns[0][line]
        for column in columns:
            true_emoji = column[line]
            if emoji != true_emoji:
                break
        else:
            earnings += bet * values[emoji_multiplier]
            
    return earnings



def get_bet():
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


def main():
    print("Welcome to my very first slotmachine!")
    balance = deposit()
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_bet =  lines * bet

        if total_bet > balance:
            print(f"You dont have enough money in your balance to make this bet. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = slot_machine_spin(ROWS, COLS, emoji_count)
    print_slot_machine(slots)

    earnings = total_earnings(slots, lines, emoji_multiplier, bet)
    print(f"your total winnings are: {earnings}")
   
main()
