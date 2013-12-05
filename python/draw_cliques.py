import mlh_graph, matplotlib.pyplot as plt, networkx as nx, csv

g = nx.MultiGraph(mlh_graph.g)
cliques = sorted(list(nx.find_cliques(g)), key=len, reverse=True)
plt.figure(0)
nx.draw_networkx(g, nx.spring_layout(g), False, ax=None, node_size=100)
plt.savefig("graph.png")
for i in range(0):
	plt.figure(i)
	h = g.subgraph(cliques[i])
	pos = nx.circular_layout(h)
	nx.draw(h, pos)
	edge_labels=dict([((u,v,),d['weight']) for u,v,d in h.edges(data=True)])
	nx.draw_networkx_edge_labels(h, pos, edge_labels = edge_labels)

community = list(nx.k_clique_communities(g, 5, cliques=nx.find_cliques(g)))[0]
plt.figure()
h = mlh_graph.g.subgraph(community)
pos = nx.circular_layout(h)
nx.draw(h, pos)
plt.savefig("clique_community.png")
edge_labels=dict([((u,v,),d['weight']) for u,v,d in h.edges(data=True)])
#nx.draw_networkx_edge_labels(h, pos, edge_labels = edge_labels)


for edge in h.edges(data=True):
	print edge[0] + "," + edge[1] + "," + str(edge[2]["weight"])


plt.show()
