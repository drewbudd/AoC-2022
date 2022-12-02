def main():
    input = open('input.txt', 'r')
    lines = input.readlines()

    for line in lines:
        print(f'{line}')

    input.close()

if __name__ == '__main__':
    main()