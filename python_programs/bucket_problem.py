x = int(input())
y = int(input())
x_80 = 0.80 * x
filled = 0
mugs_count = 0
while True:
    x = int(input())
    filled += x
    mugs_count += 1
    if filled >= x_80:
        print('BUCKET FULL!')
        print('NUMBER OF MUGS:', mugs_count)
        break
