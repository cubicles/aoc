# Advent of Code 2022
#
# created by Gabriel Salazar

from functools import reduce

def part1(data_path: str):

    priorities = []

    with open(data_path) as file:
        for line in file:
            line_index = int(len(line.rstrip())/2)
            left_side = set(line[:line_index])
            right_side = set(line[line_index:])
            priorities.append((left_side & right_side).pop())

    for idx, character in enumerate(priorities):
        char_order = ord(character)
        if char_order >= 97:
            priorities[idx] = char_order - 96
        else:
            priorities[idx] = char_order - 38

    return sum(priorities)


def part2(data_path: str, n: int):

    priorities = []
    badges = []

    with open(data_path) as file:
        for line in file:
            priorities.append(line.rstrip())
    
    while(len(priorities) != 0):
        sub_list = priorities[:n]
        sub_list = [set(item) for item in sub_list]
        badge = reduce(lambda x, y: x & y, sub_list)
        badges.append(badge.pop())
        for _ in range(n):
            priorities.pop(0)

    for idx, character in enumerate(badges):
        char_order = ord(character)
        if char_order >= 97:
            badges[idx] = char_order - 96
        else:
            badges[idx] = char_order - 38

    return sum(badges)

if __name__ == '__main__':
    # input
    data_path = 'input/day3.txt'

    # part 1 + 2
    print(part1(data_path))
    print(part2(data_path, 3))

    print('Advent of Code 2022!')
