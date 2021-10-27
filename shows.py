
import matplotlib.pyplot as plt
import numpy as np
import json

#compare their ratings per episode 


#NARCOS 

narcos = []
text = ''

narcos = '/Users/laurenleadbetter/Desktop/CS40 /HW_ 02/narcos .json'
with open(narcos) as f:
    text = f.read()
    narcos = json.loads(text)

rating = {}
episodes = 0
for episodes in range (0,30):
    rating[episodes] = narcos["_embedded"]["episodes"][episodes]['rating']['average']


##Westworld

west_world = []
text = ''

westworld = '/Users/laurenleadbetter/Desktop/CS40 /HW_ 02/westworld .json'
with open(westworld) as f:
    text = f.read()
west_world = json.loads(text)

rating2 = {}
episodes2 = 0
for episodes2 in range (0,28):
    rating2[episodes2] = west_world["_embedded"]["episodes"][episodes2]['rating']['average']

print(rating2)


x1 = rating.keys()
y1 = rating.values()
plt.plot(x1, y1, label = "Narcos")

x2 = rating2.keys()
y2 = rating2.values()
plt.plot(x2, y2, label = "Westworld")

plt.xlabel('Episode')
plt.ylabel('Rating')
plt.title ('Narcos vs Westworld: Episode Ratings')
plt.legend()
plt.show()
