"""
problem: compute sum of diagonal of a square matrix.
analyze: for each row we text two element of the diagonal. 
    two: if square matrix size n such that n // 2 = 1 then the diagonal go to the middle twice
"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        result = 0
        for i in range(size):
            result += mat[i][i] + mat[i][size -1 - i] #index is the most important part of string array or maxtrix problem
        middle, remain = divmod(size, 2)
        if remain == 1: #if size is odd the diagonal will go to the middle point twice
            result -= mat[middle][middle]
        return result