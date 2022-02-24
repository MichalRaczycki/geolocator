from geopy import distance
import json
import math


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

def print_distances(distance_dict):
    for x in distance_dict.items():
        print(f'{x}\n')
    
locations = open('data.json')
data = json.load(locations)
raw_point_coords ={}
for i in data['features']:
    raw_point_coords[i['properties']['point-id']] = tuple(i['geometry']['coordinates'])

coordinate_dict = {}
coordinate_dict[0] = (12.96441725730896, 52.54364309343404)
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
    print(compass_directions(coordinate_dict[0],coordinate_dict[next_destination]))
    print(f'next location is in:{distance_dict[current_location][next_destination]} km')
    distance+=distance_dict[current_location][next_destination]
    current_location = next_destination
    next_destination = min(distance_dict[next_destination], key=distance_dict[next_destination].get)
    if (distance_dict[current_location][next_destination] ==float('inf')):
        print(f'work is done, you have travelled {distance} kilometers')
        not_finished = False
    else:
        for x in range(0,len(coordinate_dict.items())):
            if x!= current_location:
                distance_dict[x][current_location] = float('inf')
        bearing =compass_directions(coordinate_dict[current_location],coordinate_dict[next_destination])
        print(f'to get to the next location head :{bearing}')
        print(f'next location is in:{distance_dict[current_location][next_destination]} km')
        

#print(compass_directions(coordinate_dict[1],coordinate_dict[2]))

