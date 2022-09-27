from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 #keep trac to total value of current node
        root = curr = ListNode(0) #start construct linked list
        while l1 or l2 or carry: #loop through every nodes and condition to break the loop
            if l1:
                carry += l1.val
                l1 = l1.next #move to next node
            if l2:
                carry += l2.val
                l2 = l2.next #move to next node
            carry, val = divmod(carry, 10) #use divmode(a,b) equal with a//b , a % b
            curr.next = ListNode(val) #assign referenc link
            curr = curr.next #move to next node
            
        return root.next #return the next node of dummy root node

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next