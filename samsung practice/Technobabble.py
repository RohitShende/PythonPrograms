for _t in range(int(input())):
    n = int(input())
    copies = 0
    first = {}
    second = {}
    for _n in range(n):
        x = input()
        f, s = x.split(' ')
        first[f] = 1
        second[s] = 1

    print('Case #{0}: {1}'.format(_t + 1, n - max(len(first), len(second))))
