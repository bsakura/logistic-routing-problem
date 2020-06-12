from load import *
from matrix import *
from graph import *
from ant_colony import *
from router import *
from visualizer import *

print("Samlekum, welcome to mini mtsp")

# node and edge first blood
nf = input("Enter the node file in txt: ")
ef = input("Enter the edge file in txt: ")

# destination
posts=[]
nposts= int(input("Number of destination excluding starting point: "))
startpost= int(input("Starting point: "))
posts.append(startpost)
for i in range(nposts):
    rest = int(input("Destination -"+str(i+1)+": "))
    posts.append(rest)

# create graph and subgraph
G=graphMaker("../data/"+nf,"../data/"+ef)
sG= subgraphMaker(G, posts)

# matrix distance of the subgraph
sGMatrix = intoMatrix(sG)
#print("Matrix representation of the subgraph")
#printMatrix(sGMatrix)

sales=int(input("How many salesperson(s) we got: "))

# cluster the destinations
cluster=clusterer(posts, sales, posts[0])


# data of the tour
edgelist=[]
nodelist=[]
label=labelMaker(posts)


for i in range(sales):

    print("Salesperson "+str(i+1))

    # print list of destinations
    printDest(cluster[i])

    # subgraph for each cluster
    subGraph= subgraphMaker(G, cluster[i])  

    # matrix of the subgraph
    s = intoMatrix(subGraph)
    print("Matrix representation: ")
    printMatrix(s)
       
    # generate shortest path
    ant = AntColony(np.array(s), 1, 1, 100, 0.95, alpha=1, beta=1)
    path = ant.run()

    # the routes
    simpleRoute= intoRoute(path,cluster[i])
    actRoute= astar_super(G,simpleRoute)


    print("Simple route:")
    printRoute(simpleRoute)

    print("Actual route: ")
    printRoute(actRoute)

    printDist(path)

    # append the data
    edd=intoEdge(actRoute)
    ndd=intoNode(actRoute)
    edgelist.append(edd)
    nodelist.append(ndd)


# Display nodes per positions
visRoute(G, edgelist, nodelist, label)
