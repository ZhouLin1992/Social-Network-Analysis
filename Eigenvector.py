import networkx as nx
import matplotlib.pyplot as plt
import operator
import timeit
from multiprocessing import Pool
import itertools

# undirected graph
g_fb = nx.read_edgelist('facebook_combined.txt', create_using = nx.Graph(), nodetype = int)

# eigenvector

# result:
# [(1912, 0.09540688873596533), (2266, 0.08698328226321961), (2206, 0.08605240174265634), 
# (2233, 0.08517341350597848), (2464, 0.0842787836468596), (2142, 0.08419312450068117), 
# (2218, 0.08415574433673877), (2078, 0.08413617905810125), (2123, 0.08367142125897375), (1993, 0.08353243711860492)]

g_fb_eg = nx.eigenvector_centrality(g_fb)

top = 10
max_eg = sorted(g_fb_eg.items(), key = lambda v: -v[1])[:top]
print(max_eg)