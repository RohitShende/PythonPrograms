from numpy import zeros
n = int(input('enter n?'))

if n % 2 != 0:
    n = n+1

if n < 6:
    n = 6

c = (n+1) // 2
m = zeros((n, n+1), str)
eq = n-c-1
s = n%3 + 1
# print(s)
j = 0

for i in range(eq-s, eq):
    m[i][0] = '*'
    m[i][n] = '*'

for i in range(eq, n):
    m[i][j] = '*'
    m[i][n-j] = '*'
    j += 1

j = c
for i in range(eq-s, -1, -1):
    m[i][j] = '*'
    m[i][n - j] = '*'
    m[i][c-j] = '*'
    m[i][n-(c-j)] = '*'
    j -= 1
    if i == 0:
        for k in range(s-1):
            m[i][j-k] = '*'
            m[i][n - j + k] = '*'

# print(m)
# print(m.shape)
for i in range(m.shape[0]):
    print()
    for j in range(m.shape[1]):
        if m[i][j]:
            print('*', end=' ')
        else:
            print(' ', end=' ')
