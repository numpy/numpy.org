import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines

mpl.rcParams['patch.antialiased'] = True
mpl.rcParams['lines.antialiased'] = True

# create graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 5)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# set node positions and drawing options
pos = {1: (0, 0), 2: (-1, 0.3), 3: (2, 0.17), 4: (4, 0.255), 5: (5, 0.03)}
options = {
    "node_size": 4000,
    "node_color": "white",
    "edge_color": "black",
    "edgecolors": "black",
    "linewidths": 20,
    "width": 20,
}

# draw graph
nx.draw(G, pos, **options)
ax = plt.gca()
ax.margins(0.10)
plt.axis("off")
plt.savefig("sd6-large.svg")

# set the width to 130 pixels with the following command:
# $ rsvg-convert -a -w 160 -f svg sd6-large.svg -o sd6.svg

# if you want to blur the lines
# $ convert sd6-large.svg -blur 0x8 sd6-blur.svg
# $ rsvg-convert -a -w 160 -f svg sd6-blur.svg -o sd6.svg
