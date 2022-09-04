class SpanningTreeClusterer():
    def clusterize(self,objs,metric,K):
        N = len(objs)
        c_graph = graph()
        c_graph.add_nodes(range(N))
        for i in range(N):
          for j in range(i,N):
            c_graph.add_edge((i,j),wt=metric(objs[i],objs[j]))
        stree, c_graph = minimal_spanning_tree(c_graph), graph()
        c_graph.add_nodes(range(N))
	del stree[stree.keys()[0]]
        for i in stree.keys():
          c_graph.add_edge((i,stree[i]),
                           wt=metric(objs[i],objs[stree[i]]))
        for _ in range(K-1):
          max_edge = max(c_graph.edges(), 
                         key=lambda x: metric(objs[x[0]],objs[x[1]]))
          c_graph.del_edge((max_edge))
        component_idxs = connected_components(c_graph)
        clusters = defaultdict(list)
        for i in component_idxs.keys():
          clusters[component_idxs[i]].append(objs[i])
        return clusters

