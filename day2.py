# Advent of Code 2022
#
# created by Gabriel Salazar

def yan_quen_po(p1: str, p2: str):
    match_dict = {'AX': 4, 'AY': 8, 'AZ': 3,
                  'BX': 1, 'BY': 5, 'BZ': 9,
                  'CX': 7, 'CY': 2, 'CZ': 6}
    return match_dict[p1+p2]

def yan_quen_two(p1: str, p2: str):
    match_dict = {'AX': 'Z', 'AY': 'X', 'AZ': 'Y',
                  'BX': 'X', 'BY': 'Y', 'BZ': 'Z',
                  'CX': 'Y', 'CY': 'Z', 'CZ': 'X'}
    return match_dict[p1+p2]

def part1(data_path: str):
    with open(data_path) as file:
        count = 0
        for line in file:
            formatted_line = line.rstrip().split(" ")
            player_1, player_2 = formatted_line[0], formatted_line[1]
            round_score = yan_quen_po(player_1, player_2)
            count = count + round_score
    return count

def part2(data_path: str) -> int:
    with open(data_path) as file:
        count = 0
        for line in file:
            formatted_line = line.rstrip().split(" ")
            player_1, player_2 = formatted_line[0], formatted_line[1]
            new_move = yan_quen_two(player_1, player_2)
            round_score = yan_quen_po(player_1, new_move)
            count = count + round_score
    return count

if __name__ == '__main__':
    # input
    data_path = 'input/day2.txt'

    # part 1 + 2
    print(part1(data_path))
    print(part2(data_path))

    print('Advent of Code 2022!')
