a = input("Enter array as comma seperated string :").strip().split(',')
a = [int(i) for i in a]

n = len(a)

a_min = [0]*n
a_max = [0]*n

l_max = a[0]
l_min = a[-1]


for i in range(0, n):
    l_max = max(l_max, a[i])
    a_max[i] = l_max

for i in range(n-1, -1, -1):
    l_min = min(l_min, a[i])
    a_min[i] = l_min

for i in range(1, n-1):
    if a_max[i] <= a[i] <= a_min[i]:
        print("Pivot element : {}".format(a[i]))
        break
else:
    print("No pivot element")

