import sys

try:
    par = list(map(int, [sys.argv[1], sys.argv[2]]))
    s = sum(par)
    print(s)
except Exception:
    print(0)
