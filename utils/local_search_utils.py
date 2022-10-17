from math import inf
from time import process_time

def is_swapped(node : int, swapped_list : list):
    return node in swapped_list

def possible_swap(graph : list, node1 : int, node2 : int, path : list):
    try:
        return graph[path[node1]][path[node2]] > 0 and graph[path[node2]][path[node1 + 1]] > 0 and graph[path[node2 - 1]][path[node2 + 1]] > 0
    except:
        return False

def path_len(path : list, graph : list):
    current = 0
    traveled = []
    distance = 0
    pos = 0

    while(len(traveled) != len(path) -1):
        distance_aux = graph[current][path[pos]]
        if path[pos] == 0:
            return inf
            
        elif distance_aux != 0:
            distance += graph[current][path[pos]]
            current = path[pos]
            pos += 1
            traveled.append(current)
        elif distance_aux == 0:
            return inf

    return distance

def swap_compensates(graph : list, path : list, node1 : int, node2 : int):
        new_path = path.copy()
        new_path.pop(node2)
        new_path.insert(node1 + 1, path[node2])
        
        if path_len(new_path, graph) < path_len(path, graph):
            return new_path, True
        else:
            return path, False

def make_swap(graph : list, path : list, node1, node2):
    # print(path)
    new_path = path.copy()
    new_path.pop(node2)
    new_path.insert(node1 + 1, path[node2])
        
    if path_len(new_path, graph) < path_len(path, graph):
        return new_path, True
    else:
        return path, False

def local_search(graph : list, path : list):
    swapped = []
    new_path = []
    start = process_time()
    for node in range(len(path)):
        if not is_swapped(node, swapped):
            for node2 in range(len(path)):
                if not is_swapped(node2, swapped):
                    if possible_swap(graph, node, node2, path):
                        if len(new_path) == 0:
                            swap = make_swap(graph, list(path), node, node2)
                            if swap[1]:
                                new_path = swap[0]
                                swapped.append(node)
                                swapped.append(node2)
                        else:
                            swap = make_swap(graph, new_path, node, node2)
                            if swap[1]:
                                new_path = swap[0]
                                swapped.append(node)
                                swapped.append(node2)
    end = process_time()

    return new_path, path_len(new_path, graph), end - start            
