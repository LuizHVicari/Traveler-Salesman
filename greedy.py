from time import process_time
from utils import file_reader


def greedy_traveler_salesman(graph, first=0):
    '''
    receives a graph and returns the distance found for the traveler salesman, the path and the execution time
    '''
    traveled = [first]
    distance_traveled = 0
    current = first

    start = process_time()

    while(len(traveled) != len(graph)):
        # resets the auxiliar variables for the next iteration
        minimum_distance = False
        minimum_distance_index = False

        for distance_index in range(len(graph)):

            # if the index is still available for travelling
            if not(distance_index in traveled):

                # sets the minimum distance as the first available sitance in the current position
                if not(minimum_distance) and graph[current][distance_index] != 0:
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

        end = process_time()
    
    traveled.append(first)
    traveled.remove(first)

    distance_traveled += graph[minimum_distance_index][first]

    return distance_traveled, traveled, end - start

start_time = process_time()

files = ('TSPLIB/br17.atsp', 'TSPLIB/ft53.atsp', 'TSPLIB/ft70.atsp', 'TSPLIB/ftv33.atsp', 'TSPLIB/ftv35.atsp', 'TSPLIB/ftv38.atsp', 'TSPLIB/ftv44.atsp', 'TSPLIB/ftv47.atsp', 'TSPLIB/ftv55.atsp', 'TSPLIB/ftv64.atsp', 'TSPLIB/ftv70.atsp', 'TSPLIB/ftv170.atsp', 'TSPLIB/kro124p.atsp', 'TSPLIB/p43.atsp', 'TSPLIB/rbg323.atsp', 'TSPLIB/rbg358.atsp', 'TSPLIB/rbg403.atsp', 'TSPLIB/rbg443.atsp', 'TSPLIB/ry48p.atsp')
output = ''

for file in files:
    data = greedy_traveler_salesman(file_reader(file)[0])
    output += file.replace('TSPLIB/', '').replace('.atsp', '') + ':'
    for i in range(8 - len(file.replace('TSPLIB/', '').replace('.atsp', ''))):
        output += ' '
    output +=  f' distance: {data[0]}, execution time: {data[2]:.60f} s\n'
with open('greedy_output.txt', 'w') as output_file:
    output_file.write('Greedy Output:\n' + output + f'total time:{ (process_time() - start_time)} s')