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