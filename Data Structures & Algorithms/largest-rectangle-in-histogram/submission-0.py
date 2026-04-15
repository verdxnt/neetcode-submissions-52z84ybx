class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack = [] #  the current heighest bar
        # width = 0
        # largestArea = 0
        # mimHeight = 0
         
        # for i in range(len(heights)):
        #     val = heights[i]

        #     if i > 0 and val >= stack[-1]:
        #         stack.pop() # remove the previous height in the stack
        #         # width -= 1 <-- unesscessary
        #         stack.append(val) # add the new height in the stack
        #         width = 1 # when we find a val greater or equal to curr hieghest height we reset the width\

        #         if mimHeight < val and val > mimHeight:
        #             mimHeight = val

        #         area = width * mimHeight 
        #         if area > largestArea:
        #             largestArea = area

        #     elif i > 0 and stack[-1] >= val:
        #         if val > mimHeight:
        #             mimHeight = val

        #         width += 1
        #         area = width * mimHeight
        #         if area > largestArea:
        #             largestArea = area

        

        #     else:
        #         stack.append(val)
        #         width = 1

        # return largestArea


        #     #if heights[i+1] < val

        stack = []  # each item is (start_index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            # pop while current bar is smaller
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index  # extend the new bar backward

            stack.append((start, h))

        # finish remaining bars
        n = len(heights)
        while stack:
            index, height = stack.pop()
            max_area = max(max_area, height * (n - index))

        return max_area
