import copy 
import abc
import time
import heapq
import math

# GLOBAL PARAMETERS:
# NOTE Your code goes here!
EMPTY = 0

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
    def __init__(self, initial_state):
        self.__initial_state = initial_state

    def get_initial_state( self ): # returns the initial state of the problem:
        return self.__initial_state
    
    def test_goal( self, state ): # return true or false: # NOTE Your code goes here! 
        # Look for empty cells:
        for r in state:
            for c in r:
                if c == EMPTY:
                    return False
        # Look for violation of the rule:
        # ... for rows:
        for r in state:
            freq = [ 0 ] * len( r )
            for c in r:
                freq[ c - 1 ] += 1
            if max(freq) > 1:
                return False
        # ... for columns:
        for c_idx in range( len( state ) ):
            c = [ state[i][c_idx] for i in range(len(state)) ]
            freq = [ 0 ] * len( c )
            for r in c:
                freq[ r - 1 ] += 1
            if max(freq) > 1:
                return False
        return True

    def step_cost( self, node ): # NOTE Your code goes here!
        return 1 

    def get_successor( self, state ): # returns a set of nodes from node: # NOTE Your code goes here!
        successor = []
        # Get the indexes of the next empty cell:
        for r_idx in range( len( state ) ):
            for c_idx in range( len( state ) ):
                if state[r_idx][c_idx] == EMPTY:
                    for v in range( 1, len( state ) + 1 ):
                        copy_state = copy.deepcopy( state )
                        copy_state[r_idx][c_idx] = v
                        successor.append( ( (r_idx,c_idx,v), copy_state ) )
        return successor

    def expand( self, node ): # returns a set of nodes:
        successors = [ ]
        for (action, result) in self.get_successor( node.get_state() ):
            s = Node(   result, 
                        node.get_acc_cost() + self.step_cost( node ),
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

    def __h0( self, node ):
        '''It counts the number of empty slots'''
        state = node.get_state()
        number_of_zeros = 0
        for r_idx in range( len( state ) ):
            for c_idx in range( len( state ) ):
                if state[r_idx][c_idx] == EMPTY:
                    number_of_zeros += 1
        return number_of_zeros
    
    def __h1( self, node ):
        '''It counts the horizontal and vertical repetitions.'''
        state = node.get_state()
        number_of_repetitions = 0
        # Look for violation of the rule:
        # ... for rows:
        for r in state:
            freq = [ 0 ] * len( r )
            for c in r:
                freq[ c - 1 ] += 1
            number_of_repetitions += sum([ 1 for x in freq if x > 1 ])
        # ... for columns:
        for c_idx in range( len( state ) ):
            c = [ state[i][c_idx] for i in range(len(state)) ]
            freq = [ 0 ] * len( c )
            for r in c:
                freq[ r - 1 ] += 1
            number_of_repetitions += sum([ 1 for x in freq if x > 1 ])
        return number_of_repetitions

    def __h(self, node):
        # return self.__h0(node)
        # return self.__h1(node)
        return max( self.__h0(node), self.__h1(node) )

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


initial_state = [
    [1,2,0,3],
    [3,0,2,4],
    [0,0,0,2],
    [2,0,0,0]
]

current_millis = int(time.time() * 1000)
# print( tree_search( Problem( initial_state ), FIFOFringe() ) )
# print( tree_search( Problem( initial_state ), LIFOFringe() ) )
print( tree_search( Problem( initial_state ), HFringe() ) )
print( f"DFS | Delta:  { ( int(time.time() * 1000) - current_millis ) }" )
