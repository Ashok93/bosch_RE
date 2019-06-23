import json

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbours_info = []
    
    def add_neighbour(self, neighbour_node, traversal_weight, orientation):
        neighbour_info = {'node': neighbour_node, 
                          'traversal_weight': traversal_weight,
                          'orientation': orientation}
        self.neighbours_info.append(neighbour_info)

    def __str__(self):
        node_str = "Node: " + str(self.id) + "  Neighbours: "
        for neigh_info in self.neighbours_info:
            node_str += str(neigh_info["node"].id) + ' '
        return node_str


class RoadNetworkGraph:
    def __init__(self):
        self.nodes = []
    
    def add_node(self, node):
        self.nodes.append(node)

    def get_node(self, node_id):
        return self.nodes[node_id]

    def __str__(self):
        graph_str = ""
        for node in self.nodes:
            graph_str += node.__str__() + "\n"
        return graph_str


def build_road_network_graph(road_network_string):
    
    try:
        road_network_info = json.loads(road_network_string)
    except ValueError:
        print("Please check for the proper format of the JSON string provided. \n")
        raise

    nodes_info = road_network_info["graph"]["nodes"]
    edges_info = road_network_info["graph"]["edges"]
    
    # Create road network graph instance
    road_network_graph = RoadNetworkGraph()

    # create node instances and add to the road network graph from node information
    for node_info in nodes_info:
        node = Node(node_info["id"])
        road_network_graph.add_node(node)
    
    # retrieve and add neighbours of the nodes from edge information
    for edge_info in edges_info:
        source_node = road_network_graph.get_node(edge_info["source"])
        destination_node = road_network_graph.get_node(edge_info["target"])
        edge_weight = edge_info["weight"]
        is_directed = edge_info["directed"]
        orientation = edge_info["orientation"]

        source_node.add_neighbour(destination_node, edge_weight, orientation)
        if not is_directed:
            destination_node.add_neighbour(source_node, edge_weight, orientation)

    return road_network_graph