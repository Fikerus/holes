from sys import argv
from table import table

def main():
    args = ' '.join(argv[1:])
    print(f'Input: {args}')

    unsupported = []
    number_of_holes = 0

    for symbol in args:
        if symbol in table:
            number_of_holes += table[symbol]
        else:
            unsupported.append(symbol)
    if not unsupported:
        print(number_of_holes)
    else:
        print('There are symbols that are not supported')
        print('Estimated number of holes:')
        print(f'>= {number_of_holes}')
        print('Symbols that were not counted:')
        print(', '.join(map(lambda x: f'"{x}"', unsupported)))

if __name__ == '__main__':
    main()
