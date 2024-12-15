import networkx as nx
import matplotlib.pyplot as plt
import sys



def minDistance(dist, mstSet, V):
    min = sys.maxsize 
    for v in range(V):
        if mstSet[v] == False and dist[v] < min:
            min = dist[v]
            min_index = v
    return min_index




def prims(G, pos):
    V = len(G.nodes()) 
    dist = [] 
    parent = [None]*V 
    mstSet = [] 
    
    for i in range(V):
        dist.append(sys.maxsize)
        mstSet.append(False)
    dist[0] = 0
    parent[0]= -1 
    for count in range(V-1):
        u = minDistance(dist, mstSet, V) 
        mstSet[u] = True
        
        for v in range(V):
            if (u, v) in G.edges():
                if mstSet[v] == False and G[u][v]['length'] < dist[v]:
                    dist[v] = G[u][v]['length']
                    parent[v] = u
    for X in range(V):
        if parent[X] != -1: 
            if (parent[X], X) in G.edges():
                nx.draw_networkx_edges(G, pos, edgelist = [(parent[X], X)], width = 2.5, alpha = 0.6, edge_color = 'r')
    return




def CreateGraph():
    G = nx.Graph()
    f = open('input.txt')
    n = int(f.readline())
    wtMatrix = []
    for i in range(n):
        list1 = map(int, (f.readline()).split())
        wtMatrix.append(list1)
    
    for i in range(n) :
        for j in range(n)[i:] :
            if wtMatrix[i][j] > 0 :
                    G.add_edge(i, j, length = wtMatrix[i][j]) 
    return G




def DrawGraph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels = True)  
    edge_labels = nx.get_edge_attributes(G,'length')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11) 
    return pos




if __name__ == "__main__":
    G = CreateGraph()
    pos = DrawGraph(G)
    prims(G, pos)
    plt.show()