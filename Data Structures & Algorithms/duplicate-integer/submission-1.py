class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if i != 0:
                if nums[i] in nums[0:i] or nums[i] in nums[i+1:]:
                    return True
        return False