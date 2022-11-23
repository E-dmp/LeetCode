#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(0,len(s)):
            if s[i] == "{" or s[i] == "(" or s[i] == "[" :
                 stack.append(s[i])
            elif s[i] == "}" and len(stack) > 0 and stack[len(stack) - 1] == "{":
                 stack.pop(len(stack) - 1)
            elif s[i] == ")" and len(stack) > 0 and stack[len(stack) - 1] == "(": 
                stack.pop(len(stack) - 1)
            elif s[i] == "]" and len(stack) > 0 and stack[len(stack) - 1] == "[": 
                stack.pop(len(stack) - 1)
            else:
                return False
                
        return len(stack) == 0
        
# @lc code=end

