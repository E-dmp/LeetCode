#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)  
        
# @lc code=end

