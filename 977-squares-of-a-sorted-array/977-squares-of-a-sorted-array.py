class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lp, rp  = 0, len(nums)-1
        result = [0] * len(nums)
        
        for i in reversed(range(len(nums))):
            if abs(nums[lp]) > abs(nums[rp]):
                result[i] = nums[lp] * nums[lp]
                lp += 1
            else:
                result[i] = nums[rp]* nums[rp]
                rp -= 1
            
        return result 