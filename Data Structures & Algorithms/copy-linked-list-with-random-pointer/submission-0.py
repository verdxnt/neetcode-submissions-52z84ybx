"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        k = {}
        cur = head

        #create a haspmap. key -> current original Node & value -> current original node value
        while cur is not None:
            k[cur] = Node(cur.val)
            cur = cur.next

        #go back to original and find out what their random pointer is
        cur = head
        while cur is not None:
            #this starts the new copy of the linked list
            newNode = k[cur]
            #get the new node next Node
            newNode.next = k.get(cur.next)
            #assign the new Node copy to the random pointer
            newNode.random = k.get(cur.random)

            cur = cur.next

        return k.get(head)
            