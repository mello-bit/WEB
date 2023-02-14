import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--sort", action="store_true")
parser.add_argument("dict", nargs='*')

items = parser.parse_args()
# ld = list(map(lambda x: x.split('='), items.dict))

if items.sort:
    ld = dict(
        sorted(list(map(lambda x: x.split('='), items.dict)), key=lambda x: x[0]))
else:
    ld = dict(list(map(lambda x: x.split('='), items.dict)))

for k, v in ld.items():
    print(f"Key: {k} Value: {v}")
