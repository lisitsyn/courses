def frequentItemset(transactions):
    freq_itemset = {}
    for itemset in transactions:        
        for item in itemset:
            key = tuple([item])
            if freq_itemset.has_key(key): freq_itemset[key]+=1
            else: freq_itemset[key]=1
    return freq_itemset

def pruneBySupport(itemset,support):
    return filter(lambda item: itemset[item]>support,itemset)

def unifyItemset(itemset):
    return list(set([tuple(set(tuple(x)+tuple(y)))
                     for x in itemset 
                     for y in itemset 
                     if not x==y]))
