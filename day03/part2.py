from collections import defaultdict
data = open("input.txt").read()

santa_loc = [0,0]
robo_loc = [0,0]
tmp_tuple = ()
direction_data = {}

for n, d in enumerate(data):
    if n == 0:
        direction_data[(0,0)] = 2
    if (n % 2) == 0:
        if d == "^":
            robo_loc[0] += 1
        elif d == "v":
            robo_loc[0] -= 1
        elif d == ">":
            robo_loc[1] += 1
        elif d == "<":
            robo_loc[1] -= 1
        tmp_tuple = tuple(robo_loc)
    else:
        if d == "^":
            santa_loc[0] += 1
        elif d == "v":
            santa_loc[0] -= 1
        elif d == ">":
            santa_loc[1] += 1
        elif d == "<":
            santa_loc[1] -= 1
        tmp_tuple = tuple(santa_loc)
    if tmp_tuple not in direction_data:
        direction_data[tmp_tuple] = 1
    else:
        direction_data[tmp_tuple] = direction_data.get(tmp_tuple) + 1

if tmp_tuple not in direction_data:
    direction_data[tmp_tuple] = 1
else:
    direction_data[tmp_tuple] = direction_data.get(tmp_tuple) + 1

print(len(direction_data))