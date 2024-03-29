from geopy import distance
import math 
import json
import utils.helper_functions as support
import pandas as pd
import models.Graph as Graph

"""
This script is an attempt to recreate the multi-point delivery problem:
Shortest Path Algorithm for Real Roads Network using Dijkstra
Samaher Adnan et al 2020 J. Phys.: Conf. Ser. 1530 012040
"""

def main():
    locations = open('data.json')
    data = json.load(locations)
    coordinates ={}
    for i in data['features']:
        coordinates[i['properties']['point-id']] = tuple(i['geometry']['coordinates'])
    coordinates[0] = (12.922963500022886, 52.42706852497485)

    distance_dict={}
    for current_point in range(0,len(coordinates.items())):
        distance_dict[current_point] = {}
        for y in range(0,len(coordinates.items())):
            if y!= current_point:
                distance_dict[current_point][y] = distance.distance(coordinates[current_point],coordinates[y]).km
    distance_df = pd.DataFrame(distance_dict)
    minimum_list =[]
    for x in distance_df:
        minimum_list.append(distance_df[x].min())

    minimums = pd.DataFrame(minimum_list)
    standard_distance = minimums[0].std()+1*minimums.mean()[0]
    distance_df.fillna(float('inf'))
    neighbours = distance_df[distance_df<standard_distance]

    neighbour_dict={}
    for x in neighbours:
        neighbour_dict[x]=[]
        counter = 0
        for y in neighbours[x]:
            counter += 1
            if not math.isnan(y):
                neighbour_dict[x].append((0,y)) if counter==22 else neighbour_dict[x].append((counter,y))

    distance_multiplier = 1.1
    for point in neighbour_dict:
        while len(neighbour_dict[point])<2:
            distance_multiplier+=0.1
            neighbours = distance_df[distance_df[point]<distance_multiplier*standard_distance]
            if not neighbours.empty:
                for close_point in neighbours[point]:
                    if close_point != point:
                        if (support.find_key_by_value(distance_dict[point],close_point),close_point) not in neighbour_dict[point]:
                            neighbour_dict[point].append((support.find_key_by_value(distance_dict[point],close_point),close_point))
        distance_multiplier = 1.1
    print(neighbour_dict)
    nodes = []
    init_graph={}
    for node in neighbour_dict.keys():
        init_graph[node] = {}
        nodes.append(node) 



    for point in neighbour_dict:
        for neighbour,distance in neighbour_dict[point]:
            init_graph[point][neighbour] = distance
    #print (init_graph)

    graph = Graph.Graph(nodes,init_graph)
    #previous_nodes, shortest_path = support.dijkstra_algorithm(graph=graph,start_node = 0)
    #support.print_result(previous_nodes, shortest_path,start_node=0,target_node=19)
    print(shortest_path)
    SPV= []
    SPV.append(nodes.pop(0))
    to_be_visited = nodes
    temp_start_point = SPV[0]
    temporary_distance_dict = {}
    #while to_be_visited:
    # for node in to_be_visited:
    #     temporary_distance_dict[node] = {}
    #     previous_nodes, shortest_path = support.dijkstra_algorithm(graph=graph,start_node = temp_start_point)
    #     temporary_distance_dict[node] = shortest_path
    #     temp_start_point = min(temporary_distance_dict[node], key=temporary_distance_dict.get)
    #     SPV.append(temp_start_point)
    #     to_be_visited = delete_point_from_list(to_be_visited, temp_start_point)
    #     current_node = closest_node
    #     print(temporary_distance_dict)
    
if __name__== '__main__':
    main()