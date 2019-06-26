import heapq
from graph_utils import Node, RoadNetworkGraph, build_road_network_graph
from plot_utils import visualize_road_network, visualize_shortest_path

left_turn_cases = {
    "N":["W","NW","SW"],
    "S":["E","NE","SE"],
    "E":["N","NW","NE"],
    "W":["S","SW","SE"],
    "NE":["N","W","NW"],
    "NW":["S","W","SW"],
    "SE":["N","E","NE"],
    "SW":["S","E","SE"]
}

def backtrack_graph(destination_node):
    # backtracking to build the result dictionary
    node = destination_node
    node_id = destination_node.id
    shortest_path_info = {"distance": destination_node.cost_to_node, "path": []}

    if not destination_node.cost_to_node == float('inf'):

        # Loop till the parent node is None for a node
        shortest_path_info["path"].insert(0, node_id)
        while not node.parent == None:
            node_id = node.parent.id
            shortest_path_info["path"].insert(0, node_id)
            node = node.parent
    
    return shortest_path_info

def find_shortest_path_greedy(road_network_string, start_node_id, destination_node_id):

    road_network_graph = build_road_network_graph(road_network_string)
    # visualize_road_network(road_network_graph)

    source_node = road_network_graph.get_node(start_node_id)
    destination_node = road_network_graph.get_node(destination_node_id)
    
    visited_nodes = []
    nodes_queue = []
    source_node.cost_to_node = 0
    heapq.heappush(nodes_queue, source_node)

    while len(nodes_queue):
        curr_node = heapq.heappop(nodes_queue)
        for neighbour_info in curr_node.neighbours_info:
            
            is_left_turn = False
            
            curr_neighbour = neighbour_info["node"]
            traversal_cost = neighbour_info["traversal_weight"]
            orientation = neighbour_info["orientation"]

            if curr_node.prev_heading_orientation is not None and orientation in left_turn_cases[curr_node.prev_heading_orientation]:
                is_left_turn = True
            
            if is_left_turn:
                left_turn_cost = 0.2 * curr_node.prev_edge_weight + 0.1 * traversal_cost + 0.5

            curr_cost = curr_neighbour.cost_to_node
            new_cost = curr_node.cost_to_node + traversal_cost
            new_cost = new_cost + left_turn_cost if is_left_turn else new_cost

            if new_cost < curr_cost:
                curr_neighbour.parent = curr_node
                curr_neighbour.cost_to_node = new_cost
                curr_neighbour.prev_heading_orientation = orientation
                curr_neighbour.prev_edge_weight = traversal_cost

            if curr_neighbour not in visited_nodes and curr_neighbour not in nodes_queue:
                heapq.heappush(nodes_queue, curr_neighbour)
        
        visited_nodes.append(curr_node)
    
    shortest_path_info = backtrack_graph(destination_node)

    # visualize_shortest_path(road_network_graph, shortest_path_info)

    return shortest_path_info


if __name__ == "__main__":
    road_network_string = '{"graph": {"nodes": [{"id": 0}, {"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5}, {"id": 6}, {"id": 7}, {"id": 8}], "edges": [{"directed": false, "source": 0, "target": 3, "weight": 3, "orientation": "S"}, {"directed": false, "source": 1, "target": 4, "weight": 2, "orientation": "S"}, {"directed": false, "source": 2, "target": 3, "weight": 3, "orientation": "E"}, {"directed": true, "source": 3, "target": 1, "weight": 2, "orientation": "NE"}, {"directed": false, "source": 3, "target": 4, "weight": 6, "orientation": "E"}, {"directed": true, "source": 3, "target": 6, "weight": 2, "orientation": "S"}, {"directed": false, "source": 4, "target": 5, "weight": 4, "orientation": "E"}, {"directed": false, "source": 4, "target": 8, "weight": 1, "orientation": "SE"}, {"directed": true, "source": 7, "target": 4, "weight": 3, "orientation": "N"}]}}'
    shortest_path = find_shortest_path_greedy(road_network_string, 2, 5)
    print(shortest_path)