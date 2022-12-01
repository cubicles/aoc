# Advent of Code 2022
#
# created by Gabriel Salazar

def part1(data_path: str) -> list:
    calories_list = [0]
    index = 0
    with open(data_path) as file:
        for line in file:
            if line.rstrip() != '':
                calories_list[index] = calories_list[index] + int(line.rstrip())
            else:
                index = index + 1
                calories_list.append(0)
    return calories_list

def part2(data_path: str) -> int:
    calories_list = sorted(part1(data_path))
    return sum(calories_list[-3:])

if __name__ == '__main__':
    # input
    data_path = 'input/day1.txt'

    # part 1 + 2
    print(max(part1(data_path)))
    print(part2(data_path))

    print('Advent of Code 2022!')
