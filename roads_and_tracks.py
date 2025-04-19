from typing import List, Tuple

class CityMap:
    def __init__(self, roads: List[Tuple[int, int, int]], tracks: List[Tuple[int, int, int]], friends: List[Tuple[str, int]]):
        """
        Function Description: This initialisation sets up the road graph and locations friends can be picked up from

        Approach Description: The graph is an adjacency list, where the index of the list represents the location and the value is another list containing a list of roads and a tuple with the frind that can be picked up from that location and the amount of tracks used to get there. The graph is then populated with the roads and friends. When each new track is added, it checks if the start of the track contains a friend and if the friend at the destination of the track has a higher distance than one more than the distance of the friend from the start of the tracks location it adds it to the track destinations tuple with a distance incremented by 1.

        Input:
            roads: a list of tuples containing integers representing the roads
            tracks: a list of tuples containing integers representing the tracks
            friends: a list of tuples containing strings representing the friends and the locations they live at

        Output: None

        Time Complexity: O(|R| + |T|), Θ(|R| + |T|), where |R| is the number of roads and |T| is the number of tracks

        Time Complexity Analysis: Given |R| is the number of roads and |T| is the number of tracks
            Finding the maximum location costs O(|R|) as it iterates through all the roads to find the maximum location
            The initialisation of the graph costs O(|L|) as it creates a list of size |L| where |L| is the maximum location
            Populating the graph with roads costs O(|R|) as it iterates through all the roads
            Finding the potential friends to pick up at each location costs O(3*|T|), O(|T|) as it iterates through all the tracks 3 times
            It is stated that "It is possible to get from any location to any other location by driving along some number of roads", meaning the graph is connected, meaning that |R| + 1 >= |L|
            Populating the graph with friends costs O(|F|) as it iterates through all the friends, however it is defined that |F| <= |L|, and due to it being a connected graph |F| <= |R|+1 which therefore makes O(F) <= O(R) therefore making the time complexity O(|R| + |T|)
            
            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity: O(|R|), Θ(|R|), where |R| is the amount of roads, |L| is the amount of locations

        Auxiliary Space Complexity Analysis: Given |R| is the number of roads and |L| is the amount of locations
            The graph requires O(3*|L|) auxilary space as it creates a list of length |L| with 3 elements in each list, therefore its auxiliary space complexity is O(|L|)
            The graph is populated with roads each road at both ends, therefore the auxiliary space complexity of this computation is O(2*|R|) or O(|R|)
            As defined above, |R| + 1 >= |L|, due to the graph being connected, therefore the auxiliary space complexity of the graph is O(|R|)

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Space Complexity: O(|R| + |T|), Θ(|R|), where |R| is the amount of roads and |T| is the amount of tracks

        Space Complexity Analysis: Given |R| is the number of roads, |F| is the amount of friends and |T| is the amount of tracks
            The road input requires O(|R|) space as it creates a list of size |R|
            The track input requires O(|T|) space as it creates a list of size |T|
            The friends input requires O(|F|) space as it creates a list of size |F|
            The space complexity is these plus the auxiliary space complexity of the function which is O(|R|) making the space complexity O(|R| + |T| + |F|), however as defined above |F| <= |R| making the space complexity O(|R| + |T|)

            The big Θ notation is the same as the big O notation as the space complexity is the same in the best and worst case scenarios
        """
        # Find the amount of locations
        self.locations = max(max(roads, key=lambda x: x[0])[0], max(roads, key=lambda x: x[1])[1])

        # Create the graph
        self.graph = [[[],(None, None)] for _ in range(self.locations+1)]

        # Populate the graph with roads
        for u, v, m in roads:
            self.graph[int(u)][0].append((v, m))
            self.graph[int(v)][0].append((u, m))

        # Populate the graph with friends at their home locations
        for friend, location in friends:
            self.graph[location][1] = (friend, 0)

        # Populate the graph with possible friends to pick up at each location, has to be repeated 3 times to ensure that no matter in the input order of the tracks.
        # Using the example tracks, roads and only Grizz from the assignment brief, if the tracks were inputed in order 4 -> 5, 3 -> 4, 1 -> 3, the only pickup location that would be updated would be 3 as the method only checks the immediate next location. Repeating the method 3 times ensures that the all pickup locations are updated correctly.
        for u, v, _ in tracks+tracks+tracks:
            cur_friend = self.graph[u][1]
            next_friend = self.graph[v][1]
            if cur_friend[0] is not None and cur_friend[1] != 2 and (next_friend[0] is None or cur_friend[1]+1 < next_friend[1]):
                self.graph[v][1] = (cur_friend[0], cur_friend[1]+1)

    def dijkstra(self, start: int, construct_path: bool = False, destination: int = 0) -> Tuple[List[int], List[int]]:
        """
        Function Description: This function finds the cost to travel to each location from the start location and optionally constructs the path to the destination

        Approach Description: The function uses Dijkstra's algorithm to find the shortest path to each location from the start location. It uses a min heap to store the distances to each location and the previous location to construct the path if needed. The function then constructs the path to the destination if needed.

        Input:
            start: an integer representing the starting location
            construct_path: a boolean representing whether the path to the destination should be constructed
            destination: an integer representing the destination location

        Output: A tuple containing a list of integers representing the distances to each location from the start location and a list of integers representing the path from the start to the destination

        Time Complexity: O(|R|log(|L|)), Θ(|R|log(|L|)), where |R| is the number of roads and |L| is the number of locations

        Time Complexity Analysis: Given |R| is the number of roads and |L| is the number of locations
            The initialisation of the distances list costs O(|L|) as it creates a list of size |L|
            The initialisation of the min heap costs O(1) as it creates a min heap
            The initialisation of the previous list costs O(|L|) as it creates a list of size |L|
            Inside of the while loop, each call of the get_min function costs O(log(|L|)) as it removes the minimum element from the heap
            The get_min function is called for each road, therefore the time complexity of the while loop is O(|R|log(|L|))
            The path reconstruction costs O(|L|) as it iterates through each location to construct the path
            The time complexity is therefore O(|L|) + O(1) + O(|L|) + O(|R|log(|L|)) + O(|L|)
            O(|L|) <= O(|R|) as defined in the assignmnent brief, therefore the time complexity is O(|R|log(|L|))

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity: O(|L|), Θ(|L|) where |L| is the number of locations

        Auxiliary Space Complexity Analysis: Given |R| is the number of roads and |L| is the number of locations
            The distances list requires O(|L|) auxilary space as it creates a list of length |L|
            The min heap requires O(|L|) auxilary space as it creates an array of length |L|
            The previous list requires O(|L|) auxilary space as it creates a list of length |L|
            The path list requires O(|L|) auxilary space as it creates a list of length |L|
            The time complexity is therefore O(|L|) + O(|L|) + O(|L|) + O(|L|) = O(|L|)

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Space Complexity: O(|L|), Θ(|L|) where |L| is the number of locations

        Space Complexity Analysis: Given |L| is the number of locations
            The start, construct_path, and destination inputs require O(1) space
            The space complexity of the function is the auxiliary space complexity plus O(1) which is O(|L|)

            The big Θ notation is the same as the big O notation as the space complexity is the same in the best and worst case scenarios
        """
        # Initialise the distances and min heap
        distances = [float('inf') for _ in range(self.locations+1)]
        distances[start] = 0
        min_heap = MinHeap(self.locations+1)
        min_heap.add((0, start))
        # Initialise the previous list if the path is to be constructed
        previous = [ None for _ in range(self.locations+1) ] if construct_path else None

        # Dijkstra's algorithm
        while min_heap:
            current_dist, current_loc = min_heap.get_min()

            # Break if the destination is reached and the path is to be constructed
            if current_loc == destination and len(self.graph[current_loc][0]) == 1 and construct_path:
                break

            # Skip if the distance is greater than the current distance
            if current_dist > distances[current_loc]:
                continue

            # Check each neighbor to see if the current path to that neighbor is shorter than the current distance
            for neighbor, weight in self.graph[current_loc][0]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    min_heap.add((distance, neighbor))
                    if construct_path:
                        previous[neighbor] = current_loc

        # Construct the path if needed
        path = []
        while destination is not None and construct_path:
            path.append(destination)
            destination = previous[destination]
        
        return distances, path[::-1]

    def reconstruct_path(self, start: int, stop: int, destination: int) -> List[int]:
        """
        Function Description: This function reconstructs the path from the start to the destination via the stop

        Approach Description: The function uses the dijkstra function to find the path from the start to the stop and the stop to the destination. It then combines the two paths to create the path from the start to the destination.

        Input:
            start: an integer representing the starting location
            stop: an integer representing the stopping location
            destination: an integer representing the destination location

        Output: A list of integers representing the path from the start to the destination via the stop

        Time Complexity: O(|R|log(|L|)), Θ(|R|log(|L|)), where |R| is the number of roads and |L| is the number of locations

        Time Complexity Analysis: Given |R| is the number of roads and |L| is the number of locations
            The dijkstra function is called twice, therefore the time complexity is O(2*|R|log(|L|)) or O(|R|log(|L|))
            The pop function is called on the stop_to_destination list with a time complexity is O(1)
            The time complexity is therefore O(|R|log(|L|))

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity: O(|L|), Θ(|L|), where |L| is the number of locations
        
        Auxiliary Space Complexity Analysis: Given |R| is the number of roads and |L| is the number of locations
            The dijkstra function requires O(|L|) auxilary space as it creates a list of length |L|
            The time complexity is therefore O(|L|) - 1 + O(|L|) = O(|L|)

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Space Complexity: O(|L|), Θ(|L|), where |L| is the number of locations

        Space Complexity Analysis: Given |L| is the number of locations
            The start, stop, and destination inputs require O(1) space
            The space complexity of the function is the auxiliary space complexity plus O(1) which is O(|L|)

            The big Θ notation is the same as the big O notation as the space complexity is the same in the best and worst case scenarios
        """
        start_to_stop = self.dijkstra(start, True, stop)[1]
        start_to_stop.pop()
        stop_to_destination = self.dijkstra(stop, True, destination)[1]
        return start_to_stop + stop_to_destination

    def plan(self, start: int, destination: int) -> Tuple[int, List[int], str, int]:
        """
        Function Description: This function finds the best friend to pick up and the best location to pick them up from

        Approach Description: The function uses Dijkstra's algorithm to find the shortest path to each location from the start location and the destination location. It then iterates through each road to find the friend with the shortest distance to the start location and the destination location. It then returns the time taken to pick up the friend, the path to the destination, the friend to pick up, and the location to pick them up from.

        Input:
            start: an integer representing the starting location
            destination: an integer representing the destination location

        Output: A tuple containing an integer representing the time taken to pick up the friend, a list of integers representing the path to the destination, a string representing the friend to pick up, and an integer representing the location to pick them up from

        Time Complexity: O(|R|log(|L|)), Θ(|R|log(|L|)), where |R| is the number of roads and |L| is the number of locations
        
        Time Complexity Analysis: Given |R| is the number of roads and |L| is the number of locations
            The dijkstra function is called twice, therefore the time complexity is O(2*|R|log(|L|)) or O(|R|log(|L|))
            The time complexity of the for loop is O(|R|) as it iterates through all the roads
            The reconstruct_path function is called with a time complexity of O(|R|log(|L|))
            The time complexity is therefore O(|R|log(|L|))

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity: O(|L|), Θ(|L|), where |L| is the number of locations
        
        Auxiliary Space Complexity Analysis: Given |L| is the number of locations
            min_time, best_friend, best_depth, and best_pickup_location require O(1) auxilary space
            The dijkstra function which is called twice requires O(|L|) auxilary space as it creates a list of length |L| and is therefore O(|L|) + O(|L|) = O(|L|)
            The reconstruct_path function requires O(|L|) auxilary space as it creates a list of length |L|
            The time complexity is therefore O(1) + O(|L|) + O(|L|) = O(|L|)

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Space Complexity: O(|L|), Θ(|L|), where |L| is the number of locations

        Space Complexity Analysis: Given |L| is the number of locations
            The start and destination inputs require O(1) space
            The space complexity of the function is the auxiliary space complexity plus O(1) which is O(|L|)

            The big Θ notation is the same as the big O notation as the space complexity is the same in the best and worst case scenarios
        """
        # Initialise the variables
        min_time = float('inf')
        best_friend = None
        best_distance = float('inf')
        best_pickup_location = None

        # Find the distances from the start to each location and the destination to each location
        start_distances = self.dijkstra(start)[0]
        destination_distances = self.dijkstra(destination)[0]

        # Find the location with the shortest total distance from the start to itself and itself to the destination with a friend available to be picked up. If the time is the same, choose the friend with the smallest distance to travel
        for road_index, road in enumerate(self.graph):
            if road[1][0] is not None and (start_distances[road_index]+destination_distances[road_index] < min_time) or road[1][0] is not None and (start_distances[road_index]+destination_distances[road_index] == min_time and road[1][1] < best_distance):
                min_time = start_distances[road_index]+destination_distances[road_index]
                best_friend = road[1][0]
                best_distance = road[1][1]
                best_pickup_location = road_index

        return (min_time, self.reconstruct_path(start, best_pickup_location, destination), best_friend, best_pickup_location)
    
