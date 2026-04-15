class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_profit = 0
        left = 0 #buy
    

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                cur_profit = prices[right] - prices[left]
               #if cur_profit > max_profit:
               #    max_profit = cur_profit 
                max_profit = max(cur_profit, max_profit)
        return max_profit