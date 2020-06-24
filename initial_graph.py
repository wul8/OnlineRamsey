import networkx as nx

def startGraph():
    graph = nx.Graph()
    graph.add_node(1)
    graph.add_edge(0,1,color = "red")
    return graph
