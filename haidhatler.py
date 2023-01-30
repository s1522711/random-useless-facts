import requests
import sys
fact_list = []

def delete_multiple_lines(n=1):
    """Delete the last line in the STDOUT."""
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line


def new_facts():
    print("LOADING FACTS - PLEASE WAIT!")
    loading_loopvar = 0
    fact_list.clear
    while loading_loopvar != 10:
        fact_list.append(requests.get("https://uselessfacts.jsph.pl/random.txt?language=en").text)
        print(loading_loopvar+1)
        loading_loopvar += 1
    delete_multiple_lines(10)
    print("DONE!")

new_facts()

current_fact = 0

while True:
    menu = 0
    menu = input("Enter 1 to get a random fact and e to exit: ")
    if menu == "1":
        menu=int(menu)
    else:
        menu = menu.lower()

    if menu == 1:
        if current_fact > 9:
            new_facts()
            current_fact = 0
            delete_multiple_lines(2)
        print("\n",fact_list[current_fact],"\n")
        delete_multiple_lines(2)
        current_fact += 1
    elif menu == "e":
        delete_multiple_lines(1)
        exit(0)
    else:
        print("Please enter 1 or e!")