#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        """
        :type s: string
        :rtype: int
        """

        hashmap = {}

        # create hash
        for i in range(0,len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else: hashmap[s[i]] += 1

        for i,j in enumerate(hashmap):
            if hashmap[j] == 1: return list(s).index(j)
        return -1     
        
# @lc code=end

