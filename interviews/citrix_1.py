"""
str= "Rohit Shende"
T1='R', T2='o', T3='h', T1='i', T2=t, T3=' '......
"""


arr = [int(i) for i in input().split(',')]
# selection sort
N = len(arr)

for i in range(N):
    swap_pos = i
    min_val = arr[i]
    for j in range(i+1, N):
        if arr[j] < min_val:
            swap_pos = j
            min_val = arr[j]
    arr[i], arr[swap_pos] = arr[swap_pos], arr[i]
    print(f"Iteration - {i} the array - {arr}")

print("Sorted Array - ", arr)
