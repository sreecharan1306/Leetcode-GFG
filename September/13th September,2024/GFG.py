#User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,node):
        # Code here
        if node is None:
            return;
        
        temp=node.left;
        node.left=node.right;
        node.right=temp;
        self.mirror(node.left);
        self.mirror(node.right);
