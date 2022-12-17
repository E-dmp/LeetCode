#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # ref: https://www.youtube.com/watch?v=1pkOgXD63yU


        buypPoint,sellPoint = 0,1

        maxProift = 0

        while sellPoint < len(prices):

            if prices[buypPoint] < prices[sellPoint]:
                profit = prices[sellPoint] - prices[buypPoint]
                maxProift = max(maxProift,profit)
            else:
                buypPoint = sellPoint

            sellPoint += 1

        return maxProift 
        
# @lc code=end

