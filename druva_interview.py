# write a code to print left view of a binary tree
#
#          4
#         / \
#        5   7
#       / \
#      6   8
#         /
#        9
#       /
#      10
#       \
#        11
#
# Ans: 4, 5, 6, 9, 10, 11

# 4
# 5, 7
# 6 ,8
# 9
# 10
# 11

class Node:
    left = None
    right = None

    def __init__(self, name):
        self.name = name


def get_left_view(root):
    arr = [root]
    while len(arr) > 0:
        for node in arr[:1]:
            print(node.name)

        arr2 = arr.copy()
        arr = []
        for node in arr2:
            if node.left:
                arr.append(node.left)
            if node.right:
                arr.append(node.right)


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(5)
    root.right = Node(7)
    root.left.left = Node(6)
    root.left.right = Node(8)
    root.left.left.left = Node(9)
    root.left.left.left.left = Node(10)
    root.left.left.left.left.right = Node(11)
    get_left_view(root)
