#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashMap = {}

        for i in range(0,len(nums)):
            if nums[i] not in hashMap: hashMap[nums[i]] = 1
            else: hashMap[nums[i]] += 1

        sortedMap = sorted(hashMap.items(), key = lambda i: i[1], reverse=True)

        return sortedMap[0][0]
        
# @lc code=end

