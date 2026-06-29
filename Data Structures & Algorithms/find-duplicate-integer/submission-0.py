class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        
        # phase 1: detect that a cycle exists (exact same as Linked List Cycle)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # phase 2: find where the cycle starts
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow