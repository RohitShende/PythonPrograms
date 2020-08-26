import sys
print(sys.version)
with open('special_chars.txt', 'w') as f:
    l = []
    for i in range(1, 2000):
        print(chr(i), end=' ')
        l.append(chr(i))
        # f.write(chr(i))
    print('Written successfully')