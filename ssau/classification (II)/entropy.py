def entropy(data, target_attr):
    freqs = defaultdict(int)
    data_entropy = 0.0
    for x in data:
        freqs[x[target_attr]] += 1
    for freq in freqs.values():
        data_entropy += \
        (-float(freq)/len(data)) * math.log(float(freq)/len(data), 2)
    return data_entropy

def gain(data, attr, target_attr):
    freqs = defaultdict(int)
    subset_entropy = 0.0
    for x in data:
        freqs[x[attr]] += 1
    for val in freqs.keys():
        prob = freqs[val] / sum(freqs.values())
        subset = [record for record in data if record[attr] == val]
        subset_entropy += prob * entropy(subset, target_attr)
    return (entropy(data, target_attr) - subset_entropy)
