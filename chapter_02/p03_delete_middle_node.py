from linked_list import LinkedList

#delete middle node
#to delete a middle note we have two do two peration
#one: node.value = node.next.value 
#two update reference to the next node: node.next = node.next.next
def delete_middle_node(node):
    node.value = node.next.value #update node value
    node.next = node.next.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    middle_node = ll.add(5)
    ll.add_multiple([7, 8, 9])

    print(ll)
    delete_middle_node(middle_node)
    print(ll)
