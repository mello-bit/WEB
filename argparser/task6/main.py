import os.path
import sys


count1 = 0
items = sys.argv[1:]
strings = []
num = False
count = False
sort = False
flag = False
for i in items:
    if i == '--num':
        num = True
    if i == '--sort':
        sort = True
    if i == '--count':
        count = True
if sort:
    items.pop(items.index('--sort'))
if num:
    items.pop(items.index('--num'))
if count:
    items.pop(items.index('--count'))
try:
    with open(items[0], encoding='utf8') as file:
        for line in file.readlines():
            line = line.rstrip('\n')
            strings.append(line)
    if sort:
        strings = sorted(strings)

    if num:
        for i in range(len(strings)):
            print(i, strings[i])
    else:
        for i in range(len(strings)):
            print(strings[i])

    if count:
        print('rows count:', len(strings))

except FileNotFoundError:
    print('ERROR')
