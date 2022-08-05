clear_map = lambda: print("\n" * 100)


def map(field):
    print("-" * 25)
    for i in range(3):
        print("|  ", field[0 + i * 3], "  |  ", field[1 + i * 3], "  |  ", field[2 + i * 3], "  |")
        print("-" * 25)


def check_win(field):
    for value in win_coord:
        if field[value[0]] == field[value[1]] == field[value[2]]:
            return field[value[0]]
    return False


def move_player(player):
    valid = False
    while not valid:
        go = input(f'Where to put {player} ?')
        try:
            go = int(go)
        except:
            print('Invalid input. You need to enter the numbers.')
            continue

        if go >= 1 and go <= 9:
            if str(field[go - 1]) not in "XO":
                field[go - 1] = player
                valid = True
                clear_map()
            else:
                print('This cell is already occupied')
        else:
            print('Invalid input. Enter a number from 1 to 9')


def bot_strives_victory(sum_O, sum_X):
    step = ""
    for value in win_coord:
        o = 0
        x = 0

        for i in range(0, 3):
            if field[value[i]] == "O":
                o = o + 1
            elif field[value[i]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for i in range(0, 3):
                if field[value[i]] != "O" and field[value[i]] != "X":
                    step = field[value[i]]

    return step


def bot_to_go():
    go_bot = ""
    if go_bot == "":
        go_bot = bot_strives_victory(2, 0)
    if go_bot == "":
        go_bot = bot_strives_victory(0, 2)
    if go_bot == "":
        go_bot = bot_strives_victory(1, 0)
    if go_bot == "":
        if field[4] != "X" and field[4] != "O":
            go_bot = 5
    if go_bot == "":
        if field[0] != "X" and field[0] != "O":
            go_bot = 1
    return go_bot


def game(field):
    count = 0

    while True:
        map(field)

        if count % 2 == 0:
            move_player('X')
        else:
            clear_map()
            print('The computer made a move')
            field[bot_to_go() - 1] = 'O'

        count += 1

        if count > 4:
            there_is_winner = check_win(field)
            if there_is_winner:
                print(f'Congratulations {there_is_winner}, won!')
                break

        if count == 9:
            print("It's a draw this time!")
            break

    map(field)


player = input('Enter the name of the player: ')
print(f'Hello {player}! You will be "X" and go first')

field = list(range(1, 10))
win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
game(field)
