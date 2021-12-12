data = open("input.txt").read().split("\n")

flight_dct = {}
airports = set()

for row in data:
    loc, distance = row.split(" = ")
    distance = int(distance)
    curr, dest = loc.split(" to ")
    airports.add(curr)
    airports.add(dest)
    if curr not in flight_dct:
        tmp_dct = {dest: distance}
        flight_dct[curr] = tmp_dct
    else:
        flight_dct[curr][dest] = distance
    if dest not in flight_dct:
        tmp_dct = {curr: distance}
        flight_dct[dest] = tmp_dct
    else:
        flight_dct[dest][curr] = distance

print(flight_dct)

distances = []

def find_path(start, visited_airports):
    pot_distance = 0
    for i in range(1, len(flight_dct[start].values())):
        distance = sorted(flight_dct[start].values())[-i]
        port = list(flight_dct[start].keys())[list(flight_dct[start].values()).index(distance)]
        if port not in visited_airports:
            pot_distances2 = find_path(port, visited_airports + [port]) + distance
            if pot_distance < pot_distances2:
                pot_distance = pot_distances2
    return pot_distance
    #print(port)

for dests in airports:
    distances.append(find_path(dests,  [dests]))

print(distances)
#764 too low
#777 too low