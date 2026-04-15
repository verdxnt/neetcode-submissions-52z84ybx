class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
    
        # Start with all 0s — days with no warmer future day stay 0
        result = [0] * n
        
        # Stack stores INDICES of days still waiting for a warmer day
        stack = []
        
        for today in range(n):
            
            # While there are waiting days AND today is warmer than the most recent one
            while stack and temperatures[today] > temperatures[stack[-1]]:
                
                # The waiting day finally found its warmer day!
                waiting_day = stack.pop()
                
                # Distance = today's index - waiting day's index
                result[waiting_day] = today - waiting_day
            
            # Today is now waiting for ITS warmer future day
            stack.append(today)
        
        # Any days left in stack never found a warmer day → already 0
        return result