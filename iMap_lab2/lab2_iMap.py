def min_seen_cost(array, start, seen):
    """
    This function searches for next node of array with minim cost, from the ones unseen

    :param array: an array of all distances
    :param start: the node where the path begins and ends; integer, >0
    :param seen: a list of nodes unseen yet
    :return: cost - the "cost" from the start to index
             index - the node from where we can continue the path
    """
    cost = 100000
    index = -1
    for elem in range(len(seen)):
        if seen[elem] == False:
            if cost > array[start][elem] and array[start][elem] > 0:
                cost = array[start][elem]
                index = elem
    return [index, cost]


def shortest_path(array, start):
    """
    This function returns the shortest path which includes all nodes, fininhing in the node where we began

    :param array: an array of all distances
    :param start: the node where the path begins and ends; integer, >0
    :return: path - the shortest path that we are looking for; list
             cost - the "cost" of this path; integer
    """

    seen = [False] * len(array)
    path = []
    cost = 0
    while seen.count(False) != 1:
        val = min_seen_cost(array, start, seen)
        cost += val[1]
        path.append(start)
        seen[start] = True
        start = val[0]
    path.append(seen.index(False))
    cost += array[path[len(path) - 1]][path[0]]
    path.append(path[0])
    return [path, cost]


def src_to_dest_path(array, source, destination):
    """
    This function returns the shortest path from source to destination

    :param array: an array of all distances
    :param source: the node where the path begins
    :param destination: the node where the path ends
    :return: path - the shortest path that we are looking for; list
             cost - the "cost" of this path; integer
    """
    [path, cost] = shortest_path(array, source)
    while path[-1] != destination:
        length = len(path)
        cost -= array[path[length - 2]][path[length - 1]]
        path.pop()
    return [path, cost]


def run():
    fin = open("fin.txt", "r")
    fout = open("out.txt", "w")
    array = []
    nr_nodes = int(fin.readline().strip())
    for index in range(nr_nodes):
        line = fin.readline().strip().split(",")
        for index2 in range(nr_nodes):
            line[index2] = int(line[index2])
        array.append(line)
    source = int(fin.readline().strip())
    destination = int(fin.readline().strip())

    [path, cost] = shortest_path(array, 0)
    for index in range(1, nr_nodes):
        [path_local, cost_local] = shortest_path(array, index)
        if cost_local < cost:
            path = path_local
            cost = cost_local
    road = ""
    for index in path:
        index += 1
        road += "," + str(index)
    fout.write(road[1:len(road) - 2] + "\n")
    fout.write(str(cost) + "\n")

    [path1, cost1] = src_to_dest_path(array, source - 1, destination - 1)
    [path2, cost2] = src_to_dest_path(array, destination - 1, source - 1)
    if cost1 < cost2:
        path = path1
    else:
        path = path2
        path.reverse()
    cost = min(cost2, cost1)

    fout.write(str(len(path)) + "\n")
    road = ""
    for index in path:
        road += "," + str(index + 1)
    fout.write(road[1:] + "\n")
    fout.write(str(cost) + "\n")

    fin.close()
    fout.close()
