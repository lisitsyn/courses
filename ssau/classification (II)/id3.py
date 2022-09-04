class ID3_classifier(Classifier):
    def __init__(self):
        self.tree = {}

    def train(self, trainset):
        if not trainset: return None
        attributes = trainset[0].keys()
        for x in trainset:
            if not x.keys() == attributes:
                return None
        attributes.remove('class')
        self.tree = create_DT(trainset, attributes)

    def classify(self, x):
        return traverse_classify(self.tree, x)
