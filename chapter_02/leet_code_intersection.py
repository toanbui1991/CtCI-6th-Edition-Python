"""
problem: given head of two singly linked list, find the node in which two linked intersect
problem reference: https://leetcode.com/problems/intersection-of-two-linked-lists/
analyze: two pointer traverl both linked list a and listed b will meet at intersect pont
"""
def getIntersectionNode(self, headA, headB):
    if headA and headB:
        A, B = headA, headB
        while A!=B: #two pointer traverse both a and b untill meet at intersection point 
            A = A.next if A else headB
            B = B.next if B else headA
        return A