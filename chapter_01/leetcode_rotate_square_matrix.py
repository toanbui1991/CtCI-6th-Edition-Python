"""
problem: given a square matrix, rotate that matrix 90 degree inplace (without create new matrix)
analyze: the matrix is square, so we can reference to column and row index with on int.
solution:
    one: we move each element in matrix by layer, 
    two: because it is a square matrix, we can calculate the number of layer need to operate
    three: we need to store one temp ofr top left element of given layer and assign to top right element
"""
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        remember we have square matrix
        """
        l, r = 0, len(matrix) - 1
        while l < r: #which layer to move element
            for i in range(r-l): #which element in given layer
                top, bottom = l, r #we have to know this is the squar matrix
                
                #save the topleft
                topleft = matrix[top][l+i]
                #move the bottom left into the top right
                matrix[top][l + i] = matrix[bottom-i][l]
                #move the bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                #move the top right into bottom rigth
                matrix[bottom][r-i] = matrix[top + i][r]
                #move the top left into the top right
                matrix[top + i][r] = topleft
                
            r -= 1
            l += 1