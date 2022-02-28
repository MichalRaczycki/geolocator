for coords in coordinates:
    if  coords != current_location:
        distances[current_location][coords] = distance.distance(coordinates[current_location],coordinates[coords]).km
    else:
        distances[current_location][coords] = float('inf')

next_location = support.find_key_by_value(distances[0], min(distances[0].values()))

while True:
    #calculate the distances to determine the closes one, dont calculate for current location
    for coords in coordinates:
        if  coords != current_location:
            path_length = distance.distance(coordinates[current_location],coordinates[coords]).km
            distances[coords][current_location] = distances[current_location][coords] = path_length
    else:
        #current location, since it's visited can be set to infinite as we don't want to get back to it
        distances[current_location][coords] = float('inf')
    
    next_location = support.find_key_by_value(distances[0], min(distances[0].values()))
    print(distances)
    break;