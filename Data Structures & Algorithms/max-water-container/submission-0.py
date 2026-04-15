class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        area = 0
        while l < r:
            curArea = 0
            distance = len(heights[l:r])
            minBar = min(heights[l], heights[r])
            curArea = minBar * distance
            
            if curArea > area:
                area = curArea 

            if heights[r] >= heights[l]:
                l +=1
            else:
                r -= 1
        return area

