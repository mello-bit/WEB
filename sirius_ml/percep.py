import csv
from math import exp


def sign(weigth, values):
    s = 0
    for w, x in zip(weigth, values):
        s += w * x
    
    return 1 if s > 0 else -1 




with open("p.csv", "r") as file:
    src = list(map(lambda x: [int(x[0]), int(x[1]), int(x[2]), int(
        x[3])], csv.reader(file, delimiter=',', quotechar='"')))

w1, w2, wb, lm = 0, 0, 0, 0.5
for i in src:
    x1, x2, xb, y = i
    y1 = sign(weigth=[w1, w2, wb], values=[x1, x2, xb])

    if y1 == y:
        print(w1, w2, wb)
        pass
    else:
        w1 = w1 + lm * (y - y1) * x1
        w2 = w2 + lm * (y - y1) * x2
        wb = wb + lm * (y - y1) * xb

        print(w1, w2, wb)

# print(w1, w2, wb)
for i in src:
    x1, x2, xb, y = i
    s = x1 * w1 + x2 * w2 + wb * xb
    if s > 0:
        y1 = 1
    else:
        y1 = -1

    if y1 == y:
        print("Yes")
        pass
    else:
        print("No")

        # print(w1, w2, wb)


print(round(1 / (1 + 20.08554), 3))
