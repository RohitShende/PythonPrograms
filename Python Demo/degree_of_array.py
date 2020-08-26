a = [1, 2, 3, 2, 1, 3, 3, 3, 4]

d = {}
for i in a:
    d[i] = d[i] + 1 if d.get(i) else 1
print(max(d.values()))
