def best_attribute(data, attributes):
    attr_w_gains = \
    map(lambda attr: (attr, gain(data, attr)), attributes)
    return max(attr_w_gains, key=lambda x: x[1])[0]


def majority_class(data):
    classes = [x['class'] for x in data]
    return max(set(classes),key=classes.count)
