# import configparser
# import requests
# import traceback
#
#
# def get_config():
#     pass
#
#
# config = get_config()
#
#
# class Group1:
#     base_url = config.base_url
#
#     def get(self, end_point):
#         url = self.base_url + end_point.lstrip('/')
#         try:
#             response = requests.get(url)
#             if response.status_code == 200:
#                 return response.json()
#             return None
#         except:
#             # logging
#             traceback.print_exc()
#             return None
#
#     def put(self, end_point, body):
#         url = self.base_url + end_point.lstrip('/')
#         try:
#             response = requests.put(url, json=body)
#             if response.status_code in [200, 201]:
#                 return response.json()
#             return None
#         except:
#             # logging
#             traceback.print_exc()
#             return None
#
# 500, "html"

"""
abcabcbb, pwwkew
s
 e
max_len =
"""

"""
a b c a b c b b
s               
      e  
max_len = 3
d = {c, b}
len(d) < (e-s+1)

result : {3: abc}
s == e == len(S)

output: abc

"""

"""
p w w k e w
      s  
          e

curr_len = e - s +1
max_len = 3
d = {w, k, e}
len(d) < (e-s+1)

if curr_len == max_len and e == (N-1):
    break

result : {2: pw, 3: wke, }
s == e == len(S)
"""

S = "abcabcbb"
N = len(S)
max_len = 0
d = {}
result = {}
s = 0
e = 0

print(S)
def add_to_dict(x):
    if d.get(x):
        d[x] += 1
    else:
        d[x] = 1


def remove_from_dict(x):
    if d[x] > 1:
        d[x] -= 1
    else:
        del d[x]


while s < (N-1):
    add_to_dict(S[e])
    if len(d) < (e - s + 1):
        # increment s
        remove_from_dict(S[s])
        s += 1
    else:
        curr_len = e - s + 1
        max_len = max(max_len, curr_len)
        # increment e
        if result.get(curr_len) is None:
            result[curr_len] = S[s:e+1]

        if e < N-1:
            e += 1

    print(s, e, S[s: e], curr_len, max_len)
    print(d)
    print()

print(result)
