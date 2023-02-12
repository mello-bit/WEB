import argparse


parser = argparse.ArgumentParser()
m = {
    "melodrama": 0,
    "football": 100,
    "other": 50
}
int_movie = 0

parser.add_argument("--cars", default=50, type=int)
parser.add_argument("--barbie", default=50, type=int)
parser.add_argument("--movie", default="movie", type=str)

args = parser.parse_args()

if args.cars > 100 or args.cars < 0:
    args.cars = 50
if args.barbie > 100 or args.barbie < 0:
    args.barbie = 50
if args.movie not in ["melodrama", "football", "other"]:
    int_movie = 50
else:
    int_movie = m[args.movie]

boys = int((100 - args.barbie + args.cars + int_movie) / 3)
girl = 100 - boys

print(f"boy: {boys}")
print(f"girl: {girl}")
