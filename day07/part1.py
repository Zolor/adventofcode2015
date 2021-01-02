data = open("input.txt").read().split("\n")

wires = {}
counter = 1

while True:
    new_lista = []
    for line in data:
        inp, outp = line.split(" -> ")
        inp = inp.split()
        if "NOT" in inp:
            if inp[1] not in wires:
                new_lista.append(line)
                continue
            else:
                wires[outp] = 65535 - int(wires.get(inp[1]))
        elif "RSHIFT" in inp:
            if inp[0] not in wires:
                new_lista.append(line)
                continue
            else:
                wires[outp] = int(wires.get(inp[0])) >> int(inp[2])
        elif "LSHIFT" in inp:
            if inp[0] not in wires:
                new_lista.append(line)
                continue
            else:
                wires[outp] = int(wires.get(inp[0])) << int(inp[2])
        elif "AND" in inp:
            if inp[0].isnumeric() and inp[2].isnumeric():
                wires[outp] = int(inp[0]) & int(inp[2])
            elif inp[2].isnumeric():
                if inp[0] not in wires:
                    new_lista.append(line)
                    continue
                else:
                    wires[outp] = int(wires.get(inp[0])) & int(inp[2])
            elif inp[0].isnumeric():
                if inp[2] not in wires:
                    new_lista.append(line)
                    continue
                else:
                    wires[outp] = int(inp[0]) & int(wires.get(inp[2]))
            elif inp[2] not in wires or inp[0] not in wires:
                new_lista.append(line)
                continue
            else:
                wires[outp] = int(wires.get(inp[0])) & int(wires.get(inp[2]))
        elif "OR" in inp:
            if inp[0].isnumeric() and inp[2].isnumeric():
                wires[outp] = int(inp[0]) | int(inp[2])
            elif inp[2].isnumeric():
                if inp[0] not in wires:
                    new_lista.append(line)
                    continue
                else:
                    wires[outp] = int(wires.get(inp[0])) | int(inp[2])
            elif inp[0].isnumeric():
                if inp[2] not in wires:
                    new_lista.append(line)
                    continue
                else:
                    wires[outp] = int(inp[0]) | int(wires.get(inp[2]))
            elif inp[2] not in wires or inp[0] not in wires:
                new_lista.append(line)
                continue
            else:
                wires[outp] = int(wires.get(inp[0])) | int(wires.get(inp[2]))
        #If there's just a number
        else:
            if inp[0] in wires:
                wires[outp] = wires.get(inp[0])
            elif inp[0].isnumeric():
                wires[outp] = inp[0]
            else:
                new_lista.append(line)
                continue
    data = new_lista
    counter += 1
    if len(data) == 0:
        break

print(wires.get("a"))