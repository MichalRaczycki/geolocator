from geopy import distance
import json
import utils.helper_functions as support
import argparse
import pathlib

def run(args):
    input_file = args.input
    starting_point_x = args.startx
    starting_point_y = args.starty
    calculate_path(input_file, starting_point_x, starting_point_y)


def calculate_path(input_file,starting_point_x,starting_point_y):
    
    locations = open(input_file)
    data = json.load(locations)
    coordinates ={}
    for i in data['features']:
        coordinates[i['properties']['point-id']] = tuple(i['geometry']['coordinates'])
    coordinates[0] = (starting_point_x, starting_point_y)
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
        
        
def main():
    parser = argparse.ArgumentParser(description = "calculate path from starting_point throughout all point in input_file")
    parser.add_argument("-in", help="input file path", dest="input", type=pathlib.Path, required=True)
    parser.add_argument("-startx", help="starting x coordinate [E or W]", dest = "startx", type=float, required=True)
    parser.add_argument("-starty", help="starting y coordinate [N or S]", dest = "starty", type=float, required=True)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)
    
    
if __name__=="__main__":
    main()
