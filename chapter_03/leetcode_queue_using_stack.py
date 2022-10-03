"""
problem: implement first in first out queue with two stacks with functions
    void push(int x): put the element at the end of the queue
    int pop(): remove element from front and return it
    int peek(): return element at the front of the queue
    boolean empty(): return True if empty otherwise False
analyze: how to use two stacks in this problem
    one: first in first out queue, but stack is last in first out.
    two: therefore we need two stacks, int and out if push use int if pop empty in and move to out and pop the last element.
"""

class MyQueue:

    def __init__(self):
        self.stPush = []
        self.stPop = []

    def push(self, x: int) -> None:
        self.stPush.append(x)
        
    def pop(self) -> int:
        self.peek()
        return self.stPop.pop() #pop the first in first out

    def peek(self) -> int:
        if len(self.stPop) == 0: #check empty
            while self.stPush: #revert push
                self.stPop.append(self.stPush.pop())
        return self.stPop[-1] #get the last element of stack pop is the first elemnt of push

    def empty(self) -> bool:
        return len(self.stPop) + len(self.stPush) == 0