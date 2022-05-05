class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lp, rp = 0, len(arr) - 1
        i = 0
        
        while i <= rp:
            if arr[i] == 0:
                arr[i], arr[lp] = arr[lp], arr[i]
                
                i += 1
                lp += 1
            elif arr[i] == 1:
                i+= 1
                
            else:
                arr[i], arr[rp] = arr[rp], arr[i]
                
                rp -= 1
                