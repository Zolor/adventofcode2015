data = open("input.txt").read().split("\n")

lights = {}

#op = on, off, toggle
#True = On, False = Off
def lightshow(op, range_x, range_y):
    for x in range_x:
        for y in range_y:
            tmp_tuple = (x, y)
            if tmp_tuple not in lights:
                lights[tmp_tuple] = False
            if op == "on":
                lights[tmp_tuple] = True
            elif op == "off":
                lights[tmp_tuple] = False
            elif op == "toggle":
                lights[tmp_tuple] = not lights.get(tmp_tuple)

for line in data:
    tmp_lista = [tuple(map(int, x.split(","))) if "," in x else x for x in line.split()]
    if "on" in tmp_lista:
        oper = "on"
    elif "off" in tmp_lista:
        oper = "off"
    else:
        oper = "toggle"
    tuples = []
    for item in tmp_lista:
        if type(item) == tuple:
            tuples.append(item)
    range_1 = range(tuples[0][0], tuples[1][0] + 1)
    range_2 = range(tuples[0][1], tuples[1][1] + 1)
    lightshow(oper, range_1, range_2)

lights_on = [light for light in lights.values() if light == True]
print(len(lights_on))
