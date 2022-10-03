from typing import List
"""
problem: given matrix m*n which present month of person m at bank n, get the largest money from all person.
solution: using python list or tuple opertor.
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)