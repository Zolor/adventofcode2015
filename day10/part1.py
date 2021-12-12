data = open("input.txt").read()

new = ""
count = 1

for i in range(40):
    for n, l in enumerate(data):
        if n + 1 == len(data):
            if count == 1:
                new += "1"
                new += l
            else:            
                new += str(count)
                new += l
        elif l == data[n + 1]:
            count += 1
        elif l != data[n + 1] and count > 1:
            new += str(count)
            new += l
            count = 1
        elif l != data[n + 1] and count == 1:
            new += "1"
            new += l
    data = new
    new = ""
print(len(data))
