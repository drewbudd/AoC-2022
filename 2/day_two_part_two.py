'''Advent of Code 2022 Day Two'''

def main():
    '''https://adventofcode.com/2022/day/2#part2'''
    with open('input.txt', 'r', encoding="utf8") as input_file:
        lines = input_file.readlines()

        score = 0

        for line in lines:
            opponent = line[0]
            user = line[2]
            match user:
                case 'X':  # lose
                    if opponent == 'A':
                        score += 3
                    elif opponent == 'B':
                        score += 1
                    elif opponent == 'C':
                        score += 2
                case 'Y':  # draw
                    score += 3
                    if opponent == 'A':
                        score += 1
                    elif opponent == 'B':
                        score += 2
                    elif opponent == 'C':
                        score += 3
                case 'Z':  # win
                    score += 6
                    if opponent == 'A':
                        score += 2
                    elif opponent == 'B':
                        score += 3
                    elif opponent == 'C':
                        score += 1
                case _:
                    print('input invalid')

        print(score)
        input.close()


if __name__ == '__main__':
    main()
