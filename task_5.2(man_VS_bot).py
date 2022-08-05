from random import randint


def entering_sweets(number: str) -> int:
    num = int(input(f"{number}, How many candies will you take?  (from 1 to 28): "))
    while num < 1 or num > 28:
        num = int(input(f"{number}, Enter the correct number of candies: "))
    return num


def remains(player: str, quantity: int, total: int):
    print(f'{player} took {quantity}. On the table {total} sweets.')


player_1 = input('Name of the first player: ')
player_2 = 'bot'
total_sweets, count_1, count_2 = 2021, 0, 0

whose_move = randint(0, 2)
if whose_move:
    print(f'The lot fell to the player {player_1}, he goes first')
else:
    print(f'The lot fell to the player {player_2}, he goes first')

while total_sweets > 28:
    if whose_move:
        sweets = entering_sweets(player_1)
        count_1 += sweets
        total_sweets -= sweets
        whose_move = False
        remains(player_1, sweets, total_sweets)
    else:
        sweets = randint(1, 29)
        count_2 += sweets
        total_sweets -= sweets
        whose_move = True
        remains(player_2, sweets, total_sweets)

if whose_move:
    print(f'Won {player_1}')
else:
    print(f'Won {player_2}')
