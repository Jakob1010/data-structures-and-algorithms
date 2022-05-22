class Solution:
    def countSubstrings(self, s: str) -> int:
        # abbbcbbba
        cnt = 0
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
            cnt += 1
            
        for i in range(0,len(s)-1):
            if(s[i]==s[i+1]):
                dp[i][i+1] = True
                cnt += 1
            else:
                dp[i][i+1] = False
                
        for i in range(3,len(s)+1):
            for j in range(0,len(s)-i+1):
                if s[j]==s[j+i-1] and dp[j+1][j+i-2]:
                    dp[j][j+i-1] = True
                    cnt += 1
                else:
                    dp[j][j+i-1] = False
        
        return cnt
                
            
        print(dp)