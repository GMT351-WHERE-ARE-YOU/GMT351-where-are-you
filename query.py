from pymongo import MongoClient
import trilateration_algorithm
import folium

client = MongoClient('localhost',27017)

db = client['nested']

col = db.road


myquery = { "phone number" : 20}

mydoc = col.find(myquery)

for x in mydoc:
  length = len(x["geometry"]["coordinates"][0])


track_point = int(len(x["geometry"]["coordinates"][0])/3) # kullanıcıya dair kaç nokta var.
names=[]
for i in range(track_point):
    names.append(i)

ranges = x["range"]
print(len(ranges[0]))
track = []
k = 0
for i in range(length):
  for j in range(2):
    k +=1
    tower = x["geometry"]["coordinates"][0][i]
    index = tower[j]
    track.append(index)
    if (k % 2 == 0):
      track.append(ranges[0][i])

matched = {n: () for n in range(len(names))}
print(matched)
i=0
j=9
for name in names:

        matched[name]= track[i:j]
        i +=9
        j+=9

print (matched)

final_points =[]
for s in range(len(matched)):
    final_points.append(trilateration_algorithm.trackPhone(matched[s][0],matched[s][1],matched[s][2],matched[s][3], matched[s][4], matched[s][5],matched[s][6], matched[s][7],matched[s][8]))

print(final_points)
m = folium.Map(location = [final_points[0][0],final_points[0][1]], zoom_start = 12)

for k in range(len(final_points)):
  folium.Marker([final_points[k][0],final_points[k][1]]).add_to(m)

m.save('map.html')



