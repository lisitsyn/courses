import math

trainset = ( {'classe': 'red', 'x':1.0, 'y':2.0})

metric = lambda X,Y: X['x']-Y['x']

def classify(object,trainset):
  nearest = (trainset[0],metric(trainset[0],object))
  for item in trainset:
    dist = metric(item,object)
    if dist<nearest[1]:
      nearest = (item,dist)
  return nearest[0]

