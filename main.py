Creating an eco-router for finding the most eco-friendly paths involves a combination of geographic data handling, optimization algorithms, and possibly machine learning if we decide to improve over time based on real-world feedback. However, for our initial simplified version, we’ll focus purely on optimizing routes to minimize distance and estimated fuel/carbon emissions. We will use NetworkX to model our routes and Dijkstra’s algorithm to find the shortest path by distance and weight such as elevation or road type.

To fully flesh out this project requires a fair amount of setup, including data on routes and emissions, but I will create a simplified version that you can expand upon. We’ll assume you have some kind of map data represented as a graph with estimated emission weights.

Here’s a Python program using NetworkX:

```python
import networkx as nx
import random

def generate_random_graph(num_nodes: int) -> nx.Graph:
    """Generate a random graph simulating a road network."""
    graph = nx.Graph()
    for i in range(num_nodes):
        graph.add_node(i)
    
    # Randomly connect nodes and add an 'emission' and 'distance' attribute for edges
    for _ in range(num_nodes * 2):
        u, v = random.sample(range(num_nodes), 2)
        if not graph.has_edge(u, v):
            # Randomly determine weights for emissions and distances
            distance = random.uniform(1.0, 10.0)  # Simulate some distance in km
            emission = distance * random.uniform(0.5, 2.5)  # Simulate emission factor
            graph.add_edge(u, v, emission=emission, distance=distance)
    return graph

def eco_route(graph: nx.Graph, start_node: int, end_node: int) -> tuple:
    """Find the eco-friendly route between start_node and end_node."""
    try:
        # Use Dijkstra's algorithm for a weighted graph and emissions as the weight.
        path = nx.dijkstra_path(graph, start_node, end_node, weight='emission')
        emissions = nx.dijkstra_path_length(graph, start_node, end_node, weight='emission')
        distance = nx.dijkstra_path_length(graph, start_node, end_node, weight='distance')
        return path, emissions, distance
    except nx.NetworkXNoPath:
        print("No available path exists between the given nodes.")
        return None, None, None

def main():
    # Simulate a road network graph with nodes and edges
    num_nodes = 10
    graph = generate_random_graph(num_nodes)

    start_node = 0
    end_node = 9

    print(f"Finding eco-friendly route from node {start_node} to node {end_node}.")
    
    path, emissions, distance = eco_route(graph, start_node, end_node)
    
    if path is not None:
        print(f"Eco-friendly path: {path}")
        print(f"Total emissions for this path: {emissions:.2f}")
        print(f"Total distance for this path: {distance:.2f} km")
    else:
        print("Could not find an eco-friendly path between the specified nodes.")

if __name__ == "__main__":
    main()
```

### Explanation:

1. **Graph Generation**: We create a mock-up of a road network using a random graph. Each edge in the graph represents a road connecting two nodes with attributes for distance and emission.

2. **Route Finding**: The `eco_route` function uses Dijkstra's algorithm to find the shortest path based on emissions. If no path exists, it handles that situation gracefully.

3. **Main Function**: This sets up the scenario, calls the route finding function, and prints out the results.

This code represents a basic starting point. In a real-world application:

- **Real Data**: You would replace the random graph with real geographic data.
- **Additional Weights**: Consider other factors like traffic, road type, or vehicle efficiency in the emissions calculation.
- **Dynamic Updates**: Incorporate real-time data inputs for traffic and environmental conditions.
- **User Interface**: Build a web or mobile interface for user interaction.

This setup provides the skeleton necessary for a more complex eco-routing tool.