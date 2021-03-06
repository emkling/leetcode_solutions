class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp = 0, 1
        max_val = 0
        
        while rp < len(prices):
            if prices[lp] < prices[rp]:
                profit = prices[rp] - prices[lp]
                max_val = max(max_val, profit)
                
            else:
                lp = rp
            
            rp += 1
            
        return max_val