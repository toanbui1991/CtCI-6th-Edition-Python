"""
problem: given the linked list, check if that linked list exist a loop or not
idea: if exist a loop in the linked list fast pointer will catch up with slow pointer eventially.
"""
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        #we have one operation ahead of checking condition, because we start with slow and slow is true
        #because, we move two step as a time we have to check two condition for
        #fast is None means that we have been two step from tail
        #fast.next is None means that we have been one step from tail
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False