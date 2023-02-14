import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("--num", action="store_true")
parser.add_argument("--sort", action="store_true")
parser.add_argument("--count", action="store_true")
parser.add_argument("file")
items = parser.parse_args()
strings = []
num = False
count = False
sort = False

try:
    with open(items.file, encoding='utf8') as file:
        for line in file.readlines():
            line = line.rstrip('\n')
            strings.append(line)
    if items.sort:
        strings = sorted(strings)

    if items.num:
        for i in range(len(strings)):
            print(i, strings[i])
    else:
        for i in range(len(strings)):
            print(strings[i])

    if items.count:
        print('rows count:', len(strings))

except FileNotFoundError:
    print('ERROR')
