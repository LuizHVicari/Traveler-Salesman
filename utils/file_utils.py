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


def write_markdown(graph_name : list, best_solutions : list, graph_solutions : list, graph_time : list, strategy : str, name : str = 'Output', title : str = 'Title', author : str = 'Luiz Vicari',):

    file = mdutils.MdUtils(file_name=name, title=title, author=author)
    table_content = ['Grafo', 'Melhor solução conhecida', 'Solução encontrada', 'Tempo de Execução']

    for g_name, g_time, g_best_solution, g_solution in zip(graph_name, graph_time, best_solutions, graph_solutions):
        table_content.append(g_name)
        table_content.append(g_best_solution)
        table_content.append(g_solution)
        table_content.append(g_time)

    file.new_table(4, len(graph_name) + 1, text = table_content, text_align='center')
    file.create_md_file()