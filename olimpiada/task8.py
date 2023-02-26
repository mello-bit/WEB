s = input()
start_length = len(s)


def checkChars(s: str):
    rb = s.rfind('B')
    lw = s.find('W')

    if rb == -1 or lw == -1:
        return True

    return rb <= lw


def delChars(s: str):
    lW = s.find('W')
    rB = s.rfind('B')

    if lW != -1 and rB != -1:
        s = s[:lW] + s[lW + 1:]
        s = s[:rB - 1] + s[rB:]

    return s


while not checkChars(s):
    s = delChars(s)


print(start_length - len(s))
if s == '':
    print("НИКОГО НЕ ОСТАЛОСЬ")
else:
    print(s)
