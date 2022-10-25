from typing import List
from collections import defaultdict, deque
"""
problem: given bi-direction graph with n is the number of nodes, edges is path between nodes.
    start node, end node, check that their is a path between start node and end node

breadth first search:
    - breadth first search explore graph in layer fashion.
    - use queue to keep track of what node to be processed next. nodes in queue is the child of child node
    - use visited nodes to check nodes which have been visited. If nodes have been finished continue
    - remove current when add all node which is child of the current node
"""

from collections import defaultdict, deque
#breadth first search solution
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        # Create undirected graph
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        queue = deque([source])
        
        visited = set()
        while queue:
            node = queue.popleft()
            
            visited.add(node)
            
            if node == destination:
                return True
            
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)

#depth first search solution
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        
        def dfs(node, dest):
            if node == dest:
                return True
                
            visited.add(node)
            
            all_paths = []
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                all_paths.append(dfs(neighbor, dest))
			# return true if any of the paths were able to find the value
            return any(all_paths)
        
        return dfs(source, destination)
            
            