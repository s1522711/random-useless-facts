import requests
import sys

def DeleteMultipleLines(n=1):
    """Delete the last line in the STDOUT."""
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line

def PrintFact():
    ZeFact = requests.get("https://uselessfacts.jsph.pl/random.txt?language=en")
    print("\n",ZeFact.text,"\n")
    DeleteMultipleLines(2)

while True:
    Menu = 0
    Menu = input("Enter 1 to get a random fact and e to exit: ")
    if Menu == "1":
        Menu=int(Menu)
    else:
        Menu = Menu.lower()

    if Menu == 1:
        PrintFact()
    elif Menu == "e":
        DeleteMultipleLines(1)
        exit(0)
    else:
        print("Please enter 1 or e!")