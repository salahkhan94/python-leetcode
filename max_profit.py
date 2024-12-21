class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = 10000
        for i in range(len(prices)):
            if(prices[i] < minprice):
                minprice = prices[i]
            if(prices[i]-minprice > maxprofit):
                maxprofit = prices[i]-minprice
        return maxprofit