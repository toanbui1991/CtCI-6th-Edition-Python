from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 if value==0 else 0 for value in row[::-1]] for row in image]