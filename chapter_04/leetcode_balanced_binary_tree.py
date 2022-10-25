
"""
problem: check that a binary tree is balanced or not
analyze: 
    - binary tree is a tree which have only two left and right nodes
    - depth of a node is 1 (it self) + max(left node, right node)
    - balance tree is balanced if height(root.left) - height(root.right) <= 1
    - 
idea: 
    - build recursive function which calculate the height of current node 
    with height(node) = 1 + max(node.right, node.left)
    - left == -1 or right == -1 or abs(left -right) > 1 is the condition to check sub tree is unbalance or not.
    If the sub-tree is unbalanced return -1
search variable:
    - current node
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# heigh
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def get_height(node):
            
            if node is None:
                return 0
            
            left_height, right_height = get_height(node.left), get_height(node.right)
            
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return get_height(root) != 1
            