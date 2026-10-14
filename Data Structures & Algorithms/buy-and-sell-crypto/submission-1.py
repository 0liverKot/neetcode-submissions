class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        res = 0
        left = 0
        right = 1

        while True:

            profit = prices[right] - prices[left]
            if profit > res:
                res = profit

            if prices[left] > prices[right]:
                left = right
                right += 1
                
            else: 
                right += 1

            if right >= len(prices):
                break
        
        return res

            
            

            


        
        