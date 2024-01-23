class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 1:
            return 0

        left = 0
        maxProfit = 0

        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if profit > 0:
                maxProfit = max(profit, maxProfit)
            else:
                left = right

        return maxProfit


if __name__ == "__main__":
    prices = [2, 1, 2, 1, 0, 1, 2]
    sol = Solution()
    print(sol.maxProfit(prices))
