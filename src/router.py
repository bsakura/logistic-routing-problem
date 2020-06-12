'''
filename: router.py
consisting: function about routing
affliation: milestone 2
'''

import more_itertools as mit

def clusterer(dests, sales, start):
    # cluster the destination for the salesperson

    # removing start point
    destList=[]
    for dest in dests:
        destList.append(dest)
    destList.sort()
    destList.remove(start)

    # initiating clust
    clust=[]
    for i in range(sales):
        clust.append([start])
        clust[i]= clust[i] + [list(d) for d in mit.divide(sales, destList)][i]
    
    #return
    return clust

def intoRoute(path, cluster):
    # turn the path into route

    r = []
    route=[]
    start = path[0][0][0]
    r.append(start)

    for path in path[0]:
        r.append(path[1])
    for i in range(len(r)):
        route.append(cluster[r[i]])

    # return route
    return route

def intoEdge(route):
    # turn route into edges

    d = []
    for i in range(len(route)-1):
        tuples = (route[i], route[i+1]) 
        d.append(tuples)
    
    # return edges
    return d

def intoNode(route):
    # turn route into nodes

    n = route
    
    #return nodes
    return n

def labelMaker(node):
    # create a dict of label

    lab={}
    for i in range(len(node)):
        lab[node[i]]= str(node[i]) 

    # return label
    return lab

def printDest(destList):
    # print the salesperson's dest

    # start point
    print("From: ")
    print(destList[0])

    # dests to go
    print("Destinations: ")
    for i in range(len(destList)-2):
        print(destList[i+1], end=", ")
    print(destList[len(destList)-1])

def printRoute(route):
    #print the routes

    for i in range (len(route)-1):
        print(route[i],"->", end=" ")
    print(route[len(route)-1])
    
def printDist(path):
    # print the distance

    print("Distance:")
    print(path[1])