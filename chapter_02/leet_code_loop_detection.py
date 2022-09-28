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
        #we have one operation ahead of checking condition
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False