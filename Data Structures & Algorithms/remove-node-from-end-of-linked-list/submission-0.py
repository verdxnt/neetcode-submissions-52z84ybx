# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        size = 0 
        
        # count the length of the linked list
        while cur is not None:
            size+= 1
            cur = cur.next

        targetCount = size - n + 1
        if targetCount == 1:
            return head.next

        cur = head
        for i in range(0, targetCount - 2):
            cur = cur.next
        nextNode = cur.next.next
        cur.next = nextNode

        return head

        
        

