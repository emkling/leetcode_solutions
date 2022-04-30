class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lp, rp = 0, len(nums)-1
        answer = [0] * (len(nums))
        
        for idx in reversed(range(len(nums))):
            if abs(nums[lp]) > abs(nums[rp]):
                answer[idx] = nums[lp] * nums[lp]
                lp += 1
                     
            else: 
                answer[idx] = nums[rp] * nums[rp]
                rp -= 1
                     
        return answer
            