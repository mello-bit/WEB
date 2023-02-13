import argparse


parser = argparse.ArgumentParser()
parser.add_argument("nums", nargs='*')

args = parser.parse_args()
try:
    n = list(map(int, args.nums))
    if len(n) == 0:
        print("NO PARAMS")
    elif len(n) == 1:
        print("TOO FEW PARAMS")
    elif len(n) > 2:
        print("TOO MANY PARAMS")
    else:
        print(sum(n))
except Exception as e:
    print(e.__class__.__name__)
