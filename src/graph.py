'''
filename: graph.py
consisting: functions to create graph and subgraph
affliation: milestone 1
'''

import networkx as nx
from a_star import *
from load import *

def graphMaker(nodeFile, edgeFile):
    # initiates a graph 
    G = nx.Graph()

    # nodes
    node = nodeLoader(nodeFile)
    for parse in node:
        G.add_node(int(parse[0]), pos=(float(parse[1]), float(parse[2])))

    # edges
    edge = edgeLoader(edgeFile)
    for parse in edge:
        G.add_edge(int(parse[1]), int(parse[2]), weight=float(parse[3]))

    # return graph
    return G

def subgraphMaker(G, posts):
    # initiates the subgraph
    subgraph = nx.Graph()

    #nodes
    node_pos = G.nodes().data('pos')
    for post in posts:
        subgraph.add_node(post, pos=node_pos[post])

    #edges
    for i in range(len(posts)):
        for j in range(i+1, len(posts)):
            subgraph.add_edge(posts[i], posts[j], weight= astar_path_length(G, posts[i], posts[j]))
    
    #return subgraph
    return subgraph

