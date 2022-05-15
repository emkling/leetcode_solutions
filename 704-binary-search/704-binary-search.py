class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0,  len(nums) -1 
        
        while lp <= rp:
            middle = lp + (rp - lp) // 2
            
            if nums[middle] == target:
                return middle
            
            if target > nums[middle]:
                lp = middle + 1
                
            elif target < nums[middle]:
                rp = middle - 1
                
            
            
            
        return -1 