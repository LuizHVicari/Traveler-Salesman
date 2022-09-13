from time import process_time
from utils import file_reader, write_file, greedy_traveler_salesman, write_markdown


if __name__ == '__main__':
    start_time = process_time()

    # list with all the atsp files on http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/atsp/
    files = ('TSPLIB/br17.atsp', 'TSPLIB/ft53.atsp', 'TSPLIB/ft70.atsp', 'TSPLIB/ftv33.atsp', 'TSPLIB/ftv35.atsp', 'TSPLIB/ftv38.atsp', 'TSPLIB/ftv44.atsp', 'TSPLIB/ftv47.atsp', 'TSPLIB/ftv55.atsp', 'TSPLIB/ftv64.atsp', 'TSPLIB/ftv70.atsp', 'TSPLIB/ftv170.atsp', 'TSPLIB/kro124p.atsp', 'TSPLIB/p43.atsp', 'TSPLIB/rbg323.atsp', 'TSPLIB/rbg358.atsp', 'TSPLIB/rbg403.atsp', 'TSPLIB/rbg443.atsp', 'TSPLIB/ry48p.atsp')
    output = ''
    solution = list()
    solution_time = list()

    # runs the greedy method on all the files listed above and appends its returned data on a string
    for file in files:
        data = greedy_traveler_salesman(file_reader(file)[0])
        
        if data != False:
            solution.append(f'{data[0]}')
            solution_time.append(f'{data[2] * 1000}')
        else:
            output += 'Não há solução gulosa para este grafo\n'
            solution.append('Não encontrada')
            solution_time.append('Não se aplica')

    # formats the file name
    graph_names = list()
    for file in files:
        graph_names.append(file.replace('TSPLIB/', '').replace('.atsp', ''))
    best_solutions = ['39', '6905', '38673', '1286', '1473', '1530', '1613', '1776', '1608', '1839', '1950', '2755', '36230', '5620', '1326', '1163', '2465', '2720', '14422']
    write_markdown(graph_name=graph_names, best_solutions=best_solutions, graph_solutions=solution, graph_time=solution_time, strategy='Estratégia Gulosa', name='GreedyOutput', title='Estudo estratégia gulosa para solução do problema do caixeiro viajante'.title())