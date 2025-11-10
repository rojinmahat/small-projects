import random
import time

def roll():
    print("Rolling.", end="", flush=True)
    time.sleep(1)
    print(".", end="", flush=True)
    time.sleep(1)
    print(".")
    time.sleep(0.5)
    return random.randint(1,6)

run = True

while True:
    input('Press enter to roll the dice...')
    print(f"You rolled a {roll()}")

    while True:
        again = input("Roll again?: \n").lower().strip()

        if(again == "yes" or again == "y"):
            break
        elif(again == "no" or again == "n"):
            run = False
            break
        else:
            print("Sorry, I didn't get that 😖. Try again.")
    
    if(run!=True):
        print("Goodbye! See you soon.")
        time.sleep(4)
        break
