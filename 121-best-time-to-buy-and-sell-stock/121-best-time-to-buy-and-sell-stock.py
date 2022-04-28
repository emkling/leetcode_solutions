class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp = 0, 1
        max_val = 0
        test_val = 0
        
        while rp < len(prices):
            if prices[lp] < prices[rp]:
                test_val = prices[rp] - prices[lp]
                max_val = max(test_val, max_val)
                
            else:
                lp = rp
                
            rp += 1
            
        return max_val