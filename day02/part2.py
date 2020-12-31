data = open("input.txt").read().split("\n")

total = 0

for gift in data:
    l, w, h = [int(x) for x in gift.split("x")]
    tmp_lista = [l, w, h]
    print(tmp_lista)
    smallest = min(tmp_lista)
    tmp_lista.remove(smallest)
    next_smallest = min(tmp_lista)
    total += smallest + smallest + next_smallest + next_smallest
    total += (l * w * h)

print(total)

#3828105 Too high