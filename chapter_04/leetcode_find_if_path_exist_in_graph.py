from typing import List
from collections import defaultdict, deque
"""
problem: given bi-direction graph, 
"""

from collections import defaultdict, deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        #inital check for special case
        if start == end:
            return True
        #using defaultdict to build graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        # return self.bfs(start, end, graph)
        return self.dfs(start, end, set(), graph)
        
    def bfs(self, start, end, graph):
        
        visited = set() #to keep track of nodes have been visited
        queue = deque([start]) #queue to keep track of node have ben check
        while queue: #for each node
            curr = queue.popleft()
            for child in graph[curr]:
                if child in visited:
                    continue
                visited.add(child) #visited all child nodes
                if child == end:
                    return True
                for e in graph[child]: #for each child node, get child of that child node to append to queue
                    queue.append(e)
        return False
    
    def dfs(self, node, end, visited, graph):
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                res = self.dfs(child, end, visited, graph)
                if res:
                    return True
            
            