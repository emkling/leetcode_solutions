class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1 = self.stack(s, [])
        l2 = self.stack(t, [])
        return l1 == l2
        
    
    def stack(self, s, stack):
        for char in s:
            if char is not "#":
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack