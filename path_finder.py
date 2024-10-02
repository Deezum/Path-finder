# ID: 620140477 
# Name: De'Anna-Shanae Beadle 
# Course: COMP3220 2024 Summer Semester

import sys

class PriorityQueue:
    
    def __init__(self):
        self.queue = []
    
    # ** FINISH THIS FUNCTION **
    # Should take minmum element from priority queue and return element                
    def dequeue(self):
        self.organizepriorityqueue()
        return self.queue.pop(0)
     
    # ** FINISH THIS FUNCTION **
    # Should add element to priority queue    
    def enqueue(self, el):
        self.queue.append(el)
    
    
    def isempty(self):
        return len(self.queue) == 0

    def organizepriorityqueue(self):
        for k in range(0, len(self.queue)):
            for e in range(0, len(self.queue) - k - 1):
                if self.queue[e] > self.queue[e + 1]:
                    d = self.queue[e]
                    self.queue[e] = self.queue[e + 1]
                    self.queue[e + 1] = d
                    
# ** ONLY DO THIS IF YOU WANT BONUS MARKS**
# MinHeap allows you to extract elements in O(logn) time
# Feel free to add more helper functions        

class MinHeap:
    
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [None] * (self.maxsize + 1)
        self.Heap[0] = Node('emptynode', None)  
        self.Heap[0].f = -sys.maxsize
        self.FRONT = 1
  
    def isempty(self):
        return self.size == 0

    def parentnode(self, position):
        return position // 2
  
    def rightChild(self, position):
        return (2 * position) + 1
    
    def leftchildnode(self, position):
        return 2 * position
  
    def leafnode(self, position):
        return position * 2 > self.size
  
    def swapnode(self, position1, position2):
        self.Heap[position1], self.Heap[position2] = self.Heap[position2], self.Heap[position1]
  
    def minHeapify(self, position):
        if not self.leafnode(position):
            left = self.leftchildnode(position)
            right = self.rightChild(position)
            smallest = position
            if left <= self.size and self.Heap[left] < self.Heap[smallest]:
                smallest = left
            if right <= self.size and self.Heap[right] < self.Heap[smallest]:
                smallest = right
            if smallest != position:
                self.swapnode(position, smallest)
                self.minHeapify(smallest)
                
    # Start from the last non-leaf node and move up to the root
    def minHeap(self):
        for position in range(self.size // 2, 0, -1):
            self.minHeapify(position)

    # ** FINISH THIS FUNCTION **
    # Adds element to heap        
    def enqueue(self, el):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = el
        currentnode = self.size
        while self.Heap[currentnode] < self.Heap[self.parentnode(currentnode)]:
            self.swapnode(currentnode, self.parentnode(currentnode))
            currentnode = self.parentnode(currentnode)
            
    # ** FINISH THIS FUNCTION **
    # Should take minmum element from heap and return element
    def dequeue(self):
        if self.isempty():
            return
        poppednode = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return poppednode
    
class Node:
    
    def __init__(self, label, parentnode):
        self.label = label
        self.parentnode = parentnode # parentnode node
        self.g = 0 # total path cost from start node
        self.f = 0 # final cost
        self.h = 0 # heuristic distance
    
    # allows you to compare two nodes using <
    def __lt__(self, other):
        if other == (-sys.maxsize):
            return 
        return self.f < other.f                 
  
    def __str__(self):
        return str((self.label, self.f))
    
    def set_heuristic_dist(self, heur):
        self.h = heur
    
    def parentnode2(self):
        return self.parentnode

    def get_label(self):
        #print(self)
        return self.label

    def calc_cost(self, cost):
        self.f = self.parentnode.f + cost

    def set_cost(self):
        self.g = self.h + self.f

# Returns the children/negihbours of a node in the graph including path cost
# e.g. [('A', 20), ('B', 30), ('D', 50)]
# graph - dictionary of nodes and edges
# node - label of node
def get_children(graph, node):
    children = []
    if node in graph.keys():
        children = list(graph[node].items())
    return children

def get_heuristic_dist(heurdict, label):
    if label in heurdict.keys():
        num = heurdict[label]
    return num

# ** FINISH THIS FUNCTION **
# Should return a list representing the path from start to goal
# e.g ['A', 'B', 'G'] would be a possible solution starting from start node A to goal node G
# If there is no path from start to goal, the function should return empty list
# path_graph - dictionary of nodes and edges
# heurist_dist - dictionary of heuristic distance to goal
# start - label for start node e.g. 'A'
# goal - label for goal node e.g. 'G'
# search_type - can be one of UCS, Greedy, A-Start
# fringe_type - data structure used for fring can be one of p_queue, heap

    
def path_find(path_graph, heurist_dist, start, goal, 
              search_type='UCS', fringe_type='p_queue'):
    capacity = len(path_graph)
    visited = []
    path = []
    start_node = Node(start, None)
    
    if fringe_type == 'p_queue':
        fringe = PriorityQueue()
    elif fringe_type == 'heap':
        fringe = MinHeap(capacity)
        
    if search_type == 'Greedy':
        start_node.set_heuristic_dist(get_heuristic_dist(heurist_dist, start))
        start_node.f = start_node.h
    else:
        start_node.f = 0
        
    fringe.enqueue(start_node)
    
    while not fringe.isempty():
        currentnode2 = fringe.dequeue()
        
        if currentnode2.get_label() == goal:
            path.append(goal)
            while currentnode2.parentnode2() is not None:
                parentnode_label = currentnode2.parentnode2().get_label()
                path.insert(0, parentnode_label)
                currentnode2 = currentnode2.parentnode2()
            return path
        
        if currentnode2.get_label() not in visited:
            offspring = get_children(path_graph, currentnode2.get_label())
            for seed in offspring:
                child = Node(seed[0], currentnode2)
                if search_type == 'UCS':
                    child.calc_cost(seed[1])
                elif search_type == 'A-Star':
                    child.calc_cost(seed[1])
                    child.set_heuristic_dist(get_heuristic_dist(heurist_dist, seed[0]))
                    child.set_cost()
                elif search_type == 'Greedy':
                    child.set_heuristic_dist(get_heuristic_dist(heurist_dist, seed[0]))
                    child.f = child.h
                
                if child.get_label() not in visited:
                    fringe.enqueue(child)
            visited.append(currentnode2.get_label())
    
    return path
