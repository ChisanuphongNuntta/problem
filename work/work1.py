import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.shortest_paths import weighted

G = nx.Graph()

G.add_edge('Loei Province','Nong Khai Province',weight=234)
G.add_edge('Loei Province','Nong Bua Lamphu Province',weight=99)
G.add_edge('Loei Province','Khon Kaen Province',weight=207)
G.add_edge('Loei Province','Chaiyaphum Province',weight=227)
G.add_edge('Nong Khai Province','Loei Province',weight=234)
G.add_edge('Nong Khai Province','Udon Thani Province',weight=52)
G.add_edge('Nong Khai Province','Bueng Kan Province',weight=135)
G.add_edge('Bueng Kan Province','Nong Khai Province',weight=135)
G.add_edge('Bueng Kan Province','Udon Thani Province',weight=207)
G.add_edge('Bueng Kan Province','Sakon Nakhon Province',weight=195)
G.add_edge('Bueng Kan Province','Nakhon Phanom Province',weight=181)

edge_labels = nx.get_edge_attributes(G,'weight')
print(edge_labels)

pos = nx.spring_layout(G)
nx.draw(G,pos ,with_labels=True,font_color="green",node_size= 2000)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
plt.show()