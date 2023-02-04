import sys

try:
    ar = list(map(lambda x: int(x), sys.argv[1::]))
except Exception as e:
    print(e.__class__.__name__)
else:
    if len(ar) == 0:
        print("NO PARAMS")
    else:
        for ind, val in enumerate(ar):
            if ind % 2 != 0:
                ar[ind] = val * -1

        print(sum(ar))
