class KMeansClusterer():
    def clusterize(self,objects,k,max_iter=10):
        cs = numpy.array(random.sample(objects,k))
        for iter in range(max_iter):
            new_cs = numpy.zeros([k,2])
            counts = numpy.zeros(len(cs))
            for x in objects:
                nearest_c = min(cs,key=lambda c: metric(c,x))
                for (index, centroid) in enumerate(cs):
                    if numpy.all(centroid== nearest_c):
                        new_cs[index] += x
                        counts[index] += 1
        cs = numpy.array(map(lambda x,y: x/y, new_cs, counts))
        clusters = [[c] for c in cs]
        for x in objects:
            nearest_c = min(cs,key=lambda c: metric(c,x))
            for cluster in clusters:
                if numpy.all(cluster[0] == nearest_c):
                    cluster.append(x)
        for cluster in clusters:
           cluster.pop(0)
        return clusters

