#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        stack = []
        i = 0
        for k in s:
            stack.append(k)
            
        while stack:
            s[i] = stack.pop()

            i += 1
        
# @lc code=end

