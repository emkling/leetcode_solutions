class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_start, matches = 0, 0
        result = []
        frequencies = {}
        
        for char in p:
            if char not in frequencies:
                frequencies[char] = 0
            frequencies[char] += 1
            
         
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            if right_char in frequencies:
                frequencies[right_char] -= 1
                
                if frequencies[right_char] == 0:
                    matches += 1
                    
            if matches == len(frequencies):
                result.append(window_start)
                
                
            if window_end - window_start >= len(p) -1 :
                left_char = s[window_start]
                window_start += 1
                
                if left_char in frequencies:
                    if frequencies[left_char] == 0:
                        matches -= 1
                        
                    frequencies[left_char] += 1
                    
            
        return result