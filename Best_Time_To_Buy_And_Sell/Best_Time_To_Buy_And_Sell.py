class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        past=0
        future=1
        maxprofit=0

        while future<len(prices):
            if prices[future]>prices[past]:
                maxprofit=max(maxprofit,prices[future]-prices[past])
            else : 
                past=future 
            future += 1
        return maxprofit
