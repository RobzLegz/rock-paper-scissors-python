import random

while True:
    print("Pick your choice:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    choice = int(input("Select: "))

    choice_to_pick = ["Rock", "Paper", "Scissors"]

    element = choice_to_pick[choice - 1]

    def generate_random_number():
        return random.randint(0, 2)

    computer_element = choice_to_pick[generate_random_number()]

    winning_values = {
        "Rock": "Scissors",
        "Scissors": "Paper",
        "Paper": "Rock"
    }

    if element == computer_element:
        print("--> Its a tie <--")
    else:
        if computer_element == winning_values[element]:
            print("--> You win <--")
        else:
            print("--> You lose <--")

    print(f"Your choice: {element}, computer choice: {computer_element}")

    print("")
    print("")

    print("Do you want to continue?")
    print("1 - yes")
    print("2 - no")

    con = input("Enter: ")
    if con != "1":
        break

    print("")

