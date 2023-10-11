# This text-based program takes any string input and converts it to morse code.
from art import art

dic = {
    "A": "*-",
    "B": "-***",
    "C": "-*-*",
    "D": "-**",
    "E": "*",
    "F": "**-*",
    "G": "--*",
    "H": "****",
    "I": "**",
    "J": "*---",
    "K": "-*-",
    "L": "*-**",
    "M": "--",
    "N": "-*",
    "O": "---",
    "P": "*--*",
    "Q": "--*-",
    "R": "*-*",
    "S": "***",
    "T": "-",
    "U": "**-",
    "V": "***-",
    "W": "*--",
    "X": "-**-",
    "Y": "-*--",
    "Z": "--**",
    "1": "*----",
    "2": "**---",
    "3": "***--",
    "4": "****-",
    "5": "*****",
    "6": "-****",
    "7": "--***",
    "8": "---**",
    "9": "----*",
    "0": "-----",
    " ": " ",
}
keep_going = True

print(art)

while keep_going:
    text = input("What would you like to translate? ").upper()
    morse = []
    restart = False

    for char in text:
        if char in dic:
            morse.append(dic[char])
        else:
            print("Sorry, the database doesn't contain characters with accents. Please try again.")
            restart = True
            break

    if not restart:
        result = " ".join(morse)
        print(f"Your text in morse is:\n{result}")

    should_continue = input("Would you like to translate again? Type Y or N: ").upper()

    if should_continue != "Y":
        keep_going = False
