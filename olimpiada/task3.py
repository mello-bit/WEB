mi, ma, cu = [int(input()) for _ in range(3)]

if cu < mi:
    print("Надо нагреть")
elif cu > ma:
    print("Надо остудить")
else:
    print("Нормальная температура")
