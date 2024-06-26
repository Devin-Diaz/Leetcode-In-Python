'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

TEST CASES:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]
'''

def reverseList(head):    
    current_node = head
    prev_node = None

    while current_node != None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
        
    return prev_node

'''
O(N) TC and O(1) SC. We start by creating a node that is null and a temp node that points to the head.
We then save the ref that is pointer to the next element of the temp node. Then we set the pointer of the 
head to the null node. Now we point our prev node to the current temp node, and our temp node points to that
saved reference that we saved at the beginning so we can keep advancing in the linked list. We repeat this 
process until our current temp node is at null, indicating that our prev node that has been following along
is now at the new head of the list. We have reversed the linked list.
'''