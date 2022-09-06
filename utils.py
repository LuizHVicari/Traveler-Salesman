from cmath import inf
from queue import PriorityQueue
from typing import final


def file_reader(path : str):
    '''
    receives a file path and returns a graph and it's size
    '''
    graph = list()
    with open(path) as file:
        file = file.read()
        file = file.split()

        dimension = int(file[file.index('DIMENSION:')+1])
        i = file.index('EDGE_WEIGHT_SECTION') + 1

        line = list()
        while file[i] != 'EOF':
            line.append(int(file[i]))
            if len(line) == dimension:
                graph.append(tuple(line))
                line = []
            i+=1

        graph = tuple(graph)
        
    return graph, dimension

def write_file(text: str, path : str='default_output_file.txt', mode : str='w'):
    with open(path, mode) as output_file:
        output_file.write(text)

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

if __name__ == '__main__':

    graph = ((999, 3, 5, 6),
            (4, 999, 7, 9),
            (5, 7, 999, 8),
            (4, 1, 8, 999))
    print(djikstra(graph, 4, 0))