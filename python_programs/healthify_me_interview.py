'''
a = 'hello world'
a.split(' ')
['hello', 'world']

a = 'this is a test'
d = 'is'
assert split(a, d) == a.split(d)


def split(input_str, delimiter_str):
   return []
'''


def split(input_str, delimeter=' '):
    output = []
    n = len(input_str)
    len_d = len(delimeter)
    pos = 0
    end_pos = 0
    while pos < n:
        if input_str[pos:pos + len_d] == delimeter:
            output.append(input_str[end_pos:pos])
            end_pos = pos + len_d
            pos = end_pos
        else:
            pos += 1

    if end_pos <= pos:
        output.append(input_str[end_pos:])

    return output


tests = [
    ('hi i am rohit', 'i'),
    ('this is a test', 'is'),
    ('rohit', 'rohit'),
    ('this is a test', 'test'),
    ('this is a test', 'rohit'),
    ('this is a test', 'this')
]
for test in tests:
    output = split(test[0], test[1])
    expected_output = test[0].split(test[1])
    print(f'Comparing {output} == {expected_output}')
    assert output == expected_output, f'for str {test[0]} and delimeter {test[1]} - {expected_output} did not match {output}'
print('All Tests Passed !')

### Rough Work
### i 'a'm a test 'a'nd i am 'a'gain 'a' test
### th'is' 'is' a test
### my name is rohit and 'name' is 'name'
### 01 3  67
