graph = {
    "a": ["b", "c"],
    "b": ["d", "a"],
    "c": ["g", "a"],
    "g": ["d", "c"],
    "d": ["b", "g"],
}


def minimum_distance(graph, starting_node="a", ending_node="g"):
    distance_to_end = {}
    for node in graph:
        if node == ending_node:
            distance_to_end[node] = 0
        else:
            distance_to_end[node] = None

    print(distance_to_end)

    i = 0
    while distance_to_end[starting_node] is None:
        for node, adjacent_nodes in graph.items():
            if distance_to_end[node] is None:
                adjacent_distance = []
                for n in adjacent_nodes:
                    if distance_to_end[n] is not None:
                        adjacent_distance.append(distance_to_end[n])

                if len(adjacent_distance) > 0:
                    distance_to_end[node] = min(adjacent_distance) + 1

        print(f'Iteration {i}')
        print(distance_to_end)
        i += 1

    return distance_to_end[starting_node]


print(minimum_distance(graph, starting_node='d', ending_node='a'))
