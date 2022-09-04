NN =
   lambda to_classify, trainset:
   classifier(to_classify,trainset,k=1)
kNN =
   lambda to_classify, trainset,kp:
   classifier(to_classify,trainset,k=kp)
wkNN =
   lambda to_classify, trainset,kp: 
   classifier(to_classify,trainset,
              k=kp,w=lambda i,rho: kp-i)

