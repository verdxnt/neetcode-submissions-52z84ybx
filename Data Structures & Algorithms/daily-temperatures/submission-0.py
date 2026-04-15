class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        stack = [] # stores indices
        curDay = 0
        while curDay < len(temperatures):
            while stack and temperatures[curDay] > temperatures[stack[-1]]:
                prevDay = stack.pop()
                res[prevDay] = curDay - prevDay
            
            stack.append(curDay)
            curDay += 1
        return res