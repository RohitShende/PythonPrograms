"""
1. Find the inorder successor in Binary Search Tree

input :

	    5

	  3    7

	2  4  6  8


 n=3
 output : 4

n= 6
Output: 7

N = 8
Output = -1

n = 4
output = 5

n = 5
output = 6

n = 1
output = -1

Node - left
Node
Node - right


"""


def inorder_traversal(node, l):
    if node.left:
        inorder_traversal(node.left, l)
    # print(node.name)
    l.append(node.name)
    if node.right:
        inorder_traversal(node.right, l)


def inorder_succesor(root, node):
    l = []
    inorder_traversal(root, l)
    for i, name in enumerate(l):
        if name == node:
            if (i+1) == len(l):
                return -1
            else:
                return l[i+1]
    return -1


class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)
    assert inorder_succesor(root, 3) == 4
    assert inorder_succesor(root, 6) == 7
    assert inorder_succesor(root, 8) == -1
    assert inorder_succesor(root, 4) == 5
    assert inorder_succesor(root, 5) == 6
    assert inorder_succesor(root, 1) == -1

