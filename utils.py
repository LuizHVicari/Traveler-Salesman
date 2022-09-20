from cmath import inf
from queue import PriorityQueue
from time import process_time
from random import shuffle
import mdutils


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


def greedy_traveler_salesman(graph):
    '''
    receives a graph and returns the distance found for the traveler salesman, the path and the execution time
    '''
    current = first = 0
    traveled = [first]
    distance_traveled = 0

    start = process_time()

    while(len(traveled) != len(graph)):
        # resets the auxiliar variables for the next iteration
        minimum_distance = False
        minimum_distance_index = False

        for distance_index in range(len(graph)):

            # if the index is still available for travelling
            if not(distance_index in traveled):

                # sets the minimum distance as the first available sitance in the current position
                if not(minimum_distance) and graph[current][distance_index] != 0 and distance_index != current:
                    minimum_distance = graph[current][distance_index]
                    minimum_distance_index = distance_index

                # if a smaller distance is found, sets it as the new minimum distance
                elif minimum_distance > graph[current][distance_index] and graph[current][distance_index] != 0:
                    minimum_distance = graph[current][distance_index]
                    minimum_distance_index = distance_index

        # travels to the closest point and removes it from the available points for traveling
        current = minimum_distance_index
        traveled.append(current)
        distance_traveled += minimum_distance

    # if it is possible to travel from the last element to the first one  
    if graph[current][first] != 0:

        distance_traveled += graph[minimum_distance_index][first]
    
    else:
        return [False, False, False]

    end = process_time()
    return distance_traveled, traveled, end - start


def write_markdown(graph_name : list, best_solutions : list, graph_solutions : list, graph_time : list, strategy : str, name : str = 'Output', title : str = 'Title', author : str = 'Luiz Vicari',):

    file = mdutils.MdUtils(file_name=name, title=title, author=author)
    table_content = ['Grafo', 'Melhor solução conhecida', 'Solução encontrada', 'Tempo de Execução (s)']

    for g_name, g_time, g_best_solution, g_solution in zip(graph_name, graph_time, best_solutions, graph_solutions):
        table_content.append(g_name)
        table_content.append(g_best_solution)
        table_content.append(g_solution)
        table_content.append(g_time)

    file.new_table(4, len(graph_name) + 1, text = table_content, text_align='center')

    file.create_md_file()


def local_search(graph : list(), path : list(), iterations):

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



if __name__ == '__main__':
    graph = file_reader('TSPLIB/rbg403.atsp')
    greedy = greedy_traveler_salesman(graph[0])
    solution = local_search(graph[0], greedy[1])
    print(solution)
    print(min(solution[0]))