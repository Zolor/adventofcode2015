from collections import defaultdict

direction_data = defaultdict()

data = 5

for x in range(10):
    for y in range(10):
        key = (x, y)
        if direction_data.get(key) == None:
            direction_data[key] = 1
        else:            
            direction_data[key] = (direction_data.get(key) + 1)

print(direction_data)