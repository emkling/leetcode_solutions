class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        hashmap = {}
        maxVal = 0
        
        for number in nums:
            if number in hashmap:
                hashmap[number] += 1
                if hashmap[number] > len(nums) // 2:
                    return number
            else:
                hashmap[number] = 1
        
    
            