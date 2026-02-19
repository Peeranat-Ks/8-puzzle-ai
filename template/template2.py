import copy 
import abc
import time
import heapq
import math

# GLOBAL PARAMETERS:
# NOTE Your code goes here!
EMPTY = 0

# List of all cities (fixed order)
CITIES = [
    "Arad", "Zerind", "Oradea", "Sibiu", "Timisoara", "Lugoj", "Mehadia",
    "Dobreta", "Craiova", "Rimnicu Vilcea", "Fagaras", "Pitesti",
    "Bucharest", "Giurgiu", "Urziceni", "Vaslui", "Hirsova",
    "Eforie", "Iasi", "Neamt"
]

# List of undirected edges
EDGES = [
    ("Arad", "Zerind", 75),
    ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118),
    ("Zerind", "Oradea", 71),
    ("Oradea", "Sibiu", 151),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Dobreta", 75),
    ("Dobreta", "Craiova", 120),
    ("Craiova", "Pitesti", 138),
    ("Craiova", "Rimnicu Vilcea", 146),
    ("Sibiu", "Fagaras", 99),
    ("Sibiu", "Rimnicu Vilcea", 80),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Fagaras", "Bucharest", 211),
    ("Pitesti", "Bucharest",101),
    ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Vaslui", 142),
    ("Urziceni", "Hirsova", 98),
    ("Hirsova", "Eforie", 86),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87),
]

# Map each city to its index for easy lookup
CITY_INDEX = {city: i for i, city in enumerate(CITIES)}

def build_successors( edges ):
    '''
    successors = {
        "Arad": [ "Zerind", "Sibiu", "Timisoara" ],
        "Zerind": ["Arad", "Oradea"],
        ...
    }
    '''
    successors = dict()
    for s,t,_ in edges:
        if s in successors:
            successors[ s ].append( t )
        else:
            successors[ s ] = [ t ]
        if t in successors:
            successors[ t ].append( s )
        else:
            successors[ t ] = [ s ]
    return successors

SUCCESSORS = build_successors( EDGES )

STRAIGHT_DIST_BUCHAREST = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Dobreta": 242,
    "Eforie": 161,
    "Fagaras": 178,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 98,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}


def get_map( city_index, edges ):
    # Initialize matrix with None (no edge)
    n = len(CITIES)
    matrix = [[None for _ in range(n)] for _ in range(n)]

    # Set diagonal to 0
    for i in range(n):
        matrix[i][i] = 0
    
    # Fill adjacency matrix
    for a, b, w in edges:
        i, j = city_index[a], city_index[b]
        matrix[i][j] = matrix[j][i] = w
        
    return matrix

class Node:
    def __init__(self, state, acc_cost, depth, action, predecessor, hval = math.inf):
        self.__state = state
        self.__acc_cost = acc_cost
        self.__depth = depth
        self.__action = action
        self.__predecessor = predecessor
        self.__hval = hval

    def get_state(self):
        return self.__state
    
    def get_acc_cost(self):
        return self.__acc_cost
    
    def get_depth(self):
        return self.__depth
    
    def get_action(self):
        return self.__action

    def get_predecessor(self):
        return self.__predecessor
    
    def get_hval(self):
        return self.__hval
    
    def set_hval(self,hval):
        self.__hval = hval
    
    def __lt__(self, other):
        return self.__hval < other.__hval

    def __repr__(self):
        return f"{self.__state=} -- {self.__action=} -- {self.__depth=} -- {self.__hval=}"

