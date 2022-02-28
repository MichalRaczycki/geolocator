import math

from numpy import short

def compass_directions(origin, destination):
    compass_brackets = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    destination_x, destination_y = destination
    origin_x,origin_y = origin
    delta_x = destination_x-origin_x
    delta_y = destination_y-origin_y
    degrees_temp = math.atan2(delta_x, delta_y)/math.pi*180
    if degrees_temp < 0:
        degrees_final = 360 + degrees_temp
    else:
        degrees_final = degrees_temp
    compass_lookup = round(degrees_final / 45)
    return compass_brackets[compass_lookup], degrees_final

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    max_value = float('inf')
    for node in unvisited_nodes:
        shortest_path[node] = max_value
        shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        #Retrieve current node's neighbours and distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
        unvisited_nodes.remove(current_min_node)
    return previous_nodes,shortest_path

def print_result(previous_nodes,shortest_path,start_node,target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
        
    path.append(start_node)
    
    print(f"Found the following best path with a value of {shortest_path[target_node]}")
    path_description = ''
    for index in reversed(range(len(path))):
        path_description+= f'{path[index]}->'
    path_description+= 'goal achieved'
    print(path_description)
    return None
    
    
def find_key_by_value(distances, value):
    for x in distances:
        if distances[x] == value:
            return x
        
def delete_point_from_list(to_visit, value):
    for (index, item) in enumerate(to_visit):
        if item == value:
            to_visit.pop(index)
    return to_visit