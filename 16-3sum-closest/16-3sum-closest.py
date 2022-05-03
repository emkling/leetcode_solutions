class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallest_diff = math.inf 
        
        for i in range(len(nums)- 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                target_diff = target - nums[i] - nums[left] - nums[right]
                if target_diff == 0:
                    return target
                
                if abs(target_diff) < abs(smallest_diff) or abs(target_diff) == abs(smallest_diff) and target_diff < smallest_diff:
                    smallest_diff = target_diff
                    
                if target_diff > 0:
                    left += 1
                    
                else:
                    right -=1
                    
            
        return target - smallest_diff