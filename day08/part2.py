data = open("input.txt").read().split("\n")

summa = 0

for line in data:
    new_line = ""
    print(line)
    for n, l in enumerate(line):
        if n == 0:
            new_line += '\"\\"'
        elif n == len(line) - 1:
            new_line += '\\\"\"'
        elif l.isnumeric() or l.isalpha():
            new_line += l
        else:
            if l == "\\" and line[n + 1] == "x":
                new_line += "\\"
                new_line += l
            elif l == "\\" and line[n + 1] == '"':
                new_line += "\\"
                new_line += l
            elif l == "\\":
                new_line += "\\"
                new_line += l
            elif l == '"':
                new_line += "\\"
                new_line += l
            else:
                new_line += l
    print(new_line)
    summa += len(new_line) - len(line) 

print(summa)