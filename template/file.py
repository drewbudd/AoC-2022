def main():
    input = open('input.txt', 'r')
    lines = input.readlines()

    for line in lines:
        print(f'{line}')


if __name__ == '__main__':
    main()
