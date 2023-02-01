# Advent of Code 2022
#
# created by Gabriel Salazar

def part1(data_path: str):

    stack = []

    with open(data_path) as file:
        for line in file:
            if line == "\n": break
            # Get the lines (contents)
            stack.append([line[k * 4 + 1] for k in range(len(line) // 4)])

        # Removes last row
        stack.pop()
        # Unpack using zip, join the strings and split them (removes empty
        # spaces and removes the need of tuples (zip output)
        data = [list("".join(col).strip()[::-1]) for col in zip(*stack)]
        
        # Returns after the break, reads movements
        for line in file:
            a = line.split("from")[0].strip().split(" ")[1]
            b = line.split("from")[1].strip().split(" ")[0]
            c = line.split("to")[1].strip().split(" ")[0]
            # cast a, b and c to int
            a, b, c = int(a), int(b), int(c)
            data[c - 1].extend(data[b - 1][-a:][::-1])
            data[b - 1] = data[b - 1][:-a]
    
        a = "".join([a[-1] for a in data])
        return a


def part2(data_path: str):

    stack = []

    with open(data_path) as file:
        for line in file:
            if line == "\n": break
            # Get the lines (contents)
            stack.append([line[k * 4 + 1] for k in range(len(line) // 4)])

        # Removes last row
        stack.pop()
        # Unpack using zip, join the strings and split them (removes empty
        # spaces and removes the need of tuples (zip output)
        data = [list("".join(col).strip()[::-1]) for col in zip(*stack)]
        
        # Returns after the break, reads movements
        for line in file:
            a = line.split("from")[0].strip().split(" ")[1]
            b = line.split("from")[1].strip().split(" ")[0]
            c = line.split("to")[1].strip().split(" ")[0]
            # cast a, b and c to int
            a, b, c = int(a), int(b), int(c)
            data[c - 1].extend(data[b - 1][-a:])
            data[b - 1] = data[b - 1][:-a]
    
        a = "".join([a[-1] for a in data])
        return a

if __name__ == '__main__':
    # input
    data_path = 'input/day5.txt'

    # part 1 + 2
    print(part1(data_path))
    print(part2(data_path))

    print('Advent of Code 2022!')

