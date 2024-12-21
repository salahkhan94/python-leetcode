class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if(prices[i] < prices[i-1]):
                maxprofit += prices[i-1] - buy
                buy = prices[i]
            elif(i == len(prices)-1):
                maxprofit += prices[i] - buy
        return maxprofit