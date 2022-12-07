# Advent of Code 2022
#
# created by Gabriel Salazar

def part1(data_path: str):
    with open(data_path) as file:
        count = 0
        for line in file:
            print(line)
    return 0

def part2(data_path: str):
    with open(data_path) as file:
        for line in file:
            print(line)
    return 0

if __name__ == '__main__':
    # input
    data_path = 'input/day3.txt'

    # part 1 + 2
    print(part1(data_path))
    print(part2(data_path))

    print('Advent of Code 2022!')
