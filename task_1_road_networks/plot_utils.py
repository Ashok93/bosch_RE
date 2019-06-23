import matplotlib.pyplot as plt
import networkx as nx

def build_nx_graph(road_network_graph):
    G = nx.DiGraph()

    for node in road_network_graph.nodes:
        for neighbour_info in node.neighbours_info:
            G.add_edge(node.id, neighbour_info["node"].id, weight=neighbour_info["traversal_weight"])
    
    return G

def visualize_road_network(road_network_graph):
    G = build_nx_graph(road_network_graph)

    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=30)

    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    nx.draw_networkx_edge_labels(G, pos, font_size=10, font_family='sans-serif')

    plt.axis('off')
    plt.show()

def visualize_shortest_path(road_network_graph, shortest_path_info):
    G = build_nx_graph(road_network_graph)
    shortest_path = shortest_path_info["path"]

    path_tuples = [(shortest_path[idx],shortest_path[idx+1]) for idx in range(len(shortest_path)-1)]

    s_edges = [(u, v) for (u, v, d) in G.edges(data=True) if (u,v) in path_tuples]
    n_edges = [(u, v) for (u, v, d) in G.edges(data=True) if (u,v) not in path_tuples]

    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=s_edges, arrowstyle='->', arrowsize=30, edge_color='r')

    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    nx.draw_networkx_edge_labels(G, pos, font_size=10, font_family='sans-serif')

    plt.axis('off')
    plt.show()
