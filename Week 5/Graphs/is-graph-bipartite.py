class Solution(object):
    def isBipartite(self, graph):
        """
        PROBLEM STATEMENT:
        Given an undirected graph, return true if and only if it is bipartite.
        Recall that a graph is bipartite if we can split it's set of nodes 
        into two independent subsets A and B such that every edge in the graph 
        has one node in A and another node in B.
        The graph is given in the following form: graph[i] is a list of indexes j 
        for which the edge between nodes i and j exists.  
        Each node is an integer between 0 and graph.length - 1.  
        There are no self edges or parallel edges: graph[i] does not contain i, 
        and it doesn't contain any element twice.
        :type graph: List[List[int]]
        :rtype: bool
        """
        mark = collections.defaultdict(int)
        
        def split(node):
            for adj in graph[node]:
                if adj in mark:
                    if mark[node] == mark[adj]:
                        return False
                else:
                    mark[adj] = 1 - mark[node]
                    if not split(adj):
                        return False
            return True

        for node in range(len(graph)):
            if not split(node):
                return False
        return True
