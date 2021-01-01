
test_range = range(10,20)

def test(ranges):
    for x in ranges:
        print(x)

test(test_range)

test_dct = {}

test_lista = [0,0]

test_dct[tuple(test_lista)] = None
print(test_dct)