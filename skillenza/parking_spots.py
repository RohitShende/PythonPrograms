for i in range(int(input())):
    d = {}
    for j in range(int(input())):
        x, y = [int(j) for j in input().strip().split(' ')]
        for k in range(x, y+1):
            d[k] = 1
    print(len(d))
