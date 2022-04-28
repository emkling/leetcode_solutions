class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}
        
        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]] += 1
            else:
                letters[s[i]] = 1
                
            if t[i] in letters:
                letters[t[i]] -= 1
                
            else:
                letters[t[i]] = -1
                
                
        for i in letters:
            if letters[i] != 0:
                return False
            
        
        
        return True