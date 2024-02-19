import random
import string
from time import sleep

bal = 0
def balance():
    global bal
    while True:
        bal = input("How much would you like to deposit? $ ")
        if bal.isdigit():
            bal = int(bal)
            if bal > 0:
                print(f"Balance: {bal}")
                break
            else:
                print("That is not a valid amount")
        else:
            print("Please enter in all numbers.")
    return bal

def betLines():
    while True:
        lines = input("How many lines do you want to bet on (1-3)? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                print(f"Bet lines: {lines}")
                break
            else:
                print("Please enter a valid number.")
        else:
            print("Please enter a number.")
    return lines

def betAmount():
    while True:
        amount = input("How much would you like to bet per slot? $ ")
        if amount.isdigit():
            amount = int(amount)
            return amount
        else:
            print("Please enter a number.")

def slot():
    letters = list(string.ascii_uppercase)
    row1 = []
    for i in range(3):
        row1.append(random.choice(letters))
    
    return row1

def slot2():
    letters = list(string.ascii_uppercase)
    row2 = []
    for i in range(3):
        row2.append(random.choice(letters))
    return row2

def slot3():
    letters = list(string.ascii_uppercase)
    row3 = []
    for i in range(3):
        row3.append(random.choice(letters))
    return row3

def checkWin(slot_1,slot_2,slot_3,totLines):
    if totLines == 3:
        if slot_1[0] == slot_1[1] == slot_1[2] or slot_2[0] == slot_2[1] == slot_2[2] or slot_3[0] == slot_3[1] == slot_3[2]:
            return True
        return False
    if totLines == 2:
        if slot_1[0] == slot_1[1] == slot_1[2] or slot_2[0] == slot_2[1] == slot_2[2]:
            return True
        return False
    else:
        if slot_1[0] == slot_1[1] == slot_1[2]:
            return True
        return False

def main():
    global bank
    print()
    lineNums = betLines()
    print()
    while True:
        totMoney = betAmount()
        sum = totMoney*lineNums
        if sum > bank:
            print("You do not have the valid amount in your balance.")
            print(f"Your balance: ${bank}")
        else:
            print(f"You are betting {totMoney} on {lineNums} slot(s).")
            print(f"Total per bet: ${sum}")
            break
    
    s1 = slot()
    s2 = slot2()
    s3 = slot3()
    if lineNums == 3:
        print()
        print(f"{s1[0]} | {s1[1]} | {s1[2]}")
        print(f"{s2[0]} | {s2[1]} | {s2[2]}")
        print(f"{s3[0]} | {s3[1]} | {s3[2]}")
        print()
    if lineNums == 2:
        print()
        print(f"{s1[0]} | {s1[1]} | {s1[2]}")
        print(f"{s2[0]} | {s2[1]} | {s2[2]}")
        print()
    if lineNums == 1:
        print()
        print(f"{s1[0]} | {s1[1]} | {s1[2]}")
        print()

    if checkWin(s1,s2,s3,lineNums):
        bank = sum+bank
        sleep(1)
        print("You WIN!")
        print(f"You won: ${sum}")
        print(f"Your new balance: ${bank}")
    else:
        bank = bank-sum
        sleep(1)
        print("You LOSE")
        print(f"You lost: ${sum}")
        print(f"Your new balance: ${bank}")


bank = balance()
while True:
    user = input("Roll a slot? (y/n): ").lower()
    if user == "y":
        main()
    if user == "n":
        print(f"You left with ${bank}")
        break