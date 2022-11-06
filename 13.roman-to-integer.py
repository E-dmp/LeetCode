#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        sumOfValue = 0
        hashMap = {'IV': 4,'IX': 9,'XL': 40,'XC': 90,'CM': 900,'CD': 400,"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}

        for i in hashMap:
            count = s.count(i)
            sumOfValue += hashMap[i] * count
            s = s.replace(i, '')
            
        return sumOfValue
        
# @lc code=end
