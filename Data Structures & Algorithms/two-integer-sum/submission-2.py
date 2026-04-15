class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        val_idx = {}

        for idx, value in enumerate(nums):
            diff = target - value
            if diff in val_idx:
                return [val_idx[diff],idx] #becasue we are returing the index locations
            val_idx[value] = idx

            