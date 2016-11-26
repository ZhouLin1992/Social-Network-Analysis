import networkx as nx
import matplotlib.pyplot as plt
import operator
import timeit
from multiprocessing import Pool
import itertools

g_fb = nx.read_edgelist('facebook_combined.txt', create_using = nx.Graph(), nodetype = int)

def partitions(nodes, n):
    "Partitions the nodes into n subsets"
    nodes_iter = iter(nodes)
    while True:
        partition = tuple(itertools.islice(nodes_iter,n))
        if not partition:
            return
        yield partition

def btwn_pool(G_tuple):
    return nx.betweenness_centrality_source(*G_tuple)

def between_parallel(G, processes = None):
    p = Pool(processes=processes)
    part_generator = 4*len(p._pool)
    node_partitions = list(partitions(G.nodes(), int(len(G)/part_generator)))
    num_partitions = len(node_partitions)
 
    bet_map = p.map(btwn_pool,
                        zip([G]*num_partitions,
                        [True]*num_partitions,
                        [None]*num_partitions,
                        node_partitions))
 
    bt_c = bet_map[0]
    for bt in bet_map[1:]:
        for n in bt:
            bt_c[n] += bt[n]
    return bt_c

# only one processor: it takes 157.82109149699863 seconds to finish
# [(107, 0.4805180785560146), (1684, 0.33779744973019543), (3437, 0.23611535735892838), 
# (1912, 0.22929533958687434), (1085, 0.14901509211665437), (0, 0.1463059214744287), 
# (698, 0.11533045020561006), (567, 0.09631033121856328), (58, 0.08436020590796522), (428, 0.06430906239323834)]

# start = timeit.default_timer()
# bt = nx.betweenness_centrality(g_fb)
# stop = timeit.default_timer()
# top = 10

# max_nodes =  sorted(bt.items(), key = lambda v: -v[1])[:top]
# bt_values = [5]*len(g_fb.nodes())
# bt_colors = [0]*len(g_fb.nodes())
# for max_key, max_val in max_nodes:
#     bt_values[max_key] = 150
#     bt_colors[max_key] = 2
    
# print ('It takes {} seconds to finish'.format(stop - start))
# print (max_nodes)


# multiprocessor: it takes 94.09475689499959 seconds to finish
start = timeit.default_timer()
bt = between_parallel(g_fb)
stop = timeit.default_timer()
top = 10

max_nodes =  sorted(bt.items(), key = lambda v: -v[1])[:top]
bt_values = [5]*len(g_fb.nodes())
bt_colors = [0]*len(g_fb.nodes())
for max_key, max_val in max_nodes:
    bt_values[max_key] = 150
    bt_colors[max_key] = 2
    
print ('It takes {} seconds to finish'.format(stop - start))
print (max_nodes)
