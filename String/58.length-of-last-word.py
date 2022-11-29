#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        """
        :type x: str
        :rtype: int
        """
        lastWordLength = 0
        
        # 最後の文字以降の空白があれば削除
        # 文字列逆転

        for i in range(1,len(s)):
            if s[len(s) - i] != ' ':
                s = s[:(len(s) - i + 1)][::-1]
                break

        for j in s:
            if j == ' ': break
            else: lastWordLength += 1

        return lastWordLength 
        
# @lc code=end

