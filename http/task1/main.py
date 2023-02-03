import requests


ad = input()
port = input()
a = input()
b = input()

req = requests.get(
    f"{ad}:{port}?a={a}&b={b}"
).json()

nums = req['result']
nums = ' '.join(sorted(nums))
code = req['check']

print(nums)
print(code)
