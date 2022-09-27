def isPalindrome(self, head):
    rev = None
    slow = fast = head
    #find middle point
    while fast and fast.next: #condition to break because fast move two step
        fast = fast.next.next #fast move two steps

        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev

def isPalindrome(self, head):
    fast = head
    slow = head

    #find middle (slow)
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    #reverse the second half
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    #check palindrome
    left, right = head, prev
    while right:
        if left != right:
            return False
        left = left.next
        right = right.next