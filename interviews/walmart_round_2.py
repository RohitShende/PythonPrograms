# Level order traversal of a tree
#
# root
# 	- left
# 	- right
# 	- data


def level_order(root):
    result = []
    if root is None:
        return result
    level = [root]
    while len(level) > 0:
        new_level = []
        result.append(level)
        for node in level:
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
        level = new_level

    return result


# Singly Linked list having cycle
#
#
# root
# 	- data
# 	- next
#
# None
# 1 -> None
# 1 -> 2 -> 3 -> None
# 1 -> 2 -> 3 -> 4 -> 2

def is_cycle_present(root):
    fast_runner = root
    slow_runner = root
    if root is None:
        return False

    while True:
        slow_runner = slow_runner.next
        if slow_runner is not None:
            fast_runner = slow_runner.next

        if slow_runner is None or fast_runner is None:
            return False

        if fast_runner == slow_runner and slow_runner is not None:
            return True
