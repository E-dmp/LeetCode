#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# test
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        return self.climbStairsHelper(0,1,n)

    def climbStairsHelper(self,f1,f2,n):

        if n == 0: return f2

        return self.climbStairsHelper(f2,f1+f2,n-1)


    # another
    # if n == 1: return 1
    # if n == 2: return 2
    # return self.climbStairs(n - 1) + self.climbStairs(n - 2) 
        
# @lc code=end

