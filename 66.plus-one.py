#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = -1
        counter = 0
        length = len(digits)

        # 末尾が9ではない場合
        if digits[-1] != 9:
            return digits[:-1] + [digits[-1] + 1]
        # 末尾から連続する9の個数をカウント
        while length != 0:
            if digits[i] != 9:
                break
            i -= 1
            counter += 1
            length -= 1 

        """
        Listが9だけで構成されていた場合
        [9,8,9]のように9以外の要素がある場合
        """
        if counter == len(digits):
             return [1] + counter * [0]
        else: 
            return digits[:-(counter + 1)] + [digits[-(counter + 1)] + 1] + counter * [0]
        
# @lc code=end

