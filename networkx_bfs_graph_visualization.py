import networkx as nx
import matplotlib.pyplot as plt


def breadth_first_search(node_map, root):
    visited, bfs_queue = set(), [root]
    while bfs_queue:
        vertex = bfs_queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            bfs_queue.extend(node_map[vertex] - visited)
    return visited


def visualize_graph(graph):
    g = nx.Graph(graph)
    nx.draw(g, with_labels=True)
    plt.show()


# Initialize and visualize graph_one
graph_one = {'A': {'B', 'C'}, 'B': {'A', 'D', 'E'}, 'C': {'A', 'F'}, 'D': {'B'}, 'E': {'B', 'F'}, 'F': {'C', 'E'}}
visualize_graph(graph_one)
print(breadth_first_search(graph_one, 'A'))

graph_two = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"E"}, "E": {"D"}}
visualize_graph(graph_two)
print(breadth_first_search(graph_two, 'A'))
