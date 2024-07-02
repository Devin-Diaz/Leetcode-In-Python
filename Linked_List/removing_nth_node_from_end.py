'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)

    first = dummy
    second = dummy

    for _ in range(n):
        first = first.next
        
    while first.next:
        first = first.next
        second = second.next
        
    second.next = second.next.next
    return dummy.next

'''
Two pointer technique, the trick to this problem is our first pointer will always be n steps ahead
of second pointer. By doing this as we iterate through the linked list we can find the point where
we can use the reference at the current node in our second pointer to point to the node two references
ahead which is where the first pointer is located.
'''

