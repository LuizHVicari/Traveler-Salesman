from cmath import inf
from queue import PriorityQueue
from random import shuffle
from .greedy_utils import greedy_traveler_salesman
from .random_shuffle_utils import random_shuffle_search
from .file_utils import file_reader


def djikstra(graph : tuple, destiny : int=0, origin : int=0):
    queue_ = PriorityQueue()
    final_distance = [inf for i in range(len(graph))]
    final_distance[origin] = 0
    visited = list()
    
    queue_.put((0, origin))

    while not queue_.empty():
        (distance, current) = queue_.get()
        visited.append(current)

        for index in range(len(graph)):
            if graph[current][index] > 0:
                distance = graph[current][index]

                if index not in visited:
                    old = final_distance[index]
                    new = final_distance[current] + distance

                    if new < old:
                        queue_.put((new, index))
                        final_distance[index] = new

    return final_distance 


def random_array(graph):
    array = [i for i in range(0, len(graph) - 1)]
    shuffle(array)
    return array


if __name__ == '__main__':
    graph = file_reader('TSPLIB/rbg403.atsp')
    greedy = greedy_traveler_salesman(graph[0])
    solution = random_shuffle_search(graph[0], greedy[1])
    print(solution)
    print(min(solution[0]))