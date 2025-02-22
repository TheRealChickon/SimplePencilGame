from random import randint

players = ["John", "Jack"]
winning_positions = list()  # create empty list so we can use the module .extend later when adding nums
loosing_positions = None
pencils = None
last_player = None
human = "John"


def winning_status(current_pencil):
    return current_pencil in winning_positions


def check_lists(list_to_check, value_to_find):
    for i in list_to_check:
        if value_to_find in i:
            return bool(value_to_find)


def get_pencils():
    number = (input("How many pencils would you like to use: "))

    while True:
        try:
            number = int(number)
        except ValueError:
            number = input("The number of pencils should be numeric ")
        else:
            if number > 0:
                return number
            elif number == 0:
                number = input("The number of pencils should be positive ")
            else:
                number = input("The number of pencils should be numeric ")


def ask_user():
    global last_player, pencils, human
    first_user = input(f"Who will be the first ({players[0]}, {players[1]}) ")

    while True:
        if first_user not in players:
            first_user = input(f"Choose between '{players[0]}' and '{players[1]}' ")
        else:
            return first_user


def switch_player():
    global last_player

    if last_player == players[0]:
        last_player = players[1]
    else:
        last_player = players[0]


def remove_pencil():
    #  4,8,12,16... - bot takes 3 pencils
    #  3,7,11,15... - bot takes 2 pencils
    #  2,6,10,14... - bot takes 1 pencil

    global pencils, human, last_player

    if last_player == human:

        to_remove = (input())
        while True:
            if not str(to_remove).isdigit():
                to_remove = input("Possible values: '1', '2' or '3' ")
                continue
            else:
                to_remove = int(to_remove)

            if 1 <= to_remove <= 3 and to_remove <= pencils:
                return to_remove
            else:
                if to_remove >= pencils and 1 <= to_remove <= 3:
                    to_remove = input("Too many pencils were taken ")
                else:
                    to_remove = input("Possible values: '1', '2' or '3' ")
    else:
        # print(f"WINNING: {bool(check_lists(winning_positions, pencils))}")
        if check_lists(winning_positions, pencils):
            # Check how many pencils to remove in winning position.
            if pencils in winning_positions[0]:
                to_remove = 1
                print(to_remove)

            elif pencils in winning_positions[1]:
                to_remove = 2
                print(to_remove)

            elif pencils in winning_positions[2]:
                to_remove = 3
                print(to_remove)
        else:
            if pencils == 1:
                to_remove = 1
                print(to_remove)
            else:
                to_remove = randint(1, 3)
                print(to_remove)

        return to_remove


def current_round():
    return f"{'|' * pencils}\n{last_player}'s turn:"


def bot_move():
    global pencils

    if pencils:
        pass
    else:
        pass


def play_round():
    global pencils, human, last_player

    print(current_round())
    pencils -= remove_pencil()
    switch_player()


def initiate_values():
    global pencils, last_player, winning_positions, loosing_positions

    pencils = get_pencils()

    last_player = ask_user()

    for i in range(2, 5):  # 5 because range only goes to N - 1
        winning_positions.append(list(range(i, pencils + 4, 4)))

    # print(pencils) # Dont print if first round is Human Player

    loosing_positions = list(range(5, pencils + 4, 4))


def start():
    global pencils, last_player, winning_positions, loosing_positions
    initiate_values()
    while pencils > 0:
        play_round()

    # Print the Winner, we only switch the player if the pencils > 0
    print(f"{last_player} won!")


if __name__ == "__main__":
    start()

# Done with Step 1, 2, 3, 4, 5, 6
# Defined Winning and Loosing Positions.
