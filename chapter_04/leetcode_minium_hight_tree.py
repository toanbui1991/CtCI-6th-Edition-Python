"""
problem: given tree, find nodes which will return tree with minium height
    - problem reference: https://leetcode.com/problems/minimum-height-trees/
    - problem descriptoin: a tree is present of n (number of node), edges (list of list) present edges
analyze:
    1, a tree is undirected graph in which any two vertices are connected by exactly one path
    2, any connected graph who has n nodes with n-1 edges is a tree
    3, the degree of vertex of a graph is the number of edge incident to that vertext
    4, a leaf is a vertex with degree on. an internal vertex is vertex with degree at least 2
    5, a path graph is a tree with two or more vertices that is not branched at all
    6, a tree is called rooted tree if one vertex have been desinated as root
    7, the height of a rooted tree is the number of edge on the logest
idea:
    tream layer of leav until find the middle.
note:
    1. leaf node is a node which only have one edge connected to it
    2. three is undirected graph, only have one edge between nodes
    3. team leaf node process will return root tree which in it's mininum height
    4. why continue with condition total nodes > 2. because if remaining two nodes either of them can be root
    5. immport search varialbe: 
        - number of remaining nodes to break the loop
        - current leaf node. 
"""
from collections import defaultdict
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
               
        total_node_count = n
        
        if total_node_count == 1:
            # Quick response for one node tree
            return [0]
        # build adjacency matrix, use set in this case which help you find leave
        adj_matrix = defaultdict( set )
        for src_node, dst_node in edges:
            adj_matrix[src_node].add( dst_node )
            adj_matrix[dst_node].add( src_node )
            
            
        # get leaves node whose degree is 1
        leave_nodes = [ node for node in adj_matrix if len(adj_matrix[node]) == 1 ]
        
        
        # keep doing leave nodes removal until total node count is smaller or equal to 2
        while total_node_count > 2:
            
            total_node_count -= len(leave_nodes)
            #try to find each leav node    
            leave_nodes_next_round = []
            
            # leave nodes removal
            for leaf in leave_nodes:
                #remove leaf, leaf only have one neighbor
                neighbor = adj_matrix[leaf].pop() #leaf have only one connect node
                adj_matrix[neighbor].remove( leaf )
                #check if neight is leaf to build list of new leaf
                if len(adj_matrix[neighbor]) == 1:
                    leave_nodes_next_round.append( neighbor )
                    
            leave_nodes = leave_nodes_next_round
        
        # final leave nodes are root node of minimum height trees
        return leave_nodes