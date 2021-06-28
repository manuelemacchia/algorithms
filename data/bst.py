class Node:
    def __init__(self, left, right, parent, key):
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key


class BinarySearchTree:
    def __init__(self):
        pass
    
    def recursive_search(self, node, k):
        """Search for a node with a given key within a tree.
        
        Recursive algorithm.
        
        Look for key k inside the tree whose root is node.
        Return a pointer to a node with key k if one exists, otherwise None.
        
        Time complexity: O(h), with h the height of the tree. The nodes
        encountered during the recursion form a simple path downward from the
        root of the tree.
        """
        
        if not node or node.key == k:  # node is None or key found
            return node
        
        if k <= node.key:
            return self.recursive_search(node.left, k)
        else:  # k > node.key
            return self.recursive_search(node.right, k)
        
    def iterative_search(self, node, k):
        """Search for a node with a given key within a tree.
        
        Iterative algorithm.
        
        Time complexity: O(h)
        """
        
        while node and node.key != k:  # node is not None and key not found
            if k <= node.key:
                node = node.left
            else:  # k > node.key
                node = node.right
                
        return node  # node is None or key found
    
    def minimum(self):
        pass
    
    def maximum(self):
        pass
    
    def predecessor(self):
        pass
    
    def successor(self):
        pass
    
    def insert(self):
        pass
    
    def delete(self):
        pass
    
    def inorder_tree_walk(self, node):
        """Print out all the keys in sorted order.
        
        The BST property allows us to print out all the keys of a BST in sorted
        order by a recursive algorithm.
        
        Call inorder_tree_walk(BST.root) to print all nodes.
        
        Time complexity: O(n), with n number of nodes -- after the initial call,
        the procedure calls itself twice for each node in the tree.
        """
        
        if node:  # node is not None
            self.inorder_tree_walk(node.left)
            print(node.key)
            self.inorder_tree_walk(node.right)
    
    def preorder_tree_walk(self, node):
        """Print the root before the values in either subtree."""
        
        if node:
            print(node.key)
            self.preorder_tree_walk(node.left)
            self.preorder_tree_walk(node.right)
            
    def postorder_tree_walk(self, node):
        """Print the root after the values in either subtree."""
        
        if node:
            self.postorder_tree_walk(node.left)
            self.postorder_tree_walk(node.right)
            print(node.key)


# Note 1: BST property
# The keys in a binary search tree are always stored in such a way as to satisfy
# the *binary-search-tree property*:
# Let x be a node in a BST.
# - If y is a node in the left subtree of x, then y.key <= x.key
# - If y is a node in the right subtree of x, then y.key >= x.key

# Note 2: duplicate nodes
# The general definition of BST allows the existence of duplicate nodes. In our
# implementation, we put all equal nodes on the left (y.key <= x.key where y
# is a node in the left subtree of x).