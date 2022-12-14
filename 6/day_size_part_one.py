'''Advent of Code 2022 Day Six'''


def check_if_start_marker(marker: list) -> bool:
    '''helper method that checks if start marker conditions are met'''
    marker_set = set(marker)
    if len(marker_set) == len(marker):
        return True
    return False


def main():
    '''https://adventofcode.com/2022/day/6'''
    with open('input.txt', 'r', encoding="utf8") as input_file:
        line = input_file.readline()

        for index in range(4, len(line)):
            if check_if_start_marker(line[(index - 4):index]):
                print(f'marker at {index}')
                break


if __name__ == '__main__':
    main()
