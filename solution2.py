from geopy import distance
import json
import utils.helper_functions as support

"""This script just makes the solution 1 more efficient,
reducing time complexity to sigma(n) from n^2"""

locations = open('data.json')
data = json.load(locations)
coordinates ={}
for i in data['features']:
    coordinates[i['properties']['point-id']] = tuple(i['geometry']['coordinates'])
coordinates[0] = (12.922963500022886, 52.42706852497485)
current_location = 0
#since we're already in poin 0 (the user's starting position) all we need to do first is to determine where to go first
distances = {}
for x in coordinates:
    distances[x] = {}
counter = 0

while True:
    #calculate the distances to determine the closes one, dont calculate for current location
    for coords in coordinates:
        
        if  coords != current_location:
            if coords not in distances[current_location].keys():
                path_length = distance.distance(coordinates[current_location],coordinates[coords]).km
                distances[coords][current_location] = distances[current_location][coords] = path_length
            else:
                continue
    else:
        #current location, since it's visited can be set to infinite as we don't want to get back to it
        for x in distances:
            distances[x][current_location] = float('inf')
    if min(distances[current_location].values()) == float('inf'):
        break
    next_location = support.find_key_by_value(distances[current_location], min(distances[current_location].values()))
    print(f'Next spot: {next_location}, Bearing to the next spot: {support.compass_directions(coordinates[current_location],coordinates[next_location])}')
    print(f'Distance to the next spot: {min(distances[current_location].values())*1000}m\n')
    current_location = next_location
