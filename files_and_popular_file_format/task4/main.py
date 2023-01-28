import json
import sys


with open("scoring.json") as file:
    data = json.load(file)

info = {}

for dc in data["scoring"]:
    average_point = dc["points"] / len(dc["required_tests"])
    for n in dc["required_tests"]:
        info[n] = average_point

score = 0
i = 1
for answer in sys.stdin:
    answer = answer.strip()
    if answer == "ok":
        score += info[i]

    i += 1

print(int(score))
