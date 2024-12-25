import networkx as nx

edges = []
with open('data/day_23_data.txt') as f:
    for line in f:
        c1, c2 = line.strip().split('-')
        edges.append((c1, c2))

G = nx.Graph(edges)

ans1 = 0
max_clique = []
for clique in nx.enumerate_all_cliques(G):
    if len(clique) == 3 and 't' in clique[0][0]+clique[1][0]+clique[2][0]:
        ans1 += 1

print(ans1)
print(','.join(sorted(clique))) # last clique is the largest one