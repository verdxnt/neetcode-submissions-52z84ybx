class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            cur_num = nums[i]
            if cur_num > 0:
                break
            elif i > 0 and cur_num == nums[i-1]:
                continue

            low = i+1
            high = len(nums) - 1
            
            while low < high:
                curSum = cur_num + nums[low] + nums[high]
                if curSum == 0:
                    res.append([cur_num, nums[low], nums[high]])
                    low += 1
                    high -= 1

                    while low  < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low  < high and nums[high] == nums[high + 1]:
                        high -= 1 
                        
                elif curSum > 0:
                    high -= 1
                else:
                    low += 1
        return res




