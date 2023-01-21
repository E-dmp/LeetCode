#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        length = len(nums)

        while length > 0:

            if nums[i] == 0:
                nums.append(nums[i])
                nums.pop(i) 
                length -= 1
            else:
                i += 1
                length -= 1
        
# @lc code=end

