"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Merging intervals if overlap
Inputs are sorted by start

"""

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
res = []

for i in intervals:
    if not res:
        res.append(i)
    else:
        if res[-1][1] > i[0]:
            # overlap
            res[-1][1] = max(res[-1][1], i[1])
        else:
            res.append(i)
print(res)
