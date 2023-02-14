import argparse


def print_error(mes):
    print(f"ERROR: {mes}!!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mes", nargs='?')
    item = parser.parse_args()
    print("Welcome to my program")
    print_error(item.mes)


if __name__ == '__main__':
    main()
