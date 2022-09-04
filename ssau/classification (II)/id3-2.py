def create_DT(trainset,attributes):
        classes = [x['class'] for x in trainset]
        default = majority_class(trainset)
        if len(attributes) == 1:
            return default
        if classes.count(classes[0]) == len(classes):
            return classes[0]
        else:
            best = best_attribute(trainset,attributes)
            tree = {best : {}}
            for value in set(map(lambda x: x[best], trainset)):
                subtree = create_DT(
                    [x for x in trainset if x[best] == value],
                    [attr for attr in attributes if attr != best])
                tree[best][value] = subtree
            return tree
def traverse_classify(tree, x):
        if type(tree) == type("string"):
            return tree
        else:
            attr = tree.keys()[0]
            subtree = tree[attr][x[attr]]
        return traverse_classify(x, subtree)
