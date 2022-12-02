# Advent of Code 2022
#
# created by Gabriel Salazar

def yan_quen_po(p1: str, p2: str):
    if p1 == 'A':
        if p2 == 'X':
            return 4
        if p2 == 'Y':
            return 8
        if p2 == 'Z':
            return 3
    if p1 == 'B':
        if p2 == 'X':
            return 1
        if p2 == 'Y':
            return 5
        if p2 == 'Z':
            return 9
    if p1 == 'C':
        if p2 == 'X':
            return 7
        if p2 == 'Y':
            return 2
        if p2 == 'Z':
            return 6
    else:
        return "ERROR"


def yan_quen_two(p1: str, p2: str):
    if p1 == 'A':
        if p2 == 'X':
            return 'Z'
        if p2 == 'Y':
            return 'X'
        if p2 == 'Z':
            return 'Y'
    if p1 == 'B':
        if p2 == 'X':
            return 'X'
        if p2 == 'Y':
            return 'Y'
        if p2 == 'Z':
            return 'Z'
    if p1 == 'C':
        if p2 == 'X':
            return 'Y'
        if p2 == 'Y':
            return 'Z'
        if p2 == 'Z':
            return 'X'
    else:
        return "ERROR"

def part1(data_path: str):
    with open(data_path) as file:
        count = 0
        for line in file:
            player_1 = line.rstrip().split(" ")[0]
            player_2 = line.rstrip().split(" ")[1]
            score_round = yan_quen_po(player_1, player_2)
            count = count + score_round
    return count

def part2(data_path: str) -> int:
    with open(data_path) as file:
        count = 0
        for line in file:
            player_1 = line.rstrip().split(" ")[0]
            player_2 = line.rstrip().split(" ")[1]
            new_move = yan_quen_two(player_1, player_2)
            score_round = yan_quen_po(player_1, new_move)
            count = count + score_round
    return count

if __name__ == '__main__':
    # input
    data_path = 'input/day2.txt'

    # part 1 + 2
    print(part1(data_path))
    print(part2(data_path))

    print('Advent of Code 2022!')
