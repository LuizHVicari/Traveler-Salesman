from utils import file_reader, greedy_traveler_salesman, local_search, write_markdown
from cmath import inf


if __name__ == '__main__':
    start = process_time()
    files = ('TSPLIB/br17.atsp', 'TSPLIB/ft53.atsp', 'TSPLIB/ft70.atsp', 'TSPLIB/ftv33.atsp', 'TSPLIB/ftv35.atsp', 'TSPLIB/ftv38.atsp', 'TSPLIB/ftv44.atsp', 'TSPLIB/ftv47.atsp', 'TSPLIB/ftv55.atsp', 'TSPLIB/ftv64.atsp', 'TSPLIB/ftv70.atsp', 'TSPLIB/ftv170.atsp', 'TSPLIB/kro124p.atsp', 'TSPLIB/p43.atsp', 'TSPLIB/rbg323.atsp', 'TSPLIB/rbg358.atsp', 'TSPLIB/rbg403.atsp', 'TSPLIB/rbg443.atsp', 'TSPLIB/ry48p.atsp')
    best_solutions = ['39', '6905', '38673', '1286', '1473', '1530', '1613', '1776', '1608', '1839', '1950', '2755', '36230', '5620', '1326', '1163', '2465', '2720', '14422']
    greedy_solution = list()
    greedy_path = list()
    local_search_solutions = list()
    local_best_solutions = list()
    times = list()
    total_time = 0

    iterations = 3

    for file in files:
        graph = file_reader(file)
        greedy = greedy_traveler_salesman(graph[0])
        solution = local_search(graph[0], greedy[1], iterations)
        if min(solution[0]) < inf:
            local_best_solutions.append(min(solution[0]))
            times.append(solution[2] * 1000)
        else:
            local_best_solutions.append('Não se aplica')
            times.append('Não se aplica')
       
    graph_names = list()
    for file in files:
        graph_names.append(file.replace('TSPLIB/', '').replace('.atsp', ''))

    write_markdown(
        graph_name=graph_names, 
        best_solutions=best_solutions, 
        graph_solutions=local_best_solutions, 
        graph_time=times, 
        strategy='Estratégia Gulosa', 
        name='LocalSearchOutput', 
        title='Estudo estratégia de busca local para solução do problema do caixeiro viajante'.title())
    