from linked_list import LinkedList


def partition(ll, x):
    #because of the bug here, we have to assign current with tail and then head
    #if we do not do it, program may be run forever
    current = ll.tail = ll.head
    print(current) #current start from head
    print(ll.tail)
    #loop through linked list
    while current:
        next_node = current.next #get next node
        current.next = None #unlink current node with next node
        if current.value < x:
            #two operation to have current to head (change current.next = ll.head) and ll.head = current
            current.next = ll.head #link current.next with ll.head
            ll.head = current #assign ll.head = crurent
        else:
            #move current to tail by two operation, change link (ll.tail.next = current), change tail ll.tail = current
            ll.tail.next = current
            ll.tail = current
        current = next_node #update current to

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None


def example():

    ll = LinkedList.generate(10, 0, 99)
    print(ll)
    partition(ll, ll.head.value)
    print(ll)


if __name__ == "__main__":
    example()
