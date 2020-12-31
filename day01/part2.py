data = open("input.txt").read()

floor = 0
first = True

for n, x in enumerate(data):
    if x == "(":
        floor += 1
    elif x == ")":
        floor -= 1
    if floor == -1 and first == True:
        first = False
        print(n+1)
        break
