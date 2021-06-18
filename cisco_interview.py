"""
Detect if there is a deadlock if it is there print "Deadlock"
else print the order in which the tasks should be executed such that all the dependencies are satisfied

i/p is list of dependencies (x,y) such that y is dependent on x

interviewer : zahaib mateen - zmateen@cisco.com

"""


def get_order(dependencies):
    print('*' * 20 + f' Solving for {dependencies}')
    count_of_dependencies = {}
    resolves_dependencies_of = {}

    all_nodes = set()
    order = []

    for k, v in dependencies:
        all_nodes.add(k)
        all_nodes.add(v)
        if v in count_of_dependencies:
            count_of_dependencies[v] += 1
        else:
            count_of_dependencies[v] = 1

        if k in resolves_dependencies_of:
            resolves_dependencies_of[k].append(v)
        else:
            resolves_dependencies_of[k] = [v]

    # print(count_of_dependencies)
    # print(all_nodes)
    # print(resolves_dependencies_of)

    # we need to find the nodes which have zero outgoing arrows
    # means these nodes are independent, hence they should not be present in the second place in the
    # dependencies tuple

    while len(all_nodes) > 0:
        independent_nodes = all_nodes - set(count_of_dependencies.keys())
        # print('Independent nodes:', independent_nodes)
        if len(independent_nodes) == 0 and len(all_nodes) > 0:
            return 'Cycle is present'
        for node in independent_nodes:
            order.append(node)
            if resolves_dependencies_of.get(node):
                dependent_nodes = resolves_dependencies_of[node]
                for n in dependent_nodes:
                    if count_of_dependencies[n] > 1:
                        count_of_dependencies[n] -= 1
                    else:
                        del count_of_dependencies[n]
                del resolves_dependencies_of[node]
            all_nodes.remove(node)
        # print('All nodes:', all_nodes)
        # print('Count of dependencies:', count_of_dependencies)
        # print('Resolves dependecies of:', resolves_dependencies_of)
    return order


if __name__ == '__main__':
    testcases = [
        [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'e'), ('c', 'f'), ('e', 'f'), ('g', 'h'), ('g', 'i')],
        [('a', 'b'), ('b', 'a')],
        [(0, 1), (1, 2), (2, 3), (4, 3), (0, 4), (4, 5)]
    ]
    for testcase in testcases:
        print(get_order(testcase))
