data = open("testinput.txt").read().split("\n")

summa = 0

for line in data:
    remove_specials = line.encode(encoding='UTF-8',errors='strict')
    remove_specials = remove_specials.decode('unicode_escape')
    remove_specials = remove_specials[1:-1]
    print(remove_specials)
    summa += len(line) - len(remove_specials)

print(summa)