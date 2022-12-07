# Advent of Code 2022
#
# created by Gabriel Salazar

def part1_and_2(data_path: str, stacker_count: int):
    with open(data_path) as file:
        for line in file:
            char_buffer = line

    aux_stack = []
    change = len(aux_stack)
    for idx, char in enumerate(char_buffer):
        aux_stack.append(char)
        change = len(aux_stack) - change
        if (change > 0) & (len(aux_stack) == stacker_count):
            if len(set(aux_stack)) == stacker_count:
                return idx + 1
            else:
                aux_stack.pop(0)
                pass
        if change > 0 & len(aux_stack) < stacker_count:
            change = len(aux_stack)
            pass
        if change <= 0:
            aux_stack.pop(0)
            change = len(aux_stack)
    return -1

if __name__ == '__main__':
    # input
    data_path = 'input/day6.txt'

    # part 1 + 2
    print(part1_and_2(data_path, 4))
    print(part1_and_2(data_path, 14))

    print('Advent of Code 2022!')
