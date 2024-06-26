'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

TEST CASES:

Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Input: list1 = [], list2 = [1,2]
Output: [1,2]
'''

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
    starting_node = ListNode(1)
    new_head = starting_node

    while list1 and list2 != None:
        if list1.val < list2.val:
            starting_node.next = list1
            list1 = list1.next
        else:
            starting_node.next = list2
            list2 = list2.next
            
        starting_node = starting_node.next

    if list1 != None:
        starting_node.next = list1
        
    if list2 != None:
        starting_node.next = list2
        
    return new_head.next

'''
O(N) TC and O(1) SC. We make 2 dummy nodes with a random value. This dummy node is what we use to construct our merged list.
When we return our answer that being the head of our merged list, we could just do the next reference of the dummy node.
As we iterate through our list1, and list2 inputs, we check which value is less, and our pointer in our dummy node points
to that least val. We then adjust our dummy node and our list1 or list2 node to keep iterating and constructing our merged list.
However there will be a scenario where one of the lists hits None before the other. In that case our while loop will terminate,
and we check which of the two input lists IS NOT None yet and the next pointer of our merged lists points to the remainder of
the none null list. We can do this as any remainder nodes left over will be greater then our last element in the merged list
simply due to the fact that both input lists are in ascending order. 
'''

