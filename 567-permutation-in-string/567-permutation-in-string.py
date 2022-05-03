class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start, matches = 0, 0
        frequency = {}
        
        for char in s1:
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1
            
        for window_end in range(len(s2)):
            right_char = s2[window_end]
            
            if right_char in frequency:
                frequency[right_char] -= 1
                
                if frequency[right_char] == 0:
                    matches += 1
                    
            if matches == len(frequency):
                return True
            
            if window_end >= len(s1)-1:
                left_char = s2[window_start]
                window_start += 1
                
                if left_char in frequency:
                    if frequency[left_char] == 0:
                        matches -= 1
                    
                    frequency[left_char] += 1
                    
            
        return False