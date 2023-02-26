s = list(input().replace(' ', ''))

gl = "ауоиэыяюеё"
n = "н"
count = 0

for i in range(len(s) - 1):
    if s[i] in gl and s[i + 1] in gl and i == 0:
        s[i] = n
        count += 1
    elif s[i] not in gl and s[i + 1] not in gl and i == 0:
        s[i] = gl[0]
        count += 1
    elif s[i] in gl and s[i + 1] in gl:
        s[i + 1] = n
        count += 1
    elif s[i] not in gl and s[i + 1] not in gl:
        s[i + 1] = gl[0]
        count += 1

print(count)
