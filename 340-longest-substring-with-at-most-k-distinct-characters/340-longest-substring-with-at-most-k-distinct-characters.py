class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_length = 0 
        window_start = 0
        frequency = {}
        
        for window_end in range(len(s)):
            end_char = s[window_end]
            
            if end_char not in frequency:
                frequency[end_char] = 0
            
            frequency[end_char] += 1
            
            while len(frequency) > k:
                left_char = s[window_start]
                frequency[left_char] -= 1
                if frequency[left_char] == 0:
                    del frequency[left_char]
                window_start += 1
                
            max_length = max(max_length, window_end - window_start + 1)
            
            
        return max_length