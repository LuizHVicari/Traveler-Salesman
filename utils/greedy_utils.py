from time import process_time

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