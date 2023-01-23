#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        for word in s:
            if word in t: t = t.replace(word, '', 1)
            else: return False

        return len(t) == 0  
        
# @lc code=end

