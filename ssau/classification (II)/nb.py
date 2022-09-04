class NB_classifier(Classifier):
    def __init__(self,reg_par):
      self.probs = \
      defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
      self.c_probs, self.reg_par = defaultdict(float), reg_par
    def train(self,trainset):
      for (x,c) in trainset:
          self.c_probs[c] += 1
          for index,attribute in enumerate(x):
              self.probs[c][index][attribute] += 1
      for c in self.c_probs.keys():
          for index in self.probs[c].keys():
              for attribute in self.probs[c][index]:
                  self.probs[c][index][attribute] /= self.c_probs[c]
          self.c_probs[c] /= len(trainset)
      self.probs, self.c_probs = dict(self.probs), dict(self.c_probs)
    def classify(self,x):
      scores = self.c_probs.copy()
      for c in scores.keys():
          for index,attribute in enumerate(x):
              scores[c] *= \
              (self.probs[c][index][attribute]+self.reg_par)
      return max(scores,key=scores.get),scores

