"""
1,2,3,4,5,6,7

(1,2),(3,4)...(7)
(3,2),(1,4)...

(1,3), (2,4,6)

13246

134567243
1 222222 3 444 = 4
1 2 3 2222444 = 4

even counts = 6
odd counts = 2

o e o e

134567243

5 odds
4 even

o e o e o e o e o = 9

2222
no odd then ans is 1

111
no even then evalaute again


13245799
6 odds
2 evens.      2 odds makes even, 1 odd and 1 even can make an odd, 3 odds can make an odd
odds = even + 1  = 5

2 evens, 3 odds

3 odds

1 od 2 evens

o e o e o oo o = 7

if odd is less then bottle neck is odd
if even is less then even is bottleneck and odd = even + 1 , consider 2 odds as 1 even
"""


def no_of_arrangements(s):
    odd_count = 0
    even_count = 0
    for i in s:
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if odd_count == 0 and even_count == 0:
        return 0

    if odd_count == 0:
        return 1

    if even_count == 0:
        # 111 = even = 1
        # odd
        # 1
        # 11111
        #
        # 1
        # 1111
        #
        # 3 -> 2
        # 4 -> 3
        # 5 -> 2
        pass

    if even_count > odd_count:
        return (odd_count * 2) - 1
    else:
        no_number_of_remaining_odds = odd_count - (even_count + 1)
        return (even_count * 2) + 1 + no_of_arrangements("1" * no_number_of_remaining_odds)


assert no_of_arrangements("2222") == 1
# assert no_of_arrangements("13245799") == 7
# assert no_of_arrangements("111") == 2
# assert no_of_arrangements("123456") == 6







