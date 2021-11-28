from utils import *
c_size = 100

#adjacency mtx and adjancy list initialization
mtx = np.zeros((c_size, c_size))

#list of elements positions
positions = []
k = 1

for i in range(c_size):
    for j in list(range(k, c_size)):
        pos = [i, j]
        positions.append(pos)
    k = k + 1

position_random = positions.copy()
random.shuffle(position_random)
# 500 random elements
pos_200 = position_random[:200]

# replace elements
for i in pos_200:
    k = i[0]
    m = i[1]
    mtx[k][m] = 1
    mtx[m][k] = 1
# Set format mtx
np.set_printoptions(edgeitems=5, linewidth=100)
vertex = [i for i in range(c_size)]
# Adjacency list
adj_list = {}
for i in range(100):
    res = [i for i, e in enumerate(mtx[i]) if e == 1]
    adj_list.update({i: res})
# Print adjacency list
headers = ['Vertex', 'Adjacent vertices']
data = ([(k, v) for k, v in adj_list.items()])
print(tabulate.tabulate(data[:20], headers=headers))

#graph visualization
plt.figure(figsize=(15, 15))
rows, cols = mtx.nonzero()
edges = list(zip(rows.tolist(), cols.tolist()))
gr = nx.Graph()
gr.add_nodes_from(range(c_size))
gr.add_edges_from(edges)
nx.draw(gr, node_size=200, node_color='lightgreen', with_labels=True)
plt.rcParams.update({'font.size': 40})
plt.show()

connect_component(adj_list, c_size)
breadth_first_search(adj_list, 10, 60)

# Plot
plt.figure(figsize=(15, 10))
rows, cols = mtx.nonzero()
edges = list(zip(rows.tolist(), cols.tolist()))
gr = nx.Graph()
gr.add_edges_from(edges)
node_pos = nx.get_node_attributes(gr, 'pos')
node_col = ['lightgreen' for node in gr.nodes()]
edge_col = ['black' for node in gr.edges()]
nx.draw(gr, node_size=200, node_color=node_col, edge_color=edge_col, with_labels=True)
plt.rcParams.update({'font.size': 20})
plt.show()
