#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hashmap = {}

        for i in range(0,len(nums)):
            if nums[i] in hashmap: hashmap[nums[i]] += 1
            else: hashmap[nums[i]] = 1

        for key in hashmap.keys():
            if hashmap[key] == 1: return key
        
# @lc code=end

