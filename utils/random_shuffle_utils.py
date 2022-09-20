from time import process_time
from random import shuffle
from cmath import inf

def random_shuffle_search(graph : list(), path : list(), iterations):

    distances = []
    paths = []

    if path == False:
        new_path = [i for i in range(0, len(graph) - 1)]
    else:
        new_path = path
    new_path.pop(0)

    start = process_time()

    for i in range(iterations):
        shuffle(new_path)
        new_path.append(0)
        distance = path_tester(graph, new_path)
        new_path.pop(len(new_path) - 1)

        if distance > 0 and distance < inf:
            distances.append(distance)
            paths.append(new_path)
    if distances == []:
        distances = [inf]
        paths = [inf]
    return distances, paths, process_time() - start


def path_tester(graph : list(), path : list()):
    current = 0
    traveled = []
    distance = 0
    pos = 0

    while(len(traveled) != len(path) - 1):
        distance_aux = graph[current][path[pos]]
        tester = path[pos]
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