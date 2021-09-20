class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        m = None
        for i in range(len(prices)):
            if m != None:
                x = prices[i]- m
                if x > 0:
                    if x > prof:
                        prof = x
            
            if m == None:
                m = prices[i]
            else:
                if prices[i] < m:
                    m = prices[i]
        return prof