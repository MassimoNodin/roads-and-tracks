# City Navigation Planner

This Python module provides tools to plan routes within a city, considering roads, special tracks, and potential friend pickups. It calculates the optimal route to a destination, potentially including a detour to pick up a friend along the way.

## Features

*   Represents city locations, roads, and tracks using a graph structure.
*   Calculates shortest paths using Dijkstra's algorithm.
*   Identifies the best friend to pick up and the optimal pickup location to minimize total travel time.
*   Considers constraints on friend pickups based on track usage.

## `CityMap` Class

The core component is the `CityMap` class.

### Initialization

```python
from roads_and_tracks import CityMap

# Example Data
roads = [(0, 1, 10), (1, 2, 5), (0, 3, 8), (3, 4, 2), (4, 5, 3), (2, 5, 12)]
tracks = [(1, 3, 0), (3, 4, 0), (4, 5, 0)] # Track weights are ignored in current implementation
friends = [("Alice", 0), ("Bob", 5)]

# Create a CityMap instance
city_map = CityMap(roads, tracks, friends)
```

*   **`roads`**: A list of tuples `(location1, location2, time)`. Each tuple represents a bidirectional road between two locations with a given travel time.
*   **`tracks`**: A list of tuples `(location1, location2, ignored_weight)`. These represent special one-way tracks. Friends might become available for pickup at `location2` if they were originally at `location1`, depending on the number of tracks traversed (up to a maximum of 2).
*   **`friends`**: A list of tuples `(friend_name, home_location)`. Specifies the initial location of each friend.

### Planning a Route

The `plan` method calculates the optimal route, potentially including a friend pickup.

```python
start_location = 0
destination_location = 2

time, path, friend_name, pickup_location = city_map.plan(start_location, destination_location)

print(f"Total Time: {time}")
print(f"Path: {path}")
print(f"Friend to Pick Up: {friend_name}")
print(f"Pickup Location: {pickup_location}")
```

*   **Input:**
    *   `start`: The integer ID of the starting location.
    *   `destination`: The integer ID of the destination location.
*   **Output:** A tuple containing:
    *   `time`: The minimum total time required for the journey (start -> pickup -> destination).
    *   `path`: A list of location IDs representing the optimal path.
    *   `friend_name`: The name of the friend to pick up (or `None` if no friend is picked up).
    *   `pickup_location`: The location ID where the friend is picked up (or `None`).

The algorithm determines which friend (if any) to pick up and at which location (which might be their home or a location reachable via tracks) results in the lowest overall travel time from the start to the destination. If multiple friend pickups result in the same minimum time, the one requiring fewer track traversals from the friend's home is preferred.

## Dependencies

*   Python 3.x

## How it Works

1.  **Graph Construction:** The `__init__` method builds an adjacency list representation of the city. Roads are added as bidirectional edges with associated travel times.
2.  **Friend Propagation:** It calculates potential pickup locations for friends based on the track network. A friend initially at location `A` might be available for pickup at location `B` if there's a path `A -> ... -> B` using 1 or 2 tracks.
3.  **Shortest Paths:** Dijkstra's algorithm (implemented within the `dijkstra` method) is used to find the shortest travel times from the `start` location to all other locations and from the `destination` location to all other locations.
4.  **Optimal Pickup Calculation:** The `plan` method iterates through all locations where a friend could potentially be picked up. For each potential pickup `P` of friend `F`, it calculates the total time: `time(start -> P) + time(P -> destination)`. It selects the friend and pickup location that minimize this total time, considering the track traversal constraint as a tie-breaker.
5.  **Path Reconstruction:** Once the optimal pickup location `P` is found, the path is reconstructed by combining the shortest path from `start` to `P` and the shortest path from `P` to `destination`.
