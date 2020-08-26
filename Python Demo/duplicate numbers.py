a = [1, 1, 2, 3, 4, 1, 5, 4, 2, 1, 3]

d = {}

for element in a:
    if d.get(element):
        d[element] = d[element] + 1
    else:
        d[element] = 1

for key, value in d.items():
    if value > 1:
        print(key)