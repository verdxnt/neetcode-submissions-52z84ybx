class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix_arr = [1] * n
        suffix_arr = [1] * n

        
        prefix = 1
        for i in range(0, len(nums)):
            prefix_arr[i] = prefix
            prefix = prefix * nums[i]
        
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            suffix_arr[i] = suffix
            suffix = suffix * nums[i]

        for i in range(0, len(prefix_arr)):
            res[i] = prefix_arr[i] * suffix_arr[i]
        
        return res