class MinStack:


    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

        #if there isnt a val already in the stack, add val to stack
        if not self.minStk:
            self.minStk.append(val)
        #if there is a value in the stack, compare if it is less than val, if value in minStk is < than val add the same value to the stack (shows its till the lowest)
        elif self.minStk[-1] < val:
            self.minStk.append(self.minStk[-1])
        # else if that value is greater than val, we add val to the stack and minStack
        else:
            self.minStk.append(val)
        
       
    def pop(self) -> None:
        self.stk.pop()
        self.minStk.pop()
    

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]
            
            
        
