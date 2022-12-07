#!/usr/bin/env zsh

pwd 

touch $1

echo "# Advent of Code 2022
#
# created by Gabriel Salazar

def part1(data_path: str):
    with open(data_path) as file:
        for line in file:
            print(line)

def part2(data_path: str):
    with open(data_path) as file:
        for line in file:
            print(line)

if __name__ == '__main__':
    # input
    data_path = 'input/day2.txt'

    # part 1 + 2
    print(part1(data_path))
    print(part2(data_path))

    print('Advent of Code 2022!')
" >> $1

echo "$1 file created!"

nvim $1
