# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        #traverse to the end get slow pointer iun the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse second half of the linked list
        second = slow.next
        slow.next = None
        prev = None
        cur = second
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        first, second = head, prev
        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next

