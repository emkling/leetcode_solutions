class Solution:
    def minWindow(self, s: str, t: str) -> str:
        matches, window_start, substring_start = 0, 0, 0
        frequency = {}
        min_length = len(s) + 1
        
        for char in t:
            if char not in frequency:
                frequency[char] = 0
                
            frequency[char] += 1
            
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            if right_char in frequency:
                frequency[right_char] -= 1
                if frequency[right_char] >= 0:
                    matches += 1

            while matches == len(t):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    substring_start = window_start
                    
                    
                left_char = s[window_start]
                window_start += 1
            
                if left_char in frequency:
                    if frequency[left_char] == 0:
                        matches -= 1

                    frequency[left_char] += 1

        
        if min_length > len(s):
            return ""
        
        return s[substring_start:substring_start+min_length]
                