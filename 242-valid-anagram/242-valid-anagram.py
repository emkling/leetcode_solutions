class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        
        
        for char in s:
            if char not in hashmap:
                hashmap[char] = 0
                
            hashmap[char]+= 1
            
            
        for char in t:
            if char in hashmap:
                if hashmap[char] == 0:
                    return False
                else:
                    hashmap[char] -= 1
                    continue
            else:
                return False
            
            
            
        return True