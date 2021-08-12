import networkx as nx
import pandas as pd

df = pd.read_csv ('Edges.csv')
sociomatrix = df.values

G = nx.DiGraph()
G.add_nodes_from(range(1, 89))
for i in range(79):
    for j in range(16):
        if (sociomatrix[i,j]!="0"):
            a,b=sociomatrix[i,j].split(",")
            c=int(a)
            d=int(b)
            G.add_edge(c, d)

e=G.in_degree (48)
print("in degree =",e)

f=G.out_degree (48)
print("out degree =",f)

g = nx.closeness_centrality (G,48)
print("closeness centrality =",g)

h=nx.betweenness_centrality (G,48)
print("betweenness centrality =",h)
