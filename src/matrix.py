'''
filename: matrix.py
consisting: matrix functions
affliation: milestone 1
'''
import sys

def intoMatrix(subgraph):
    # turning subgraph into matrix

    nodes = list(subgraph.nodes())
    edges = subgraph.edges().data('weight')
    index = { name : index for index, name in enumerate(nodes) }
    
    m = [[sys.maxsize for i in range(len(nodes))] for j in range(len(nodes))]
    for i,j,k in edges:
        m[index[i]][index[j]] = k
        m[index[j]][index[i]] = k
      
    #return matrix
    return m

def printMatrix(matrix):
    # print matrix

    n = len(matrix[0])
    for i in range(n): 
        for j in range(n):
            if i==j:
                print(" inf\t\t", end="||") 
            else:
                print(" {:0.4f}".format(matrix[i][j])+"\t||",end="")                
        print()