class Problem:
    def __init__(self, initial_state, goal_state, map ):
        self.__initial_state = initial_state
        self.__goal_state = goal_state
        self.__map = map

    def get_initial_state( self ): # returns the initial state of the problem:
        return self.__initial_state
    
    def test_goal( self, state ): # return true or false: # NOTE Your code goes here! 
        return state == self.__goal_state

    def step_cost( self, source_node, target_state ): # NOTE Your code goes here!
        return self.__map[CITY_INDEX[source_node.get_state()]][CITY_INDEX[target_state]]

    def get_successor( self, state ): # returns a set of nodes from node: # NOTE Your code goes here!
        successors = []
        if state in SUCCESSORS:
            successors = SUCCESSORS[state]
        
        ans = []
        for s in successors:
            ans.append( ( (state,s), s ) )

        return ans

    def expand( self, node ): # returns a set of nodes:
        successors = [ ]
        for (action, result) in self.get_successor( node.get_state() ):
            s = Node(   result, 
                        node.get_acc_cost() + self.step_cost( node, result ),
                        node.get_depth() + 1,
                        action,
                        node  )
            successors.append( s )
        return successors
    
    def solution( self, node ):
        sol = []
        while node is not None:
            sol.append(node.get_action()) # Insertion at the end of the list.
            # sol.insert(0,node.get_action()) # Insertion at the beginning of the list.
            node = node.get_predecessor()
        sol.reverse()
        return sol

class Fringe(abc.ABC): 
    def add(self, node):
        pass
    def insert_all(self,list_of_nodes):
        pass
    def pop(self):
        pass
    def empty(self):
        pass
    def __len__(self):
        pass

class FIFOFringe(Fringe): # NOTE Your code goes here!
    def __init__(self):
        super().__init__()
        self.__queue = []

    def add(self, node):
        self.__queue.append( node )

    def insert_all(self,list_of_nodes):
        for n in list_of_nodes:
            self.add( n )

    def pop(self):
        if not self.empty():
            n = self.__queue[0]
            self.__queue = self.__queue[1:]
            return n
        else:
            return None

    def empty(self):
        return len(self.__queue) == 0
    
    def __len__(self):
        return len(self.__queue)
    
class LIFOFringe(Fringe): # NOTE Your code goes here!
    def __init__(self):
        super().__init__()
        self.__queue = []

    def add(self, node):
        self.__queue.append( node )

    def insert_all(self,list_of_nodes):
        for n in list_of_nodes:
            self.add( n )

    def pop(self):
        return self.__queue.pop()

    def empty(self):
        return len(self.__queue) == 0
    
    def __len__(self):
        return len(self.__queue)

class HFringe(Fringe): # NOTE Your code goes here!
    def __init__(self):
        super().__init__()
        self.__queue = []

    def __h(self, node ):
        return STRAIGHT_DIST_BUCHAREST[ node.get_state() ] 

    def __f(self,node):
        return self.__h( node ) + node.get_acc_cost()

    def add(self, node):
        # node.set_hval( self.__h( node ) )
        node.set_hval( self.__f( node ) )
        heapq.heappush(self.__queue, ( node.get_hval(), node ))

    def insert_all(self,list_of_nodes):
        for n in list_of_nodes:
            self.add( n )

    def pop(self):
        return heapq.heappop( self.__queue )[1]
    
    def empty(self):
        return len(self.__queue) == 0
    
    def __len__(self):
        return len(self.__queue)

def tree_search( problem, fringe ): # returns a solution, or failure:
    fringe.add( Node( problem.get_initial_state(), 0, 0, 0, None ) ) # Add to the last position of the list.
    while True:
        if fringe.empty():
            return None
        
        node = fringe.pop() # Remove from the front of the list.
        print(f"{len(fringe)=} -- {node=}")
        if problem.test_goal( node.get_state() ):
            print("Solution is found!!!")
            return problem.solution( node )
        else:
            fringe.insert_all( problem.expand( node )  )


initial_state = "Arad"
goal_state = "Bucharest"

current_millis = int(time.time() * 1000)
# print( tree_search( Problem( initial_state,goal_state, get_map( CITY_INDEX, EDGES ) ), FIFOFringe() ) )
# print( tree_search( Problem( initial_state,goal_state, get_map( CITY_INDEX, EDGES ) ), LIFOFringe() ) )
print( tree_search( Problem( initial_state,goal_state, get_map( CITY_INDEX, EDGES ) ), HFringe() ) )
print( f"DFS | Delta:  { ( int(time.time() * 1000) - current_millis ) }" )
