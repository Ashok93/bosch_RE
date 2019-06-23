class Node:
    def __init__(self, id):
        self.id = id
        self.neighbours_info = []
    
    def add_neighbour(self, neighbour_node, traversal_weight, orientation):
        neighbour_info = {'node': neighbour_node, 
                          'traversal_weight': traversal_weight.
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