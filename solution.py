from geopy import distance
import json

#geolocator  = Nomanatim(user_agent="Measurement_locator")

locations = open('data.json')
data = json.load(locations)
raw_point_coords ={}
for i in data['features']:
    raw_point_coords[i['properties']['point-id']] = i['geometry']['coordinates']

coordinate_dict = {}
for x in sorted(raw_point_coords.items(),key = lambda x :x[0]):
    coordinate_dict[x[0]]=x[1]
# for x,y  in coordinate_dict.items():
#      print(f'{x} -> {y}')

print (len(coordinate_dict.items()))
current_point = 1
for point,coords in coordinate_dict.items():
    for x in range(len(coordinate_dict.items()))+1:
        print(f'point:{point}, coords:{coords}, x:{x}')
        
            
        