def neighbors(bpoint,points,k):
  ...

def vote(points,w = lambda i: i):
  votes = collections.defaultdict(float)
  for point in points: votes[point[0].cluster] += w(i)
  votes = \
sorted(votes.items(),key=lambda item:item[1], reverse=True)
  return votes[0][0]

def wkNN(to_classify, train_set,k,q):
  result = []
  for x in to_classify:
    nearest = neighbors(x,train_set,k)
    c = vote(nearest,lambda i: q**i)
    result.append(point(x.coords,))
  return result
