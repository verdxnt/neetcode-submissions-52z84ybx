class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
        
        for val in dict1:
            if dict1[val] > 1:
                return True
        return False