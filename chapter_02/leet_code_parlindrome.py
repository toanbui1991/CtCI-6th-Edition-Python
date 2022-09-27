#idea: reverse the first half and find the middle point as the same time. compare reverse first half with the second half.
# reference about palindrome: https://en.wikipedia.org/wiki/Palindromic_prime.
# palindrome: is number or string which we will read from the left is the same as read from the right. it is always with odd length
# in this case: we use two pointer (fast, slow), fast will move with 2 step while slow will move with one step 

def isPalindrome(self, head):
    rev = None #rev variable to hold initial linked list we want to construct
    slow = fast = head #starting point of fast and slow pointer
    while fast and fast.next: #condition to break the loop
        fast = fast.next.next #move fast pointer two step
        # slow.next, rev, slow = rev, slow, slow.next
        rev, rev.next, slow = slow, rev, slow.next #the swap syntax do all signment as the same time
    if fast: #move one more step if linked list with odd lentgh
        slow = slow.next
    #compare between 
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev