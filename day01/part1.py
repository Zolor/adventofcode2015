data = open("input.txt").read()

floor = 0

for x in data:
    if x == "(":
        floor += 1
    elif x == ")":
        floor -= 1

print(floor)