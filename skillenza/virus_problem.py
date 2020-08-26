from collections import Counter



if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        c = Counter(s)
        m = max(c.values())
        c = [x for x, y in c.items() if y == m]
        # print(c)
        print(min(c))

