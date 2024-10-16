import sys


def main():
    print('Print stdout', file=sys.stderr)
    print('Print stderr', file=sys.stderr)
    user_input = input()
    print('User input: "{}"'.format(user_input), file=sys.stderr)

if __name__ == '__main__':
    main()