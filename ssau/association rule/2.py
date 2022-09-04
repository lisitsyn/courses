def countFrequencies(transactions, itemset):
    freq_itemset = dict([(x,0) for x in itemset])
    for element in transactions:
        for item in freq_itemset.keys():
          if set(item).issubset(set(element)): freq_itemset[item]+=1
    return freq_itemset

def apriori(transactions,support):
    L1 = frequentItemset(transactions)
    L = pruneBySupport(L1,support)
    result = []
    while len(L)>0:
        result.append(L)
        L = unifyItemset(L)
        L = countFrequencies(transactions,L)
        L = pruneBySupport(L,support)
    return result

