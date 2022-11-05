#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
import math

# LeetCodeの仕様？ 
# length/2 intになる

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x = str(x)
        length = len(x)
        
        mid = length/2

        for i in range(mid + 1):
            if x[i] != x[-(i + 1)]:
                return False
        return True 
        
# @lc code=end

