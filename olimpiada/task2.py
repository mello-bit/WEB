a = int(input())
b = int(input())
t = int(input())
count = 0


while t > 0:
    t -= a
    if t >= 0:
        count += 1
    t -= b


print(count)
