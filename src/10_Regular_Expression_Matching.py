# Runtime 73ms
# Memory 16.40mb

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n_s=len(s)
        n_p=len(p)
        dp=[[False] * (n_p+1) for _ in range(n_s+1)]
        dp[0][0]=True
        
        
        for i in range(1,n_p+1):
            if p[i-1]=="*":
                dp[0][i]=dp[0][i-2]
        
        for i in range(1,n_s+1):
            for j in range(1,n_p+1):
                if s[i-1]==p[j-1] or p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                
                elif p[j-1]=="*":
                    dp[i][j]=dp[i][j-2]
                    if p[j-2]=='.' or p[j-2]==s[i-1]:
                        dp[i][j]=dp[i][j] or dp[i-1][j]
                    
            
        return dp[n_s][n_p]