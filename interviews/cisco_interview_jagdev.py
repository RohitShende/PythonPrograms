def is_bracket_matching(S):
    from collections import Counter
    c = Counter(S)
    d = {}
    if c['['] == c[']'] and c['{'] == c['}']:
        return True, 0
    if c['['] > c[']']:
         d['['] = c['['] - c[']']
    if c['['] < c[']']:
        d[']'] = c[']'] - c['[']
    if c['{'] > c['}']:
        d['{'] = c['{'] - c['}']
    if c['{'] < c['}']:
        d['}'] = c['}'] - c['{']

    return False, d


def check_colon_placement(S):
    arr = S.strip().split(":")
    d = {"before": [], "after": []}
    for i, start in enumerate(arr[:-1]):
        end = arr[i+1]
        start = start.strip()
        end = end.strip()
        if start[-1] not in ('"'):
            d['before'].append(start)
        if end[0] not in ('"', '{', '['):
            d['after'].append(end)
    if len(d['before']) + len(d['after']) == 0:
        return True, 0
    return False, d

"jtur@cisco.com"

def is_valid_json(S):
    print(is_bracket_matching(S))
    print(check_colon_placement(S))
    return True


s = """
[[{"data": [{["vmm": {"attrs":} {"id":[ "uni/vmmp", "vend": 'mdb', "name": "{]", "type": "virtual", 
"child"- "[{},[1;2]]"}}}], "total"="1"}]

[]
{}
"""
print(is_valid_json(s))


"""

{
}

[
]

stacks : [{k: v}, {}, "aaa", 1]
s: [[{{


"""
