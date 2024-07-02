'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # Edge case
    if not head: return []

    # Finding midpoint of linked list
    slow, fast = head, head
    while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
    
    # reversing second half of the linked list
    prev, cur = None, slow.next
    while cur:
            save_next = cur.next
            cur.next = prev
            prev = cur
            cur = save_next
    slow.next = None

    # linking each node, starting from first half of list, then second, then first...
    head_1, head_2 = head, prev
    while head_2:
        save_next = head_1.next
        head_1.next = head_2
        head_1 = head_2
        head_2 = save_next

'''
A procedural problem but it reviews a lot of linked list fundementals that being, reversing, and finding midpoint of
LL. For concerns the only dodgy part to me is the ending part once we have our two sub lists set up. My weak point
is working with references slightly especially under pressure. 
'''
