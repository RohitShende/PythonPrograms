"""
Author: Rohit Shende
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return '<NODE> {}'.format(self.val)


root = Node('root', Node('left', Node('left.left'), Node('left.right')),
            Node('right', Node('right.left', Node('right.left.left'), Node('right.left.right')), Node('right.right')))

import pickle


def DFS(node, lst=[]):
    if node.left:
        lst = DFS(node.left, lst)
    if node.right:
        lst = DFS(node.right, lst)
    lst.append(node)
    return lst


def BFS(node, lst=[]):
    temp_lst = [node]
    while len(temp_lst) > 0:
        x = temp_lst.pop(0)
        lst.append(x)
        if x.left:
            temp_lst.append(x.left)
        if x.right:
            temp_lst.append(x.right)
    return lst


def serialize(node):
    # Uses DFS to serialize
    if node.left:
        node.left = serialize(node.left)
    if node.right:
        node.right = serialize(node.right)
    return pickle.dumps(node)


def deserialize(node):
    # uses BFS to deserialize
    if node:
        node = pickle.loads(node)
        temp_lst = [node]
        while len(temp_lst) > 0:
            x = temp_lst.pop(0)
            if x.left:
                x.left = pickle.loads(x.left)
                temp_lst.append(x.left)
            if x.right:
                x.right = pickle.loads(x.right)
                temp_lst.append(x.right)
    return node


print('DFS :', DFS(root))
print('BFS :', BFS(root))

serialized_root = serialize(root)
print('Serialized Root :', serialized_root)

deserialized_root = deserialize(serialized_root)
print('DeSerialized Root :', deserialized_root)


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
print('Successfully tested !!!')