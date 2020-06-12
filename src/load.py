
def nodeLoader(nodeFile):
    #load nodes

    nodes = []
    with open(nodeFile, "r") as f:
        lines = f.readlines()
        for line in lines:
            nodes.append(line.strip().split(" "))
    #return nodes
    return nodes

def edgeLoader(edgeFile):
    #load edges
    
    edges = []
    with open(edgeFile, "r") as f:
        for line in f:
            edges.append(line.strip().split(" "))
    #return edges
    return edges

