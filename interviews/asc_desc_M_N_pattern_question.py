"""
Question : A pattern is given to you which consists of M and N character
M means descending
N means ascending
M -> 2,1
N -> 1,2

Now if a pattern is given to you, you have to calculate the
lowest value number sequence that satisfies this pattern.

We can have values from 1 to 9 in the output, non repeating digits
input pattern length cannot be greater than 8

example:
ip : M
op : 21
The candidates that are valid sequence of M can be 21, 32, 43, 82, 91, etc.
but out of them the lowest value is 21

ip: N
op: 12
The candidates that are valid sequence of N can be 12, 14, 23, 89 etc.
but out of them the lowest value is 12

ip: MMN
op: 3214
The values that can satisfy this pattern are 4312, 3214, 9745, 7436 etc.
But the lowest value is 3214
"""


def count_consecutive_m(pattern):
    c = 0
    for i in pattern:
        if i=='M':
            c +=1
        else:
            break
    return c


def find_sequence(pattern: str):
    if pattern is None or len(pattern.strip()) == 0:
        return -1
    if 'M' not in pattern and 'N' not in pattern:
        return -1
    output_arr = []
    current_highest = 0
    for i, c in enumerate(pattern):
        if c == 'M':
            cM = count_consecutive_m(pattern[i+1:])
            if output_arr:
                if pattern[i-1] == 'M':
                    output_arr.append(output_arr[-1]-1)
                else:
                    output_arr[-1] += cM+1
                    current_highest = output_arr[-1]
                    output_arr.append(current_highest-1)
            else:
                output_arr.extend([2+cM, 1+cM])
                current_highest = 2+cM
        elif c == 'N':
            if output_arr:
                current_highest += 1
                output_arr.append(current_highest)
            else:
                output_arr.extend([1, 2])
                current_highest = 2
        else:
            return -1

    output = int(''.join([str(i) for i in output_arr]))
    print(output)
    return output


assert find_sequence(None) == -1
assert find_sequence('') == -1
assert find_sequence('  ') == -1
assert find_sequence('_abdl') == -1
assert find_sequence('M') == 21
assert find_sequence('N') == 12
assert find_sequence('MM') == 321
assert find_sequence('NN') == 123
assert find_sequence('MN') == 213
assert find_sequence('NM') == 132
assert find_sequence('MNM') == 2143
assert find_sequence('MMNN') == 32145
assert find_sequence('NNMMM') == 126543
assert find_sequence('MNMN') == 21435
assert find_sequence('MMMMM') == 654321
assert find_sequence('NNNNN') == 123456
assert find_sequence('MNMMN') == 215436
assert find_sequence('MMMMNMN') == 54321768
assert find_sequence('NNMMNMNN') == 125437689
assert find_sequence('NMMNNM') == 1432576
