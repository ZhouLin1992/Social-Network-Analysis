import networkx as nx
import matplotlib.pyplot as plt
import operator
import timeit
from multiprocessing import Pool
import itertools

# undirected graph
g_fb = nx.read_edgelist('facebook_combined.txt', create_using = nx.Graph(), nodetype = int)

# page rank
g_fb_pr = nx.pagerank(g_fb)

# result
# [(3437, 0.007614586844749602), (107, 0.006936420955866113), (1684, 0.006367162138306825), 
# (0, 0.006289602618466542), (1912, 0.0038769716008844957), (348, 0.002348096972780577), 
# (686, 0.0022193592598000193), (3980, 0.0021703235790099928), (414, 0.0018002990470702264), (698, 0.0013171153138368812)]

top = 10
max_pagerank = sorted(g_fb_pr.items(), key = lambda v: -v[1])[:top]
print(max_pagerank)
