
import matplotlib.pyplot as plt
import numpy as np
import json

earthquakes = []

file = '/Users/laurenleadbetter/Desktop/CS40 /HW_ 02/all_hour.geojson.json'
with open(file) as f:
    text = f.read()
    earthquakes += json.loads(text)


alaska = 0
california = 0 
other = 0


for entry in range(0,10,1):
    for earthquake in earthquakes:
        if 'alaska' in earthquake['features'][entry]['properties']['place'].lower(): 
            alaska += 1 
        elif 'CA' in earthquake['features'][entry]['properties']['place']: 
            california += 1 
        else:
            other += 1
print("alaska count: ", alaska)
print("california count: ", california)
print("other count: ",other)






fig = plt.figure()

# ax = fig.add_axes([0,0,1,1])

location = ['Alaska', 'California', 'Other']
earthquakes_count = [alaska,california,other]
#ax.bar(location,earthquakes_count)

plt.bar(location,earthquakes_count) 
plt.title('Ten Most Recent Earthquakes: Location by State')
plt.xlabel('State')
plt.ylabel('Number of Earthquakes')

plt.show()