"""
problem: design a MinStack class which retrieve min element in constant time. this also have to have 
solution: for every push using tuple to keep track of current value and the current min
"""
class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if len(self.stack) == 0: 
            self.stack.append((val,val)) #first element in the stack is the min
        else:
            top = self.stack[-1][1] #get the min value in the tuples
            self.stack.append((val,min(top,val))) #Update/Keep the new min 

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1] #Return the min in the top tuple, O(1)