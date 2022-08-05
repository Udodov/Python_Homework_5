from random import randint

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
            if (str(field[go - 1]) not in "XO"):
                field[go - 1] = player
                valid = True
                clear_map()
            else:
                print('This cell is already occupied')
        else:
            print('Invalid input. Enter a number from 1 to 9')


def game(field):
    count = 0

    while True:
        map(field)

        if count % 2 == 0:
            move_player('X')
        else:
            move_player('O')
        count += 1

        if count > 4:
            tmp = check_win(field)
            if tmp:
                print(f'Congratulations {tmp}, won!')
                break

        if count == 9:
            print("It's a draw this time!")
            break

    map(field)


player_1 = input('Enter the name of the first player: ')
player_2 = input('Enter the name of the second player: ')

whose_move = randint(0, 2)
if whose_move:
    print(f'The lot fell to the player {player_1}, he will be "X" and will go first')
else:
    print(f'The lot fell to the player {player_2}, he will be "X" and will go first')

field = list(range(1, 10))
win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
game(field)
