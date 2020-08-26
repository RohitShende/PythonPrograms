str = "indira college ke bacche"

d ={}

for e in str:
    if d.get(e):
        d[e] += 1
    else:
        d[e] = 1

for e in str[::-1]:
    if d.get(e):
        if d[e] == 1:
            print(e)
            break