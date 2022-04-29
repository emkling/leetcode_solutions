class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        test_sum = 0
        
        for i in nums:
            if test_sum < 0:
                test_sum = 0
            
            test_sum += i
            max_sum = max(max_sum, test_sum)
            
        
        return max_sum