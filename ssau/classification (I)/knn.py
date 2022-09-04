def wkNN_classify(obj, rest, k, metric, w = lambda i: 1):
    distances = \
    map(lambda (x,c): (x,c,metric(obj,x)), rest)
    sorted_distances = \
    sorted(distances, key = lambda (x,c,m): m)[0:k]
    votes = defaultdict(float)
    for i, (x,c,m) in enumerate(sorted_distances):
        votes[c] += w(i)
    return max(votes,key=votes.get)

def parzen_classify(obj, rest, metric, K = lambda m: 1/m):
    distances = \
    map(lambda (x,c): (x,c,metric(obj,x)), rest)
    votes = defaultdict(float)
    for (x,c,m) in distances:
        votes[c] += K(m)
    return max(votes,key=votes.get)
