'''
filename: visualizer.py
consisting: fuction to visualize the route taken each salesperson
affliation: milestone 3
'''

import networkx as nx
import matplotlib.pyplot as plt

def visRoute(G, edgelist, nodelist, label):
    # visualize the route

    colorList = ['salmon','gold','lightseagreen','powderblue','pink','lightcoral','teal','orange']

    # visualize the whole graph
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, node_color="lightgray", edge_color="lightgray", with_labels=False, node_size=6)
    nx.draw_networkx_labels(G, pos, labels=label, font_size=6, font_family='monospace')
    
    # visualize the route taken for each salespersons
    for i in range(len(nodelist)):
        nx.draw_networkx_nodes(G, pos, nodelist=nodelist[i][:1], node_color='red', edgescolor='coral', node_size=80, with_labels=True)
        nx.draw_networkx_nodes(G, pos, nodelist=nodelist[i][1:len(nodelist[i])-1], node_color=colorList[i], node_size=80, with_labels=True)
        nx.draw_networkx_edges(G, pos=pos, edge_color=colorList[i], edgelist=edgelist[i])

    # show
    plt.show()

