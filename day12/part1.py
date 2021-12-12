import re

data = open("input.txt").read().split("\n")
resultat = 0
numbers = re.findall(r'[-+]?\d+', data[0])


for x in numbers:
    resultat += int(x)

print(resultat)