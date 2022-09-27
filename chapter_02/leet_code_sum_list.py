import pytest
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_number(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next

#build test case for this function using pytest
test_case = [
    ([ListNode(0),ListNode(1)], [ListNode(0),ListNode(1),ListNode(2)], [ListNode(0), ListNode(2), ListNode(2)]),
    ([], [0,1], [0, 1]),
    ([9,9], [1], [0, 0, 1])]
@pytest.mark.parametrize("l1, l2, output", test_case)
def test_add_two_number(l1, l2, output):
    assert add_two_number(l1, l2) == output
