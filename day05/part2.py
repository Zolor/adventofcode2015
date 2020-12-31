data = open("input.txt").read().split("\n")

nice = 0


def naughty_or_nice(kid):
    first_test = False
    for p in range(len(kid)):
        if p == len(kid) - 1:
            break
        else:
            tmp_letters = kid[p] + kid[p + 1]
            for p2 in range(len(kid)):
                if p == p2:
                    continue
                elif p2 + 1 == len(kid):
                    break
                elif tmp_letters == kid[p2] + kid[p2 + 1]:
                    first_test = True
                    break
    second_test = False
    if first_test:
        for k in range(len(kid)):
            if k + 1 == len(kid) - 1:
                break
            else:
                if kid[k] == kid[k + 2]:
                    second_test == True
                    break
    else:
        return False
    if first_test and second_test:
        return True
    else:
        return False

for row in data:
    if naughty_or_nice(row) == True:
        nice += 1

print(nice)
