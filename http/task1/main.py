import requests


ad = input()
port = input()
a = input()
b = input()

req = requests.get(
    f"{ad}:{port}?a={a}&b={b}"
)

if req.ok:
    req = req.json()
    nums = req['result']
    code = req['check']
    print(*sorted(nums))
    print(code)
