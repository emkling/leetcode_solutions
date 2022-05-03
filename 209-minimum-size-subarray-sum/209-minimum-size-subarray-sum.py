class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        test_sum = 0
        min_length = math.inf
        window_start = 0
        
        for window_end in range(len(nums)):
            test_sum += nums[window_end]
            
            while test_sum >= target:
                min_length = min(min_length, window_end - window_start + 1)
                test_sum -= nums[window_start]
                window_start += 1
            
            
        if min_length == math.inf:
            return 0
        
        return min_length
    
    

