"""
Binary Tree
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"<Node {self.data}>"

    def __repr__(self):
        return f"<Node {self.data}>"


def traverse_tree(root):
    l = [root]
    while len(l) > 0:
        node = l.pop(0)
        print(node)
        if node.left:
            l.append(node.left)
        if node.right:
            l.append(node.right)


def create_tree(arr):
    # L M R
    root = Node(arr[0])
    l = [root]
    N = len(arr)
    x = 1
    while x < N:
        node = l.pop()

        if x < N:
            node.left = Node(arr[x])
            l.append(node.left)
        x += 1
        if x < N:
            node.right = Node(arr[x])
            l.append(node.right)
        x += 1

    return root


"""
fill_tree
7

"""

"""
       1
    2    3
   4 5  6  7
   
   
"""

if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5])
    traverse_tree(root)
