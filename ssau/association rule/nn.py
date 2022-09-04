def frequencies(transactions):
  ...
def frequencies(transactions,items):
  ...

def prune(freqs,support):
  return filter(lambda x: freqs[x]>=support, freqs)

def crossjoin(items):
  pairs = [tuple(set(x).union(set(y))) for x in items
                                       for y in items
                                       if not x==y]
  return list(set(pairs))

def frequent_sets(transactions,support):
  
