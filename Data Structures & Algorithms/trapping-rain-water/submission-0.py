class Solution:
    def trap(self, height: List[int]) -> int:

        lenH = len(height)
        if lenH == 0:
            return 0
        #[0,2,0,3,1,0,1,3,2,1]
        maxLeftFoward = [0] * lenH
        maxRightBackward = [0] * lenH
    

        # currLeftMax = 0
        # currRightMax = 0

        #[0, 2, 0, 3, 1, 0, 1, 3, 2, 1] <--- heights
        #[0, 0, 2, 2, 3, 3, 3, 3, 3, 3] -----> max heihts to the left of each index
        #[3, 3, 3, 3, 3, 3, 3, 2, 1, 0] <----- max height to the right of each index
        # at each index, we take the minimum of left and right maxes and subtract it from the height.
        # if value is >= 1, there theres at least 1 water. if value is <= 0, then theres no water
        maxLeftFoward[0] = height[0]
        for i in range(1,lenH):
            maxLeftFoward[i] = max(maxLeftFoward[i-1], height[i])

        maxRightBackward[lenH-1] = height[lenH-1]
        for i in range(lenH - 2, -1, -1):
            maxRightBackward[i] = max(maxRightBackward[i+1], height[i])

        trappedWater = 0
        for i in range(lenH):
            trappedWater += min(maxLeftFoward[i],maxRightBackward[i]) - height[i]
        return trappedWater


        

