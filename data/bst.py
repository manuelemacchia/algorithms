class Node:
    def __init__(self, left, right, parent, key):
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key


class BinarySearchTree:
    def __init__(self):
        pass
    
    def search(self):
        pass
    
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
        # Call on BST.root to print all nodes.
        
        # The BST property allows us to print out all the keys of a BST in 
        # sorted order by a recursive algorithm.
        # Time complexity: O(n) with n the number of nodes -- after the initial
        # call, the procedure calls itself twice for each node in the tree.
        
        if node:  # node is not None
            self.inorder_tree_walk(node.left)
            print(node.key)
            self.inorder_tree_walk(node.right)
    
    def preorder_tree_walk(self, node):
        # Prints the root before the values in either subtree
        
        if node:
            print(node.key)
            self.preorder_tree_walk(node.left)
            self.preorder_tree_walk(node.right)
            
    def postorder_tree_walk(self, node):
        # Prints the root after the values in either subtree
        
        if node:
            self.postorder_tree_walk(node.left)
            self.postorder_tree_walk(node.right)
            print(node.key)


# Note 1
# The keys in a binary search tree are always stored in such a way as to satisfy
# the *binary-search-tree property*:
# Let x be a node in a BST.
# - If y is a node in the left subtree of x, then y.key <= x.key
# - If y is a node in the right subtree of x, then y.key >= x.key