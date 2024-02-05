class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        #dp[i][j] :=the lenght of the longest common subsequence from text1[0..i] , text2[0...j]
        
        dp =[[0]* (n+1) for _ in range(m+1)]
        
        
        
        for i in range(m):
              for j in range(n):
                  if text1[i] == text2[j]:
                        dp[i+1][j+1] = 1+dp[i][j]
                        print(dp[i+1][j+1])
                  else:
                        dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        return dp[m][n]
  

ins = Solution()
text1 = "abcde"
text2 = "ace" 
res = ins.longestCommonSubsequence(text1, text2)
print(res)
        