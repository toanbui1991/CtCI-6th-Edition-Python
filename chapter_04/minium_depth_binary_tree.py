from typing import Optional
from collections import deque
"""
problem: given binary tree find the shortest path
analyze:
    one: the depth of a path is the number of node from root to last node of that path
idea:
    using queue with each element (node, level of that node) to keep track of node we have visied
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # DFS
    def minDepth1(self, root):
        if not root:
            return 0
        if None in [root.left, root.right]: #case node have one leaf or no leaf
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else: #case with two leaf
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    
    # BFS   
    def minDepth(self, root):
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #using bfs
        #idea: using queue to keep track of nodes which we have treverse, each element is (node, level of that node)
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right:
                return level
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))

    def minDepth(self, root):
        #using dfs (this approach is easier to understand with visualization)
        if not root: #case with root is none
            return 0
        if not root.left and not root.right: #case with root but do not have any left
            return 1
        if root.left and not root.right: #move the leaf 
            return 1 + self.minDepth(root.left)
        if root.right and not root.left: #move the leaf
            return 1 + self.minDepth(root.right)
        #case with node have both left and right leaf
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            