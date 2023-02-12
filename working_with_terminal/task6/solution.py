import sys


s = sys.argv[1::]
sort_it = False
start_ind = 0
if '--sort' in s:
    sort_it = True

res = {}
for i in s:
    if i != '--sort':
        key, val = i.split('=')
        res[key] = val

if sort_it:
    sorted_keys = sorted(res)
else:
    sorted_keys = res.keys()

for key in sorted_keys:
    print(f"Key: {key} Value: {res[key]}")
