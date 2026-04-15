class Solution:
    def isValid(self, s: str) -> bool:
        openParentheses = []
        parenthesesMatch = {")" : "(", "}" : "{", "]" : "["}

        if len(s)== 1:
            return False
       
        for paren in s:
            #checks if it is an open parentheses
            if paren == "{" or paren == "(" or paren == "[":
                openParentheses.append(paren)
            #check if closed parentheses:
            else:
                potentialMatch = parenthesesMatch[paren]
                #if theres move parentheses in the stack
                if len(openParentheses) > 0 and openParentheses[-1] == potentialMatch:
                    openParentheses.pop()
                else:
                    return False
                
        return len(openParentheses) == 0


        