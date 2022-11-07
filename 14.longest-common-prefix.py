#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        basePrefix = strs[0]

        for i in range(1,len(strs)):

            while basePrefix != strs[i][:len(basePrefix)]:

                basePrefix = basePrefix[:-1]

                if basePrefix == "": return ""

        return basePrefix 
        
# @lc code=end

