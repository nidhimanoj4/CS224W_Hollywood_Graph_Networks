import snap
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import community

def main():
	num_nodes = [] # list of number of nodes in each community
	edges_file = "edges-100k_copy.txt"
	G = nx.read_edgelist(edges_file) # nodetype=int
	print(G.number_of_edges())
	partition = community.best_partition(G)

	size = float(len(set(partition.values())))
	pos = nx.spring_layout(G)
	count = 0.
	for com in set(partition.values()):
		count += 1.
		list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
		print(list_nodes)
		print("\n")
		num_nodes.append(len(list_nodes))
		nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20, node_color = str(count / size))

	plt.hist(num_nodes, log=True)
	plt.xlabel = "Size of Community"
	plt.ylabel = "Number of Communities"

	nx.draw_networkx_edges(G, pos, alpha=0.5)
	plt.show()


main()