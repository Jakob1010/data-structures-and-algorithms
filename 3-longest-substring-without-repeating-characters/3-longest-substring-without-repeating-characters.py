class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        substring = {}
        start = 0
        max_len = 1
        substring[s[0]] = 1
        
        for i in range(1,len(s)):
            while s[i] in substring:
                substring[s[start]] -= 1
                if substring[s[start]] == 0:
                    del substring[s[start]]
                start += 1
            max_len = max(max_len,i-start+1)
            substring[s[i]] = 1
            
        return max_len