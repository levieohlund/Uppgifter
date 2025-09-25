import random
#loop
while True:
    choice = input("Do you want to roll the dice? (y/n) ").strip().lower()
    print(f"Du skrev: '{choice}'")
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("invalid choice")
