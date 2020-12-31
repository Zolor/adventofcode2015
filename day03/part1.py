from collections import defaultdict
data = open("input.txt").read()

loc = [0,0]

direction_data = {}

for d in data:
    if tuple(loc) not in direction_data:
        direction_data[tuple(loc)] = 1
    else:
        direction_data[tuple(loc)] = direction_data.get(tuple(loc)) + 1
    if d == "^":
        loc[0] += 1
    elif d == "v":
        loc[0] -= 1
    elif d == ">":
        loc[1] += 1
    elif d == "<":
        loc[1] -= 1
if tuple(loc) not in direction_data:
    direction_data[tuple(loc)] = 1
else:
    direction_data[tuple(loc)] = direction_data.get(tuple(loc)) + 1

print(len(direction_data))