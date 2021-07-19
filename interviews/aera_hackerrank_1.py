
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'get_storage' function below.
#
# The function is expected to return an INTEGER.
#


class Node:
    def __init__(self, name, weight):
        self.name = name
        self.group = None
        self.group_weight = weight
        self.weight = weight

    def __repr__(self):
        return f"<Node name: {self.name} | group: {self.group} | group_weight: {self.group_weight}>"


class Group:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"<Group name: {self.name} | weight: {self.weight}>"


def get_storage(connection_nodes, connection_edges, connections_from, connections_to, storage, threshold):
    # Write your code here
    ans = []

    nodes = [Node(i, weight) for i, weight in zip(range(connection_nodes), storage)]
    print(nodes)
    groups = {node.name: Group(node.name, node.weight) for node in nodes}
    print(groups)

    for i in range(connection_edges):
        count = 0
        node1 = nodes[connections_from[i]]
        node2 = nodes[connections_to[i]]

        print('*' * 20, "Iteration number", i, node1.group, node2.group, node1.name, node2.name)
        del_keys = []
        if node1.group is None and node2.group is None:
            group_key = ','.join([str(node1.name), str(node2.name)])
            del_keys.append(node1.name)
            del_keys.append(node2.name)

        elif node1.group is None and node2.group is not None:
            # node 2 in group
            group_key = ','.join([str(node1.name), str(node2.group.name)])
            del_keys.append(node1.name)
            del_keys.append(node2.group.name)

        elif node1.group is not None and node2.group is None:
            # node 1 in group
            group_key = ','.join([str(node1.group.name), str(node2.name)])
            del_keys.append(node1.group.name)
            del_keys.append(node2.name)

        else:
            # both are groups
            if node1.group.name != node2.group.name:
                group_key = ','.join([str(node1.group.name), str(node2.group.name)])
                del_keys.append(node1.group.name)
                del_keys.append(node2.group.name)
            else:
                group_key = None

        if group_key:
            new_group_weight = node1.group_weight + node2.group_weight
            new_group = Group(group_key, new_group_weight)
            groups[group_key] = new_group

            for key in group_key.split(','):
                nodes[int(key.strip())].group = new_group
                nodes[int(key.strip())].group_weight = new_group_weight

            for key in del_keys:
                del groups[key]

        print(groups)
        print(nodes)

        for v in groups.values():
            if v.weight <= threshold:
                count += 1
        ans.append(count)
        print("COUNT : ", count)

    return ans


if __name__ == '__main__':
    connection_nodes, connection_edges = [int(i) for i in input().split()]
    connections_from = []
    connections_to = []
    for i in range(connection_edges):
        from_, to_ = [int(i) for i in input().split()]
        connections_from.append(from_)
        connections_to.append(to_)

    connection_nodes = int(input())
    storage = []
    for i in range(connection_nodes):
        storage.append(int(input()))
    threshold = int(input())

    results = get_storage(connection_nodes, connection_edges, connections_from, connections_to, storage, threshold)
    for i in results:
        print(i)


"""
Testcases

5 3
0 1
1 4
0 4
5
1
2
3
4
5
4

Output:
3
2
2


3 2
0 1
1 2
3
1
2
3
4

Output:
2
0
"""