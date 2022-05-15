class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        subset = []
        subset.append([])
        
        start,end = 0, 0
        
        for i in range(len(nums)):
            start = 0
            
            
            if i > 0 and nums[i] == nums[i-1]:
                start = end + 1
            
            end = len(subset) - 1
            
            for j in range(start, end+1):
                set1 = list(subset[j])
                set1.append(nums[i])
                subset.append(set1)
                
                
                
        return subset