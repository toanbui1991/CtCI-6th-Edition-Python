from typing import List
"""
problem: given integer array target and integer n. we have stream of [1, n].
build array witht stack operation. that array will store stack operation (push pop)
push: put element to the top of stack
pop: remove elemet from the top of stack
problem reference: https://leetcode.com/problems/build-an-array-with-stack-operations/
analyze: given integer array target means that it is a sorted array.
solution: we just run simulation we push element to stack check if elemet is equal to target, if equal keep otherwise pop
and then move to the next number in the steam.
"""

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        target_idx, cur_read_num = 0, 1
        
        stack_operation = []
        
        while target_idx < len(target):
            
            # Push current read number
            stack_operation.append('Push')
            
            if target[target_idx] == cur_read_num:
                # Current read number is what we need, keep it and update target index
                target_idx += 1
            
            else:
                # Pop out unnecessary element
                stack_operation.append('Pop')
                
            # current read number always +1 after each iteration
            cur_read_num += 1
            
        return stack_operation

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        target_id, curr_num = 0, 1
        stack_operation = []
        while target_id < len(target):
            stack_operation.append("Push")
            if target[target_id] != curr_num:
                stack_operation.append("Pop")
            else:
                target_id += 1
            curr_num += 1
        return stack_operation
        