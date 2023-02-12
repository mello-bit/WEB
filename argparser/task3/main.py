import argparse


def count_lines(file):

    try:
        with open(file) as fl:
            return len(fl.readlines())

    except FileNotFoundError:
        return 0


parser = argparse.ArgumentParser()
parser.add_argument("--file")
args = parser.parse_args()

print(count_lines(args.file))
