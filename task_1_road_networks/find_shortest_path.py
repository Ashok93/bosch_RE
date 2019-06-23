import json
import heapq
from graph_utils import Node, RoadNetworkGraph
from plot_utils import visualize_road_network, visualize_shortest_path

def get_road_network_graph(road_network_string):
    
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


def find_shortest_path(road_network_string, start_node_id, destination_node_id):

    road_network_graph = get_road_network_graph(road_network_string)
    visualize_road_network(road_network_graph)

    source_node = road_network_graph.get_node(start_node_id)
    destination_node = road_network_graph.get_node(destination_node_id)
    
    visited_nodes = []
    nodes_queue = []
    heapq.heappush(nodes_queue, (0, source_node))
    is_destination_reached = False
    
    parent_info = {}
    for node in road_network_graph.nodes:
        parent_info[node.id] = {"parent_node": None, "cost": float('inf')}
    
    parent_info[source_node.id]["cost"] = 0

    while len(nodes_queue) and not is_destination_reached:
        curr_node = heapq.heappop(nodes_queue)[1]
        print(curr_node)
        for neighbour_info in curr_node.neighbours_info:
            curr_neighbour = neighbour_info["node"]
            curr_neighbour_cost = neighbour_info["traversal_weight"]
            curr_best_cost = parent_info[curr_neighbour.id]["cost"]

            new_cost = parent_info[curr_node.id]["cost"] + curr_neighbour_cost
            
            if new_cost < curr_best_cost:
                parent_info[curr_neighbour.id] = {"parent_node": curr_node, "cost": new_cost}
            
            if curr_neighbour not in visited_nodes and curr_neighbour not in [n[1] for n in nodes_queue]:
                heapq.heappush(nodes_queue, (new_cost ,curr_neighbour))
        
        visited_nodes.append(curr_node)
    
    # backtracking to build the result dictionary
    node_id = destination_node.id
    shortest_path_info = {"distance": parent_info[node_id]["cost"], "path": []}

    if not parent_info[destination_node.id]["cost"] == float('inf'):

        # Loop till the parent node is None for a node
        shortest_path_info["path"].insert(0, node_id)
        while not parent_info[node_id]["parent_node"] == None:
            node_id = parent_info[node_id]["parent_node"].id
            shortest_path_info["path"].insert(0, node_id)

    visualize_shortest_path(road_network_graph, shortest_path_info)

    return shortest_path_info

if __name__ == "__main__":
    road_network_string = '{"graph": {"nodes": [{"id": 0}, {"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5}, {"id": 6}, {"id": 7}, {"id": 8}], "edges": [{"directed": false, "source": 0, "target": 3, "weight": 3, "orientation": "S"}, {"directed": false, "source": 1, "target": 4, "weight": 2, "orientation": "S"}, {"directed": false, "source": 2, "target": 3, "weight": 3, "orientation": "W"}, {"directed": true, "source": 3, "target": 1, "weight": 2, "orientation": "NE"}, {"directed": false, "source": 3, "target": 4, "weight": 6, "orientation": "E"}, {"directed": true, "source": 3, "target": 6, "weight": 2, "orientation": "S"}, {"directed": false, "source": 4, "target": 5, "weight": 4, "orientation": "E"}, {"directed": false, "source": 4, "target": 8, "weight": 1, "orientation": "SE"}, {"directed": true, "source": 7, "target": 4, "weight": 3, "orientation": "N"}]}}'
    shortest_path = find_shortest_path(road_network_string, 2, 4)
    print(shortest_path)
