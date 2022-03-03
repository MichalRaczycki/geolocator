from geopy import distance
import json
import utils.helper_functions as support


def print_distances(distance_dict):
    for x in distance_dict.items():
        print(f'{x}\n')
    
locations = open('data.json')
data = json.load(locations)
print(data)
raw_point_coords ={}
for i in data['features']:
    raw_point_coords[i['properties']['point-id']] = tuple(i['geometry']['coordinates'])

coordinate_dict = {}
coordinate_dict[0] = (12.922963500022886, 52.42706852497485)
for x in sorted(raw_point_coords.items(),key = lambda x :x[0]):
    coordinate_dict[x[0]]=x[1]

#print(coordinate_dict)

distance_dict={}
for current_point in range(0,len(coordinate_dict.items())):
    distance_dict[current_point] = {}
    for y in range(0,len(coordinate_dict.items())):
        if y!= current_point:
            distance_dict[current_point][y] = distance.distance(coordinate_dict[current_point],coordinate_dict[y]).km
        
#print_distances(distance_dict)
distance = 0
current_location = 0
next_destination = min(distance_dict[0], key=distance_dict[0].get)
not_finished = True
while not_finished:
    print(support.compass_directions(coordinate_dict[0],coordinate_dict[next_destination]))
    print(f'next location {current_location} is in:{distance_dict[current_location][next_destination]*1000} m')
    
    distance+=distance_dict[current_location][next_destination]
    for x in range(0,len(coordinate_dict.items())):
            if x!= current_location:
                distance_dict[x][current_location] = float('inf')
    current_location = next_destination
    next_destination = min(distance_dict[next_destination], key=distance_dict[next_destination].get)
    if (distance_dict[current_location][next_destination] ==float('inf')):
        print(f'work is done, you have travelled {distance} kilometers')
        not_finished = False
    else:
        continue
        
        


