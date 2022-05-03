class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lp, rp = 0, 1
        
        
        while lp < len(nums):
            if nums[rp - 1] != nums[lp]:
                nums[rp] = nums[lp]
                rp += 1
            lp += 1
            
        return rp