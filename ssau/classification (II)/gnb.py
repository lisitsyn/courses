class GNB_classifier(Classifier):
    def __init__(self,dimension):
        self.mu,self.sigma,self.apriori = \
        (defaultdict(lambda: numpy.zeros(dimension)),
        defaultdict(lambda: numpy.zeros(dimension))),{}
    def train(self,trainset):
        class_count = defaultdict(int)
        for (x,c) in trainset:
            class_count[c] += 1
            self.mu[c]+= x
        for c in self.mu.keys():
            self.mu[c] /= class_count[c]
            self.apriori[c] = float(class_count[c])/len(trainset)
        for (x,c) in trainset:
            self.sigma[c] = (self.mu[c]-x)**2
        for c in self.mu.keys():
            self.sigma[c] /= ((class_count[c])-1)
    def classify(self,x):
        rates = {}
        for c in self.apriori.keys():
            rates[c] = self.apriori[c]*numpy.exp(
       -((x-self.mu[c])**2)/(2*self.sigma[c]**2)).prod()
        return max(rates,key=rates.get)

