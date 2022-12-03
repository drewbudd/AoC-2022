def main():
    input = open('input.txt', 'r')
    lines = input.readlines()

    score = 0

    for line in lines:
        opponent = line[0]
        user = line[2]
        match user:
            case 'X':
                score += 1
                if opponent == 'A':
                    score += 3
                elif opponent == 'C':
                    score += 6
            case 'Y':
                score += 2
                if opponent == 'B':
                    score += 3
                elif opponent == 'A':
                    score += 6
            case 'Z':
                score += 3
                if opponent == 'C':
                    score += 3
                elif opponent == 'B':
                    score += 6
            case _:
                print('input invalid')

    print(score)
    input.close()


if __name__ == '__main__':
    main()
