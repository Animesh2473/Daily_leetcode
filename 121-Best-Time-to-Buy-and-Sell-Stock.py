class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)):
            baught = prices[i]
            for j in range(i+1,len(prices)):
                sell = prices[j]
                maximum = max(sell-baught,maximum)
        return maximum
