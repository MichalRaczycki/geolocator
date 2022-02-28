
class Graph(object):
    
    """
    Implementation of data structures used in Dijkstra's 
    algorithm for finding the shortest path between two points in a graph
    described by Alexey Klochay
    """
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.constuct_graph(nodes,init_graph)
    
    def construct_graph(self, nodes, init_graph):
        """
        Check if the graph is symmetrical.
        Args:
            nodes (list): list of all the nodes 
            init_graph (dict): empty dictionary
        Returns:
           instance of graph
        """
        graph = {}
        for node in nodes:
            graph[node] = {}
            
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
        return graph
    
    def get_nodes(self):
        #Return the nodes of the graph
        return self.nodes
    
    def get_outgoing_edges(self,node):
        #Return neighbours of a node
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        #Returns weight of connection between nodes
        return self.graph[node1][node2]
            