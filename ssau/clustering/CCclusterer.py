class ConnectedComponentClusterer():
    def clusterize(self,objs,R_max):
        cluster_graph = graph()
        N = len(objs)
        cluster_graph.add_nodes(range(N))
        for i in range(N):
            for j in range(N):
                if not i==j and metric(objs[i],objs[j])<R_max:
                    try: cluster_graph.add_edge((i,j))
                    except: pass
        component_idxs = connected_components(cluster_graph)
        clusters = defaultdict(list)
        for i in component_idxs.keys():
            clusters[component_idxs[i]].append(objs[i])
