'''
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an 
additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node is represented as a 
pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random 
pointer points to, or null if it does not point to any node.
'''

def copy_random_list(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head: return None
    hashmap = dict()

    curr_node = head
    while curr_node:
        hashmap[curr_node] = Node(curr_node.val)
        curr = curr.next
    
    curr_node = head
    while curr_node:
        hashmap[curr_node].next = hashmap.get(curr_node.next)
        hashmap[curr_node].random = hashmap.get(curr_node.random)
        curr = curr.next
    
    return hashmap[head]

'''
This problem was actually fun because I understood it xD. It niche how we utilize a map to make copies 
of the node by associating they key, with a new instance of a node and passing the val of the original node
in that instance. Once we do that we can keep using the copy node and using it's next and random pointers
the following copy values.
'''
