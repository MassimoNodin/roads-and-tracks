import unittest
from assignment1 import CityMap

class TestCityMap(unittest.TestCase):
    
    def setUp(self):
        # Common setup for tests using the initial CityMap
        self.roads1 = [(0,1,4), (0,3,2), (2,0,3), (3,1,2), (2,4,2), (4,5,3)]
        self.tracks1 = [(1,3,3), (3,4,2), (4,3,2), (4,5,4), (5,1,6)]
        self.friends1 = [("Grizz", 1), ("Ice", 3)]
        self.myCity1 = CityMap(self.roads1, self.tracks1, self.friends1)
        
        # Setup for the second set of inputs
        self.roads2 = [(0,1,4), (0,3,2), (2,0,3), (3,1,2), (2,4,2), (4,5,3)]
        self.tracks2 = [(1,3,4), (3,4,2), (4,3,2), (4,5,1), (5,1,6)]
        self.friends2 = [("Grizz", 1), ("Ice", 3)]
        self.myCity2 = CityMap(self.roads2, self.tracks2, self.friends2)
        
        # Setup for the third set of inputs
        self.roads3 = [(0,1,4), (0,3,2), (2,0,3), (3,1,2), (2,4,2), (2,5,2)]
        self.tracks3 = [(1,3,4), (3,4,2), (4,5,1), (5,1,6)]
        self.friends3 = [("Grizz", 1)]
        self.myCity3 = CityMap(self.roads3, self.tracks3, self.friends3)
    
    def test_example_1_1(self):
        # Example 1.1, simple example
        result = self.myCity1.plan(start=2, destination=5)
        self.assertEqual(result, (5, [2,4,5], "Ice", 4))
    
    def test_example_1_2(self):
        # Example 1.2, meeting the friend at destination
        result = self.myCity1.plan(start=0, destination=4)
        self.assertEqual(result, (5, [0,2,4], "Ice", 4))
    
    def test_example_1_3_solution(self):
        # Example 1.3, possible solution 2
        result = self.myCity1.plan(start=2, destination=1)
        self.assertTrue(result == (7, [2,0,3,1], "Ice", 3) or result == (7, [2,0,1], "Grizz", 1))
    
    def test_example_1_4(self):
        # Example 1.4, going beyond the destination
        result = self.myCity1.plan(start=2, destination=0)
        self.assertEqual(result, (7, [2,0,3,0], "Ice", 3))
    
    def test_example_2_1(self):
        # Example 2.1, the less train, the better
        result = self.myCity2.plan(start=2, destination=5)
        self.assertEqual(result, (5, [2,4,5], "Ice", 4))
    
    def test_example_2_2(self):
        # Example 2.2, a more complex scenario
        result = self.myCity3.plan(start=2, destination=5)
        self.assertEqual(result, (6, [2,4,2,5], "Grizz", 4))

    def test_my_example_1(self):
        roads = [(0,1,2)]
        tracks = [(0,1,3)]
        friends = [('Sarah', 0)]
        myCity = CityMap(roads, tracks, friends)

        got = myCity.plan(start=1, destination=1)
        expected = (0, [1], 'Sarah', 1)
        self.assertEqual(got, expected)
    
    def test_my_example_2(self):
        roads = [(0,1,2), (1,2,3), (2,3,4)]
        tracks = [(0,2,3),(2,3,4),(3,1,3)]
        friends = [('Roberta Sparrow', 0)]
        myCity = CityMap(roads, tracks, friends)

        got = myCity.plan(start=1, destination=1)
        expected = (4, [1,0,1], 'Roberta Sparrow', 0)
        self.assertEqual(got, expected)
    
    def test_my_example_3(self):
        roads = [(0,1,2), (1,2,3)]
        tracks = [(0,2,3)]
        friends = [('RB', 2)]
        myCity = CityMap(roads, tracks, friends)

        got = myCity.plan(start=1, destination=1)
        expected = (6, [1,2,1], 'RB', 2)
        self.assertEqual(got, expected)
    
    def test_my_example_4(self):
        roads = [(0,1,1), (1,2,1), (2,3,1), (3,4,1), (4,5,1)]
        tracks = []
        friends = [('Jessica Hyde', 5)]
        myCity = CityMap(roads, tracks, friends)

        got = myCity.plan(start=1, destination=1)
        expected = (8, [1,2,3,4,5,4,3,2,1], 'Jessica Hyde', 5)
        self.assertEqual(got, expected)
    
    def test_my_example_5(self):
        roads = [(0,1,1), (1,2,1), (2,3,1), (3,4,1), (4,5,1)]
        tracks = [(0,5,10), (1,3,1), (2,5,1)]
        friends = [('Minnie', 0), ('Mouse', 1)]
        myCity = CityMap(roads, tracks, friends)

        got = myCity.plan(start=5, destination=5)
        expected = (0, [5], 'Minnie', 5)
        self.assertEqual(got, expected)
    
    def test_my_example_6(self):
        roads = [(0,1,1), (1,2,1), (2,3,1), (3,4,1), (4,5,1), (0,5,10)]
        tracks = []
        friends = [('Ariel', 5)]
        myCity = CityMap(roads, tracks, friends)

        got = myCity.plan(start=0, destination=5)
        expected = (5, [0,1,2,3,4,5], 'Ariel', 5)
        self.assertEqual(got, expected)

    def test_example_1(self):
        roads = [(3, 4, 2), (4, 0, 5), (2, 4, 2), (0, 2, 2), (1, 0, 3)]
        tracks = []
        friends = [('Seulgi', 4)]
        myCity = CityMap(roads, tracks, friends)

        path = myCity.plan(start=0, destination=1)
        expected = (11, [0, 2, 4, 2, 0, 1], 'Seulgi', 4)
        error_message = f'Current wrong path: {path}'
        self.assertEqual(path, expected, error_message)

        path = myCity.plan(start=3, destination=1)
        expected = (9, [3, 4, 2, 0, 1], 'Seulgi', 4)
        error_message = f'Current wrong path: {path}'
        self.assertEqual(path, expected, error_message)

        path = myCity.plan(start=4, destination=4)
        expected = (0, [4], 'Seulgi', 4)
        error_message = f'Current wrong path: {path}'
        self.assertEqual(path, expected, error_message)

        path = myCity.plan(start=4, destination=3)
        expected = (2, [4, 3], 'Seulgi', 4)
        error_message = f'Current wrong path: {path}'
        self.assertEqual(path, expected, error_message)
        
        path = myCity.plan(start=2, destination=1)
        expected = (9, [2, 4, 2, 0, 1], 'Seulgi', 4)
        error_message = f'Current wrong path: {path}'
        self.assertEqual(path, expected, error_message)

        path = myCity.plan(start=1, destination=0)
        expected = (11, [1, 0, 2, 4, 2, 0], 'Seulgi', 4)
        error_message = f'Current wrong path: {path}'
        self.assertEqual(path, expected, error_message)

    def test_example_2(self):
        roads = [(4, 0, 3), (0, 2, 4), (2, 3, 2), (4, 2, 2), (3, 0, 4), (1, 2, 1)]
        tracks = [(2, 3, 3), (4, 0, 1), (0, 1, 2)]
        friends = [('Winter', 0), ('Joy', 3), ('Irene', 2), ('Karina', 4)]
        myCity = CityMap(roads, tracks, friends)

        path = myCity.plan(start=4, destination=0)
        expected = [(3, [4, 0], 'Winter', 0), (3, [4, 0], 'Karina', 4)]
        error_message = f'Current wrong path: {path}'
        self.assertIn(path, expected, error_message)

        path = myCity.plan(start=1, destination=1)
        expected = (0, [1], 'Winter', 1)
        error_message = f'Current wrong path: {path}'
        self.assertEqual(path, expected, error_message)

    def test_example_3(self):
        roads = [(1, 0, 5), (4, 0, 5), (2, 4, 4), (0, 3, 4), (4, 1, 5)]
        tracks = [(1, 3, 1), (1, 0, 3), (4, 0, 2), (1, 4, 3)]
        friends = [('Winter', 1), ('Bebe', 4), ('Wendy', 3)]
        myCity = CityMap(roads, tracks, friends)

        path = myCity.plan(start=0, destination=0)
        expected = [(0, [0], 'Bebe', 0), (0, [0], 'Winter', 0)]
        error_message = f'Current wrong path: {path}'
        self.assertIn(path, expected, error_message)

        path = myCity.plan(start=0, destination=3)
        expected = (4, [0, 3], 'Wendy', 3)
        error_message = f'Current wrong path: {path}'
        self.assertEqual(path, expected, error_message)

        path = myCity.plan(start=1, destination=0)
        expected = (5, [1, 0], 'Winter', 1)
        error_message = f'Current wrong path: {path}'
        self.assertEqual(path, expected, error_message)

    def test_example_4(self):
        roads = [(1, 0, 1), (1, 3, 3), (3, 0, 1), (2, 4, 1), (1, 2, 5), (0, 4, 3)]
        tracks = [(2, 0, 5), (4, 0, 4), (0, 1, 3), (4, 1, 5)]
        friends = [('Winter', 4), ('CH', 2)]
        myCity = CityMap(roads, tracks, friends)
    
        path = myCity.plan(start=1, destination=3)
        expected = [(2, [1, 0, 3], 'Winter', 1), (2, [1, 0, 3], 'Winter', 0), (2, [1, 0, 3], 'CH', 0)]
        error_message = f'Current wrong path: {path}'
        self.assertIn(path, expected, error_message)

        path = myCity.plan(start=2, destination=0)
        expected = [(4, [2, 4, 0], 'Winter', 4), (4, [2, 4, 0], 'CH', 2)]
        error_message = f'Current wrong path: {path}'
        self.assertIn(path, expected, error_message)
        
        path = myCity.plan(start=4, destination=4)
        expected = (0, [4], 'Winter', 4)
        error_message = f'Current wrong path: {path}'
        self.assertEqual(path, expected, error_message)
        
if __name__ == '__main__':
    unittest.main()