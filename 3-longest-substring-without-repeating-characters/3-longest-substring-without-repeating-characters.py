class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        frequency = {}
        window_start = 0
        max_length = 0
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            if right_char in frequency:
                
                window_start = max(window_start, frequency[right_char] + 1)
                
            frequency[right_char] = window_end
            
            max_length = max(max_length, window_end - window_start + 1)\
        
        
        return max_length