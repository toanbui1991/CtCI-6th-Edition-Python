from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #to reverse a linked list for each step, we have to curr.next = prev
        prev = None #tail.next is None
        curr = head #start at head node
        while curr: #loop through untill meet the last node
            #get the next node first otherwise it will change the sequence unexpectedly
            curr.next, prev, curr = prev, curr, curr.next #using in line swap
        return prev

# Recursively    
class Solution:
    def reverseList(self, head: ListNode, prev=None) -> ListNode:
        if not head: #condition to break recursion
            return prev
        #each recurstion -> get next node, change curr.next = prev
        next_node = head.next
        head.next = prev
        return self.reverseList(next_node, head) #this will update current node and nex prev node