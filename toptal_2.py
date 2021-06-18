# A precedence rule is given as "P>E", which means that letter "P" is
# followed directly by the letter "E". Write a function, given an array of precedence rules,
# that finds the word represented by the given rules.
#
# Note: Each represented word contains a set of unique characters,
# i.e. the word does not contain duplicate letters.
#
# Examples:
# findWord(["P>E","E>R","R>U"]) // PERU
# findWord(["I>N","A>I","P>A","S>P"]) // SPAIN

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'{self.prev}-{self.name}-{self.next}'


def findWord(arr):
    # print(arr)
    dict = {}
    for i in arr:
        k, v = i.split('>')
        dict[k] = Node(k)
        dict[v] = Node(v)
    print(dict)

    for i in arr:
        k, v = i.split('>')
        dict[v].next = dict[k]
        dict[k].prev = dict[v]

    print(dict)

    # for i in dict:
    #     if i.prev is None:
    #         # found root node
    #         while i.next:
    #             print(i.name, end='')
    #             i = i.next
    #         break



print(findWord(["P>E", "E>R", "R>U"]))
print(findWord(["I>N","A>I","P>A","S>P"]))