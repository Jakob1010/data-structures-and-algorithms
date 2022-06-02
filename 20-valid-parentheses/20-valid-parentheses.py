class Solution:
    def isValid(self, s: str) -> bool:
        parenth_dict = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack = []
        
        for i in range(0,len(s)):
            if len(stack) != 0 and stack[-1] in parenth_dict and parenth_dict[stack[-1]] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        
        if len(stack) == 0: 
            return True
        else:
            return False