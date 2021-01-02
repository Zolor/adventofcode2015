import re

data = open("testinput.txt").read().split("\n")

for line in data:
    out = re.sub(r'\W+', '', line)
    print(out)

print('\\\"\"')
