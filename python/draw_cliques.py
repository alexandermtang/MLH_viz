import mlh_graph, matplotlib.pyplot as plt, networkx as nx

g = nx.MultiGraph(mlh_graph.g)
cliques = sorted(list(nx.find_cliques(g)), key=len, reverse=True)
plt.figure(0)
nx.draw_networkx(g, nx.spring_layout(g), False, ax=None, node_size=100)

community = list(nx.k_clique_communities(g, 5, cliques=nx.find_cliques(g)))[0]
plt.figure()
h = mlh_graph.g.subgraph(community)
pos = nx.circular_layout(h)
nx.draw(h, pos)
edge_labels=dict([((u,v,),d['weight']) for u,v,d in h.edges(data=True)])
#nx.draw_networkx_edge_labels(h, pos, edge_labels = edge_labels)

plt.show()
