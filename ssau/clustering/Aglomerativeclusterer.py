class AglomerativeClusterer():
    def clusterize(self,objects,till,metric):
        clusters = [[x] for x in objects]
        iteration = 0
        while len(clusters)>till:
            n_idx = (0,1)
            n_dist = metric(clusters[0],clusters[1])
            for i, cluster_lhs in enumerate(clusters):
                for j, cluster_rhs in enumerate(clusters):
                    m = metric(cluster_lhs,cluster_rhs)
                    if n_dist>m and not i==j:
                        n_dist = m
                        n_idx = (i,j)
            aglomerated = clusters[n_idx[0]]+clusters[n_idx[1]]
            clusters = \
            [clusters[i] for i in range(len(clusters)) \
            if i != n_idx[0] and i != n_idx[1]]
            clusters.append(aglomerated)
            iteration += 1
        return clusters
