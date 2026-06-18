class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        str1, str2 = "",""
        
        while cur1 is not None:
            str1 = str(cur1.val) + str1         
            cur1 = cur1.next
            
        while cur2 is not None:
            str2 = str(cur2.val) + str2
            cur2 = cur2.next
        
        total = int(str1) + int(str2)
        digitList = [int(d) for d in str(total)[::-1]]
        
        dummy = ListNode(0)
        cur = dummy
        for num in digitList:
            cur.next = ListNode(int(num))
            cur = cur.next

        return dummy.next