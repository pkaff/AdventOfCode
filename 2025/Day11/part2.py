import networkx as nx
import matplotlib.pyplot as plt
input = {line.split(':')[0]: line.split(':')[1].strip().split() for line in open("input.txt", "r").readlines()}
start = 'svr'
end = 'out'
G = nx.DiGraph(input)
# color_map = []
# for node in G:
#     if str(node) == 'svr' or str(node) == 'out':
#         color_map.append('green')
#     elif str(node) == 'fft' or str(node) == 'dac':
#         color_map.append('red')
#     else:
#         color_map.append('blue')
# nx.draw(G, node_color=color_map, with_labels=True)
# plt.savefig("graph.png", dpi=1000)
# plt.show()
# exit()
# print(input)
# valid_paths = 0
# for path in nx.all_simple_paths(G, source='svr', target='out'):
#     valid_paths += 1
# print(valid_paths)
paths = []
for to_visit in ['fft', 'dac']:
    desc = nx.descendants(G, to_visit)
    anc = nx.ancestors(G, to_visit)

    paths.extend([path for p in desc for path in nx.all_simple_paths(G, to_visit, p)])
    paths.extend([path for p in anc for path in nx.all_simple_paths(G, p, to_visit)])

def remove_edges(G, node=0):
  desc = nx.descendants(G, node)
  anc = nx.ancestors(G, node)
  nodes = anc.union(desc).union({node})
  Q = nx.DiGraph()
  for i, j in G.edges:
    # remove edges with either source or target not in nodes
    if (i not in nodes) or (j not in nodes):
      continue
    # remove edges immediately connecting ancestors to descendants
    if (i in anc) and (j in desc):
      continue
    Q.add_edge(i,j)
  return Q  
