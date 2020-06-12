'''
#    Copyright (C) 2004-2015 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

Modified A-Star from the reference above
'''
from heapq import heappush, heappop
from itertools import count
from networkx import NetworkXError
import networkx as nx

def astar_path(G, source, target,  weight='weight'):

    push = heappush
    pop = heappop

    c = count()
    queue = [(0, next(c), source, 0, None)]

    enqueued = {}
    explored = {}

    while queue:
        # Pop the smallest item from queue.
        _, __, curnode, dist, parent = pop(queue)

        if curnode == target:
            path = [curnode]
            node = parent
            while node is not None:
                path.append(node)
                node = explored[node]
            path.reverse()
            return path

        if curnode in explored:
            continue

        explored[curnode] = parent

        for neighbor, w in G[curnode].items():
            if neighbor in explored:
                continue
            ncost = dist + w.get(weight, 1)
            if neighbor in enqueued:
                qcost, h = enqueued[neighbor]
                if qcost <= ncost:
                    continue
            else:
                h = 0
            enqueued[neighbor] = ncost, h
            push(queue, (ncost + h, next(c), neighbor, ncost, curnode))

    raise nx.NetworkXNoPath("Node %s not reachable from %s" % (source, target))

def astar_path_length(G, source, target, weight='weight'):
    
    path = astar_path(G, source, target, weight)
    return sum(G[u][v].get(weight, 1) for u, v in zip(path[:-1], path[1:]))

def astar_super(G, routeList):
    
    listFinal =[]
    for i in range (len(routeList)-1):
        listFinal.append(routeList[i])
        a=astar_path(G,routeList[i],routeList[i+1])
        for k in range (len(a)-2):
            listFinal.append(a[k+1])
    listFinal.append(routeList[len(routeList)-1])
    return listFinal
