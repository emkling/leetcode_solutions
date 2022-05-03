class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for idx, number in enumerate(nums):
            complement = target - number
            if complement in hashmap:
                return [hashmap[complement], idx]
            else:
                hashmap[number] = idx
                
        
                