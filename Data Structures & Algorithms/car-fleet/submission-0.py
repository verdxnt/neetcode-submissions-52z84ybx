class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        #Ex:
        #   [4 1 0 7]  <- Position
        #   [2 2 1 1]  <- speed
        
       
        stack = [] # the stack will be the tool that i use to manage the number of fleets i have
        pair = [(positon, speed) for positon, speed in zip(position, speed)]  # i need to sort the positions of the cars.
    
        # Step 2: Sort by position, CLOSEST to target first (descending)
        pair.sort(reverse=True)
        
        # Step 3: Stack stores arrival times of each fleet
        stack = []
        
        for positon, speed in pair:

            time  =  (target - positon)/speed
            stack.append(time)
            # stack[-1] represents the recently car time, stack[-2] represets the one before stack[-1] (the previous car time)
            # if the time of the new car is less than or equall to the time of the previous car, we just pop off the previous time becasue it is part of the previous cars fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            

        return len(stack)

