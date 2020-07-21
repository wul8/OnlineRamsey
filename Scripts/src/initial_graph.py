import networkx as nx

def startGraph():
    graph = nx.Graph()
    graph.add_node(1)
    return graph

# Test of graph2
def startGraph_2():
    graph = nx.Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1,2,color = "red")
    graph.add_node(3)
    graph.add_node(4)
    graph.add_edge(2,3,color = "red")
    graph.add_edge(3,4,color = "blue")
    graph.add_node(5)
    graph.add_edge(3,5,color = "blue")
    return graph