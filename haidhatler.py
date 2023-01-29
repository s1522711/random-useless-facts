import requests
import sys

def delete_multiple_lines(n=1):
    """Delete the last line in the STDOUT."""
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line

def PrintFact():
    fact = requests.get("https://uselessfacts.jsph.pl/random.txt?language=en")
    print("\n",fact.text,"\n")
    delete_multiple_lines(2)

while True:
    menu = 0
    menu = input("Enter 1 to get a random fact and e to exit: ")
    if menu == "1":
        menu=int(menu)
    else:
        menu = menu.lower()

    if menu == 1:
        PrintFact()
    elif menu == "e":
        delete_multiple_lines(1)
        exit(0)
    else:
        print("Please enter 1 or e!")