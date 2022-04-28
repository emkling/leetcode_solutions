class Solution:
    def isValid(self, s: str) -> bool:
        char = {')':'(', '}':'{', ']':'['}
        
        stack = []
        
        for c in s:
            if c not in char:
                stack.append(c)
            
            else:
                if stack and stack[-1] == char[c]:
                    stack.pop()
                else:
                    return False
                
                
        return True if not stack else False
            