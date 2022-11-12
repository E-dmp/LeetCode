#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hashmap = {}
        sortedList = []

        # create hash
        for i in nums1:
            if i in hashmap: hashmap[i] += 1
            else:hashmap[i] = 1
        
        for j in nums2:
            if j in hashmap and hashmap[j] > 0: 
                hashmap[j] -= 1
                sortedList.append(j)
                
        return set(sortedList)
        
# @lc code=end

