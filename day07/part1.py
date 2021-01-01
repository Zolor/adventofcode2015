data = open("testinput.txt").read().split("\n")

wires = {}
counter = 1

while True:
    new_lista = []
    for line in data:
        inp, outp = line.split(" -> ")
        inp = inp.split()
        print(inp)
        print(outp)
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
            if inp[2] not in wires:
                new_lista.append(line)
                continue
            else:
                wires[outp] = int(wires.get(inp[0])) & int(wires.get(inp[2]))
        elif "OR" in inp:
            if inp[2] not in wires:
                new_lista.append(line)
                continue
            else:
                wires[outp] = int(wires.get(inp[0])) | int(wires.get(inp[2]))
        #If there's just a number
        else:
            if inp[0] in wires:
                wires[outp] = wires.get(inp[0])
            else:
                wires[outp] = inp[0]
    data = new_lista
    counter += 1
    print(data)
    if len(data) == 0 or counter > 7:
        break


print(wires)