class Graph:
    def __init__(self, adjacency):
        # Represent the graph with adjacency lists.
        
        # Nodes are represented with the indices of the adjacency list, i.e.,
        # the number of nodes in the graph is len(adjacency).
        
        # adjacency has n elements, with n the number of nodes. Each element i,
        # corresponding to node i, is itself a list containing the nodes j such
        # that (i, j) is a (directed) edge in the graph.
        self.adjacency = adjacency


class Queue:
    def __init__(self, n):
        self.n = n
        self.head = 0
        self.tail = 0
        self.queue = [None] * (n+1)  # See note 1
        
    def __repr__(self):
        return (
            f"{str(self.queue)}\n"
            f"head: {self.head}, tail: {self.tail}"
        )
        
    def is_empty(self):
        if self.tail == self.head:
            return True
        return False
        
    def enqueue(self, elem):
        if self.tail+1 == self.head:
            raise IndexError("Queue is full")
        
        self.queue[self.tail] = elem
        
        if self.tail == self.n:
            self.tail = 0  # wrap around
        else:
            self.tail += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        dequeued = self.queue[self.head]
        
        if self.head == self.n:
            self.head = 0  # wrap around
        else:
            self.head += 1
        
        return dequeued


def breadth_first_search(g: Graph, s):
    """Conduct a breadth-first search inside g, starting from node s.
    
    It is guaranteed that all nodes v such that v is reachable from s will be
    returned inside the explored set.
    
    Time complexity: linear O(n+e), with n number of nodes of the graph and e 
    number of edges of the graph.
    
    We assume initialization operations to be O(1) in time. Membership check
    and adding to a set both are O(1) in time.
    Each node is enqueued and dequeued exactly once. Enqueue/dequeue is O(1),
    thus queue maintenance is O(n).
    The procedure scans each adjacency list at most once, because it scans the
    adjacency list of a node v only when v is dequeued, which is done only once.
    Since the sum of the lenghts of all adjacency lists is equal to the number
    of edges in the graph, this procedure requires O(e).
    """
    
    # Initialize set of explored nodes
    explored = set(s)
    
    # Initialize a queue where gray nodes are stored, i.e., nodes that may
    # have yet-to-discover neighbors (nodes that have not yet had their
    # adjacency lists fully examined).
    queue = Queue(len(g.adjacency))
    queue.enqueue(s)
    
    while not queue.is_empty():
        v = queue.dequeue()
        
        for w in g.adjacency[v]:  # iterate over v's neighbors
            if w not in explored:
                explored.add(w)
                queue.enqueue(w)
                
    return explored