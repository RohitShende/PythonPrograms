import sys
from collections import OrderedDict

d = OrderedDict()
n = 10**4
for i in range(n):
    d[sys.getsizeof(i)] = i

print(*[f"{key} bytes till {val}" for key, val in d.items()], sep='\n')
