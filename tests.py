from path_finder import path_find

graph = {
	    'A': {'B': 20, 'D': 80, 'G': 95},
	    'B' : {'E': 50, 'F': 10},
	    'C' : {'D': 50, 'H': 20},
	    'D' : {'G': 10},
	    'F' : {'D': 40, 'C': 10}
    }
graph2 = {    
    'A': {'Z': 75, 'T': 118, 'S': 140},
    'B' : {'G': 90, 'U': 85, 'P': 101, 'F': 211},
    'C' : {'P': 138, 'R': 146, 'D': 120},
    'D' : {'M': 75, 'C': 120},
    'E' : {'H': 86},
    'F' : {'S': 99, 'B': 211},
    'G' : {'B': 90},
    'H' : {'U': 98, 'E': 86},
    'I' : {'N': 87, 'V': 92},
    'L' : {'T': 111, 'M': 70},
    'M' : {'L': 70, 'D': 75},
    'N' : {'I': 87},
    'O' : {'Z': 71, 'S': 151},
    'P' : {'R': 97, 'B': 101, 'C': 138},
    'R' : {'S': 80, 'P': 97, 'C': 146},
    'S' : {'A': 140, 'O': 151, 'R': 80},
    'T' : {'A': 118, 'L': 70},
    'U' : {'B': 85, 'H': 98, 'V': 142},
    'V' : {'I': 92, 'U': 142},
    'Z' : {'A': 75, 'O': 71}
}

# straight line distances from node to goal node
# feel free to add in some values for this
heurist_dist = {
    'A': 90,
    'B': 55,
    'C': 55,
    'D': 8,
    'E': 100,
    'F': 45,
    'G': 0,
    'H': 100
}

heurist_dist2 = {
    'A': 366,
    'B': 0,
    'C': 160,
    'D': 242,
    'E': 161,
    'F': 176,
    'G': 77,
    'H': 151,
    'I': 226,
    'L': 224,
    'M': 241,
    'N': 234,
    'O': 380,
    'P': 100,
    'R': 193,
    'S': 253,
    'T': 329,
    'U': 80,
    'V': 199,
    'Z': 374
}

import unittest

class TestPath(unittest.TestCase):

    def test_path1(self):
        path1 = path_find(graph, heurist_dist, 'A', 'G', search_type='A-Star', fringe_type='p_queue')
        self.assertEqual(path1, ['A', 'B', 'F', 'D', 'G'])

    def test_path2(self):
        path2 = path_find(graph2, heurist_dist2, 'A', 'B', search_type='A-Star', fringe_type='p_queue')
        self.assertEqual(path2, ['A', 'S', 'R', 'P', 'B'])

    def test_path3(self):
        path3 = path_find(graph2, heurist_dist2, 'T', 'B', search_type='A-Star', fringe_type='p_queue')
        self.assertEqual(path3, ['T', 'A', 'S', 'R', 'P', 'B'])
    
    def test_path4(self):
        path4 = path_find(graph, heurist_dist, 'F', 'G', search_type='UCS', fringe_type='p_queue')
        self.assertEqual(path4, ['F', 'D', 'G'])
    
    def test_path5(self):
        path5 = path_find(graph2, heurist_dist2, 'A', 'B', search_type='Greedy', fringe_type='p_queue')
        self.assertEqual(path5, ['A', 'S', 'R', 'P', 'B'])
    
    def test_path6(self):
        path6 = path_find(graph2, heurist_dist2, 'T', 'B', search_type='UCS', fringe_type='p_queue')
        self.assertEqual(path6, ['T', 'A', 'S', 'R', 'P', 'B'])
    
    def test_path7(self):
        path7 = path_find(graph2, heurist_dist2, 'O', 'B', search_type='Greedy', fringe_type='p_queue')
        self.assertEqual(path7, ['O', 'S', 'R', 'P', 'B'])
    
    def test_path8(self):
        path8 = path_find(graph2, heurist_dist2, 'O', 'B', search_type='UCS', fringe_type='p_queue')
        self.assertEqual(path8, ['O', 'S', 'R', 'P', 'B'])
    
    def test_path9(self):
        path9 = path_find(graph, heurist_dist, 'A', 'G', search_type='Greedy', fringe_type='p_queue')
        self.assertEqual(path9, ['A', 'G'])
    
    def test_path10(self):
        path10 = path_find(graph2, heurist_dist2, 'D', 'B', search_type='UCS', fringe_type='p_queue')
        self.assertEqual(path10, ['D', 'C', 'P', 'B'])

class TestBonus(unittest.TestCase):
    def test_path1(self):
        path1 = path_find(graph, heurist_dist, 'A', 'G', search_type='A-Star', fringe_type='heap')
        self.assertEqual(path1, ['A', 'B', 'F', 'D', 'G'])

    def test_path2(self):
        path2 = path_find(graph2, heurist_dist2, 'A', 'B', search_type='A-Star', fringe_type='heap')
        self.assertEqual(path2, ['A', 'S', 'R', 'P', 'B'])

    def test_path3(self):
        path3 = path_find(graph2, heurist_dist2, 'T', 'B', search_type='A-Star', fringe_type='heap')
        self.assertEqual(path3, ['T', 'A', 'S', 'R', 'P', 'B'])
    
    def test_path4(self):
        path4 = path_find(graph, heurist_dist, 'E', 'G', search_type='UCS', fringe_type='heap')
        self.assertEqual(path4, [])
    
    def test_path5(self):
        path5 = path_find(graph2, heurist_dist2, 'A', 'B', search_type='Greedy', fringe_type='heap')
        self.assertEqual(path5, ['A', 'S', 'R', 'P', 'B'])

if __name__ == '__main__':
    unittest.main()