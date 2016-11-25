import networkx as nx
import matplotlib.pyplot as plt
import operator
import timeit

# undirected graph
g_fb = nx.read_edgelist('facebook_combined.txt', create_using = nx.Graph(), nodetype = int)

# basic info about the graph

# Type: Graph
# Number of nodes: 4039
# Number of edges: 88234
# Average degree:  43.6910
print (nx.info(g_fb))

# the graph is not directed
print (nx.is_directed(g_fb))

# Degree Centrality
dg_centrality = nx.degree_centrality(g_fb)
sorted_dg_centrality = sorted(dg_centrality.items(), key=operator.itemgetter(1), reverse=True)
sorted_dg_centrality[:10]

# node 107 has the highest Degree Centrality
print (nx.degree(g_fb, [107]))

# node 107 has 1045 friends, normalized Degree Centrality
print (1045 / g_fb.number_of_nodes())