"""
Adapted from the 1008/2085 MaxHeap implementation
MaxHeap authored by: Brendon Taylor, modified by Massimo Nodin
"""

class MinHeap:

    def __init__(self, max_size: int) -> None:
        self.length = 0
        self.array = [None for _ in range(max_size + 1)]

    def __len__(self) -> int:
        return self.length

    def rise(self, k: int) -> None:
        item = self.array[k]
        while k > 1 and item < self.array[k // 2]:
            self.array[k] = self.array[k // 2]
            k = k // 2
        self.array[k] = item

    def add(self, element) -> bool:
        self.length += 1
        self.array[self.length] = element
        self.rise(self.length)

    def smallest_child(self, k: int) -> int:
        if 2 * k == self.length:
            return 2 * k
        elif 2 * k + 1 > self.length:
            return 2 * k
        else:
            if self.array[2 * k] < self.array[2 * k + 1]:
                return 2 * k
            else:
                return 2 * k + 1

    def sink(self, k: int) -> None:
        item = self.array[k]

        while 2 * k <= self.length:
            min_child = self.smallest_child(k)
            if self.array[min_child] >= item:
                break
            self.array[k] = self.array[min_child]
            k = min_child

        self.array[k] = item

    def get_min(self):
        if self.length == 0:
            raise IndexError('Heap is empty')

        min_elt = self.array[1]
        self.length -= 1
        if self.length > 0:
            self.array[1] = self.array[self.length + 1]
            self.sink(1)
        return min_elt