# 4. Solicitar Entrada en Ventanas Emergentes
import networkx as nx

def create_city_graph():
    G = nx.Graph()
    cities = ["A", "B", "C", "D", "E", "F", "G", "H"]
    G.add_nodes_from(cities)
    edges = [("A", "B", 1), ("A", "C", 4), ("B", "C", 2), ("B", "D", 5),
             ("C", "D", 1), ("D", "E", 3), ("E", "F", 1), ("F", "G", 2),
             ("G", "H", 1), ("E", "H", 5)] 
    G.add_weighted_edges_from(edges)
    return G
