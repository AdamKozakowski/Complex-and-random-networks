
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy

# 1. Visit the following sites and check what kind of data can you acquire and what kind of visualization
# can you make. Download a chosen data set and draw as a network.

# fishy_graph = nx.read_edgelist("./datasets/fish-guppy-familiar-1.edges", nodetype=int, data=(("weight", float),))
# nx.draw_circular(fishy_graph)
# plt.show()

# 2. Go to Stanford Large Network Dataset Collection by Jure Leskovec
# (https://snap.stanford.edu/data/index.html) and download data for the social circles from
# Facebook (ego-Facebook).

fb_graph = nx.read_edgelist("./facebook_combined.txt.gz")
# layout = nx.spring_layout(fb_graph)
# nx.draw(fb_graph, pos=layout,node_size=5, node_color='skyblue', edge_color='gray', alpha=0.5)
# plt.show()

# Calculate for this network:
# (a) Degree distribution P(k)  ... 
# hist = nx.degree_histogram(fb_graph)
# sns.displot(hist, stat="probability",discrete=True)
# plt.xlabel("Degree k")
# plt.ylabel("Probability")

# # ... and an average degree < k >
# avg_deg = sum(dict(fb_graph.degree()).values()) / len(fb_graph)
# print("average degree < k >: ", avg_deg)
# # outupt: average degree < k >: 43.69101262688784
# plt.axvline(x=avg_deg, color='red', linestyle='dashed', linewidth=2, label=f'Average Degree <k> = {avg_deg:.2f}')

# plt.legend()
# plt.show()
# # (b) Distribution of clustering coefficients ... 
# clustering_coefficients = nx.clustering(fb_graph)
# sns.displot(clustering_coefficients, stat="probability")
# plt.xlabel("Clustering Coefficient")
# plt.ylabel("probability")
# plt.show()

# # ... and an average clustering coefficient. 
# avg_clustering_coefficient = sum(clustering_coefficients.values()) / len(clustering_coefficients)
# print("average clustering coefficient: ", avg_clustering_coefficient)
# output: average clustering coefficient: 0.6055467186200862

# (c) Distribution of the shortest paths, 
# Distribution_shortest_path = nx.all_shortest_paths(fb_graph)
# sns.displot(clustering_coefficients, stat="probability")
# plt.xlabel("Clustering Coefficient")
# plt.ylabel("probability")
# plt.show()



# ... the diameter ....
# diameter=nx.diameter(fb_graph)
# print("the diameter: ",diameter)
# output: the diameter:  8

# # ....and the average path length.
# avg_shortest_path_length= nx.average_shortest_path_length(fb_graph)
# print("the average path length: ", avg_shortest_path_length)
# output: the average path length:  3.6925068496963913

### adj matrix ###
# fb_adj_matrix = nx.adjacency_matrix(fb_graph).todense()
# print(fb_adj_matrix)


### csr3 storage type ###

#directed vs undirected links ###