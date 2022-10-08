from sys import argv
from table import table

def main():
    args = ' '.join(argv[1:])
    print(args)
    print(sum(map(lambda x: table[x], args)))

if __name__ == '__main__':
    main()
