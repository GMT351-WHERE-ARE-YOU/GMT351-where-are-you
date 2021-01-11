import json

'''
Function returns the points coordinates that join line.
'''
def coordinates(file):
  with open(file) as f:
    data = json.load(f)

  for feature in data['features']:

    a = feature['geometry']['coordinates']

  return a
