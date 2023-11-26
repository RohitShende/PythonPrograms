"""
Interview 1:

Add 2 big numbers stored as strings

num1 = "123"
num2 = "456"
result = "579"

"""


def add(num1: str, num2: str) -> str:
    result = []
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    while i >= 0 or j >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        addition = n1 + n2 + carry
        carry = addition // 10
        result.append(str(addition % 10))
        i -= 1
        j -= 1
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1])


if __name__ == '__main__':
    # Test add function
    assert add('123', '456') == '579'
    assert add('999', '1') == '1000'
    assert add('999', '999') == '1998'
    assert add('999', '9999') == '10998'
    assert add('999', '99999') == '100998'
    assert add('999', '999999') == '1000998'
    assert add('999', '9999999') == '10000998'
    assert add('999', '99999999') == '100000998'
    assert add('999', '999999999') == '1000000998'
    assert add('999', '9999999999') == '10000000998'
    assert add('999', '111') == '1110'
    assert add('999', '1111') == '2110'
    assert add('999', '') == '999'
    assert add('', '999') == '999'
